# Function Health Reference

Deep-research reference notes for interpreting [Function Health](https://www.functionhealth.com/) blood-panel results, organized by panel.

## What this is

A set of long-form, citation-heavy markdown documents written to support **interpreting your own labs against optimal-for-longevity ranges, not just lab-flagged "in range / out of range" cutoffs.** Each panel file covers:

- What each marker measures (assay, units, biological role)
- Why it matters (with primary literature: meta-analyses, large cohorts, MR studies, RCTs)
- Conventional reference range vs. optimization / functional-medicine "optimal" range
- Common confounders, drug effects, and assay artifacts
- Suggested follow-up tests when something is flagged

Effect-size files (`effect_sizes_*.md`) tabulate how much a given intervention (lifestyle, supplement, or drug) moves a given marker, with effect size, time-to-peak, and source citation.

## Important caveats

- **Calibrated to a healthy young male (~20 yo) by default.** Optimal ranges, prior probabilities, and threshold judgments throughout assume that demographic. Female, older, or known-disease readers should treat the optimization framings with skepticism and lean on the conventional reference ranges + their physician's read.
- **Not medical advice.** These are research notes. Talk to a doctor before changing supplements, medications, or diet based on a lab result.
- **"Optimal" ranges are practitioner-consensus, not RCT-validated.** Where mainstream medicine and longevity / functional-medicine views diverge (TSH, ferritin, ApoB, vit D, etc.), both positions are presented. The reader should weight them according to their own clinical context.
- **Effect sizes are population averages.** Individual response varies; the projection method (see `effect_sizes_INDEX.md`) is meant to be tested against your own next draw, not trusted as a guarantee.

## Files

### Panel reference docs
| File | Coverage |
|---|---|
| `autoimmunity_panel.md` | ANA, RF, anti-dsDNA, etc. |
| `biomarker_confounds_reference.md` | Diurnal, fasting, hydration, exercise, biotin, supplement confounds |
| `blood_cbc_indices.md` | Hgb, Hct, MCV, MCH, MCHC, RDW, RBC, platelets, ABO/Rh |
| `heart_lipids_basic.md` | Total chol, LDL-C, HDL-C, TG, non-HDL, ApoB |
| `heart_lipids_advanced.md` | Lp(a), NMR LipoProfile, particle subfractions, ApoE genotyping |
| `heavy_metals_and_biological_age.md` | Pb, Hg, As, Cd; PhenoAge; biological-age clocks |
| `hormones_male_panel.md` | Total T, Free T, SHBG, FSH, LH, E2, DHEA-S, prolactin |
| `immune_cbc_differential.md` | WBC, neutrophils, lymphocytes, monocytes, eosinophils, NLR |
| `kidney_electrolytes_pancreas.md` | Cr, BUN, eGFR, Na, K, Cl, CO₂, Ca, Phos, lipase |
| `liver_panel.md` | ALT, AST, ALP, GGT, bilirubin, albumin, total protein |
| `metabolic_panel.md` | Glucose, HbA1c, insulin, HOMA-IR, uric acid |
| `nutrients_omega_fatty_acids.md` | Omega-3 Index, EPA, DHA, AA:EPA ratio, omega-6:3 |
| `nutrients_vitamins_minerals.md` | Vit D, B12, folate, MMA, Hcy, ferritin, TSAT, iron, Mg, Zn, Cu, selenium |
| `prostate_psa.md` | PSA, free PSA |
| `thyroid_panel.md` | TSH, FT4, FT3, rT3, TPO Ab, TgAb |
| `urinalysis_panel.md` | UA dipstick + microscopy: glucose, ketones, protein, blood, nitrites, casts, etc. |

### Cross-panel effect sizes
| File | Coverage |
|---|---|
| `effect_sizes_INDEX.md` | Cross-cutting interventions; how to build a personal projection |
| `effect_sizes_cardiovascular.md` | ApoB, LDL-C, Lp(a), hs-CRP, BP — interventions and their measured deltas |
| `effect_sizes_endocrine.md` | T, SHBG, E2, DHEA-S, cortisol, TSH, prolactin |
| `effect_sizes_hematology_other.md` | Hgb, Hct, ferritin, TSAT, RDW, WBC subsets, platelets |
| `effect_sizes_metabolic_liver.md` | Glucose, A1c, insulin, UA, ALT/AST/GGT |
| `effect_sizes_nutrients.md` | Vit D, B12, folate, Mg, Zn, omega-3 — supplementation and dietary effect sizes |

## How to use

1. Get a Function Health draw (or any equivalent panel from Quest / LabCorp / Boston Heart).
2. For each marker that's flagged or sub-optimal, open the corresponding panel file and read:
   - "Optimal" section to understand where it sits vs. longevity-optimal targets
   - Confounders / drug effects to rule out artifact
   - Follow-up section for higher-resolution tests to order
3. For interventions, open the corresponding `effect_sizes_*.md` file to see expected magnitude and time-to-peak — set this as your hypothesis before the next draw.
4. Re-test on a cadence appropriate to the marker (most lipids: 3–4 months; vit D: 8–12 weeks after loading; thyroid: 6–8 weeks after dose change; A1c: 3 months minimum).

## Game-plan engine (`etl/`)

A deterministic, MILP-based optimizer that reads structured data extracted from the research markdown above and returns the minimum set of food/supplement/activity interventions that maximally close gaps to optimal range across all out-of-range markers.

### What's in the box

- **118 marker YAMLs** (`etl/data/markers/`) — every marker the research files cover, with reference range, optimal subrange, units, direction (lower-/higher-is-better/in-band), and demographic modifiers (south_asian, sex, age tighter/looser targets).
- **424 intervention YAMLs** (`etl/data/interventions/`) — foods, supplements, activities, behaviors with dose, mechanisms (from a controlled enum), dietary tags, and exclusions.
- **2,063 effect YAMLs** (`etl/data/effects/`) — one per (intervention, marker) pair, with signed effect bounds in pct or absolute units, baseline modifiers, evidence tag (meta / rct / cohort / mr / mechanism / one_trial), time-to-peak window, and primary-literature citations.
- **MILP solver v2** (`etl/fhetl/solver.py`) — multi-mechanism overlap modeling. Interventions belong to their full mechanism set; a per-(intervention, marker) constraint prevents double-counting when an intervention has multiple mechanisms.
- **Streamlit UI** (`etl/app.py`) — single-user personal dashboard. Auto-loads from a Function Health `biomarker_dump.json` if you drop one in `.context/`. Shows current → projected per marker with Healthy/Optimal zone tracking, a recommended stack with evidence grades, a coverage matrix, and per-row remove buttons that re-solve in place.
- **Pydantic schemas + validator** (`etl/fhetl/schemas.py`, `etl/fhetl/validator.py`) — referential and plausibility checks. `uv run python -m fhetl.cli validate data/` should always be 0 failed, 0 warnings.

### Quickstart

```bash
cd etl
uv sync                                       # install deps
uv run pytest tests/ -q                       # 62 passing
uv run python -m fhetl.cli validate data/     # 0 failed, 0 warnings

# CLI plan generation
uv run python -m fhetl.cli plan --apob 110 --ldl-c 145 --hdl-c 35 \
    --tg 200 --hba1c 6.0 --ferritin 50 --vitamin-d 25 --budget 5

# Personal UI (loads .context/biomarker_dump.json if present)
uv run streamlit run app.py
```

### Personal data

The Streamlit app reads a Function Health–shaped `biomarker_dump.json` from `.context/` at the repo root and pre-populates lab values. **`.context/` is gitignored** — your actual lab values never leave your local clone. If the file isn't present, the app falls back to empty inputs you fill in manually.

The lab-name → canonical-id mapping in `etl/personal_labs.py` is keyed on Function Health's display names ("Ferritin", "Apolipoprotein B (ApoB)", etc.) and handles their qualitative quirks (`<10` → midpoint, `NEGATIVE` → 0, `A Pattern` → 1, etc.). To use a different lab's export, extend `NAME_TO_ID` with your lab's display names.

### Architecture

```
biomarker_dump.json (.context/, gitignored)
        │
        ▼
personal_labs.py  ── canonical IDs + parsing ──┐
                                                │
data/markers/   ─────────────────────────────┐  │
data/interventions/ ─────────────────────────┤  ▼
data/effects/   ─────────────────────────────┴► solver.py (MILP)
                                                │
                                                ▼
                                              app.py (Streamlit)
                                              or fhetl.cli plan
```

The solver is deterministic and runs in milliseconds — every UI interaction (changing budget, excluding an intervention, toggling South-Asian targets) triggers an immediate re-solve.

### Caveats specific to the engine

- **Healthy ≠ Optimal.** The UI distinguishes Function Health's lab range (your "healthy" range, what FH flags as out-of-range) from the engine's tighter optimal subrange. You can target either.
- **Effect estimates are population averages with conservative baseline modifiers.** `baseline_mod_lean = 0.5` halves the effect for users already near optimal; some markers (vitamin D, leptin) use 0.2 because the source supports near-zero response in replete subjects.
- **Solver picks at most `budget` interventions** — not the top-N by effect. It optimizes total normalized gap closure across all your out-of-range markers under the mechanism-overlap constraint, so removing one intervention often promotes a substitute that covers the same markers.
- **No runtime LLM.** All recommendations come from the deterministic MILP over structured YAML data. Research extraction (Phase 2/3) used Claude subagents one-time-only; the running engine is pure Python.

## License

These are personal research notes shared as-is for educational use. Cited primary literature is the authoritative source — chase the citations when a number drives a real decision.
