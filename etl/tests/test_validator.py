"""Tests for the referential + plausibility validator."""
from pathlib import Path

import pytest
import yaml

from fhetl.schemas import Effect, Intervention
from fhetl.validator import Registry, ValidationResult, validate_effect, validate_intervention


# Minimal valid registry built from in-memory data — does NOT touch the on-disk canonical refs,
# so the tests stay independent of corpus state.
@pytest.fixture
def registry() -> Registry:
    return Registry(
        marker_ids={"apob", "ldl_c", "hdl_c"},
        intervention_ids={"psyllium_husk_10g", "olive_oil_30ml"},
        mechanism_ids={"viscous_fiber", "bile_acid_sequestration", "mufa_substitution"},
    )


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
    pmid: "30101536"
"""


def _effect(overrides: dict | None = None) -> Effect:
    data = yaml.safe_load(VALID_EFFECT_YAML)
    if overrides:
        data.update(overrides)
    return Effect.model_validate(data)


def test_valid_effect_against_registry_passes(registry: Registry):
    result = validate_effect(_effect(), registry)
    assert result.ok
    assert result.errors == []


def test_effect_unknown_marker_rejected(registry: Registry):
    result = validate_effect(_effect({"marker_id": "ldl_particle_number"}), registry)
    assert not result.ok
    assert any("marker" in e.lower() for e in result.errors)


def test_effect_unknown_intervention_rejected(registry: Registry):
    result = validate_effect(_effect({"intervention_id": "unknown_supplement"}), registry)
    assert not result.ok
    assert any("intervention" in e.lower() for e in result.errors)


def test_effect_implausible_pct_magnitude_warned(registry: Registry):
    """pct effects > 60% are implausible for non-pharma interventions; warn."""
    result = validate_effect(_effect({"effect_lo": -85, "effect_hi": -70}), registry)
    assert result.ok  # not rejected
    assert any("implausible" in w.lower() or "magnitude" in w.lower() for w in result.warnings)


VALID_INTERVENTION_YAML = """
id: psyllium_husk_10g
canonical_name: Psyllium husk
type: supplement
dose_amount: 10
dose_unit: g_per_day
mechanisms: [viscous_fiber, bile_acid_sequestration]
"""


def _intervention(overrides: dict | None = None) -> Intervention:
    data = yaml.safe_load(VALID_INTERVENTION_YAML)
    if overrides:
        data.update(overrides)
    return Intervention.model_validate(data)


def test_valid_intervention_against_registry_passes(registry: Registry):
    result = validate_intervention(_intervention(), registry)
    assert result.ok


def test_intervention_unknown_mechanism_warned_not_rejected(registry: Registry):
    """Unknown mechanisms produce a warning so research can extend the enum with review."""
    result = validate_intervention(_intervention({"mechanisms": ["viscous_fiber", "new_pathway"]}), registry)
    assert result.ok
    assert any("mechanism" in w.lower() for w in result.warnings)
    assert any("new_pathway" in w for w in result.warnings)


def test_registry_loads_from_canonical_yaml(tmp_path: Path):
    """Registry.from_canonical loads markers and mechanisms from the canonical YAML files."""
    markers_yaml = tmp_path / "markers.yaml"
    markers_yaml.write_text(yaml.safe_dump({"markers": [
        {"id": "apob", "panel": "cardiovascular"},
        {"id": "ldl_c", "panel": "cardiovascular"},
    ]}))
    mechanisms_yaml = tmp_path / "mechanisms.yaml"
    mechanisms_yaml.write_text(yaml.safe_dump({"mechanisms": [
        {"id": "viscous_fiber", "description": "x"},
    ]}))

    registry = Registry.from_canonical(markers_yaml, mechanisms_yaml)
    assert "apob" in registry.marker_ids
    assert "ldl_c" in registry.marker_ids
    assert "viscous_fiber" in registry.mechanism_ids
