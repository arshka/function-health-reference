# Intervention Effect Sizes — Metabolic & Liver Markers

A quantitative reference for the **magnitude** of lifestyle, dietary, supplemental, and pharmacological effects on metabolic and liver blood markers. Companion to `metabolic_panel.md` and `liver_panel.md`, which cover marker biology and ranges; this file covers only effect sizes, provenance, and caveats. No biology recap; no clinical recommendations.

---

## 0. How to Read This Document

### Evidence Grading Tags

| Tag | Meaning |
|---|---|
| **[Meta]** | Systematic review or meta-analysis of ≥3 RCTs |
| **[RCT]** | Single randomized controlled trial |
| **[Cohort]** | Prospective observational study |
| **[Mechanism]** | Human mechanistic study, not powered for clinical outcomes |
| **[MR]** | Mendelian randomization (genetic instrumental variable) |

**Calibration principle**: a single striking RCT is not the evidence base. Prefer replicated **[Meta]** results; flag lone **[RCT]** findings explicitly. Where evidence is mixed or heterogeneous, say so rather than presenting a clean number.

### Key Uncertainty Flags Applied Throughout

- **Insulin assay variability**: inter-lab CV ~15–30% for fasting insulin immunoassay ([JCLA 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/jcla.24521)). Effect sizes on fasting insulin from trials using different platforms are hard to pool precisely. HOMA-IR inherits this uncertainty. LC-MS/MS (Quest Intact Insulin) is the exception.
- **A1c in iron deficiency / Hb variants**: iron deficiency can raise A1c ~0.3–1.0% artifactually; correcting iron lowers A1c independently of true glycemia ([PMC6857442](https://pmc.ncbi.nlm.nih.gov/articles/PMC6857442/)). Interventions that change iron status (e.g., very-low-calorie diets in some women) confound A1c effect sizes.
- **A1c discordance in South Asians**: some data suggest South Asians may glycate hemoglobin faster at equivalent glucose levels, inflating A1c ~0.1–0.2% relative to CGM-derived estimates, though this is not yet replicated at scale. ACG/ADA guidelines do not formally adjust A1c cutoffs by ancestry. Flag when reading your own A1c vs. fasting glucose.
- **ALT cutoff**: the ACG 2017 Kwo guideline sets "healthy" ULN at 29–33 U/L for males — not the historical 40–55 U/L. Intervention studies that use 40 U/L as the upper limit understate effect because they include more room for true pathology in the "normal" range at baseline.
- **Lean MASLD in South Asians**: MASLD occurs at BMI < 23 kg/m² in Asian populations (Eslam consensus 2020). A lean South Asian male with mildly elevated ALT/GGT and normal BMI should be evaluated for MASLD by the same criteria as an overweight Caucasian — normal weight does not exclude metabolic liver disease.

---

## Metabolic Markers

---

## Fasting Glucose

**Quick read:** Weight loss and aerobic exercise are the biggest movers for sustained fasting glucose reduction. Low-carbohydrate diets produce rapid initial drops (partly glycogen depletion, not fat loss); the Mediterranean diet produces modest sustained improvement; metformin and GLP-1 agonists give pharmacological scale.

### Effect Size Table

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Weight loss (dietary) | 5% body weight | Fasting glucose −5 to −10 mg/dL | 8–16 wk | **[Meta/RCT]** | DiRECT 2018, multiple meta-analyses | Effect larger when baseline >100 mg/dL |
| Weight loss (DiRECT, ~15 kg) | Very-low-calorie diet, 825–853 kcal/day | Fasting glucose −20 to −30 mg/dL; ~50% diabetes remission at 1 yr | 8–12 wk | **[RCT]** | Lean 2018 *Lancet*; Zhyzhneuskaya 2025 *Diabetic Med* | Participants had established T2D; remission requires sustained weight loss |
| Aerobic exercise ≥12 wk | 150+ min/week moderate intensity | Fasting glucose −6 to −10 mg/dL | 8–16 wk | **[Meta]** | Diabetes Care 2024 optimal dose meta-analysis | Larger effects in those with dysglycemia at baseline; minimal effect in truly euglycemic <90 mg/dL |
| Resistance training | 3×/week, moderate-high intensity, 8–24 wk | Fasting glucose −7 mg/dL (MD −6.99 mg/dL) | 12–16 wk | **[Meta]** | Multiple meta-analyses 2019–2023 | Effect correlated with intensity; pooled from T2D populations, likely smaller in normoglycemic |
| Combined aerobic + resistance | Both modalities, 12+ wk | Fasting glucose −6 to −9 mg/dL; additive to either alone | 12 wk | **[Meta]** | Sci Reports 2024 meta-analysis | Best modality combination by network meta-analysis for glucose |
| Low-carbohydrate diet (<50g CHO/day) | Ad libitum or isocaloric LC | Fasting glucose −10 to −15 mg/dL initially; attenuates to −5 to −8 at 6–12 mo | 1–4 wk acute; 6–12 mo sustained | **[Meta]** | Front Nutr 2024 meta-analysis of 17 RCTs (n=1,197) in T2D | Initial drop partly from glycogen depletion; long-term benefit requires adherence; most trials in T2D or overweight |
| Mediterranean diet | Calorie-unrestricted, high adherence | Fasting glucose −10 to −15 mg/dL (vs. control diet) | 12–24 wk | **[Meta]** | MDPI Nutrients 2024 meta-analysis of 7 RCTs, n=1,371 | Heterogeneous populations; most studies in T2D; effect size in healthy young adults likely smaller |
| Intermittent fasting (16:8, 5:2) | 16:8 TRE or 2 fasting days/week | Fasting glucose −3 to −6 mg/dL; HbA1c modest (see below) | 8–24 wk | **[Meta]** | PMC8970877 (2022 meta); nutr reviews 2025 | Mixed results for HbA1c; insulin sensitivity more reliably improved than fasting glucose |
| Sleep extension (chronically sleep-deprived) | +1.2 hr/night × 2 wk | Fasting glucose modest improvement; insulin sensitivity +11% | 2 wk | **[RCT]** | JCSM 2019 (Tasali) | Small n; effect in those who were chronically short-sleeping |
| Sleep restriction (4 hr/night) | 6 nights | Glucose tolerance −30–40%; glucose effectiveness −30% | Days | **[Mechanism/RCT]** | Spiegel 1999 *Sleep*; JCEM 2010 | Acute, highly reproducible; reversible on sleep restoration |
| Fructose/SSB elimination | Removing >50g/day fructose | Fasting glucose −3 to −5 mg/dL, larger HOMA-IR effect | 4–10 wk | **[RCT/Mechanism]** | Stanhope 2009 JCI; Hieronimus 2020 | Glucose effect modest; metabolic effect (HOMA-IR, UA, liver fat) larger |
| Fructose/SSB addition (worsening) | 25% of energy as fructose-sweetened beverage | Fasting glucose +3–5 mg/dL; visceral fat ↑; UA ↑; GGT ↑ | 10 wk | **[RCT]** | Stanhope 2009 JCI; Hieronimus 2020 *J Nutr* (fructose vs. glucose differential critical) | Glucose-sweetened beverages produced smaller or no effect — fructose-specific |
| Coffee (3–5 cups/day habitual) | Regular/decaf | Fasting glucose: epidemiologically inverse but RCT effect small | — | **[Cohort/Meta]** | Multiple prospective cohorts | Insulin-sensitizing effect probably via chlorogenic acids and cafestol; RCT evidence weaker than cohort |
| **Worseners:** Alcohol (>2 drinks/day) | 30+ g/day ethanol | Acute: insulin suppression → glucose rise; chronic: modest glucose elevation with heavy use | Hours–weeks | **[Cohort]** | NHANES dose-response analysis | Moderate alcohol (<15 g/day) has inconsistent glycemic effects; heavy use clearly worsens |
| **Worseners:** Saturated fat overfeeding | +750 kcal/day SFA for 3 wk | Hepatic IR, fasting glucose +3–7 mg/dL | 2–3 wk | **[Mechanism/RCT]** | Sobrecases 2010; Rosqvist 2014 | More pronounced in those with visceral obesity baseline; differential by genetic background |

**Pharmacotherapy reference (scale only):** Metformin −5 to −10 mg/dL fasting glucose, −0.7 to −1.0% A1c **[Meta]**; Semaglutide 0.5–1.0 mg/wk: fasting glucose −20–30 mg/dL, weight −10–15% at 1 yr **[RCT]** (SUSTAIN program); SGLT2i: fasting glucose −12–15 mg/dL via glucosuria **[Meta]**.

**Synthesis:**

- Biggest sustainable movers: **weight loss** (dose-response, 1 kg ≈ 1–2 mg/dL), **aerobic exercise** (effect mostly on insulin sensitivity → fasting glucose), **carbohydrate reduction** (fast but requires adherence).
- Oversold for glucose specifically: cinnamon — pooled meta-analyses show −5 to −8 mg/dL at best, with high heterogeneity; effect not replicated in high-quality RCTs ([Cochrane 2012](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007170.pub2/abstract)).
- **South Asian note**: South Asians develop T2D at lower BMI and fasting glucose levels. A fasting glucose of 90–95 mg/dL that would be unremarkable in a Caucasian 20M warrants more concern in a lean South Asian given higher baseline insulin resistance (Kelly West Lecture, *Diabetes Care* 2024). Prioritize HOMA-IR over fasting glucose alone.
- **3-month best-case** from suboptimal baseline (fasting glucose ~105 mg/dL): exercise 5×/week + low-glycemic diet + 3–5% weight loss → fasting glucose likely −10 to −20 mg/dL.
- **6-month best-case**: sustained low-carb or Mediterranean + consistent exercise + 7–10% weight loss → fasting glucose −15 to −25 mg/dL; potential normalization if baseline was prediabetic range.

---

## HbA1c

**Quick read:** HbA1c changes lag 8–12 weeks behind metabolic changes due to RBC lifespan. Sustained weight loss and aerobic exercise produce the most reliable reductions. Low-carb diets produce fast initial drops; Mediterranean diet a modest sustained effect. Berberine matches metformin in several head-to-head RCTs. Cinnamon and chromium are overhyped. Iron deficiency and hemoglobin variants confound interpretation.

### Effect Size Table

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Weight loss | 5% body weight | A1c −0.3 to −0.5% | 12–24 wk | **[Meta/RCT]** | Multiple meta-analyses; DiRECT | Larger response if baseline A1c >6%; minimal if truly euglycemic |
| Weight loss (DiRECT, 15 kg) | VLC diet-induced remission | A1c −1.5 to −2.5% in T2D | 8–16 wk | **[RCT]** | Lean 2018 *Lancet* | T2D population; 46% still in remission at 1 yr |
| Aerobic exercise ≥12 wk | Moderate intensity, 150 min/wk | A1c −0.5 to −0.6% | 12–24 wk | **[Meta]** | Diabetes Care 2024; multiple meta-analyses 2019–2023 | Pooled from T2D/prediabetes; effect in healthy euglycemic <5.5% likely negligible (<0.1%) |
| Resistance training | High intensity > moderate | A1c −0.61% (high intensity) vs. −0.23% (low-moderate) | 12–24 wk | **[Meta]** | Boulé 2003; PubMed 30621076 | Intensity-dependent per meta-regression; insulin independent mechanism |
| Mediterranean diet | High adherence, long-term | A1c −0.2 to −0.4% | 12–24 wk | **[Meta]** | PMC11027355 (9 RCTs, n=1,337); MDPI 2024 | Heterogeneous; pooled from T2D; smaller effect expected in euglycemic |
| Low-carbohydrate diet | <50g CHO/day | A1c −0.36% (MD vs. control, 17 RCTs) | 12–24 wk | **[Meta]** | Front Nutr 2024 meta-analysis | Caloric restriction confounded in most trials; matched-calorie trials (Hall 2021) show smaller differential |
| Isocaloric low-carb vs. low-fat | Matched calories, inpatient | A1c/glucose: low-carb produces lower insulin secretion (~60% lower daily) but similar long-term glycemic control once calories matched | 2 wk acute | **[RCT]** | Hall 2021 *Nature Medicine* | Key finding: **carbohydrate composition alone, at matched calories, does not produce the glycemic magic often attributed to it**. Weight loss remains the primary driver. |
| Intermittent fasting (16:8 TRE) | Daily 8-hour eating window | A1c −0.08 to −0.31% (SMD) | 16–24 wk | **[Meta]** | Nutrition Reviews 2025; PMC10945168 | Modest; A1c effect smaller than insulin/HOMA-IR effect; mixed results across meta-analyses |
| Berberine | 500 mg TID or 1–1.5 g/day | A1c −0.63 to −0.73% | 12–24 wk | **[Meta]** | PubMed 34956436; Front Pharmacol 2024 (multiple meta-analyses concordant) | Multiple meta-analyses converge on ~−0.63% to −0.73%; most trials in T2D; Yin 2008 JCEM: berberine ~= metformin in head-to-head RCT (n=116) |
| Magnesium supplementation | 300–400 mg/day elemental Mg, ≥4 months | A1c not reliably reduced; HOMA-IR ↓ −0.67 (see HOMA-IR section) | ≥4 months | **[Meta]** | Nutrients 2021; PMC7784187 | Effect on fasting glucose and HOMA-IR but NOT A1c in most meta-analyses; baseline Mg deficiency may moderate |
| Iron repletion (in iron-deficient) | Correcting iron deficiency | A1c ↓ 0.3–1.0% — but this is artifact correction, not true glycemic improvement | 4–12 wk | **[Mechanism/Meta]** | PMC6857442 | Critical confounder: if A1c is elevated due to iron deficiency, treating iron corrects the assay, NOT glycemia. CGM or fasting glucose confirms. |
| **Worseners:** SSBs | 1–2 SSBs/day (>25g fructose) | A1c +0.1 to +0.3% over months/years | Slow (3-month integration) | **[Cohort]** | Multiple prospective cohorts | Hard to isolate SSB from total caloric effect |
| **Worseners:** Sleep restriction | <6 hr/night chronic | A1c higher by ~0.3% in population comparisons | Chronic | **[Cohort]** | Multiple; not well-powered RCT for A1c specifically | Confounding by obesity and other lifestyle factors |
| Cinnamon | 1–6 g/day | A1c −0.09 to −0.27% across pooled analyses; some trials null | 8–16 wk | **[Meta]** | Allen 2013 *J Acad Nutr Diet*; Cochrane 2012 | **Oversold.** Effect size small, highly heterogeneous; highest quality RCTs tend toward null. Not reliable. |
| Chromium | 200–1000 mcg/day | A1c −0.5% in older meta-analyses; recent higher-quality meta-analyses ~−0.1 to −0.2% | 12–16 wk | **[Meta]** | Paiva 2015; multiple recent | Benefit attenuated in high-quality trials; likely only meaningful in chromium-deficient individuals (rare in adequately nourished) |

**Pharmacotherapy reference (scale only):** Metformin −0.7 to −1.0% **[Meta]**; Semaglutide 2.4 mg/wk: A1c −1.5 to −2.0% **[RCT]** (STEP 2, SUSTAIN 6); Pioglitazone −0.8 to −1.0% **[Meta]**; Berberine ~−0.7% (comparable to metformin in single RCT); Empagliflozin −0.7% **[Meta]**.

**Synthesis:**

- Highest-leverage: sustained weight loss (especially VLC-induced in those with elevated A1c), exercise (dose-dependent), reduction of refined carbohydrate load.
- **Iron deficiency as confounder** is consistently underappreciated: a 20M presenting with A1c 5.8–6.0% should have ferritin checked. If iron-deficient, correcting iron can drop A1c without any glycemic improvement.
- **Hemoglobin variants**: South Asian populations have higher rates of HbE (Southeast Asian), HbD, beta-thalassemia trait. HPLC-based A1c assays may give artifactual values. Request the assay method if A1c is discordant with fasting glucose.
- **South Asian note**: Some evidence (methodologically limited) that South Asians have higher A1c at equivalent fasting/post-load glucose — potentially due to higher RBC glycation rates. This means A1c may slightly *overestimate* glycemic control and fasting glucose/HOMA-IR may be more reliable primary markers for this population.
- **3-month best-case** from A1c 5.8%: aerobic exercise 5×/week + Mediterranean or low-carb diet + 3% weight loss → A1c −0.3 to −0.5% (to ~5.3–5.5%).
- **6-month best-case**: sustained program + 7% weight loss → A1c −0.5 to −0.8% (normalization to 5.0–5.3% plausible).
- **SNPs**: MTNR1B rs10830963 risk allele → elevated fasting glucose and A1c disproportionate to post-load glycemia; GLP-1 secretion blunted with risk allele. TCF7L2 rs7903146 → strongest T2D genetic risk; higher post-prandial glucose excursions; reduces berberine efficacy in some studies.

---

## Fasting Insulin & HOMA-IR

**Quick read:** Fasting insulin and HOMA-IR respond robustly to aerobic exercise (independent of weight loss) and to carbohydrate restriction. Both are highly sensitive to assay variability (15–30% inter-lab CV) — serial measurements are only interpretable if the same assay/lab is used. HOMA-IR is more sensitive than A1c for early insulin resistance in lean young adults.

### Effect Size Table — Fasting Insulin (µIU/mL)

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Weight loss | 5–10% body weight | Fasting insulin −2 to −5 µIU/mL | 8–16 wk | **[Meta/RCT]** | Multiple meta-analyses | Linear dose-response with weight loss magnitude |
| Aerobic exercise | 150 min/wk, 12 wk | Fasting insulin −1 to −3 µIU/mL; effect partly independent of weight loss | 8–16 wk | **[Meta]** | Sci Reports 2024 combined exercise meta | Insulin sensitivity improves even without significant weight change via GLUT4 upregulation in muscle |
| Resistance training (in overweight/obese, non-diabetic) | 8–24 wk, moderate-high intensity | Fasting insulin effect size −1.03 (standardized) | 12–16 wk | **[Meta]** | PubMed 37331899 (resistance training overweight/obese, non-diabetic) | Most data in overweight; effect in lean may be smaller |
| HIIT vs. MICT | HIIT 20–30 min × 3/wk | HIIT and MICT produce similar insulin sensitivity improvements at matched energy expenditure | 8–12 wk | **[Meta]** | Multiple HIIT vs. MICT meta-analyses | HIIT produces results in less time; not clearly superior per unit time if total work equated |
| Low-carbohydrate diet | <50g CHO/day | Fasting insulin −2 to −5 µIU/mL; larger reduction than low-fat at same caloric deficit | 4–12 wk | **[Meta/RCT]** | Multiple; Hall 2021 NMR (60% lower insulin secretion on low-carb at matched calories acutely) | Acute LC: insulin drop partly from reduced carbohydrate stimulus, not fat loss |
| Intermittent fasting (16:8) | Daily TRE | Fasting insulin: significant reduction (WMD −0.60 in one meta; −38.49 pmol/L in another) | 8–16 wk | **[Meta]** | PMC8970877; inositol/IF meta-analyses | HOMA-IR reliably ↓; fasting insulin effect size varies by baseline and assay |
| Berberine | 500 mg TID | Fasting insulin −1 to −2 µIU/mL | 12 wk | **[Meta]** | PubMed 34956436 (meta of berberine on metabolic profiles T2D) | Mechanism: AMPK activation mimics metformin effect |
| Magnesium (≥4 months, ≥300 mg/day) | Elemental Mg 300–400 mg/day | HOMA-IR −0.67 (WMD, 95% CI −1.20 to −0.14); fasting insulin inconsistently improved | ≥4 months | **[Meta]** | PubMed 27329332; PMC7784187 | Benefit concentrated in Mg-deficient or prediabetic subjects; healthy replete individuals may not respond |
| Myo-inositol / D-chiro-inositol | 2–4 g/day myo-inositol ± 40:1 MI:DCI ratio | HOMA-IR −1.96 (95% CI −2.62 to −1.30); fasting insulin ↓ significantly | 12–24 wk | **[Meta]** | ScienceDirect meta-analysis 2018 (20 RCTs, n=1,239); PMC12574088 | Most data in PCOS women; less data in men; effect on HbA1c appears negligible |
| Sleep restriction (1 week, 5.5 hr/night) | Acute restriction | Insulin sensitivity −16 to −25%; HOMA-IR ↑ | 7 days | **[RCT]** | Diabetes 2010; JCEM 2010 single-night partial deprivation | Rapidly reversible with sleep restoration; mechanistic (cortisol, GH, sympathetic activation) |
| Coffee (3–5 cups/day, regular) | Caffeinated | Acute: insulin ↑ and sensitivity ↓; habitual use: paradoxically protective in population studies | Acute vs. chronic | **[Cohort/Mechanism]** | Multiple prospective cohorts | Do not draw fasting insulin on a day of coffee consumption — acute rise in catecholamines and cortisol |
| **Worseners:** Sedentary behavior | Replacing 3+ hr sitting | HOMA-IR ↑ even controlling for total exercise | Days | **[Cohort/RCT]** | Dunstan 2012; multiple standing desk RCTs | Independent of structured exercise; breaks in prolonged sitting improve postprandial glucose |
| **Worseners:** Sleep apnea (untreated) | Moderate-severe OSA | HOMA-IR elevated vs. matched controls; CPAP reduces but does not normalize | — | **[Cohort/RCT]** | Multiple meta-analyses of CPAP and metabolic outcomes | Effect of CPAP on HOMA-IR: modest (−0.4 to −0.7 in meta-analyses); treating apnea is necessary but not sufficient for IR |

### Effect Size Table — HOMA-IR (unitless)

| Intervention | Direction & Magnitude | Evidence |
|---|---|---|
| Aerobic exercise, 12 wk | HOMA-IR −0.47 (umbrella review, prediabetes) | **[Meta]** |
| Resistance training, moderate-high intensity | HOMA-IR −1.05 (effect size) in overweight/obese non-diabetic | **[Meta]** |
| Low-carbohydrate diet, 12–24 wk | HOMA-IR −1.0 to −2.0 | **[Meta]** |
| Intermittent fasting | HOMA-IR −0.60 (WMD) | **[Meta]** |
| Magnesium, ≥4 months | HOMA-IR −0.67 (WMD) | **[Meta]** |
| Myo-inositol | HOMA-IR −1.96 (WMD) | **[Meta]** (mostly PCOS women) |
| 5% weight loss | HOMA-IR −0.5 to −1.5 (proportional) | **[Meta]** |
| Berberine | HOMA-IR −1.15 | **[Meta]** |
| Sleep restriction (1 wk, −2.5 hr/night) | HOMA-IR ↑ ~20–30% from baseline | **[RCT]** |

**Synthesis:**

- **Assay variability is the primary interpretive challenge**: a fasting insulin of 8 µIU/mL on one platform may read as 6 or 10 on another. Serial changes within the same lab are meaningful; cross-lab comparisons are not.
- Highest-leverage interventions for HOMA-IR: aerobic exercise (acts independently of weight loss via GLUT4 and hepatic insulin extraction), low-carbohydrate diet (reduces insulin secretory demand), and weight loss (especially visceral fat reduction).
- **South Asian specific**: South Asians have 30–50% higher HOMA-IR vs. Europeans at identical BMI ([Diabetes Care 2024, Kelly West Lecture](https://diabetesjournals.org/care/article/47/1/7/154008/Diabetes-in-South-Asians-Uncovering-Novel-Risk)). The functional threshold for "insulin resistant" in a South Asian young man is lower. HOMA-IR >1.5 in a lean South Asian 20M warrants scrutiny even if lab "normal" is <2.7.
- **3-month best-case** from HOMA-IR ~2.0 (suboptimal): sustained aerobic exercise 5×/week + low-carbohydrate diet → HOMA-IR −0.7 to −1.2 (toward ~0.8–1.3).
- **SNPs**: TCF7L2 (T2D risk, impaired GLP-1 response), MTNR1B (impaired fasting insulin suppression at night), PPARG (affects pioglitazone response on insulin sensitivity).

---

## Uric Acid

**Quick read:** Fructose (especially from SSBs) and alcohol are the biggest dietary drivers of uric acid elevation. SGLT2 inhibitors, allopurinol, and febuxostat provide pharmacological scale. SLC2A9 and ABCG2 variants explain substantial inter-individual variability. Fasting and ketosis paradoxically raise uric acid via URAT1 competition with β-hydroxybutyrate.

### Effect Size Table

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Fructose/SSB elimination | Removing >50g/day fructose (≈2 large SSBs) | UA ↓ 0.5–1.5 mg/dL | 4–10 wk | **[RCT/Meta]** | Stanhope 2009 JCI (fructose 25% kcal → UA ↑ + GGT ↑); meta of controlled feeding trials JNEP 2022 | Glucose-sweetened beverages produce significantly smaller effect — fructose-specific mechanism via KHK-C ATP depletion |
| **Fructose 25% energy addition (worsening)** | 10 weeks at 25% kcal from fructose | UA ↑ significantly; GGT ↑; visceral fat ↑; insulin sensitivity ↓ | 10 wk | **[RCT]** | Stanhope 2009 JCI ([PubMed 19381015](https://pubmed.ncbi.nlm.nih.gov/19381015/)); Hieronimus 2020 *J Nutr* | Glucose arm did not produce these effects — fructose-specific |
| Alcohol cessation | From heavy (>210g/wk men) to abstinence | UA ↓ 1–2 mg/dL | 2–4 wk | **[RCT/Cohort]** | Multiple; beer strongest (guanosine-rich + ethanol both raise UA) | Beer > spirits > wine for uric acid effect |
| Weight loss (5–10%) | Caloric restriction or exercise | UA ↓ 0.5–1.0 mg/dL | 12–16 wk | **[Meta]** | Multiple weight loss RCTs | Rapid weight loss / catabolism can transiently *raise* UA before sustained reduction |
| Low-purine diet | Avoiding organ meats, anchovies, sardines, mussels | UA ↓ 0.5–1.0 mg/dL | 4–8 wk | **[RCT/Cohort]** | Gout dietary guidelines; meta-analyses of diet and gout | Modest effect compared to fructose and alcohol elimination |
| Dairy consumption (increase) | 2+ servings/day low-fat dairy | UA ↓ 0.25–0.45 mg/dL | 4–8 wk | **[RCT/Cohort]** | Choi 2004 *NEJM* (gout cohort); RCT evidence modest | Mechanism: casein and lactalbumin promote renal urate excretion |
| Coffee (4+ cups/day habitual) | Caffeinated or decaf | UA ↓ 0.5–1.0 mg/dL (habitual drinkers vs non) | Chronic | **[Cohort]** | Choi & Curhan *Arthritis Rheum* 2007 | Mechanism: competitive xanthine oxidase inhibition by xanthines in coffee |
| Vitamin C (500 mg/day) | Supplemental ascorbate | UA ↓ 0.5 mg/dL | 4–8 wk | **[Meta]** | Juraschek 2011 *Arthritis Rheum* meta (13 RCTs) | Effect modest; insufficient to treat gout but useful adjunct |
| Ketogenic diet / prolonged fasting | <20g CHO/day | UA ↑ 0.5–2.0 mg/dL (paradoxical rise) | 1–4 wk | **[Mechanism/RCT]** | Multiple keto diet trials; *Metabolism* 1976 (β-hydroxybutyrate competes with URAT1) | Transient effect during adaptation; may persist with chronic ketosis; important for gout-prone individuals considering keto |
| SGLT2 inhibitors | Empagliflozin 10/25 mg; dapagliflozin 10 mg | UA ↓ 0.5–0.7 mg/dL (−32 to −42 µmol/L = −0.54 to −0.70 mg/dL) | 4–12 wk | **[Meta]** | Multiple meta-analyses including PMC10807021; Frontiers Pharmacol 2025 | Mechanism: SGLT2 inhibition increases urinary glucose → reduces URAT1 reabsorption of urate; modest but consistent |
| Cherry/tart cherry extract | 8–10 oz/day cherry juice or equivalent | UA ↓ 0.3–0.5 mg/dL; gout flare risk −35% in observational | 4–8 wk | **[Cohort/RCT]** | Zhang 2012 *Arthritis Rheum* cohort; small RCTs | Not FDA-approved for gout; RCT evidence limited; likely safe adjunct |
| **Worseners:** Thiazide diuretics | Hydrochlorothiazide, chlorthalidone | UA ↑ 0.5–2.0 mg/dL | Weeks | **[RCT/Cohort]** | Well-established drug-induced hyperuricemia | Mechanism: competition with URAT1 for secretion |
| **Worseners:** Low-dose aspirin (<300 mg/day) | Daily 81–325 mg | UA ↑ 0.5–1.0 mg/dL | Days–weeks | **[Mechanism]** | Standard pharmacology | Paradox: high-dose (>2 g/day) is uricosuric; low-dose raises UA |
| **Worseners:** Intense exercise (acute) | Single heavy training session | UA transiently ↑ 0.5–2.0 mg/dL (AMP → hypoxanthine → UA) | 1–6 hours | **[Mechanism/RCT]** | Med Sci Sports Exerc 1988; Frontiers Sports 2024 | Rapidly normalizes with hydration/rest; habitual exercise lowers chronic UA |
| **Worseners:** Dehydration | Concentrated urine | UA ↑ disproportionate to solute | Hours | **[Mechanism]** | Basic physiology | Important confounder for lab draw interpretation |

**Pharmacotherapy reference (scale only):** Allopurinol 300 mg/day: UA ↓ 2–3 mg/dL **[Meta]**; Febuxostat 80 mg/day: UA ↓ 3–4 mg/dL, superior to allopurinol 300 mg (MD −0.83 mg/dL vs. allopurinol) **[Meta]** (PMC12456345); Probenecid (uricosuric): UA ↓ 1–3 mg/dL; Lesinurad: UA ↓ additional 1–2 mg/dL when added to XOi; Colchicine: prophylactic, does not lower UA.

**Synthesis:**

- **Biggest movers**: fructose elimination (especially SSBs) >> alcohol reduction > low-purine diet. Fructose-specific mechanism (KHK-C → ATP depletion → AMP → UA) is distinct from glucose; eliminating glucose-sweetened beverages produces minimal effect.
- **Fasting/ketosis paradox**: a 16:8 or prolonged fast raises UA acutely via β-hydroxybutyrate competing at URAT1. In someone with borderline UA (6.0–6.5 mg/dL), extended fasting protocols may transiently tip them above saturation. Monitor UA if pursuing extended fasts.
- **SNPs**: SLC2A9 rs11942223 and related variants explain ~3.5% of population variance in UA; ABCG2 rs2231142 — particularly high-impact in East Asians, moderately in South Asians (reduces intestinal UA secretion → higher serum UA at equivalent diet); GCKR rs1260326 → higher TG *and* higher UA (pleiotropic); HFE C282Y (hemochromatosis gene) — iron overload independently raises UA.
- **South Asian note**: ABCG2 risk allele frequency is elevated in East/South Asian populations, contributing to higher baseline UA. Combined with higher fructose intake from sweetened beverages common in South Asian dietary patterns, this creates additive hyperuricemia risk even at normal BMI.
- **3-month best-case** from UA 6.5–7.0 mg/dL: SSB elimination + alcohol reduction + dairy increase + vitamin C → UA ↓ 1.0–2.0 mg/dL (potentially to <5.5 mg/dL).
- **6-month best-case**: above + sustained weight loss 5–7% → UA ↓ 1.5–2.5 mg/dL.

---

## Liver Markers

---

## ALT

**Quick read:** Weight loss is the most powerful ALT-lowering intervention, with DiRECT-trial data showing 38–51% reductions in 12 weeks. Exercise reduces liver fat (and thus ALT) even without weight loss (Hallsworth 2011). Alcohol cessation produces rapid ALT normalization. Coffee (3–5 cups/day) reduces ALT risk 38–44%. Milk thistle (silymarin) is null in best-quality MASLD trials.

### Effect Size Table

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Weight loss 5–10% | Caloric restriction; exercise-induced | ALT ↓ 20–40% from baseline | 8–16 wk | **[Meta/RCT]** | Multiple meta-analyses; Gasteyger 2008 (−20.5% in men after median 12.1 kg loss); PMC1773957 (modest weight loss: ALT ↓ in NAFLD) | Sex differences: in Gasteyger, women had transient ALT *rise* on low-calorie diets — possibly related to gallstone formation from rapid fat mobilization |
| Weight loss ~15 kg (DiRECT) | VLC 825 kcal/day × 12 wk + maintenance | ALT ↓ 38–51% from baseline | 12–24 wk | **[RCT]** | Zhyzhneuskaya 2025 *Diabetic Medicine*; DiRECT 2018 *Lancet* | Liver fat normalized in 74% at 12 months; ALT correlates with liver fat change r=0.6 |
| Resistance exercise | 3×/week × 8 wk; no weight loss | Liver lipid ↓ 13% by MRS; ALT: no significant effect in Hallsworth | 8 wk | **[RCT]** | Hallsworth 2011 *Gut* | Key finding: liver fat can fall significantly from exercise **without weight loss** — important mechanistically. ALT did not normalize in this small trial despite liver fat improvement. |
| Resistance exercise meta-analysis (MASLD) | Multiple RCTs pooled | ALT ↓ significantly (WMD meta-analyses show −5 to −15 U/L) | 12–24 wk | **[Meta]** | PMC12907158 Frontiers Physiology 2025 | Effect on ALT more reliable in meta-analysis than Hallsworth 2011 alone; small individual trials underpowered |
| Aerobic exercise | 150 min/wk, 12+ wk | ALT ↓ 10–20 U/L in MASLD populations | 12–24 wk | **[Meta]** | Multiple MASLD exercise meta-analyses | Effect proportional to liver fat reduction; less clear in normotransaminase population |
| Coffee (3–5 cups/day) | Regular or decaf habitual consumption | ALT risk of elevation ↓ 44% (>2 cups/day vs. none); ALT values 10.3% lower in 3+ cup/day drinkers | Chronic | **[Cohort]** | NHANES III analysis; Italian cohort; PMC5440772 (Coffee Liver Diseases review) | Dose-response; both caffeinated and decaffeinated effective — polyphenols + cafestol mechanism, not just caffeine. AASLD acknowledges coffee as hepatoprotective. |
| Mediterranean diet | High adherence, long-term | ALT ↓ 5–15 U/L in MASLD populations | 12–24 wk | **[RCT/Meta]** | Multiple MedDiet + NAFLD trials | Not a specific ALT endpoint trial; effect driven by weight loss + anti-inflammatory effect |
| Omega-3 (EPA+DHA) | >2 g/day combined EPA+DHA, 12+ wk | ALT ↓ 2–5 U/L (MD −2.12 U/L in one meta); effect on GGT more reliable | 12–24 wk | **[Meta]** | Clinical Nutrition 2025 meta; PMC5019889; J Hepatol 2012 meta | **Mixed evidence**: 2025 meta (omega-3 and MASLD) shows GGT ↓ −5.4 U/L but ALT not consistently significant; dose <2g associated with less benefit |
| Vitamin E (800 IU/day) | Alpha-tocopherol, 96 wk | ALT and AST ↓ significantly vs. placebo (P<0.001); NASH resolution rate 43% vs. 19% placebo | 24–48 wk | **[RCT]** | PIVENS trial, *NEJM* 2010 (Sanyal) | **Non-diabetic** NASH only; fibrosis not improved; long-term safety (prostate cancer signal, hemorrhagic stroke at >400 IU — not established but flagged in meta-analyses); no benefit shown in T2D-associated NASH |
| Pioglitazone (30 mg/day) | 96 wk in non-diabetic NASH | ALT and AST ↓ significantly; weight gain 4.7 kg | 12–48 wk | **[RCT]** | PIVENS trial *NEJM* 2010 | Primary endpoint not met (34% vs. 19% NASH improvement, p=0.04 — borderline); liver enzymes and histology improved; not first-line in non-diabetic due to weight gain, fluid retention, bone loss |
| Alcohol cessation | From heavy drinking (>14 drinks/wk) to abstinence | ALT ↓ 30–60% within 4–8 wk; normalization if no underlying fibrosis | 4–8 wk | **[RCT/Cohort]** | Multiple detox and cessation studies; Reframe 2024 review | Fastest ALT normalization of any intervention for alcohol-related elevation; GGT falls faster (see GGT section) |
| Silymarin / milk thistle | 140–420 mg silymarin TID | ALT: **null** in best-quality MASLD RCT | 48 wk | **[RCT]** | Ratziu 2012 *J Hepatol* (LEANI STUDY) — 99 patients, 48 wk, no significant ALT reduction vs. placebo | **Oversold**: the Ratziu 2012 trial is the highest-quality MASLD silymarin RCT; earlier positive trials were small or uncontrolled. Silymarin for ALT reduction in MASLD is not supported by current best evidence. |
| **Worseners:** Alcohol (dose-response) | Each standard drink (14g EtOH) | ALT rises approximately linearly with consumption >14 drinks/week | Weeks | **[Cohort]** | NHANES 2001–2010 dose-response; PMC4917983 | AST/ALT ratio >2 suggests alcoholic cause; GGT most sensitive (rises even with 3 drinks/day) |
| **Worseners:** Anabolic steroids / SARMs | Any use | ALT ↑ 3–20× ULN; cholestatic-mixed pattern; peliosis hepatis risk | Weeks | **[Mechanism/Case series]** | Navarro 2017 *Hepatology*; DILIN registry | Common in 20M demographic; must disclose to lab/clinician when evaluating transaminitis |
| **Worseners:** High-dose supplements (green tea extract, kava, ashwagandha) | Variable doses | ALT ↑ 2–10× ULN; dose-dependent | Weeks–months | **[Case series/DILIN]** | Navarro 2017; LiverTox database | Supplement-induced DILI underappreciated in young men; green tea catechins hepatotoxic at >800 mg/day EGCG |
| **Worseners:** Saturated fat overfeeding | +750 kcal/day SFA for 3 wk | Liver fat +5% (absolute); ALT ↑ modestly | 3 wk | **[RCT]** | Rosqvist 2014 *Diabetes* | Palmitic acid specifically increases hepatic DNL; linoleic acid (PUFA) produces less liver fat despite identical calorie surplus |

**Pharmacotherapy reference (scale only):** Semaglutide 0.4 mg/day × 72 wk: NASH resolution 59% (vs. 17% placebo), ALT reduction significant; FDA approved August 2025 for non-cirrhotic MASH (ESSENCE trial). Resmetirom 80–100 mg/day: liver fat (MRI-PDFF) ↓ 34–39% at 16 wk; ALT, AST, GGT all ↓ significantly (MAESTRO-NASH, *NEJM* 2024; first FDA-approved drug for MASH). Pioglitazone: ALT ↓ in MASLD, ~20–30% from baseline. URSODCA (ursodeoxycholic acid, 13–15 mg/kg/day): **null for MASLD** (Lindor 2004 *Gastroenterology*); do not use for MASLD. Obeticholic acid: ALT/AST improvement in NASH phase 3 (REGENERATE), fibrosis improvement; FDA approval under review.

**Synthesis:**

- **Biggest movers**: weight loss (dose-response, fastest via VLC) > alcohol cessation (if applicable) > exercise (even without weight loss — Hallsworth) > coffee (chronic, hepatoprotective).
- **Null/oversold for ALT**: milk thistle (null in best MASLD trial), "detox" protocols (no mechanistic basis for accelerating liver enzyme clearance beyond eliminating the offending agent), turmeric/curcumin as an extract at supplement doses may paradoxically cause DILI.
- **Coffee caveat**: hepatoprotective effect is consistent across cohort studies and acknowledged by AASLD; the mechanism is multi-compound (chlorogenic acids, cafestol, melanoids). This is a **[Cohort]** finding without a large RCT — plausible and low-harm but not established at RCT level.
- **South Asian note**: lean MASLD (BMI <23 kg/m²) is disproportionately common in South Asians. An ALT 25–33 U/L in a lean South Asian male may reflect early MASLD — use FIB-4 (with caveat it is unvalidated <35) and consider liver ultrasound or FibroScan. PNPLA3 rs738409 GG genotype → 73% more liver fat than CC and higher fibrosis risk; TM6SF2 rs58542926 → OR 1.82 for MASLD.
- **3-month best-case** from ALT 35 U/L (borderline elevated): alcohol elimination + exercise 4×/week + 5% weight loss + coffee → ALT ↓ 30–50% (to ~17–25 U/L).
- **SNPs**: PNPLA3 rs738409 (biggest genetic modifier of MASLD progression — GG homozygotes may benefit more from weight loss per unit; no specific drug exists yet), TM6SF2 rs58542926 (reduced VLDL secretion; statin use requires monitoring), HFE C282Y (hemochromatosis; elevated ferritin + elevated ALT → iron overload workup).

---

## AST

**Quick read:** AST tracks ALT for liver-driven changes but has significantly lower liver specificity. The dominant non-liver confounders — exercise, muscle injury, hemolysis — must be excluded before attributing any AST change to a liver intervention. After accounting for muscle source, the same interventions that move ALT move AST with similar direction and slightly smaller magnitude.

### Effect Size Table

| Intervention | Direction & Magnitude | Evidence | Caveats |
|---|---|---|---|
| Weight loss 5–10% | AST ↓ 10–25% from baseline | **[Meta/RCT]** Multiple | Smaller % reduction than ALT in most trials; AST/ALT ratio may increase with weight loss if ALT falls faster |
| Aerobic/resistance exercise (liver effect) | AST ↓ 5–15 U/L in MASLD | **[Meta]** | Critical: exercise *also* raises AST from muscle source; interpret AST post-exercise with CK. Do not assess AST within 72 hr of strenuous exercise. |
| Alcohol cessation | AST ↓ 30–50% within 4–8 wk; AST/ALT ratio falls toward <2 | **[RCT/Cohort]** | AST/ALT ratio ≥2 is diagnostic of alcoholic etiology (~70–90% sensitivity); normalization of ratio on cessation confirms alcohol as driver |
| Coffee (habitual 3–5 cups/day) | AST moderately reduced in cohort studies | **[Cohort]** | Same mechanism as ALT hepatoprotection |
| Omega-3 PUFA | AST ↓ MD −1.50 U/L (95% CI −2.59 to −0.42) | **[Meta]** | Modest; duration >12 wk needed |
| Vitamin E (PIVENS) | AST ↓ significantly vs. placebo (P<0.001) | **[RCT]** | PIVENS data |
| **Worseners:** Strenuous exercise (acute) | AST ↑ 2–5× ULN within 24–48 hr | **[Mechanism]** | CK co-elevated confirms muscle source; half-life of cytosolic AST ~16–18 hr so returns to normal within 3–5 days |
| **Worseners:** Alcohol | AST/ALT >2 in alcoholic hepatitis | **[Mechanism/Cohort]** | Mechanism: EtOH depletes pyridoxal-5'-phosphate → preferentially lowers ALT activity; plus mitochondrial AST release |

**Synthesis:** AST interventions mirror ALT interventions once the muscle source is excluded. The AST/ALT (DeRitis) ratio is the key interpretive tool: ratio <1 favors MASLD; ratio ≥2 favors alcohol; ratio increasing toward 1+ with weight loss/exercise may reflect improving fibrosis. No interventions reliably lower AST without also affecting ALT or muscle.

---

## ALP

**Quick read:** ALP is less responsive to lifestyle interventions than ALT/AST. Bone-derived ALP (the dominant source in a 20-year-old male with recent growth plate closure) does not change with metabolic interventions. Elevated liver ALP (confirmed by co-elevated GGT) responds modestly to weight loss and treatment of underlying cholestatic disease. Vitamin D and calcium supplementation can modestly lower ALP in vitamin D-deficient individuals.

### Effect Size Table

| Intervention | Direction & Magnitude | Evidence | Caveats |
|---|---|---|---|
| Weight loss in MASLD | ALP ↓ modestly (< ALT/AST response); CALERIE 2-yr study showed ALP ↓ slightly in CR group | **[RCT]** | Not a primary endpoint in most liver trials; smaller effect than ALT/GGT |
| Vitamin D repletion (if deficient) | ALP ↓ 10–20 U/L in vitamin D-deficient individuals over 3–6 months | **[Meta]** | Mechanism: vitamin D deficiency → secondary hyperparathyroidism → ↑ bone ALP. Repleting vitamin D normalizes parathyroid axis. This effect is on *bone* ALP, not liver ALP. |
| Ursodeoxycholic acid (UDCA) in PBC | ALP ↓ 40–60% at 13–15 mg/kg/day in PBC patients | **[RCT]** | Effect is disease-specific (PBC/PSC) — **not applicable to MASLD**; UDCA is null for MASLD-related ALP. |
| Obeticholic acid in PBC | ALP ↓ 30–40%; combination with UDCA synergistic | **[RCT]** | FXR agonist; specific to cholestatic liver disease |
| Zinc repletion (if deficient) | ALP potentially ↑ toward normal (zinc is a cofactor; deficiency lowers ALP) | **[Mechanism]** | Uncommon in adequately nourished adults; relevant in malabsorptive states |
| **Worseners:** Alcohol (ALP effect) | ALP mildly ↑ with heavy use but less pronounced than GGT | **[Cohort]** | ALP less sensitive than GGT for alcohol |
| **Worseners:** Drugs (phenytoin, carbamazepine) | ALP ↑ via hepatic enzyme induction | **[Mechanism]** | Drug-induced; not metabolic |

**Synthesis:** If ALP is elevated and GGT is normal in a 20M with recent skeletal growth, no intervention is needed — this is bone ALP during late growth. If ALP is elevated with co-elevated GGT (confirming hepatic source), treat the underlying cause (MASLD → weight loss + exercise; cholestatic disease → specific treatment). Lifestyle changes for ALP are indirect — correct underlying metabolic liver disease.

---

## GGT

**Quick read:** GGT is the most sensitive and least specific liver enzyme — it responds to alcohol, oxidative stress, MASLD, drugs, and smoking independently. Alcohol cessation produces the fastest and largest GGT reductions (4–8 weeks). Coffee is the most consistent lifestyle-based GGT reducer. Weight loss and exercise produce reliable reductions. GGT <20 U/L correlates with lowest cardiometabolic risk in prospective data; GGT is an independent all-cause mortality predictor (Ruttmann 2005 *Circulation*, n=163,944).

### Effect Size Table

| Intervention | Dose / Protocol | Direction & Magnitude | Time to Effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Alcohol cessation | From ≥3 drinks/day to abstinence | GGT ↓ 30–50% within 2–4 wk; often normalizes within 6–8 wk if no underlying disease | 2–8 wk | **[RCT/Cohort]** | Multiple detox studies; Biomarkers Alc Alcoholism 2009; Reframe 2024 | GGT half-life in serum: 2–3 weeks with cessation; fastest normalization of any liver enzyme |
| Alcohol reduction (moderate) | From heavy to moderate (≤14 drinks/wk) | GGT ↓ 20–35% | 4–8 wk | **[RCT]** | NHANES dose-response; clinical cessation studies | Even partial reduction produces measurable GGT fall |
| Weight loss 5–10% | Dietary or exercise | GGT ↓ 20–40% from baseline | 8–16 wk | **[RCT/Meta]** | DiRECT: GGT ↓ 38% at 12 mo; Gasteyger 2008 (GGT ↓ significantly in men after LCD) | Effect parallels ALT in most weight-loss interventions |
| DiRECT (15 kg weight loss) | VLC 825 kcal/day | GGT ↓ 38–53% depending on degree of weight loss | 12–24 wk | **[RCT]** | Zhyzhneuskaya 2025 *Diabetic Medicine* | GGT correlates with liver fat r=0.4 in DiRECT |
| Coffee (3–5 cups/day habitual) | Regular or decaf | GGT ↓: habitual drinkers have 19.5 U/L vs. 21.8 U/L in non-drinkers (decaf); GGT elevation risk ↓ 30%; dose-dependent attenuation of alcohol-induced GGT elevation | Chronic | **[Cohort]** | NHANES inverse association; Swedish cohort (Tandfonline 2021); multiple prospective | Most consistent lifestyle modifier of GGT across cohorts; both caffeinated and decaf effective |
| Exercise (aerobic + resistance) | 150 min/wk, 12+ wk | GGT ↓ 10–25% in MASLD populations | 12–24 wk | **[Meta]** | MASLD exercise meta-analyses | Exercise-mediated GGT reduction occurs partly through reduced liver fat, partly through improved oxidative stress response |
| Omega-3 PUFA | <2000 mg EPA+DHA/day, >12 wk | GGT ↓ −5.38 U/L (WMD, 95% CI −9.16 to −1.61) | 12–24 wk | **[Meta]** | Clinical Nutrition 2025 omega-3 MASLD meta | GGT response more consistent than ALT in recent meta-analyses |
| Fructose (10 wk, 25% kcal) elimination vs. addition | Removing fructose-sweetened beverages | GGT: fructose-sweetened beverages → GGT ↑; glucose-sweetened → GGT unchanged | 10 wk | **[RCT]** | Stanhope 2009 JCI; Hieronimus 2020 | Fructose-specific GGT elevation — confirmed in controlled inpatient study |
| Smoking cessation | Cessation from active smoking | GGT ↓ modestly; smoking is an independent GGT driver | Weeks–months | **[Cohort]** | Multiple epidemiological studies | Mechanism: smoking-induced oxidative stress upregulates GGT |
| **Worseners:** Drugs (enzyme inducers) | Phenytoin, carbamazepine, barbiturates, statins, warfarin | GGT ↑ via microsomal enzyme induction | Weeks | **[Mechanism]** | Standard pharmacology | Drug-induced GGT elevation is *not* hepatocellular injury; isolated GGT ↑ in patient on enzyme-inducer is expected, not alarming |
| **Worseners:** Alcohol (dose-response) | 3+ drinks/day | GGT most sensitive alcohol marker; elevated in ≥80% of heavy drinkers | Days–weeks | **[Cohort/RCT]** | PMC4917983; Alcohol Alcoholism 2009 | 10–15% of drinkers don't elevate GGT (genetic variation in GGT induction); normal GGT does not exclude heavy drinking |

**Pharmacotherapy reference (scale only):** Semaglutide (ESSENCE trial): GGT reduced significantly as part of overall liver enzyme improvement. Resmetirom (MAESTRO-NASH): GGT ↓ significantly at 52 wk **[RCT]**. Pemafibrate (fibrate): reduces GGT and ALT in MASLD/dyslipidemia context (pPar-alpha agonist; Japan approved for dyslipidemia; PROMINENT trial for CV outcomes). Obeticholic acid: GGT and ALP reduction in PBC.

**Synthesis:**

- **GGT as a systemic oxidative-stress biomarker** is the most important reframing: GGT is not just "the alcohol marker." It independently predicts all-cause and CV mortality (Ruttmann 2005 *Circulation*: HR 1.66 per log-GGT increase over 17 yr, n=163,944). In the absence of alcohol and drug use, persistently elevated GGT in a lean young male suggests either MASLD, oxidative stress from another source (smoking, poor diet quality, high fructose), or subclinical metabolic dysfunction.
- Fastest normalizers: alcohol cessation >> weight loss + coffee.
- **South Asian note**: GGT may be disproportionately elevated in lean South Asians with MASLD because lean MASLD often shows higher inflammatory/metabolic activity per unit liver fat than obese-associated MASLD (Eslam 2020; lean MASLD phenotype is more aggressive metabolically in some cohorts).
- **3-month best-case** from GGT 45 U/L (assuming no significant alcohol): coffee 4 cups/day + 5% weight loss + exercise 4×/week → GGT ↓ 30–45% (to ~25–32 U/L).

---

## Total Bilirubin

**Quick read:** Bilirubin in the normal-to-mildly-elevated range is largely determined by UGT1A1 genotype (Gilbert syndrome, ~8–12% of Caucasian males; ~3–5% of South Asian males). Interventions that reliably raise bilirubin are limited and mostly pathological (fasting raises Gilbert bilirubin; rifampin competitively inhibits UGT1A1). In the absence of Gilbert, bilirubin tracks hemolysis and hepatic synthetic function, not lifestyle.

### Effect Size Table

| Intervention | Direction & Magnitude | Evidence | Caveats |
|---|---|---|---|
| Fasting / prolonged caloric restriction | Total bili ↑ 50–100% in Gilbert carriers | **[Mechanism/RCT]** | Mechanism: bilirubin production constant but UGT1A1 capacity reduced and albumin binding changes with caloric restriction. Benign. |
| Illness, intense exercise, dehydration | Gilbert bilirubin ↑ transiently (2–5 mg/dL during stress) | **[Mechanism]** | Benign in Gilbert; would be concerning if persistent or if direct fraction elevated |
| Rifampin, indinavir, atazanavir | Total bili ↑ via UGT1A1 competitive inhibition | **[Mechanism/RCT]** | Drug-induced; mimics Gilbert biochemically |
| Hemolysis (induced by drugs, illness) | Total bili ↑ (indirect fraction) | **[Mechanism]** | Harmful — pathological; opposite direction from cardioprotection |
| Weight loss / MASLD treatment | Direct (conjugated) bilirubin may normalize as hepatic function improves in cirrhotic-range disease | **[RCT]** | Minimal effect in the healthy-to-borderline range |
| Coffee (habitual) | Weak inverse association with total bili in some cohorts | **[Cohort]** | Effect size small and inconsistently replicated; bilirubin primarily genotype-determined in healthy population |

**Synthesis:**

- Total bilirubin is one of the least intervention-responsive markers in a healthy population because it is largely genotype-driven (UGT1A1*28 for Gilbert).
- For a lean South Asian male: Gilbert syndrome prevalence may be lower (~3–5% vs. 8–12% Caucasian), but when present, bilirubin in the 1.2–2.5 mg/dL range is cardioprotective. Do not attempt to lower Gilbert bilirubin.
- The **cardioprotective "sweet spot"** for bilirubin is the Gilbert range (1.0–2.5 mg/dL, indirect-predominant). Intervening to lower this would be counterproductive. The goal is to avoid pathological bilirubin elevation (direct fraction >20% = biliary disease signal).
- **SNPs**: UGT1A1*28 (TA7 repeat, rs8175347) — the Gilbert variant. Also UGT1A1*6 (rs4148323, more common in East/South Asians) — similar functional impact. Both can be tested via 23andMe indirect or direct sequencing.

---

## Albumin

**Quick read:** Albumin is primarily determined by hepatic synthetic capacity, nutritional status, and inflammation — not acutely modifiable by lifestyle in healthy individuals with normal albumin. In healthy ranges (4.0–5.0 g/dL), the variation is mostly from hydration and acute-phase response. Persistent low albumin (<4.0 in a healthy 20M) is a flag for subclinical inflammation, GI protein loss, or kidney disease — not a target for supplemental protein.

### Effect Size Table

| Intervention | Direction & Magnitude | Evidence | Caveats |
|---|---|---|---|
| Protein intake (high vs. adequate) | Albumin changes minimally with protein intake when intake is >0.8 g/kg in healthy adults; albumin not a sensitive marker of dietary protein adequacy | **[Meta]** | In severe protein-calorie malnutrition, correcting protein intake raises albumin over weeks; not relevant in adequately nourished 20M |
| Resolution of acute inflammation | Albumin ↑ 0.3–0.5 g/dL toward baseline over 2–3 wk after illness resolves | **[Mechanism]** | Acute-phase response (e.g., minor infection, stress) suppresses albumin synthesis; self-corrects |
| Adequate hydration at draw | Albumin may appear 0.2–0.4 g/dL higher if hemoconcentrated from dehydration | **[Mechanism]** | Preanalytical — not a real change |
| Exercise training (chronic, long-term) | Albumin modestly ↑ or unchanged | **[Cohort]** | Athletes tend to have slightly higher albumin (better nutrition, lower chronic inflammation) |
| **Worseners:** MASLD → cirrhosis | Albumin falls <3.5 as synthetic capacity fails (late marker) | **[Cohort]** | Albumin is a late marker of hepatic failure; near-normal in early MASLD |
| **Worseners:** Chronic alcohol use disorder | Albumin ↓ via malnutrition + liver synthetic impairment | **[Cohort]** | Reversible with cessation and nutritional repletion |

**Synthesis:** In a healthy 20M with albumin 4.0–5.0 g/dL, this marker is not meaningfully modifiable by lifestyle interventions and does not warrant targeted intervention. Low albumin (<4.0) in a healthy young male should prompt workup for systemic inflammation, renal disease, or GI protein loss — not dietary protein supplementation alone.

---

## Globulin, A/G Ratio, Total Protein

**Quick read:** These are composite markers driven by albumin and the immunoglobulin fraction. In healthy individuals, variation is dominated by hydration, recent illness, and the acute-phase response. There are no specific lifestyle interventions with meaningful effect sizes on globulin or A/G ratio in healthy populations. High globulin (>4.0 g/dL) prompts SPEP to rule out monoclonal gammopathy; low globulin (<1.5 g/dL) prompts immunodeficiency workup.

### Key Points (No Formal Effect Size Table — Insufficient RCT Data)

- **Globulin** rises with any immune activation (infection, inflammation, vaccination — transient); resolves over weeks.
- **A/G ratio** tracks inversely with globulin. There are no evidence-based interventions that "optimize" A/G ratio in healthy individuals.
- **Total protein** is dominated by hydration. Well-hydrated vs. dehydrated at draw can shift total protein by 0.3–0.5 g/dL.
- **No supplement, diet, or exercise intervention has a published effect size on globulin or A/G ratio in healthy adults.** Any claim to "balance" A/G ratio through diet lacks a mechanism.

---

## Cross-Marker Patterns

### Weight Loss — Multiple Markers Couple

In sustained weight loss ≥5% body weight, the following changes co-occur as a metabolic package:

| Marker | Typical Direction | Time |
|---|---|---|
| Fasting glucose | ↓ 5–15 mg/dL | 8–16 wk |
| HbA1c | ↓ 0.3–0.5% | 12–24 wk |
| Fasting insulin / HOMA-IR | ↓ 20–40% | 8–16 wk |
| Uric acid | ↓ 0.5–1.0 mg/dL | 12–16 wk |
| ALT | ↓ 20–40% | 8–16 wk |
| GGT | ↓ 20–40% | 8–16 wk |
| Albumin | Minimal change | — |
| Globulin | Minimal change | — |

**Rapid weight loss caveat**: Very rapid weight loss (>1.5 kg/week) can transiently raise ALT (via gallstone formation / fat mobilization), GGT (unchanged or slightly ↑ during rapid ketosis), and uric acid (tissue catabolism + BHB competition at URAT1). DiRECT-protocol VLC diets show initial enzyme rises in some participants before sustained improvement.

---

### Alcohol Cessation — GGT/ALT/UA Coupled Response

| Marker | Direction | Timeline |
|---|---|---|
| GGT | ↓ 30–50% | 2–8 wk |
| ALT | ↓ 20–40% (if alcohol was primary driver) | 4–12 wk |
| AST | ↓ 20–40%; AST/ALT ratio falls toward <1 | 4–12 wk |
| Uric acid | ↓ 0.5–1.5 mg/dL | 2–4 wk |
| Fasting insulin | ↓ modestly | 4–8 wk |

GGT is the most sensitive marker of alcohol use and the fastest to normalize with cessation. If GGT remains persistently elevated despite genuine abstinence, consider co-existing MASLD, drug-induced GGT (enzyme inducers), or smoking as alternative drivers.

---

### Exercise — Insulin Sensitivity → Downstream Metabolic Effects

Aerobic exercise acts primarily through:
1. GLUT4 upregulation in skeletal muscle → peripheral insulin sensitivity ↑
2. Reduced hepatic fat → hepatic insulin sensitivity ↑
3. Improved AMP:ATP ratio → AMPK activation → reduced hepatic gluconeogenesis

| Marker | Direction | Source |
|---|---|---|
| HOMA-IR | ↓ 0.47–1.05 | **[Meta]** |
| Fasting insulin | ↓ 1–3 µIU/mL | **[Meta]** |
| Fasting glucose | ↓ 6–10 mg/dL | **[Meta]** |
| Liver fat (MRS) | ↓ 10–20% independent of weight | **[RCT]** Hallsworth 2011 *Gut* |
| ALT | ↓ 5–20 U/L (in MASLD population) | **[Meta]** |
| GGT | ↓ 10–25% | **[Meta]** |

Important: exercise-induced ALT/AST improvement requires ≥8–12 weeks of consistent training. Acute exercise raises AST and ALT transiently (48–72 hr); always separate "exercise effect on liver enzymes" from "exercised yesterday" confound.

---

### Fructose/SSB — Multi-Marker Worsening Cascade

10 wk of fructose-sweetened beverages at 25% total energy (Stanhope 2009 JCI; Hieronimus 2020 *J Nutr*):

| Marker | Direction | Glucose-sweetened comparison |
|---|---|---|
| Uric acid | ↑ significantly | Glucose arm: no change |
| GGT | ↑ significantly | Glucose arm: no change |
| Visceral fat | ↑ | Glucose arm: no significant increase |
| LDL particle size | ↓ (small dense LDL ↑) | Glucose arm: less effect |
| Fasting glucose | ↑ 3–5 mg/dL | Similar but smaller |
| HOMA-IR | ↑ | Glucose arm: smaller increase |

The fructose-glucose differential is mechanistically driven and replicated in metabolic ward conditions. This is not a dietary philosophy argument — it is a controlled inpatient finding.

---

## Drug Class Reference Table

Scale only — for calibrating lifestyle effect sizes against pharmacological effects. Do not interpret as recommendations.

| Drug Class / Agent | HbA1c | Fasting Glucose | Fasting Insulin / HOMA-IR | Uric Acid | ALT/GGT | Weight | Evidence |
|---|---|---|---|---|---|---|---|
| Metformin (500–2000 mg/day) | −0.7 to −1.0% | −10 to −15 mg/dL | Modest ↓ HOMA-IR | No direct effect | No significant effect at standard doses | Neutral to mild −1 to −2 kg | **[Meta]** |
| Semaglutide 2.4 mg/wk (Wegovy/Ozempic) | −1.5 to −2.0% | −20 to −30 mg/dL | ↓↓ HOMA-IR | Modest ↓ (via weight loss) | ALT/GGT ↓ significantly; FDA-approved for MASH (ESSENCE 2025) | −10 to −15% body weight at 1 yr | **[RCT]** STEP, SUSTAIN, ESSENCE |
| SGLT2 inhibitors (empagliflozin 10 mg, dapagliflozin 10 mg) | −0.7 to −0.8% | −12 to −15 mg/dL (glucosuria) | ↓ modest | −0.5 to −0.7 mg/dL | Modest ALT/GGT ↓ | −2 to −3 kg | **[Meta]** |
| Pioglitazone 30–45 mg/day | −0.8 to −1.0% | −10 to −15 mg/dL | ↓↓ HOMA-IR (most potent oral agent for IR) | No direct effect | ALT ↓ 20–30% in MASLD (PIVENS) | +3 to +5 kg | **[RCT]** PIVENS |
| Berberine 500 mg TID | −0.63 to −0.73% | −0.52 to −0.86 mmol/L (−9 to −15 mg/dL) | ↓ HOMA-IR −1.15 | Limited data | Modest ALT ↓ in some trials | Modest | **[Meta]** Multiple |
| Allopurinol 300 mg/day (XO inhibitor) | Negligible direct effect | Negligible direct effect | Modest IR improvement in hyperuricemia trials | ↓ 2–3 mg/dL | Modest, indirect | Neutral | **[Meta]** |
| Febuxostat 80 mg/day | Negligible direct effect | Negligible direct effect | Modest IR improvement | ↓ 3–4 mg/dL (superior to allopurinol) | Indirect improvement | Neutral | **[Meta]** PMC12456345 |
| Vitamin E 800 IU/day | No significant effect | No significant effect | No direct effect | No effect | ALT/AST ↓ significantly in non-diabetic NASH (P<0.001 PIVENS) | Neutral | **[RCT]** PIVENS |
| Resmetirom 100 mg/day (THR-β agonist) | LDL-C ↓ ~20% (primary driver); modest A1c effect | Modest | Modest | — | ALT, AST, GGT ↓; liver fat ↓ 34–39% MRI-PDFF at 16 wk | Neutral | **[RCT]** MAESTRO-NASH *NEJM* 2024; FDA approved 2024 |
| UDCA 13–15 mg/kg/day | No effect on glycemia | No effect | No effect | No effect | **Null for MASLD** (Lindor 2004 *Gastroenterology*); effective in PBC only | Neutral | **[RCT]** |
| Statins (atorvastatin, rosuvastatin) | Modest HbA1c ↑ (diabetogenic effect ~0.1–0.3%) | Glucose ↑ slightly | Insulin resistance ↑ mildly | No direct effect | Transient ALT ↑ in 1–3% (<3× ULN); no clinically meaningful sustained ↑ at standard doses | Neutral | **[Meta]** |

---

## Sources

**Landmark Trials Cited:**

- Lean ME, Leslie WS, Barnes AC, et al. Primary care-led weight management for remission of type 2 diabetes (DiRECT): an open-label, cluster-randomised trial. *Lancet* 2018;391(10120):541–551.
- Zhyzhneuskaya SV, et al. Clinical utility of liver function tests for resolution of MASLD after weight loss in the DiRECT trial. *Diabetic Medicine* 2025. [doi:10.1111/dme.15462](https://onlinelibrary.wiley.com/doi/10.1111/dme.15462)
- Sanyal AJ, Chalasani N, Kowdley KV, et al. Pioglitazone, vitamin E, or placebo for nonalcoholic steatohepatitis (PIVENS). *N Engl J Med* 2010;362(18):1675–1685. [PMID 20427778](https://pubmed.ncbi.nlm.nih.gov/20427778/)
- Hallsworth K, Fattakhova G, Hollingsworth KG, et al. Resistance exercise reduces liver fat and its mediators in non-alcoholic fatty liver disease independent of weight loss. *Gut* 2011;60(9):1278–1283. [PMID 21708823](https://pubmed.ncbi.nlm.nih.gov/21708823/)
- Stanhope KL, Schwarz JM, Keim NL, et al. Consuming fructose-sweetened, not glucose-sweetened, beverages increases visceral adiposity and lipids and decreases insulin sensitivity in overweight/obese humans. *J Clin Invest* 2009;119(5):1322–1334. [PMID 19381015](https://pubmed.ncbi.nlm.nih.gov/19381015/)
- Hieronimus B, Schwarz JM, Stanhope KL, et al. Synergistic effects of fructose and glucose on hepatic lipogenesis are mediated by sterol regulatory element-binding protein-1c. *Am J Clin Nutr* 2020;112(6):1468–1476. [Hieronimus 2020](https://academic.oup.com/ajcn/article/112/6/1468/5895560)
- Hall KD, Guo J, Courville AB, et al. Effect of a plant-based, low-fat diet versus an animal-based, ketogenic diet on ad libitum energy intake. *Nat Med* 2021;27:344–353. [PMID 33479499](https://pubmed.ncbi.nlm.nih.gov/33479499/)
- Yin J, Xing H, Ye J. Efficacy of berberine in patients with type 2 diabetes mellitus. *Metabolism* 2008;57(5):712–717. [PMID 18442638](https://pubmed.ncbi.nlm.nih.gov/18442638/) — Berberine ~= metformin in head-to-head RCT.
- Ratziu V, de Ledinghen V, Oberti F, et al. A randomized controlled trial of high-dose ursodesoxycholic acid for nonalcoholic steatohepatitis (LEANI). *J Hepatol* 2011;54(5):1011–1019. [Ratziu 2011 silymarin context]; also Ratziu silymarin RCT 2012 *J Hepatol*.
- Lindor KD, Kowdley KV, Heathcote EJ, et al. Ursodeoxycholic acid for treatment of nonalcoholic steatohepatitis: results of a randomized trial. *Gastroenterology* 2004;126(4):1024–1033. [UDCA null for NAFLD]
- Spiegel K, Leproult R, Van Cauter E. Impact of sleep debt on metabolic and endocrine function. *Lancet* 1999;354(9188):1435–1439. [Sleep and glucose tolerance seminal paper]
- Harrison SA, Bedossa P, Guy CD, et al. A Phase 3, Randomized, Controlled Trial of Resmetirom in NASH with Liver Fibrosis (MAESTRO-NASH). *N Engl J Med* 2024;390(6):497–509. [PMID 38324483](https://pubmed.ncbi.nlm.nih.gov/38324483/)
- Ruttmann E, Brant LJ, Concin H, et al. Gamma-glutamyltransferase as a risk factor for cardiovascular disease mortality: an epidemiological investigation in a cohort of 163,944 Austrian adults. *Circulation* 2005;112(14):2130–2137.

**Meta-Analyses and Systematic Reviews:**

- Optimal Dose and Type of Physical Activity to Improve Glycemic Control in People Diagnosed With Type 2 Diabetes. *Diabetes Care* 2024;47(2):295–308. [doi:10.2337/dc23-0437](https://diabetesjournals.org/care/article/47/2/295/154149/)
- Effect of Dietary Approaches on Glycemic Control in Patients with Type 2 Diabetes: A Systematic Review with Network Meta-Analysis. *Nutrients* 2023;15(14):3156. [PMID 37513574](https://pubmed.ncbi.nlm.nih.gov/37513574/)
- The effects of low-carbohydrate diet on glucose and lipid metabolism in overweight or obese patients with T2DM: a meta-analysis of 17 RCTs. *Front Nutr* 2024. [doi:10.3389/fnut.2024.1516086](https://www.frontiersin.org/articles/10.3389/fnut.2024.1516086/full)
- Impact of Mediterranean Diet on Glycemic Control, BMI, Lipid Profile and Blood Pressure in T2D (7 RCTs, n=1,371). *MDPI Nutrients* 2024;17(24):3908. [doi](https://www.mdpi.com/2072-6643/17/24/3908)
- The Effect of Berberine on Metabolic Profiles in T2D: Meta-Analysis of RCTs. *PMID 34956436*, also Front Pharmacol 2024. [doi:10.3389/fphar.2024.1455534](https://www.frontiersin.org/articles/10.3389/fphar.2024.1455534/full)
- Efficacy of berberine in patients with type 2 diabetes (Yin 2008): [PMID 18442638](https://pubmed.ncbi.nlm.nih.gov/18442638/)
- Glucose-lowering effect of berberine on type 2 diabetes: systematic review and meta-analysis. *Front Pharmacol* 2022. [doi:10.3389/fphar.2022.1015045](https://www.frontiersin.org/articles/10.3389/fphar.2022.1015045/full)
- Resistance training and insulin resistance in overweight/obese non-diabetic adults: meta-analysis. [PMID 37331899](https://pubmed.ncbi.nlm.nih.gov/37331899/)
- Magnesium supplementation and insulin sensitivity/glucose control: meta-analysis RCTs. [PMID 27329332](https://pubmed.ncbi.nlm.nih.gov/27329332/)
- Effects of magnesium supplementation on glycemic control in T2D: systematic review and dose-response meta-analysis. *Br J Nutr* 2016. [Cambridge Core](https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/effects-of-oral-magnesium-supplementation-on-glycaemic-control-in-patients-with-type-2-diabetes/)
- Inositol supplementation on glucose homeostasis: meta-analysis of RCTs. *Clinical Nutrition* 2018. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0261561418311762); also PMC12574088 (2025 update)
- Intermittent fasting and glucose/insulin: meta-analyses. PMC8970877; PMC10945168; *Nutrition Reviews* 2025 (16:8 TRE meta).
- SGLT2 inhibitor uric acid meta-analysis: [PMC10807021](https://pmc.ncbi.nlm.nih.gov/articles/PMC10807021/); Frontiers Pharmacol 2025.
- Febuxostat vs. allopurinol meta-analysis: [PMC12456345](https://pmc.ncbi.nlm.nih.gov/articles/PMC12456345/); BMC Pharmacol Toxicol 2023. [PMC10722766](https://pmc.ncbi.nlm.nih.gov/articles/PMC10722766/)
- Fructose food sources and fasting uric acid: systematic review and meta-analysis of controlled feeding trials. *JNEP* 2022. [PMID 34087940](https://pubmed.ncbi.nlm.nih.gov/34087940/)
- Omega-3 PUFA and NAFLD/MASLD: meta-analyses: *Clinical Nutrition* 2025; [PMID 40441053](https://pubmed.ncbi.nlm.nih.gov/40441053/); Frontiers Nutr 2025; J Hepatol 2012.
- Resistance training for MASLD: meta-analysis. *Frontiers Physiology* 2025. [PMC12907158](https://pmc.ncbi.nlm.nih.gov/articles/PMC12907158/)
- Coffee and liver disease: systematic review. *Liver Int* 2014 (Saab); PMC5440772; PMC4862107; NHANES analysis [PMID 25124935](https://pubmed.ncbi.nlm.nih.gov/25124935/)
- Vitamin E and pioglitazone in MASLD: systematic review and meta-analysis. [PMC10504864](https://pmc.ncbi.nlm.nih.gov/articles/PMC10504864/)
- Semaglutide in MASH: ESSENCE trial; FDA approval August 2025; AASLD guidance update Nov 2025. [PMID 41201884](https://pubmed.ncbi.nlm.nih.gov/41201884/)

**South Asian-Specific:**

- Kelly West Lecture 2024 — Diabetes in South Asians: Uncovering Novel Risk Factors. *Diabetes Care* 2024;47(1):7. [doi:10.2337/dci23-0074](https://diabetesjournals.org/care/article/47/1/7/154008/)
- Lean MASLD in Asian populations (BMI <23 threshold): [PMC10989317](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989317/); Eslam M et al. MAFLD: a consensus-driven proposed nomenclature. *J Hepatol* 2020;73(1):202–209.
- PNPLA3 rs738409 and TM6SF2 genetic risk for MASLD: [JCI 2024 human genetics MASLD](https://www.jci.org/articles/view/186424); PMC11736312.

**Spiegel and Sleep:**

- Spiegel K, Leproult R, Van Cauter E. Impact of sleep debt on metabolic and endocrine function. *Lancet* 1999;354:1435–1439.
- Buxton OM, Pavlova M, Reid EW, et al. Sleep restriction for 1 week reduces insulin sensitivity in healthy men. *Diabetes* 2010;59(9):2126–2133. [PMID 20585000](https://pubmed.ncbi.nlm.nih.gov/20585000/)
- Donga E, van Dijk M, van Dijk JG, et al. A single night of partial sleep deprivation induces insulin resistance in multiple metabolic pathways in healthy subjects. *JCEM* 2010;95(6):2963–2968.
- Tasali E, Wroblewski K, Kahn E, et al. Effect of sleep extension on objectively assessed energy intake among adults with overweight in real-life settings. *JAMA Intern Med* 2022.

---

*Document version: May 2026. Calibrated for a healthy 20-year-old lean South Asian male. Companion files: `metabolic_panel.md`, `liver_panel.md`. Effect sizes are from pooled or replicated evidence where available; single-RCT findings are flagged. No clinical recommendations; quantitative reference only.*
