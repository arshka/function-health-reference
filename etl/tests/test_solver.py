"""Tests for the MILP solver."""
import pytest

from fhetl.schemas import Citation, Effect, Intervention, Marker
from fhetl.solver import Plan, UserProfile, solve


def _marker_apob() -> Marker:
    return Marker(
        id="apob",
        name="Apolipoprotein B",
        panel="cardiovascular",
        units="mg/dL",
        direction="lower_is_better",
        ref_lo=40,
        ref_hi=125,
        opt_lo=40,
        opt_hi=80,
    )


def _iv(id: str, mechanisms: list[str], type: str = "supplement") -> Intervention:
    return Intervention(
        id=id,
        canonical_name=id,
        type=type,
        dose_amount=1,
        dose_unit="unit",
        mechanisms=mechanisms,
    )


def _effect(
    intervention_id: str,
    effect_lo: float,
    effect_hi: float,
    direction: str = "decrease",
    marker_id: str = "apob",
) -> Effect:
    return Effect(
        intervention_id=intervention_id,
        marker_id=marker_id,
        direction=direction,
        effect_type="pct",
        effect_lo=effect_lo,
        effect_hi=effect_hi,
        baseline_mod_elevated=1.0,
        baseline_mod_lean=0.5,
        evidence_tag="meta",
        evidence_weight=1.0,
        time_lo_wk=4,
        time_hi_wk=8,
        citations=[Citation(author="X", journal="Y", year=2020)],
    )


@pytest.fixture
def apob_scenario():
    """User with elevated ApoB (110), several interventions to choose from."""
    markers = {"apob": _marker_apob()}
    interventions = {
        "psyllium": _iv("psyllium", ["viscous_fiber"]),
        "plant_sterols": _iv("plant_sterols", ["cholesterol_absorption_inhibition"]),
        "berberine": _iv("berberine", ["ldlr_upregulation"]),
        "soy_protein": _iv("soy_protein", ["sfa_reduction"], type="food"),
        "coconut_oil": _iv("coconut_oil", ["sfa_reduction"], type="food"),
    }
    effects = [
        _effect("psyllium", -10, -7),       # −8.5% midpoint
        _effect("plant_sterols", -10, -7),  # −8.5% midpoint
        _effect("berberine", -15, -10),     # −12.5% midpoint
        _effect("soy_protein", -7, -5),     # −6% midpoint
        _effect("coconut_oil", 6, 10, direction="increase"),  # RAISES ApoB
    ]
    profile = UserProfile(marker_values={"apob": 110}, phenotype="elevated")
    return profile, markers, interventions, effects


def test_solver_returns_plan(apob_scenario):
    profile, markers, interventions, effects = apob_scenario
    plan = solve(profile, markers, interventions, effects, budget=3)
    assert isinstance(plan, Plan)
    assert len(plan.interventions) <= 3
    assert len(plan.interventions) >= 1  # something should help


def test_solver_never_selects_raising_intervention(apob_scenario):
    """coconut_oil raises ApoB; the solver must never select it."""
    profile, markers, interventions, effects = apob_scenario
    plan = solve(profile, markers, interventions, effects, budget=5)
    assert "coconut_oil" not in plan.interventions


def test_solver_respects_budget(apob_scenario):
    profile, markers, interventions, effects = apob_scenario
    plan = solve(profile, markers, interventions, effects, budget=2)
    assert len(plan.interventions) <= 2


def test_solver_picks_highest_effect_at_budget_1(apob_scenario):
    """With budget=1, the solver picks berberine (highest single-intervention effect at −12.5%)."""
    profile, markers, interventions, effects = apob_scenario
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["berberine"]


def test_solver_returns_empty_when_at_optimal():
    """If the user is already at optimal, no interventions are selected."""
    markers = {"apob": _marker_apob()}
    interventions = {"psyllium": _iv("psyllium", ["viscous_fiber"])}
    effects = [_effect("psyllium", -10, -7)]
    profile = UserProfile(marker_values={"apob": 70}, phenotype="elevated")  # already <80
    plan = solve(profile, markers, interventions, effects, budget=3)
    assert plan.interventions == []


