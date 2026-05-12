"""Tests for solver v3: severity-weighted objective + crossing bonuses.

V3 changes:
  - Objective swaps `Σ capped_imp / gap_pct` for `Σ capped_imp` so severity
    (gap size) is no longer normalized out — bigger gaps offer more potential
    reward.
  - Two binary indicators per marker: `cross_ref` (currently-critical reaches
    clinical reference boundary) and `cross_opt` (anything-not-optimal reaches
    optimal subrange). Each crossing earns an extra gap_pct units of reward,
    weighted by α and β respectively.
  - Plan exposes `crossings_to_healthy` and `crossings_to_optimal` so the UI
    can show categorical wins directly from the optimization, not by
    reclassifying projected values against user-specific lab ranges.

These tests use generic marker shapes (not Function-Health-specific labs) so
they verify the math generalizes to any dataset.
"""
import pytest

from fhetl.schemas import Citation, Effect, Intervention, Marker
from fhetl.solver import UserProfile, solve


def _marker_lower(
    mid: str = "x",
    ref_lo: float = 0,
    ref_hi: float = 100,
    opt_lo: float = 0,
    opt_hi: float = 50,
) -> Marker:
    return Marker(
        id=mid, name=mid, panel="p", units="u",
        direction="lower_is_better",
        ref_lo=ref_lo, ref_hi=ref_hi, opt_lo=opt_lo, opt_hi=opt_hi,
    )


def _marker_higher(
    mid: str = "y",
    ref_lo: float = 30,
    ref_hi: float = 200,
    opt_lo: float = 50,
    opt_hi: float = 200,
) -> Marker:
    return Marker(
        id=mid, name=mid, panel="p", units="u",
        direction="higher_is_better",
        ref_lo=ref_lo, ref_hi=ref_hi, opt_lo=opt_lo, opt_hi=opt_hi,
    )


def _iv(iv_id: str, mechanisms: list[str], active_ingredient: str | None = None) -> Intervention:
    return Intervention(
        id=iv_id, canonical_name=iv_id, type="supplement",
        dose_amount=1, dose_unit="unit", mechanisms=mechanisms,
        active_ingredient=active_ingredient,
    )


def _effect(
    iv_id: str,
    lo: float,
    hi: float,
    *,
    marker_id: str = "x",
    direction: str = "decrease",
) -> Effect:
    return Effect(
        intervention_id=iv_id, marker_id=marker_id,
        direction=direction, effect_type="pct",
        effect_lo=lo, effect_hi=hi,
        baseline_mod_elevated=1.0, baseline_mod_lean=0.5,
        evidence_tag="meta", evidence_weight=1.0,
        time_lo_wk=4, time_hi_wk=8,
        citations=[Citation(author="X", journal="Y", year=2020)],
    )


