"""Tests for solver v2: multi-mechanism overlap.

V1 placed each intervention in exactly ONE mechanism class (its first mechanism).
V2 places each intervention in its FULL mechanism set, with a per-(i, j) constraint
that prevents an intervention from contributing to a marker via more than one
mechanism class (no double-counting).

The visible behavior change: an intervention with [shared_mech, unique_mech] can
"escape" overlap with another [shared_mech]-only intervention by being primary in
its unique class — letting both contribute. V1 silently lost that, because the
multi-mech intervention's secondary mechanism was invisible.
"""
import pytest

from fhetl.schemas import Citation, Effect, Intervention, Marker
from fhetl.solver import UserProfile, solve


def _marker_ldl() -> Marker:
    return Marker(
        id="ldl_c",
        name="LDL-C",
        panel="cardiovascular",
        units="mg/dL",
        direction="lower_is_better",
        ref_lo=40,
        ref_hi=200,
        opt_lo=40,
        opt_hi=100,
    )


def _iv(id: str, mechanisms: list[str]) -> Intervention:
    return Intervention(
        id=id,
        canonical_name=id,
        type="supplement",
        dose_amount=1,
        dose_unit="unit",
        mechanisms=mechanisms,
    )


def _effect(intervention_id: str, lo: float, hi: float, marker_id: str = "ldl_c") -> Effect:
    return Effect(
        intervention_id=intervention_id,
        marker_id=marker_id,
        direction="decrease",
        effect_type="pct",
        effect_lo=lo,
        effect_hi=hi,
        baseline_mod_elevated=1.0,
        baseline_mod_lean=0.5,
        evidence_tag="meta",
        evidence_weight=1.0,
        time_lo_wk=4,
        time_hi_wk=8,
        citations=[Citation(author="X", journal="Y", year=2020)],
    )


def test_multi_mech_intervention_escapes_overlap_via_unique_class():
    """psyllium [viscous_fiber, BAS] and cholestyramine [BAS] both reduce LDL by 10%.

    Without v2: psyllium's primary class is viscous_fiber; cholestyramine is in BAS.
    They share NO class. Both contribute. (V1 already gives total 20%.)

    With v2 multi-class membership: psyllium is in BOTH {VF, BAS}. The solver still
    chooses an arrangement where psyllium covers VF and cholestyramine covers BAS,
    so the outcome is the same. This test guards against regressions.
    """
    markers = {"ldl_c": _marker_ldl()}
    interventions = {
        "psyllium": _iv("psyllium", ["viscous_fiber", "bile_acid_sequestration"]),
        "cholestyramine": _iv("cholestyramine", ["bile_acid_sequestration"]),
    }
    effects = [_effect("psyllium", -10, -10), _effect("cholestyramine", -10, -10)]
    profile = UserProfile(marker_values={"ldl_c": 150}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=2)
    assert set(plan.interventions) == {"psyllium", "cholestyramine"}
    # Combined improvement should be ~20% (the gap is 33%, well above 20%).
    assert plan.improvements_pct["ldl_c"] == pytest.approx(20.0, abs=0.01)


def test_unique_mechanism_unlocks_paired_contribution():
    """The case where v2 strictly outperforms v1:

    A=[shared, unique], B=[shared]. Both reduce LDL by 10%.

    V1: both A and B's FIRST mechanism is `shared`. They land in the same class.
    Solver picks one as primary → total improvement is only 10%.

    V2: A is in both `shared` AND `unique` classes. Solver picks A primary in
    `unique` and B primary in `shared` → total improvement is 20%.
    """
    markers = {"ldl_c": _marker_ldl()}
    interventions = {
        "A": _iv("A", ["shared_mech", "unique_to_a"]),
        "B": _iv("B", ["shared_mech"]),
    }
    effects = [_effect("A", -10, -10), _effect("B", -10, -10)]
    profile = UserProfile(marker_values={"ldl_c": 150}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=2)
    assert set(plan.interventions) == {"A", "B"}
    # With v2's multi-class membership, A can escape the shared class via its
    # unique mechanism. Total should be 20%, not 10%.
    assert plan.improvements_pct["ldl_c"] == pytest.approx(20.0, abs=0.01)


def test_intervention_cannot_double_count_via_multiple_mechanisms():
    """An intervention with two mechanisms targeting one marker must contribute
    its effect EXACTLY ONCE.

    Without the per-(i, j) constraint, v2's multi-class membership would allow a
    single intervention to be 'primary' in BOTH of its classes for the same
    marker, counting its effect twice. The per-(i, j) constraint prevents this.

    Setup: A=[mech_x, mech_y] is the only intervention. Effect -10% on LDL.
    Expected improvement: 10% (not 20%).
    """
    markers = {"ldl_c": _marker_ldl()}
    interventions = {
        "A": _iv("A", ["mech_x", "mech_y"]),
    }
    effects = [_effect("A", -10, -10)]
    profile = UserProfile(marker_values={"ldl_c": 150}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["A"]
    assert plan.improvements_pct["ldl_c"] == pytest.approx(10.0, abs=0.01)


def test_singleton_intervention_no_mechanisms_still_works():
    """An intervention with NO mechanisms gets its own singleton class,
    just like v1. Sanity check that v2 doesn't regress empty-mechanism behavior.
    """
    markers = {"ldl_c": _marker_ldl()}
    interventions = {"foo": _iv("foo", [])}
    effects = [_effect("foo", -10, -10)]
    profile = UserProfile(marker_values={"ldl_c": 150}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=1)
    assert plan.interventions == ["foo"]
    assert plan.improvements_pct["ldl_c"] == pytest.approx(10.0, abs=0.01)


def test_three_way_shared_mechanism_overlap():
    """Three interventions all share the same primary mechanism.

    Only one can be primary in that class. With budget=3, the other two add
    nothing (v1 behavior preserved).
    """
    markers = {"ldl_c": _marker_ldl()}
    interventions = {
        "A": _iv("A", ["m"]),
        "B": _iv("B", ["m"]),
        "C": _iv("C", ["m"]),
    }
    effects = [_effect("A", -10, -10), _effect("B", -8, -8), _effect("C", -5, -5)]
    profile = UserProfile(marker_values={"ldl_c": 150}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=3)
    # Solver should pick only the best one in the shared class (A, -10%).
    # Adding B or C costs a budget slot for no marginal gain (parsimony penalty).
    assert plan.interventions == ["A"]
    assert plan.improvements_pct["ldl_c"] == pytest.approx(10.0, abs=0.01)
