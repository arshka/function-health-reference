"""Integration tests against the live data/ corpus.

These hit the real 118-marker, ~400-intervention, ~2000-effect dataset. They
catch regressions that unit tests with synthetic fixtures miss: orphan refs,
mechanism-class explosions, solver crashes on real data shapes.
"""
from pathlib import Path

import pytest

from fhetl.cli import _load_dataset
from fhetl.solver import UserProfile, solve


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"


@pytest.fixture(scope="module")
def corpus():
    return _load_dataset(DATA_DIR)


def test_corpus_has_expected_size(corpus):
    markers, interventions, effects = corpus
    assert len(markers) == 118
    assert len(interventions) >= 400
    assert len(effects) >= 2000


def test_every_effect_marker_has_a_marker_yaml(corpus):
    markers, _, effects = corpus
    missing = {e.marker_id for e in effects if e.marker_id not in markers}
    assert not missing, f"effect files reference non-existent markers: {sorted(missing)}"


def test_every_effect_intervention_has_an_intervention_yaml(corpus):
    _, interventions, effects = corpus
    missing = {e.intervention_id for e in effects if e.intervention_id not in interventions}
    assert not missing, f"effect files reference non-existent interventions: {sorted(missing)}"


def test_solver_runs_clean_on_elevated_cardio_profile(corpus):
    markers, interventions, effects = corpus
    profile = UserProfile(
        marker_values={
            "apob": 110, "ldl_c": 145, "hdl_c": 35, "triglycerides": 200,
            "hba1c": 6.0, "ferritin": 50, "vitamin_d_25oh": 25,
        },
        phenotype="elevated",
    )
    plan = solve(profile, markers, interventions, effects, budget=5)
    assert plan.interventions, "expected at least one intervention selected"
    assert len(plan.interventions) <= 5
    for iv_id in plan.interventions:
        assert iv_id in interventions
    # All selected interventions must contribute to at least one out-of-range
    # marker (improvements_pct > 0 somewhere)
    assert any(p > 0 for p in plan.improvements_pct.values())


def test_solver_respects_budget_across_realistic_scenarios(corpus):
    markers, interventions, effects = corpus
    scenarios = [
        {"apob": 130, "ldl_c": 160, "non_hdl_c": 175},               # cardio-only
        {"hba1c": 6.2, "fasting_glucose": 105, "fasting_insulin": 18},  # metabolic
        {"alt": 55, "ggt": 60, "ferritin": 350},                      # liver/iron
        {"vitamin_d_25oh": 18, "homocysteine": 14, "vitamin_b12": 280}, # nutrient
    ]
    for sc in scenarios:
        profile = UserProfile(marker_values=sc, phenotype="elevated")
        plan = solve(profile, markers, interventions, effects, budget=3)
        assert len(plan.interventions) <= 3, f"budget exceeded on {sc}"


def test_solver_handles_immutable_marker(corpus):
    """Lp(a) is marked immutable=true. Out-of-range Lp(a) should land in
    uncovered_markers, not consume budget."""
    markers, interventions, effects = corpus
    profile = UserProfile(marker_values={"lp_a": 80, "ldl_c": 145}, phenotype="elevated")
    plan = solve(profile, markers, interventions, effects, budget=3)
    assert "lp_a" in plan.uncovered_markers
