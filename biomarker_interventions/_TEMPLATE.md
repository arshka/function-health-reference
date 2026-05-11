# {Biomarker Name} — Intervention Research

> One-line summary of what moves this biomarker the most (highest-leverage 1-2 interventions, magnitude, direction). Example: "Soluble fiber (psyllium 10g/d) and SFA reduction together drop LDL-C by ~25–35 mg/dL in 8–12 wk; high-intensity statin remains the only intervention that reaches >50% reduction."

**Cross-link:** Reference biology / clinical interpretation lives in `../{panel_file.md}` §{section}. This file is INTERVENTION-only — what moves the marker, by how much, in how long, with what evidence.

---

## Evidence-Grading Legend

| Tag | Meaning |
|---|---|
| **[Meta]** | Replicated meta-analysis of ≥5 RCTs with consistent direction |
| **[RCT]** | Single high-quality RCT (≥100 participants or pivotal design) |
| **[Cohort]** | Prospective observational; can't establish causality |
| **[MR]** | Mendelian randomization — genetic proxies estimating causal effect |
| **[Mechanism]** | Pharmacology / physiology extrapolation; no direct human RCT for *this specific effect* |
| **[1-Trial]** | Single small trial worth knowing but not yet replicated |

Population caveat applies throughout: most cited evidence is from NW European adults aged 40+ with elevated baselines. Floor effects shrink magnitudes ~30–60% in lean healthy young adults at near-optimal baseline. South Asian / lean-male specific data flagged where it exists.

---

## 1. Foods that LOWER {biomarker} (or improve direction)

| Food | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Example: Oats (β-glucan) | 3 g/d β-glucan (~60–70 g dry oats) | LDL-C −0.20 mmol/L (~−8 mg/dL) | 4–8 wk | **[Meta]** | Whitehead et al., *Am J Clin Nutr* 2014; Ho et al. 2016 (PMC5394769) | Gel-forming fiber binds bile acids; effect plateaus above ~5 g/d β-glucan. |

(target: 8–20 entries — be exhaustive within evidence quality. Cover fruits, vegetables, whole grains, legumes, nuts, seeds, fish, dairy, fermented foods, beverages with mechanism + cited effect size.)

---

## 2. Foods that RAISE {biomarker} (or worsen direction)

| Food | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|

(target: 5–15 entries. Cover refined carbs, ultra-processed foods, specific oils, alcohol, etc. with mechanism + magnitude.)

---

## 3. Supplements

### Lowering / improving

| Supplement | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|

### Raising / worsening (or claimed-but-doesn't-work)

| Supplement | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|

(For each supplement: include mechanism, NNT/effect size when available, RCT vs. mechanistic evidence, interactions, safety. Flag commonly-marketed-but-unsupported supplements explicitly with [no-effect] or [conflicting].)

---

## 4. Activities & Behaviors

Aerobic / endurance, resistance / strength, HIIT / sprint, NEAT / step count, sleep duration & quality, sleep timing & circadian alignment, stress reduction / breath / meditation / vagal training, sauna / heat exposure, cold exposure, alcohol intake (or cessation), smoking (or cessation), caffeine, hydration, fasting / time-restricted eating, posture / standing time, sex / sexual activity (where relevant for hormones).

| Activity | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|

---

## 5. Wearable-Trackable Metric Relationships

How does this biomarker correlate with or respond to changes in: VO₂max, resting HR, HRV (SDNN/RMSSD), step count, sleep duration, sleep regularity, exercise minutes per week, training load? Include both *observational correlations* and *interventional change* where data exists.

| Wearable metric | Direction of relationship | Magnitude / effect size | Evidence | Source | Caveats |
|---|---|---|---|---|---|

---

## 6. Synthesis & Highest-Leverage Stack

- **Highest-leverage single intervention** (ceiling effect, magnitude, time):
- **Best stack of 3** (additive but with diminishing returns):
- **Realistic 12-week delta** for a healthy 20yM at near-optimal baseline:
- **Realistic 12-week delta** for someone with elevated baseline (e.g., {marker} > {threshold}):
- **Where pharmacotherapy becomes necessary** (when lifestyle ceiling is reached):

---

## 7. South Asian / lean-male-specific notes

(Only include if SA-specific evidence exists. Otherwise omit this section.)

---

## 8. Interactions & Confounders for Recommendation Engine

Things that would make a default recommendation WRONG for this user, or that cause the marker to move in unexpected directions:
- Genetic modifiers (APOE, MTHFR, FADS1/2, HFE, etc.) — name SNP + effect direction
- Drug interactions (e.g., metformin lowers B12; PPI lowers Mg; biotin breaks immunoassays)
- Confounding lifestyle factors (e.g., aerobic training plasma-volume-expands Hgb downward without true RBC change)
- Timing artifacts (fasting state, time of day, recent exercise, recent illness)

---

## 9. Open questions / weak evidence

Things where the evidence is weak, conflicting, or absent. Important to keep here so the recommendation engine doesn't *over*-promise. Example: "Berberine LDL-C effect is mostly from Chinese RCTs; transportability to SA / European-ancestry not well established."

---

## Source format conventions

- Cite primary literature (PubMed PMID where available) over secondary sources.
- Prefer meta-analyses → large RCTs → cohorts → mechanism papers.
- Use *Journal Year;Vol(Issue):Pages* format. Include PMID or DOI when available.
- For supplements: cite both efficacy data AND a safety / interaction reference.
- Do NOT cite Function Health's recommendation engine, dr*****.com sites, or commercial supplement promoters. Cite the underlying research.
