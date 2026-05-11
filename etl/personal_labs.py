"""Map a Function Health biomarker_dump.json into {marker_id: float} for the solver.

The dump uses Function's lab-display names. This file holds the explicit
display-name → canonical-marker-id mapping plus qualitative-value parsing
(NEGATIVE, <10, A Pattern, etc.) so the Streamlit app can pre-populate.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# Repo-root .context dir (one level above etl/)
DEFAULT_DUMP = Path(__file__).resolve().parent.parent / ".context" / "biomarker_dump.json"


# Function-Health-display-name → canonical marker ID. None = intentionally skip
# (not a biomarker the engine targets, or duplicate of another mapped row).
NAME_TO_ID: dict[str, str | None] = {
    # Iron / nutrients
    "Ferritin": "ferritin",
    "Iron Binding Capacity": "tibc",
    "Iron": "serum_iron",
    "Iron % Saturation": "tsat",
    "Magnesium, RBC": "magnesium_rbc",
    "Zinc": "zinc",
    "Methylmalonic Acid (MMA)": "mma",
    "Vitamin D": "vitamin_d_25oh",
    "Homocysteine": "homocysteine",
    # Folate / B12 missing from this dump but mapping reserved for future:
    # "Folate": "folate",
    # "Vitamin B12": "vitamin_b12",
    # "Copper": "copper",
    # "Selenium": "selenium",

    # Heavy metals
    "Lead": "lead_blood",
    # Mercury / cadmium / arsenic missing from this dump
    "Biological Age": "phenoage",

    # Thyroid
    "Thyroxine (T4) Free": "ft4",
    "Triiodothyronine (T3) Free": "ft3",
    "Thyroid-Stimulating Hormone (TSH)": "tsh",
    "Thyroid Peroxidase Antibodies (TPO)": "tpo_ab",
    "Thyroglobulin Antibodies (TgAb)": "tgab",
    # rT3 not in this dump

    # Cardio basic
    "Apolipoprotein B (ApoB)": "apob",
    "LDL-Cholesterol": "ldl_c",
    "HDL-Cholesterol": "hdl_c",
    "Total Cholesterol": "total_cholesterol",
    "Total Cholesterol / HDL Ratio": "tc_hdl_ratio",
    "Non-HDL Cholesterol": "non_hdl_c",
    "Triglycerides": "triglycerides",
    "High-Sensitivity C-Reactive Protein (hs-CRP)": "hs_crp",
    "Lipoprotein (a)": "lp_a",

    # Advanced lipids
    "LDL Particle Number": "ldl_particle_number",
    "LDL Small": "ldl_small",
    "LDL Medium": "ldl_medium",
    "HDL Large": "hdl_large",
    "LDL Pattern": "ldl_pattern",  # A=1, B=2
    "LDL Peak Size": "ldl_peak_size",
    # apob_apoa1_ratio not directly in dump

    # Omega fatty acids
    "Omega-3 Total / OmegaCheck": "omega3_index",
    "Omega-3 Total": None,  # duplicate of OmegaCheck row
    "Omega-3: EPA": "epa",
    "Omega-3: DPA": "dpa",
    "Omega-3: DHA": "dha",
    "Omega-6 Total": "omega6_total",
    "Omega-6: Arachidonic Acid": "arachidonic_acid",
    "Omega-6: Linoleic Acid": "linoleic_acid",
    "Arachidonic Acid/EPA Ratio": "aa_epa_ratio",
    "Omega 6 / 3 Ratio": "omega6_3_ratio",

    # Liver
    "Aspartate Aminotransferase (AST)": "ast",
    "Alanine Transaminase (ALT)": "alt",
    "Alkaline Phosphatase (ALP)": "alp",
    "Gamma-glutamyl Transferase (GGT)": "ggt",
    "Total Bilirubin": "total_bilirubin",
    "Albumin": "albumin",
    "Globulin": "globulin",
    "Albumin / Globulin Ratio": "albumin_globulin_ratio",
    "Total Protein": "total_protein",

    # Kidney / electrolytes / pancreas
    "Blood Urea Nitrogen (BUN)": "bun",
    "Creatinine": "creatinine",
    "Creatinine-Based Estimated Glomerular Filtration Rate (eGFR)": "egfr",
    "Sodium": "sodium",
    "Potassium": "potassium",
    "Chloride": "chloride",
    "Carbon Dioxide": "bicarbonate",
    "Calcium": "calcium_serum",
    "Amylase": "amylase",
    "Lipase": "lipase",
    "Albumin, Random Urine without Creatinine": None,  # not directly UACR (no Cr ratio)

    # Metabolic
    "Glucose": "fasting_glucose",
    "Insulin": "fasting_insulin",
    "Hemoglobin A1c (HbA1c)": "hba1c",
    "Uric Acid": "uric_acid",
    "Leptin": "leptin",
    # HOMA-IR not directly in dump (computed)

    # Male hormones
    "Testosterone, Total": "total_testosterone",
    "Testosterone, Free": "free_testosterone",
    "Sex Hormone Binding Globulin (SHBG)": "shbg",
    "Estradiol (E2)": "estradiol_e2",
    "DHEA Sulfate": "dhea_s",
    "Luteinizing Hormone (LH)": "lh",
    "Follicle Stimulating Hormone (FSH)": "fsh",
    "Prolactin": "prolactin",
    "Cortisol": "cortisol",

    # CBC
    "White Blood Cell (WBC) Count": "wbc_count",
    "Red Blood Cell (RBC) Count": "rbc_count",
    "Hemoglobin": "hemoglobin",
    "Hematocrit": "hematocrit",
    "Mean Corpuscular Volume (MCV)": "mcv",
    "Mean Corpuscular Hemoglobin (MCH)": "mch",
    "Mean Corpuscular Hemoglobin Concentration (MCHC)": "mchc",
    "Red Cell Distribution Width (RDW)": "rdw",
    # Platelets not present in this dump

    # Immune (absolute counts in cells/uL — convert to ×10⁹/L by /1000)
    "Neutrophils": "neutrophils",
    "Lymphocytes": "lymphocytes",
    "Monocytes": "monocytes",
    "Eosinophils": "eosinophils",
    "Basophils": "basophils",
    # NLR not directly given (computable from neut/lym ratio)

    # Autoimmunity / PSA
    "Antinuclear Antibodies (ANA) Screen": "ana",
    "Rheumatoid Factor (RF)": "rf",
    "Prostate Specific Antigen (PSA), Total": "psa_total",
    "Prostate Specific Antigen (PSA), Free": "psa_free",
    "Prostate Specific Antigen (PSA) %, Free": "psa_free_percent",
    # anti-CCP, anti-dsDNA not in dump

    # Urinalysis (qualitative → numeric encoding handled below)
    "Color - Urine": "urine_appearance_color",
    "Specific Gravity - Urine": "urine_specific_gravity",
    "pH - Urine": "urine_ph",
    "Glucose - Urine": "urine_glucose",
    "Bilirubin - Urine": "urine_bilirubin",
    "Ketones - Urine": "urine_ketones",
    "Occult Blood - Urine": "urine_blood",
    "Protein - Urine": "urine_protein",
    "Nitrite - Urine": "urine_nitrites",
    "Leukocyte Esterase - Urine": "urine_leukocyte_esterase",

    # Explicitly skipped (not biomarkers the engine targets)
    "Appearance - Urine": None,  # subjective clarity, redundant with Color
    "White Blood Cell (WBC) - Urine": None,  # microscopy component
    "Red Blood Cell (RBC) - Urine": None,
    "Squamous Epithelial Cells - Urine": None,
    "Bacteria - Urine": None,
    "Hyaline Casts - Urine": None,
    "Myelocytes %": None,  # not in canonical
    "Absolute Myelocytes": None,
    "Neutrophils %": None,  # using absolute
    "Lymphocytes %": None,
    "Monocytes %": None,
    "Eosinophils %": None,
    "Basophils %": None,
    "ABO Group": None,
    "Rhesus (Rh) Factor": None,
}


# Multipliers applied AFTER numeric parsing, keyed by canonical marker ID.
# Use to harmonize lab units with the canonical Marker.units (which the solver
# uses for ref/opt comparisons).
UNIT_CONVERSIONS: dict[str, float] = {
    # Lab gives absolute count in cells/uL. Canonical markers use ×10⁹/L.
    # 1 cell/uL == 1e-3 ×10⁹/L.
    "neutrophils": 1e-3,
    "lymphocytes": 1e-3,
    "monocytes": 1e-3,
    "eosinophils": 1e-3,
    "basophils": 1e-3,
}


# Color / appearance numeric encoding (Armstrong-ish 1-5 hydration scale).
COLOR_SCALE: dict[str, float] = {
    "CLEAR": 1.0,
    "STRAW": 1.5,
    "PALE YELLOW": 2.0,
    "PALE": 2.0,
    "YELLOW": 3.0,
    "DARK YELLOW": 4.0,
    "AMBER": 5.0,
}

# LDL pattern: A = good (encoded as 1), B = bad (2)
LDL_PATTERN_SCALE: dict[str, float] = {"A": 1.0, "B": 2.0}


def _parse_value(raw: str, marker_id: str) -> float | None:
    """Convert a Function-display string into a float (or None if uninterpretable)."""
    if raw is None:
        return None
    s = str(raw).strip().upper()
    if not s:
        return None

    # Hard-coded categorical mappings come first
    if marker_id == "urine_appearance_color":
        for key, v in COLOR_SCALE.items():
            if key in s:
                return v
        return None
    if marker_id == "ldl_pattern":
        s2 = s.replace(" PATTERN", "").strip()
        if s2 in LDL_PATTERN_SCALE:
            return LDL_PATTERN_SCALE[s2]
        return None

    # Qualitative dipstick / antibody readouts → 0
    if s in {"NEGATIVE", "NONE SEEN", "NONE DETECTED", "NOT DETECTED",
             "NORMAL", "NEG"}:
        return 0.0

    # Censored numeric e.g. "<10", "<1.0", ">2000"
    m = re.match(r"^[<>]\s*(-?\d+(?:\.\d+)?)$", s)
    if m:
        n = float(m.group(1))
        return n / 2 if s.startswith("<") else n  # midpoint for left-censored

    # Try direct float first (the dump usually keeps value clean of units).
    try:
        return float(s)
    except ValueError:
        pass

    # Last resort: strip trailing non-numeric junk (units that occasionally bleed
    # into the value field). Use \s after the number to anchor — don't strip
    # decimal points.
    m = re.match(r"^(-?\d+(?:\.\d+)?)\s+\S", s)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    return None


def _parse_range_bound(s: str | None) -> float | None:
    """Parse a Function Health range bound. None means open-ended."""
    if s is None:
        return None
    s = str(s).strip()
    if not s or s.lower() in {"infinity", "-infinity"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def load_personal_labs(
    dump_path: Path = DEFAULT_DUMP,
) -> tuple[dict[str, float], dict[str, tuple[float | None, float | None]]]:
    """Read biomarker_dump.json.

    Returns (values, lab_ranges) where:
      - values: {marker_id: float} — ready for the solver
      - lab_ranges: {marker_id: (rangeMin, rangeMax)} from Function Health's
        per-marker reference ranges. Either bound can be None (open-ended).
        Use these instead of the engine's canonical ref_lo/ref_hi for display
        so the user sees the same "outside healthy" classification their lab
        showed them. Solver still uses opt_lo/opt_hi for gap calculations.
    """
    if not dump_path.exists():
        return {}, {}
    name_index = {k.strip(): v for k, v in NAME_TO_ID.items()}
    raw = json.loads(dump_path.read_text())
    values: dict[str, float] = {}
    ranges: dict[str, tuple[float | None, float | None]] = {}
    for entry in raw:
        name = entry.get("name", "").strip()
        if name not in name_index:
            continue
        marker_id = name_index[name]
        if marker_id is None:
            continue
        if marker_id in values:
            continue
        val = _parse_value(entry.get("value"), marker_id)
        if val is None:
            continue
        mult = UNIT_CONVERSIONS.get(marker_id, 1.0)
        values[marker_id] = val * mult
        lo = _parse_range_bound(entry.get("rangeMin"))
        hi = _parse_range_bound(entry.get("rangeMax"))
        if lo is not None:
            lo *= mult
        if hi is not None:
            hi *= mult
        if lo is not None or hi is not None:
            ranges[marker_id] = (lo, hi)
    return values, ranges


def unmapped_names(dump_path: Path = DEFAULT_DUMP) -> list[str]:
    """Diagnostic: which lab names in the dump aren't in NAME_TO_ID?"""
    if not dump_path.exists():
        return []
    name_index = {k.strip() for k in NAME_TO_ID}
    raw = json.loads(dump_path.read_text())
    return sorted({e.get("name", "").strip() for e in raw
                   if e.get("name", "").strip() not in name_index})


if __name__ == "__main__":
    labs, ranges = load_personal_labs()
    print(f"Loaded {len(labs)} marker values, {len(ranges)} with lab ranges.")
    for k, v in sorted(labs.items()):
        rng = ranges.get(k)
        rng_str = f"  range [{rng[0]}, {rng[1]}]" if rng else ""
        print(f"  {k:35s}  {v:>10g}{rng_str}")
    unmapped = unmapped_names()
    if unmapped:
        print(f"\nUnmapped lab names ({len(unmapped)}):")
        for n in unmapped:
            print(f"  {n}")