def test_severity_weighting_prefers_big_gap_over_trivial():
    """Two markers, budget=1. Marker A has a big gap, marker B has a tiny gap.
    Each can be improved by exactly one dedicated intervention. The severity-
    weighted objective should pick the intervention that closes more raw %.

    Under the old normalized objective, both interventions delivered ~equal
    score (1.0 each, since each fully closes its own gap). V3 picks A because
    capped_imp for A (~40%) >> capped_imp for B (~2%).
    """
    markers = {
        "big_gap": _marker_lower("big_gap", opt_hi=50, ref_hi=100),       # val=90 → 40% gap
        "tiny_gap": _marker_lower("tiny_gap", opt_hi=98, ref_hi=100),     # val=100 → 2% gap
    }
    interventions = {
        "fix_big": _iv("fix_big", ["mech_big"]),
        "fix_tiny": _iv("fix_tiny", ["mech_tiny"]),
    }
    effects = [
        _effect("fix_big", -50, -50, marker_id="big_gap"),
        _effect("fix_tiny", -10, -10, marker_id="tiny_gap"),
    ]
    profile = UserProfile(marker_values={"big_gap": 90, "tiny_gap": 100}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["fix_big"], (
        "severity weighting should prefer the marker with a big gap; "
        f"got {plan.interventions}"
    )


def test_critical_crossing_fires_and_is_exposed_on_plan():
    """A currently-critical marker that the solver can push into the healthy
    range should have `cross_ref` fire and appear in plan.crossings_to_healthy.
    """
    # val=130, ref_hi=125, opt_hi=80. Critical (130 > 125). One intervention
    # delivers -15% → 130 * 0.85 = 110.5, well inside the reference range but
    # not yet optimal. So we expect cross_ref=1, cross_opt=0.
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -15, -15, marker_id="x")]
    profile = UserProfile(marker_values={"x": 130}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["a"]
    assert plan.crossings_to_healthy == ["x"]
    assert plan.crossings_to_optimal == []


def test_optimal_crossing_fires_and_is_exposed_on_plan():
    """A healthy-not-optimal marker fully closed lands in `crossings_to_optimal`
    but NOT in `crossings_to_healthy` (it was never critical)."""
    # val=90, ref_hi=125, opt_hi=80. Healthy (in 80..125), not optimal.
    # Intervention delivers -15% → 76.5 (optimal). gap_pct = (90-80)/90 = 11.1%.
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -15, -15, marker_id="x")]
    profile = UserProfile(marker_values={"x": 90}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.crossings_to_healthy == []
    assert plan.crossings_to_optimal == ["x"]


def test_critical_to_optimal_fires_both_bonuses():
    """A single jump from critical all the way into optimal triggers BOTH
    binaries — appropriately rewarded as the most valuable transition."""
    # val=130, ref_hi=125, opt_hi=80. gap = (130-80)/130 = 38.5%. Needs ~38.5% drop.
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -50, -50, marker_id="x")]  # huge effect
    profile = UserProfile(marker_values={"x": 130}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.crossings_to_healthy == ["x"]
    assert plan.crossings_to_optimal == ["x"]


def test_partial_progress_fires_no_crossings():
    """A marker that improves but doesn't reach any threshold leaves both
    binaries at 0. The improvement still counts in continuous reward and the
    intervention is still selected."""
    # val=130, ref_hi=125, opt_hi=80. Needs ≥3.85% to escape critical. -2% drop
    # is below threshold → neither binary fires.
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -2, -2, marker_id="x")]
    profile = UserProfile(marker_values={"x": 130}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["a"]
    assert plan.crossings_to_healthy == []
    assert plan.crossings_to_optimal == []
    assert plan.improvements_pct["x"] == pytest.approx(2.0, abs=0.01)


def test_higher_is_better_marker_crossing():
    """Crossing logic works for higher_is_better direction (e.g., HDL, vitamin D).
    val=20, ref_lo=30, opt_lo=50. Currently critical (20 < 30). +50% → 30 = ref boundary
    exactly, which is the healthy zone. cross_ref should fire."""
    markers = {"vd": _marker_higher("vd", ref_lo=30, opt_lo=50, ref_hi=200, opt_hi=200)}
    interventions = {"sun": _iv("sun", ["uvb"])}
    effects = [_effect("sun", 50, 50, marker_id="vd", direction="increase")]
    profile = UserProfile(marker_values={"vd": 20}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["sun"]
    # 20 * 1.5 = 30 (== ref_lo, which is "healthy"). cross_ref requires
    # capped_imp ≥ imp_for_ref = (30-20)/20 * 100 = 50%. Exactly meets.
    assert plan.crossings_to_healthy == ["vd"]


def test_alpha_zero_disables_ref_crossings():
    """With α=0, the solver gets no bonus for ref crossings — it should still
    deliver the same continuous-improvement decision, but `crossings_to_healthy`
    may be empty (solver is indifferent to setting the binary).

    Sanity check that the knob actually controls bonus strength."""
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -15, -15, marker_id="x")]
    profile = UserProfile(marker_values={"x": 130}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1, alpha_ref_cross=0.0)
    # The intervention should still be picked (continuous reward + opt-bonus
    # isn't relevant here since it doesn't reach optimal anyway).
    assert plan.interventions == ["a"]


