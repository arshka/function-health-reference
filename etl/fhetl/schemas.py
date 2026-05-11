"""Pydantic schemas for the biomarker intervention dataset."""
from typing import Literal

from pydantic import BaseModel, Field, model_validator


EVIDENCE_WEIGHTS: dict[str, float] = {
    "meta": 1.0,
    "rct": 0.85,
    "cohort": 0.65,
    "mr": 0.7,
    "mechanism": 0.4,
    "one_trial": 0.5,
}


class Citation(BaseModel):
    author: str
    journal: str
    year: int = Field(ge=1970, le=2030)
    vol: int | None = None
    page: int | str | None = None
    pmid: str | None = Field(default=None, pattern=r"^\d{7,9}$")


EvidenceTag = Literal["meta", "rct", "cohort", "mr", "mechanism", "one_trial"]
Direction = Literal["increase", "decrease"]
EffectType = Literal["pct", "absolute"]
MarkerDirection = Literal["lower_is_better", "higher_is_better", "in_band"]
InterventionType = Literal["food", "supplement", "activity", "behavior"]
ExclusionType = Literal["condition", "drug_interaction", "gene", "dietary"]


class Exclusion(BaseModel):
    type: ExclusionType
    value: str


class Intervention(BaseModel):
    id: str
    canonical_name: str
    type: InterventionType
    dose_amount: float = Field(ge=0)
    dose_unit: str
    dose_split: str | None = None
    mechanisms: list[str] = Field(default_factory=list)
    dietary_tags: list[str] = Field(default_factory=list)
    exclusions: list[Exclusion] = Field(default_factory=list)


class DemographicModifier(BaseModel):
    trait: str
    opt_lo: float | None = None
    opt_hi: float | None = None
    skip: bool = False

    @model_validator(mode="after")
    def _check_range(self) -> "DemographicModifier":
        if self.opt_lo is not None and self.opt_hi is not None and self.opt_lo > self.opt_hi:
            raise ValueError(
                f"demographic_modifier opt_lo ({self.opt_lo}) must be ≤ opt_hi ({self.opt_hi})"
            )
        return self


class Marker(BaseModel):
    id: str
    name: str
    panel: str
    units: str
    direction: MarkerDirection
    ref_lo: float
    ref_hi: float
    opt_lo: float
    opt_hi: float
    immutable: bool = False
    demographic_modifiers: list[DemographicModifier] = Field(default_factory=list)

    @model_validator(mode="after")
    def _check_ranges(self) -> "Marker":
        if self.ref_lo > self.ref_hi:
            raise ValueError(
                f"ref_lo ({self.ref_lo}) must be ≤ ref_hi ({self.ref_hi})"
            )
        if self.opt_lo > self.opt_hi:
            raise ValueError(
                f"opt_lo ({self.opt_lo}) must be ≤ opt_hi ({self.opt_hi})"
            )
        if self.opt_lo < self.ref_lo or self.opt_hi > self.ref_hi:
            raise ValueError(
                f"optimal range [{self.opt_lo}, {self.opt_hi}] must lie within "
                f"reference range [{self.ref_lo}, {self.ref_hi}]"
            )
        return self


class Effect(BaseModel):
    intervention_id: str
    marker_id: str
    direction: Direction
    effect_type: EffectType
    effect_lo: float
    effect_hi: float
    baseline_mod_elevated: float = Field(ge=0, le=2)
    baseline_mod_lean: float = Field(ge=0, le=2)
    evidence_tag: EvidenceTag
    evidence_weight: float = Field(ge=0, le=1)
    time_lo_wk: int = Field(ge=0, le=520)
    time_hi_wk: int = Field(ge=0, le=520)
    citations: list[Citation] = Field(min_length=1)

    @model_validator(mode="after")
    def _check_coherent(self) -> "Effect":
        if self.effect_lo > self.effect_hi:
            raise ValueError(
                f"effect_lo ({self.effect_lo}) must be ≤ effect_hi ({self.effect_hi})"
            )
        if self.direction == "decrease" and self.effect_hi > 0:
            raise ValueError(
                f"direction=decrease requires non-positive effect bounds "
                f"(got effect_lo={self.effect_lo}, effect_hi={self.effect_hi})"
            )
        if self.direction == "increase" and self.effect_lo < 0:
            raise ValueError(
                f"direction=increase requires non-negative effect bounds "
                f"(got effect_lo={self.effect_lo}, effect_hi={self.effect_hi})"
            )
        if self.time_lo_wk > self.time_hi_wk:
            raise ValueError(
                f"time_lo_wk ({self.time_lo_wk}) must be ≤ time_hi_wk ({self.time_hi_wk})"
            )
        if self.baseline_mod_lean > self.baseline_mod_elevated:
            raise ValueError(
                f"baseline_mod_lean ({self.baseline_mod_lean}) must not exceed "
                f"baseline_mod_elevated ({self.baseline_mod_elevated}); cited evidence "
                f"assumes elevated-baseline subjects and lean-baseline effects are smaller"
            )
        expected_weight = EVIDENCE_WEIGHTS[self.evidence_tag]
        if abs(self.evidence_weight - expected_weight) > 0.01:
            raise ValueError(
                f"evidence_weight={self.evidence_weight} does not match canonical weight "
                f"{expected_weight} for evidence_tag={self.evidence_tag!r}"
            )
        return self
