"""Referential integrity + plausibility validator.

Runs *after* Pydantic shape/coherence validation. This layer needs external
state (canonical reference IDs) and produces structured errors + warnings.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from fhetl.schemas import Effect, Intervention


# Per-marker plausibility ceilings for non-pharmacological interventions.
# Effects exceeding these are flagged as warnings — not errors — because
# the source paper may genuinely show a larger effect (e.g., red yeast rice
# is statin-equivalent and legitimately produces 25%+ ApoB reductions).
PCT_CEILING_DEFAULT = 60.0  # %
ABS_CEILING_PER_MARKER: dict[str, float] = {
    "ldl_c": 80.0,   # mg/dL — beyond this is pharma territory
    "apob": 60.0,    # mg/dL
    "hba1c": 2.0,    # %
}


@dataclass(frozen=True)
class Registry:
    """Canonical reference set for referential integrity checks."""

    marker_ids: set[str] = field(default_factory=set)
    intervention_ids: set[str] = field(default_factory=set)
    mechanism_ids: set[str] = field(default_factory=set)

    @classmethod
    def from_canonical(
        cls,
        markers_yaml: Path,
        mechanisms_yaml: Path,
        interventions_yaml: Path | None = None,
    ) -> "Registry":
        with markers_yaml.open() as f:
            markers = yaml.safe_load(f).get("markers", [])
        with mechanisms_yaml.open() as f:
            mechanisms = yaml.safe_load(f).get("mechanisms", [])
        intervention_ids: set[str] = set()
        if interventions_yaml and interventions_yaml.exists():
            with interventions_yaml.open() as f:
                intervention_ids = {iv["id"] for iv in yaml.safe_load(f).get("interventions", [])}
        return cls(
            marker_ids={m["id"] for m in markers},
            intervention_ids=intervention_ids,
            mechanism_ids={m["id"] for m in mechanisms},
        )


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_effect(effect: Effect, registry: Registry) -> ValidationResult:
    result = ValidationResult()

    if effect.marker_id not in registry.marker_ids:
        result.errors.append(f"unknown marker_id: {effect.marker_id!r}")

    # Intervention registry check is skipped if the registry has no interventions yet
    # (allows extracting effects before all intervention files exist).
    if registry.intervention_ids and effect.intervention_id not in registry.intervention_ids:
        result.errors.append(f"unknown intervention_id: {effect.intervention_id!r}")

    # Plausibility (warnings only)
    magnitude = max(abs(effect.effect_lo), abs(effect.effect_hi))
    if effect.effect_type == "pct" and magnitude > PCT_CEILING_DEFAULT:
        result.warnings.append(
            f"implausible magnitude: {magnitude}% exceeds {PCT_CEILING_DEFAULT}% ceiling "
            f"for non-pharma interventions on {effect.marker_id}"
        )
    elif effect.effect_type == "absolute":
        ceiling = ABS_CEILING_PER_MARKER.get(effect.marker_id)
        if ceiling is not None and magnitude > ceiling:
            result.warnings.append(
                f"implausible magnitude: {magnitude} exceeds {ceiling} ceiling "
                f"for {effect.marker_id}"
            )

    return result


def validate_intervention(intervention: Intervention, registry: Registry) -> ValidationResult:
    result = ValidationResult()

    for mechanism in intervention.mechanisms:
        if mechanism not in registry.mechanism_ids:
            result.warnings.append(
                f"unknown mechanism {mechanism!r} on intervention {intervention.id!r}; "
                f"add to canonical/mechanisms.yaml if novel, or normalize to existing"
            )

    return result
