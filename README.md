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
- **MILP solver v3** (`etl/fhetl/solver.py`) — severity-weighted objective with clinical-priority crossing bonuses. Multi-mechanism overlap modeling: interventions belong to their full mechanism set; a per-(intervention, marker) constraint prevents double-counting; a per-(marker, mechanism class) constraint ensures only one intervention is "primary" via any given pathway. The objective is `Σ capped_imp_j + α·Σ gap_pct_j·cross_ref_j + β·Σ gap_pct_j·cross_opt_j + γ·Σ cross_ref_j`, where `cross_ref_j` fires when a critical marker reaches its reference boundary and `cross_opt_j` fires when any marker reaches its optimal subrange. Defaults (α=2.0, β=0.5, γ=10.0) bias toward escaping clinical-out-of-range first, then reaching aspirational targets.
- **Streamlit UI** (`etl/app.py`) — single-user personal dashboard. Auto-loads from a Function Health `biomarker_dump.json` if you drop one in `.context/`. Shows current → projected per marker with Optimal / Healthy / Outside-Healthy zone tracking, a plain-language summary of categorical wins and what's still on the table, a recommended stack with evidence grades, a coverage matrix, and per-row remove buttons that re-solve in place. All headline counts derive from the same zone classification so the UI tells one consistent story.
- **Corpus completeness audit** (`etl/scripts/audit_coverage.py`) — deterministic Python script that diffs the per-marker research markdown against the YAML effect corpus and surfaces gaps. Uses `mistune` AST table parsing, explicit allow/deny lists for section headings, `rapidfuzz` three-tier fuzzy matching against the canonical intervention catalog, and Pydantic `Effect.model_validate()` on every stub. Outputs `coverage_report.md` (gaps / extras / unmatched / unknown sections) plus `proposed_effects/*.yaml` stub effect YAMLs ready for review-then-`mv` into `data/effects/`. Idempotent, reproducible byte-for-byte. No runtime LLM. Hand-maintained `etl/scripts/intervention_aliases.yaml` resolves stubborn phrase-to-ID mismatches.
- **Pydantic schemas + validator** (`etl/fhetl/schemas.py`, `etl/fhetl/validator.py`) — referential and plausibility checks. `uv run python -m fhetl.cli validate data/` should always be 0 failed, 0 warnings.

### Quickstart

```bash
cd etl
uv sync                                       # install deps
uv run pytest tests/ -q                       # 74 passing
uv run python -m fhetl.cli validate data/     # 0 failed, 0 warnings

# CLI plan generation
uv run python -m fhetl.cli plan --apob 110 --ldl-c 145 --hdl-c 35 \
    --tg 200 --hba1c 6.0 --ferritin 50 --vitamin-d 25 --budget 5

# Personal UI (loads .context/biomarker_dump.json if present)
uv run streamlit run app.py

# Corpus completeness audit (deterministic; no LLM)
uv run python scripts/audit_coverage.py             # full audit → coverage_report.md
uv run python scripts/audit_coverage.py --recall-test  # CI health gate
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

- **Healthy ≠ Optimal.** The UI distinguishes Function Health's lab range (your "healthy" range, what FH flags as out-of-range) from the engine's tighter optimal subrange. You can target either. Note: the solver computes gaps against the canonical reference ranges in `data/markers/`, while the UI's zone tiles classify your current value against your lab's own ranges where available — the two can disagree at boundary cases (the dashboard summary uses the UI zones as the single source of truth).
- **Effect estimates are population averages with conservative baseline modifiers.** `baseline_mod_lean = 0.5` halves the effect for users already near optimal; some markers (vitamin D, leptin) use 0.2 because the source supports near-zero response in replete subjects.
- **Solver picks at most `budget` interventions** under four constraints that prevent over-claiming: (1) cap-at-gap — total projected improvement per marker can't exceed the marker's `gap_pct`, so a 30%-strong intervention on a 10% gap caps at 10%; (2) per-mechanism-class — only one intervention can be "primary" through any given mechanism on any given marker, so two omega-3 sources don't double-count; (3) per-(intervention, marker) — a multi-mechanism intervention can only fire through one of its mechanisms per marker; (4) per-active-ingredient — at most one selection per `active_ingredient` group (e.g. `vitamin_d3_1000iu`, `vitamin_d3_3000iu`, `vitamin_d3_loading_50000iu_weekly` all share `vitamin_d3`, so the stack will never include two protocols of the same compound).
- **Stacking is additive across distinct mechanisms.** Contributions from different mechanism classes sum linearly until capped at gap. Diminishing returns are not currently modeled (see Roadmap below).
- **No runtime LLM.** All recommendations come from the deterministic MILP over structured YAML data. Research-text extraction (`scripts/audit_coverage.py`) is pure Python — `mistune` + `rapidfuzz` + Pydantic, fully reproducible. Earlier corpus generation used Claude subagents one-time-only; nothing in the running engine or audit pipeline calls an LLM.

### Roadmap / open TODOs

- **Diminishing returns across mechanisms.** The current solver treats contributions from non-overlapping mechanism classes as purely linearly additive (subject to cap-at-gap). In reality, 4 strong interventions on 4 different mechanisms typically yield ~60–80% of the linear sum, not 100% — biology saturates even when pathways are distinct. Three viable approaches:
  - *Concave aggregation:* replace `capped_imp_j ≤ Σ_k m_jk` with a concave function (sqrt-like / sigmoid). Most theoretically correct; requires piecewise-linear approximation to keep the MILP linear.
  - *Per-intervention decay:* successive interventions on a marker contribute at 80%, 70%, 60%, etc. Cheaper, less principled.
  - *Mechanism-count cap:* "at most 3–4 mechanisms can contribute to any single marker." One-line constraint, matches the empirical heuristic that beyond 3–4 mechanisms the marginal benefit per added intervention drops sharply.

  None of these is implemented today. The cap-at-gap rule masks the issue for severe markers (the gap itself is the binding constraint), but moderate-gap markers with 5+ interventions in the stack will project optimistically.

- **Lab-range-aware solver gap.** The solver targets canonical optimal boundaries; when a user's lab uses a stricter reference range than canonical (e.g. Function Health's Vitamin D minimum is 30 ng/mL vs canonical 20), the dashboard can show a marker as "still outside healthy" even after the solver thinks it's done. A `--respect-lab-range` mode that passes the user's lab boundaries into the gap computation would close this.

- **In-band markers.** Markers with `direction: in_band` (e.g. sodium, MCV, TSH) currently score zero in the solver — neither rewarded for staying nor penalized for drifting. Worth modeling as a two-sided gap if real cases arise.

## License

These are personal research notes shared as-is for educational use. Cited primary literature is the authoritative source — chase the citations when a number drives a real decision.
