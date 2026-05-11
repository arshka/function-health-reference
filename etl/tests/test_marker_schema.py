"""Tests for the Marker schema."""
import pytest
import yaml
from pydantic import ValidationError

from fhetl.schemas import Marker


VALID_MARKER_YAML = """
id: apob
name: Apolipoprotein B
panel: cardiovascular
units: mg/dL
direction: lower_is_better
ref_lo: 40
ref_hi: 125
opt_lo: 40
opt_hi: 80
immutable: false
demographic_modifiers:
  - trait: south_asian
    opt_lo: 40
    opt_hi: 70
"""


def _load(overrides: dict | None = None) -> dict:
    data = yaml.safe_load(VALID_MARKER_YAML)
    if overrides:
        data.update(overrides)
    return data


def test_valid_marker_parses():
    marker = Marker.model_validate(_load())
    assert marker.id == "apob"
    assert marker.direction == "lower_is_better"
    assert marker.opt_hi == 80
    assert marker.immutable is False
    assert len(marker.demographic_modifiers) == 1
    assert marker.demographic_modifiers[0].trait == "south_asian"


def test_rejects_reference_range_reversed():
    with pytest.raises(ValidationError, match="ref_lo.*ref_hi"):
        Marker.model_validate(_load({"ref_lo": 125, "ref_hi": 40}))


def test_rejects_optimal_range_reversed():
    with pytest.raises(ValidationError, match="opt_lo.*opt_hi"):
        Marker.model_validate(_load({"opt_lo": 80, "opt_hi": 40}))


def test_rejects_optimal_range_outside_reference_range():
    """Optimal range must be contained within the reference range."""
    with pytest.raises(ValidationError, match="optimal.*reference"):
        Marker.model_validate(_load({"opt_lo": 20, "opt_hi": 80, "ref_lo": 40}))


def test_rejects_unknown_direction():
    with pytest.raises(ValidationError):
        Marker.model_validate(_load({"direction": "lower_better"}))


def test_immutable_defaults_false():
    data = _load()
    del data["immutable"]
    marker = Marker.model_validate(data)
    assert marker.immutable is False


def test_demographic_modifier_optional():
    data = _load()
    del data["demographic_modifiers"]
    marker = Marker.model_validate(data)
    assert marker.demographic_modifiers == []


def test_demographic_modifier_range_must_be_ordered():
    with pytest.raises(ValidationError):
        Marker.model_validate(_load({
            "demographic_modifiers": [{"trait": "south_asian", "opt_lo": 70, "opt_hi": 40}]
        }))
