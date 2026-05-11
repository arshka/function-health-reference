"""Tests for the Effect schema — one rule per test."""
import pytest
import yaml
from pydantic import ValidationError

from fhetl.schemas import Effect


VALID_EFFECT_YAML = """
intervention_id: psyllium_husk_10g
marker_id: apob
direction: decrease
effect_type: pct
effect_lo: -10
effect_hi: -7
baseline_mod_elevated: 1.0
baseline_mod_lean: 0.5
evidence_tag: meta
evidence_weight: 1.0
time_lo_wk: 4
time_hi_wk: 8
citations:
  - author: Jovanovski
    journal: AJCN
    year: 2018
    vol: 108
    page: 922
    pmid: "30101536"
"""


def _load(overrides: dict | None = None) -> dict:
    """Load the valid YAML and apply per-test overrides."""
    data = yaml.safe_load(VALID_EFFECT_YAML)
    if overrides:
        data.update(overrides)
    return data


def test_valid_effect_parses():
    """A well-formed effect YAML parses into an Effect model."""
    effect = Effect.model_validate(_load())
    assert effect.intervention_id == "psyllium_husk_10g"
    assert effect.marker_id == "apob"
    assert effect.effect_lo == -10
    assert effect.effect_hi == -7
    assert effect.evidence_tag == "meta"
    assert len(effect.citations) == 1
    assert effect.citations[0].pmid == "30101536"


def test_rejects_effect_range_reversed():
    """effect_lo > effect_hi is rejected (range must be ordered)."""
    with pytest.raises(ValidationError, match="effect_lo.*effect_hi"):
        Effect.model_validate(_load({"effect_lo": -7, "effect_hi": -10}))


def test_rejects_sign_mismatched_with_direction_decrease():
    """direction=decrease must have non-positive effect bounds."""
    with pytest.raises(ValidationError, match="decrease"):
        Effect.model_validate(_load({"effect_lo": 7, "effect_hi": 10, "direction": "decrease"}))


def test_rejects_sign_mismatched_with_direction_increase():
    """direction=increase must have non-negative effect bounds."""
    with pytest.raises(ValidationError, match="increase"):
        Effect.model_validate(_load({"effect_lo": -10, "effect_hi": -7, "direction": "increase"}))


def test_rejects_time_range_reversed():
    """time_lo_wk > time_hi_wk is rejected."""
    with pytest.raises(ValidationError, match="time"):
        Effect.model_validate(_load({"time_lo_wk": 8, "time_hi_wk": 4}))


def test_rejects_lean_modifier_exceeding_elevated():
    """baseline_mod_lean must not exceed baseline_mod_elevated."""
    with pytest.raises(ValidationError, match="baseline"):
        Effect.model_validate(_load({"baseline_mod_lean": 1.2, "baseline_mod_elevated": 1.0}))


def test_rejects_evidence_weight_inconsistent_with_tag():
    """evidence_weight must match the canonical weight for its evidence_tag."""
    with pytest.raises(ValidationError, match="evidence_weight"):
        Effect.model_validate(_load({"evidence_tag": "meta", "evidence_weight": 0.4}))


def test_rejects_unknown_evidence_tag():
    """Evidence tag outside the controlled enum is rejected."""
    with pytest.raises(ValidationError):
        Effect.model_validate(_load({"evidence_tag": "meta-analysis"}))


def test_rejects_pmcid_in_pmid_field():
    """PMID field must be digits only (PMCIDs like PMC5394769 are rejected)."""
    data = _load()
    data["citations"][0]["pmid"] = "PMC5394769"
    with pytest.raises(ValidationError):
        Effect.model_validate(data)


def test_rejects_missing_citations():
    """An effect must have at least one citation."""
    with pytest.raises(ValidationError):
        Effect.model_validate(_load({"citations": []}))
