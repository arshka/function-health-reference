# Biomarker Interventions — Per-Marker Research

Per-biomarker, deeply-cited research on **what foods, supplements, activities, and wearable-trackable behaviors move each measured marker** — positively and negatively. Built to power the dashboard's "game plan" recommendation engine.

## Purpose

The existing `effect_sizes_*.md` files at the repo root are organized **by panel**, with intervention-cells densely cited but coverage shallow on individual foods/supplements. This folder inverts that: **one file per biomarker**, exhaustive coverage of every food/supplement/activity with documented effect on that biomarker, with primary-literature citations and quantified effect sizes.

This is intentionally **NOT** a copy of Function Health's recommendation list — Function recommends ~188 "foods to eat" mapped opaquely to biomarker IDs without effect sizes or evidence grades. This folder is the audit-from-scratch version: every claim cited, every effect size quantified, every weak-evidence claim flagged.

## Folder structure

```
biomarker_interventions/
├── README.md                  (this file)
├── _TEMPLATE.md               (format every per-marker file follows)
├── INDEX.md                   (full marker → file map; cross-cutting synthesis)
├── cardiovascular/
│   ├── ApoB.md
│   ├── LDL-C.md
│   ├── HDL-C.md
│   ├── ...
├── advanced_lipids/
│   ├── Lp(a).md
│   ├── LDL_particle_number.md
│   ├── ...
├── metabolic/
│   ├── HbA1c.md
│   ├── fasting_glucose.md
│   ├── ...
├── liver/
├── male_hormones/
├── thyroid/
├── vitamins_minerals/
├── iron/
├── omega_fatty_acids/
├── cbc/
├── immune/
├── kidney_electrolytes_pancreas/
├── heavy_metals_phenoage/
├── autoimmunity_psa/
└── urinalysis/
```

## File format

Every per-marker file follows `_TEMPLATE.md`:

1. **Foods that LOWER / improve direction** (table: food, dose, magnitude, time, evidence tag, source, caveats)
2. **Foods that RAISE / worsen direction** (same table format)
3. **Supplements** (separated into improving vs. ineffective/worsening; same table format)
4. **Activities & behaviors** (aerobic, resistance, sleep, stress, sauna, cold, alcohol, smoking, caffeine, fasting, hydration, etc.)
5. **Wearable-trackable metric relationships** (VO₂max, RHR, HRV, sleep duration / regularity, step count, exercise minutes)
6. **Synthesis & highest-leverage stack** (single best, best-3 stack, realistic deltas at near-optimal vs elevated baseline, when pharmacotherapy is needed)
7. **South Asian / lean-male notes** (where SA-specific evidence exists)
8. **Interactions & confounders for the recommendation engine** (genetic modifiers, drug interactions, lifestyle confounders, timing artifacts)
9. **Open questions / weak evidence**

## Evidence-grading legend

Same as `effect_sizes_*.md` files at repo root:

| Tag | Meaning |
|---|---|
| **[Meta]** | Replicated meta-analysis of ≥5 RCTs |
| **[RCT]** | Single high-quality RCT |
| **[Cohort]** | Prospective observational |
| **[MR]** | Mendelian randomization |
| **[Mechanism]** | Pharmacology / physiology extrapolation |
| **[1-Trial]** | Single small trial, unreplicated |

## How to use this folder for the dashboard

When the dashboard wants to suggest interventions for a flagged marker:

1. Open `biomarker_interventions/{group}/{marker}.md`
2. Pull the highest-leverage entries from §1-4 that match the user's tracked behaviors / dietary preferences (vegetarian, lean baseline, etc.)
3. Use the magnitudes in the tables to estimate the projected delta at the next draw
4. Apply genetic / interaction modifiers from §8 if known (23andMe data, current meds, age, ethnicity)
5. Stack interventions per §6 with the diminishing-returns caveat (combined effect typically 60-80% of linear sum)
6. Mark recommendations with the evidence tag from the source row so the user can see what's well-established vs. mechanistic vs. weak

## Caveats (apply throughout)

1. **Population transportability.** Most cited evidence is NW European, age 40+, with elevated baseline. Effects in lean SA 20yM with near-optimal markers are typically 30–60% of cited magnitude (floor effects).
2. **No medical advice.** This is research synthesis. Drug + supplement interactions are flagged but not exhaustive — physician review required before stacking.
3. **Effect sizes are population averages.** Individual response varies. The effect sizes are hypothesis-generators tested at the next draw, not guarantees.
4. **Genetic modifiers are sparse.** Cross-marker SNP modifiers are listed in `effect_sizes_INDEX.md` §SNP Modifiers; per-marker SNPs are repeated here in §8.
5. **"Optimal" target ranges live in the panel files**, not here. This folder is interventions only.

## License

Personal research notes shared as-is. The cited primary literature is authoritative — chase the citations when a number drives a real decision.
