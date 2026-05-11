"""Tests for the Intervention schema."""
import pytest
import yaml
from pydantic import ValidationError

from fhetl.schemas import Intervention


VALID_INTERVENTION_YAML = """
id: psyllium_husk_10g
canonical_name: Psyllium husk
type: supplement
dose_amount: 10
dose_unit: g_per_day
dose_split: 5g TID with water
mechanisms: [viscous_fiber, bile_acid_sequestration]
dietary_tags: [vegan, vegetarian, gluten_free]
exclusions:
  - type: condition
    value: bowel_obstruction
  - type: drug_interaction
    value: levothyroxine_within_2h
"""


def _load(overrides: dict | None = None) -> dict:
    data = yaml.safe_load(VALID_INTERVENTION_YAML)
    if overrides:
        data.update(overrides)
    return data


def test_valid_intervention_parses():
    iv = Intervention.model_validate(_load())
    assert iv.id == "psyllium_husk_10g"
    assert iv.type == "supplement"
    assert iv.dose_amount == 10
    assert "viscous_fiber" in iv.mechanisms
    assert len(iv.exclusions) == 2


def test_rejects_unknown_type():
    with pytest.raises(ValidationError):
        Intervention.model_validate(_load({"type": "drug"}))


def test_rejects_negative_dose():
    with pytest.raises(ValidationError):
        Intervention.model_validate(_load({"dose_amount": -5}))


def test_mechanisms_default_empty():
    data = _load()
    del data["mechanisms"]
    iv = Intervention.model_validate(data)
    assert iv.mechanisms == []


def test_dietary_tags_default_empty():
    data = _load()
    del data["dietary_tags"]
    iv = Intervention.model_validate(data)
    assert iv.dietary_tags == []


def test_exclusions_default_empty():
    data = _load()
    del data["exclusions"]
    iv = Intervention.model_validate(data)
    assert iv.exclusions == []


def test_rejects_unknown_exclusion_type():
    with pytest.raises(ValidationError):
        Intervention.model_validate(_load({
            "exclusions": [{"type": "vibes", "value": "bad"}]
        }))