def test_crossing_does_not_force_overshoot():
    """The cross_opt binary requires capped_imp ≥ gap_pct, but capped_imp is
    ALSO bounded above by gap_pct. So setting cross_opt=1 pins capped_imp to
    exactly gap_pct (no overshoot). Verify projected value lands at opt_hi,
    not below it, when interventions are theoretically capable of more."""
    # val=90, opt_hi=80, ref_hi=125. gap_pct = 11.1%. Intervention delivers 30%
    # raw — far more than needed. capped_imp must cap at 11.1% (=gap_pct).
    markers = {"x": _marker_lower("x", ref_hi=125, opt_hi=80)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -30, -30, marker_id="x")]
    profile = UserProfile(marker_values={"x": 90}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.crossings_to_optimal == ["x"]
    # 90 * (1 - 0.1111) ≈ 80
    assert plan.projected_marker_values["x"] == pytest.approx(80.0, abs=0.5)


def test_no_crossings_when_nothing_to_fix():
    """No markers in needs_fixing → empty crossings, empty plan."""
    markers = {"x": _marker_lower("x", opt_hi=100, ref_hi=200)}
    interventions = {"a": _iv("a", ["m"])}
    effects = [_effect("a", -10, -10, marker_id="x")]
    profile = UserProfile(marker_values={"x": 50}, phenotype="elevated")  # already optimal
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == []
    assert plan.crossings_to_healthy == []
    assert plan.crossings_to_optimal == []


def test_flat_critical_escape_bonus_flips_a_close_call():
    """When two interventions are close on severity-weighted score, the flat γ
    bonus tips the balance toward the critical escape — a borderline marker
    that's just outside ref AND just outside optimal vs. a moderately-healthy
    marker that can fully reach optimal.

    Setup (lower_is_better):
      - "small_crit": val=101, ref_hi=100, opt_hi=95. Just-barely critical AND
        nearly-optimal. gap_to_opt ≈ 5.94%. Fix delivers 2% → escapes critical.
        Reward without γ: 2 + α·5.94 = 13.88
      - "med_healthy": val=115, ref_hi=200, opt_hi=100. Healthy-not-optimal.
        gap = 13%. Fix delivers 13% → reaches optimal.
        Reward: 13 + β·13 = 19.5

    Without γ, the healthy→optimal move wins (19.5 > 13.88). With γ=10 default,
    the critical escape wins (23.88 > 19.5) — exactly the clinical-priority
    behavior we want for borderline calls.
    """
    markers = {
        "small_crit": _marker_lower("small_crit", ref_hi=100, opt_hi=95),
        "med_healthy": _marker_lower("med_healthy", ref_hi=200, opt_hi=100),
    }
    interventions = {
        "fix_crit": _iv("fix_crit", ["mech_crit"]),
        "fix_healthy": _iv("fix_healthy", ["mech_healthy"]),
    }
    effects = [
        _effect("fix_crit", -2, -2, marker_id="small_crit"),
        # Effect slightly larger than the gap so capped_imp pins exactly at
        # gap_pct and cross_opt definitely fires.
        _effect("fix_healthy", -15, -15, marker_id="med_healthy"),
    ]
    profile = UserProfile(
        marker_values={"small_crit": 101, "med_healthy": 115},
        phenotype="elevated",
    )
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["fix_crit"]
    assert "small_crit" in plan.crossings_to_healthy
    # Inverse: with γ=0, the healthy→opt move should win on continuous + β alone.
    plan_no_gamma = solve(
        profile, markers, interventions, effects, budget=1, gamma_ref_flat=0.0,
    )
    assert plan_no_gamma.interventions == ["fix_healthy"]


def test_alpha_bump_makes_critical_escape_beat_healthy_to_optimal_at_equal_severity():
    """At equal severity, critical→healthy should outscore healthy→optimal
    purely on the severity-weighted bonuses (α=2 > β=0.5). Verifies the
    α-bump effect independently of γ.
    """
    # Two markers with the SAME gap_pct (40%). One sits in critical zone,
    # one in healthy zone. Each is fixable by one dedicated intervention.
    markers = {
        # critical: val=100, ref_hi=80, opt_hi=60 → gap to ref ≈ 20%, gap to opt = 40%
        "crit": _marker_lower("crit", ref_hi=80, opt_hi=60),
        # healthy-not-optimal: val=100, ref_hi=125, opt_hi=60 → in healthy, gap to opt = 40%
        "heal": _marker_lower("heal", ref_hi=125, opt_hi=60),
    }
    interventions = {
        "fix_crit": _iv("fix_crit", ["mech_a"]),
        "fix_heal": _iv("fix_heal", ["mech_b"]),
    }
    effects = [
        _effect("fix_crit", -45, -45, marker_id="crit"),  # closes to ~55, well past ref AND opt
        _effect("fix_heal", -45, -45, marker_id="heal"),  # closes to ~55, reaches opt
    ]
    profile = UserProfile(marker_values={"crit": 100, "heal": 100}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    # With α=2, β=0.5, γ=10: critical→optimal earns α·gap_pct + β·gap_pct + γ + continuous
    # = 2·40 + 0.5·40 + 10 + 40 = 80 + 20 + 10 + 40 = 150
    # healthy→optimal: β·gap_pct + continuous = 0.5·40 + 40 = 60
    # Critical wins by a comfortable margin.
    assert plan.interventions == ["fix_crit"]


def test_active_ingredient_groups_dedupe_dose_variants():
    """Two interventions sharing an `active_ingredient` are dose / formulation
    variants of the same compound. The solver must select at most one,
    regardless of whether they have non-overlapping mechanism classes that
    would otherwise let both fire on different markers.

    This is the "two vitamin D3 protocols in the same stack" bug: the loading
    dose has only `vitamin_d_provision`, the daily 3000 IU dose has
    `vitamin_d_provision` AND `anti_inflammatory`, so without grouping the
    solver picks both — loading wins vitamin_d_provision on one marker,
    daily wins anti_inflammatory on another. Active-ingredient grouping says
    only one variant can be selected at all.
    """
    markers = {
        "vit_d_marker": _marker_higher("vit_d_marker", ref_lo=30, opt_lo=40, opt_hi=80, ref_hi=100),
        "inflam_marker": _marker_lower("inflam_marker", ref_hi=10, opt_hi=2),
    }
    interventions = {
        # Both deliver vitamin D, but different mechanism breadths.
        "vit_d3_loading": _iv("vit_d3_loading", ["vitamin_d_provision"], active_ingredient="vitamin_d3"),
        "vit_d3_daily":   _iv("vit_d3_daily", ["vitamin_d_provision", "anti_inflammatory"], active_ingredient="vitamin_d3"),
        # Unrelated intervention for the inflammation marker.
        "curcumin": _iv("curcumin", ["anti_inflammatory"]),
    }
    effects = [
        _effect("vit_d3_loading", 30, 30, marker_id="vit_d_marker", direction="increase"),
        _effect("vit_d3_daily", 20, 20, marker_id="vit_d_marker", direction="increase"),
        _effect("vit_d3_daily", -15, -15, marker_id="inflam_marker"),
        _effect("curcumin", -20, -20, marker_id="inflam_marker"),
    ]
    profile = UserProfile(
        marker_values={"vit_d_marker": 25, "inflam_marker": 12},
        phenotype="elevated",
    )
    plan = solve(profile, markers, interventions, effects, budget=5)
    # Whichever vitamin D variant wins, the OTHER must not be in the stack.
    vit_d_picks = [iv for iv in plan.interventions if iv.startswith("vit_d3_")]
    assert len(vit_d_picks) <= 1, (
        f"Expected at most one vitamin D variant; got {vit_d_picks}"
    )
    # Curcumin (different active) should still be picked — it doesn't share
    # the active_ingredient group, so the constraint doesn't touch it.
    assert "curcumin" in plan.interventions


def test_active_ingredient_none_does_not_constrain():
    """Backward compatibility: interventions with active_ingredient=None
    (the default) are not affected by the grouping constraint — they stack
    as before."""
    markers = {"x": _marker_lower("x", ref_hi=100, opt_hi=40)}
    interventions = {
        # Both have None active_ingredient — ungrouped.
        "a": _iv("a", ["mech_a"]),
        "b": _iv("b", ["mech_b"]),
    }
    effects = [
        _effect("a", -20, -20, marker_id="x"),
        _effect("b", -25, -25, marker_id="x"),
    ]
    profile = UserProfile(marker_values={"x": 90}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=2)
    # No grouping constraint — both should be selectable (and indeed selected
    # because each contributes via a distinct mechanism class to close the gap).
    assert "a" in plan.interventions
    assert "b" in plan.interventions


def test_alpha_beta_gamma_are_tunable():
    """All three crossing-bonus weights are pluggable via solve() kwargs.
    Setting α=γ=0 should make the solver fall back to "just close the biggest
    gap" behavior, ignoring critical-priority signals.
    """
    markers = {
        "small_crit": _marker_lower("small_crit", ref_hi=100, opt_hi=80),
        "big_healthy": _marker_lower("big_healthy", ref_hi=200, opt_hi=100),
    }
    interventions = {
        "fix_crit": _iv("fix_crit", ["mech_crit"]),
        "fix_healthy": _iv("fix_healthy", ["mech_healthy"]),
    }
    effects = [
        _effect("fix_crit", -6, -6, marker_id="small_crit"),
        _effect("fix_healthy", -50, -50, marker_id="big_healthy"),
    ]
    profile = UserProfile(
        marker_values={"small_crit": 105, "big_healthy": 180},
        phenotype="elevated",
    )
    # With critical-priority weights zeroed out, the larger-severity healthy→opt
    # move should win on continuous reward + β alone.
    plan = solve(
        profile, markers, interventions, effects,
        budget=1, alpha_ref_cross=0.0, gamma_ref_flat=0.0,
    )
    assert plan.interventions == ["fix_healthy"]