def test_solver_mechanism_overlap_does_not_double_count():
    """Two interventions in the same mechanism class don't both contribute their full effect."""
    markers = {"apob": _marker_apob()}
    interventions = {
        # Same mechanism: only one's effect should count, not the sum
        "psyllium": _iv("psyllium", ["viscous_fiber"]),
        "oat_beta_glucan": _iv("oat_beta_glucan", ["viscous_fiber"]),
        # Different mechanism: stacks on top
        "plant_sterols": _iv("plant_sterols", ["cholesterol_absorption_inhibition"]),
    }
    effects = [
        _effect("psyllium", -10, -7),         # midpoint −8.5%
        _effect("oat_beta_glucan", -7, -4),   # midpoint −5.5%
        _effect("plant_sterols", -10, -7),    # midpoint −8.5%
    ]
    profile = UserProfile(marker_values={"apob": 110}, phenotype="elevated")

    plan = solve(profile, markers, interventions, effects, budget=3)
    # All 3 fit in the budget, but the projected improvement should NOT be 8.5+5.5+8.5=22.5%
    # — psyllium and oat_beta_glucan overlap. Expected: max(8.5, 5.5) + 8.5 = 17% (no cross-class discount).
    # The MILP picks the better one within the viscous_fiber class.
    projected = plan.projected_marker_values["apob"]
    # 110 · (1 - 0.17) = 91.3
    assert 88 < projected < 95, f"projected apob {projected} suggests mechanism overlap not enforced"

    # And the selected stack must include psyllium (the better viscous-fiber pick), not oat_beta_glucan
    assert "psyllium" in plan.interventions
    assert "plant_sterols" in plan.interventions


def test_solver_treats_immutable_marker_as_uncovered():
    """A marker flagged immutable=true should NOT be a solver target; it goes straight to uncovered."""
    markers = {
        "apob": _marker_apob(),
        "lp_a": Marker(
            id="lp_a", name="Lipoprotein(a)", panel="advanced_lipids", units="mg/dL",
            direction="lower_is_better", ref_lo=0, ref_hi=75, opt_lo=0, opt_hi=30,
            immutable=True,
        ),
    }
    interventions = {
        "psyllium": _iv("psyllium", ["viscous_fiber"]),
        "fake_lpa_lowerer": _iv("fake_lpa_lowerer", ["niacin_pathway"]),
    }
    effects = [
        _effect("psyllium", -10, -7),
        # Even if some intervention claims to lower Lp(a), the immutable flag wins:
        _effect("fake_lpa_lowerer", -10, -7, marker_id="lp_a"),
    ]
    profile = UserProfile(marker_values={"apob": 110, "lp_a": 100}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=3)
    assert "lp_a" in plan.uncovered_markers
    assert "fake_lpa_lowerer" not in plan.interventions
    # ApoB should still be addressed
    assert "psyllium" in plan.interventions


def test_solver_reports_uncovered_markers():
    """If a marker has no eligible intervention, it shows up as uncovered."""
    markers = {
        "apob": _marker_apob(),
        "lp_a": Marker(
            id="lp_a", name="Lipoprotein(a)", panel="advanced_lipids", units="mg/dL",
            direction="lower_is_better", ref_lo=0, ref_hi=75, opt_lo=0, opt_hi=30,
        ),
    }
    interventions = {"psyllium": _iv("psyllium", ["viscous_fiber"])}
    effects = [_effect("psyllium", -10, -7)]  # only affects apob
    profile = UserProfile(marker_values={"apob": 110, "lp_a": 80}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=3)
    assert "lp_a" in plan.uncovered_markers
    assert "apob" not in plan.uncovered_markers
