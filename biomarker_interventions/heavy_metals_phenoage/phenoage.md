# PhenoAge (Levine Phenotypic Age) — Intervention Research

> **PhenoAge is a derived score, not a biomarker.** It is a mortality-calibrated composite of chronological age plus 9 standard chemistry markers (Levine 2018 *Aging*; Liu 2018 *PLOS Med*): albumin, creatinine, glucose, log-CRP, lymphocyte %, MCV, RDW, alkaline phosphatase, WBC. There is no "PhenoAge intervention" — you optimize the components. Of the 9, **CRP, glucose, and WBC are the most lifestyle-responsive**; albumin, lymphocyte %, MCV, RDW, and ALP are less directly modifiable in a healthy young adult. The single highest-leverage cross-cutting interventions are **smoking cessation** (CRP ↓, WBC ↓; PhenoAge ↓ ~1.5–3 yr), **weight loss when applicable** (CRP ↓, glucose ↓; PhenoAge ↓ ~1–3 yr per 10 kg in obesity), **Mediterranean / DASH diet** (CRP ↓ 20–40%), **adequate sleep** (glucose ↓ 3–5 mg/dL, WBC ↓), and **regular exercise** (multiple components). Pharmacologic interventions with documented PhenoAge or biological-age effects: **GLP-1 agonists** (large CRP / glucose / weight effects), **statins** (CRP ↓ 20–40%), **rapamycin** (PEARL trial: DunedinPACE ↓ ~3% — extrapolation to PhenoAge unproven), **metformin** (TAME trial pending). **Critical caveat: at 20yM, PhenoAge has a noise floor of ±2–3 years from CRP / WBC / glucose / ALP day-to-day variability** — small changes are not meaningful.

**Cross-link:** Reference biology / clinical interpretation lives in `../../heavy_metals_and_biological_age.md` §3 and `../../effect_sizes_hematology_other.md` §PhenoAge Components. Intervention research for individual components lives in their respective biomarker files (`../immune/CRP.md`, `../metabolic/fasting_glucose.md`, `../cbc/WBC.md`, `../cbc/MCV.md`, `../cbc/RDW.md`, `../liver/ALP.md`, `../liver/albumin.md`, `../kidney_electrolytes_pancreas/creatinine.md`, `../immune/lymphocyte_pct.md`). This file is the **cross-cutting synthesis** — interventions that move multiple components simultaneously.

---

## Evidence-Grading Legend

| Tag | Meaning |
|---|---|
| **[Meta]** | Replicated meta-analysis of ≥5 RCTs |
| **[RCT]** | Single high-quality RCT |
| **[Cohort]** | Prospective observational |
| **[MR]** | Mendelian randomization |
| **[Mechanism]** | Pharmacology / physiology extrapolation |
| **[1-Trial]** | Single small trial |

Population caveat: **most PhenoAge intervention magnitude estimates are derived by applying lifestyle-intervention effect sizes for the 9 components × Levine formula coefficients, then summing.** Direct RCTs measuring PhenoAge as a primary endpoint are rare (Belsky 2023 CALERIE; Kaeberlein PEARL; a few small lifestyle trials). At baseline near-optimal (PhenoAge ≈ chronological age in a healthy 20yM), floor effects shrink magnitudes ~30–60%.

**Levine PhenoAge formula reminder** (component coefficients drive magnitude estimates):

```
xb = -19.907
     - 0.0336 × albumin (g/L)
     + 0.0095 × creatinine (µmol/L)
     + 0.1953 × glucose (mmol/L)
     + 0.0954 × ln(CRP, mg/L)
     - 0.0120 × lymphocyte percent (%)
     + 0.0268 × MCV (fL)
     + 0.3306 × RDW (%)
     + 0.00188 × ALP (U/L)
     + 0.0554 × WBC count (10⁹/L)
     + 0.0804 × chronological age (years)
```

Note: CRP is **log-transformed**, so the same absolute change matters more at low CRP. RDW has the largest single-marker coefficient relative to its dynamic range. WBC coefficient × typical effect size (1 ×10⁹/L) ≈ 1 year of PhenoAge.

---

## 1. Foods that LOWER PhenoAge (via component improvements)

| Food | Dose / pattern | Direction & magnitude (estimated PhenoAge effect) | Time to effect | Evidence (component pathway) | Source | Caveats |
|---|---|---|---|---|---|---|
| **Mediterranean diet** (extra-virgin olive oil, fish, vegetables, legumes, nuts, whole grains, moderate dairy) | Adoption | CRP ↓ 20–40% (~0.3–0.8 mg/L absolute drop in elevated baseline); glucose ↓ 3–5 mg/dL; WBC ↓ 0.2–0.5 ×10⁹/L; estimated PhenoAge ↓ ~0.5–2 years over 6 months | 3–6 months | **[Meta — CRP; RCT — PREDIMED]** | Schwingshackl 2017 *Nutrients* (Mediterranean → CRP ↓); Estruch 2018 *NEJM* PREDIMED; Casas 2014 *PLOS One* | Largest single dietary intervention with PhenoAge-relevant component effects. In a lean healthy young adult with low baseline CRP <0.5 mg/L, effects are floor-limited (~0.2 yr PhenoAge). |
| **DASH diet** (high vegetables, fruits, low-fat dairy, whole grains, lean protein, low Na) | Adoption | CRP ↓ ~15–30%; BP ↓ 5–11 mmHg SBP; glucose ↓ 2–4 mg/dL; estimated PhenoAge ↓ ~0.3–1.5 years | 3–6 months | **[RCT]** | Sacks 2001 *NEJM*; Chiavaroli 2019 *Nutrients* meta-analysis | Similar profile to Mediterranean. SA-friendly (vegetable-heavy). |
| **Fatty fish** (salmon, sardines, mackerel, herring, trout) — 2–3 servings/wk | Continuous | EPA/DHA → CRP ↓ ~0.2–0.4 mg/L (in elevated baseline); modest TG ↓; estimated PhenoAge ↓ ~0.2–0.8 years (CRP component) | 8–12 weeks | **[Meta]** | Li 2014 *J Cardiovasc Pharmacol Ther* meta-analysis (fish oil → CRP ↓); see also `../omega_fatty_acids/EPA_DHA.md` | Floor effects in lean young adults. |
| **Whole grains** (oats, barley, quinoa, whole wheat) — 3–5 servings/d | Continuous | Soluble fiber + resistant starch → glucose ↓ 2–5 mg/dL; CRP ↓ ~10–20%; modest WBC ↓; estimated PhenoAge ↓ ~0.3–1 year | 3–6 months | **[Meta]** | Aune 2016 *BMJ* (whole grain meta); Whitehead 2014 *Am J Clin Nutr* (β-glucan → CRP ↓) | |
| **Legumes** (lentils, chickpeas, black beans, kidney beans) — 4+ servings/wk | Continuous | Soluble fiber + plant protein → glucose ↓ 2–4 mg/dL; CRP ↓ ~10–20%; estimated PhenoAge ↓ ~0.3–1 year | 3–6 months | **[Meta]** | Sievenpiper 2009 *Diabetes Care* (legumes → glycemic control); Salehi-Abargouei 2015 *Br J Nutr* (legumes → CRP ↓) | SA-friendly staple. |
| **Leafy greens / cruciferous vegetables** (spinach, kale, broccoli, Brussels sprouts) — daily | Continuous | Folate / B12 / nitrate / sulforaphane → modest CRP ↓; supports lymphocyte function; estimated PhenoAge ↓ ~0.1–0.4 years | 8–12 weeks | **[Meta]** | Aune 2017 *Int J Epidemiol* (vegetables → all-cause mortality); Hayes 2008 (sulforaphane Nrf2) | Modest direct PhenoAge effect; large ancillary mortality / disease benefits. |
| **Berries / polyphenol-rich fruits** (blueberries, strawberries, pomegranate) — daily | Continuous | Polyphenols → CRP ↓ ~10–20% in some trials; estimated PhenoAge ↓ ~0.1–0.4 years | 8–12 weeks | **[Meta + small RCTs]** | Joseph 2014 *Adv Nutr* (berries → CRP); inconsistent across trials | Floor effects in young lean adults. |
| **Nuts** (walnuts, almonds, pistachios, pecans) — 30 g/d | Continuous | EPA/DHA precursors (walnuts), MUFA, fiber → CRP ↓ ~10–25%; modest LDL ↓; estimated PhenoAge ↓ ~0.2–0.6 years | 8–12 weeks | **[Meta]** | Ros 2010 *Arch Intern Med*; PREDIMED nut arm (Estruch 2018) | |
| **Extra-virgin olive oil** (replacing butter / refined oils) — 30+ g/d | Continuous | Polyphenols → CRP ↓ ~15–25%; modest LDL ↓; estimated PhenoAge ↓ ~0.2–0.6 years | 8–12 weeks | **[Meta + RCT]** | Schwingshackl 2015 *Nutrients* (olive oil → CRP); PREDIMED EVOO arm | Use raw / low-heat to preserve polyphenols. |
| **Green tea** | 2–4 cups/d | Catechins (EGCG) → modest CRP ↓ ~5–15%; modest fasting glucose ↓ ~2 mg/dL; estimated PhenoAge ↓ ~0.1–0.3 years | 8–12 weeks | **[Meta]** | Serban 2015 *J Am Heart Assoc* (green tea → CRP); Liu 2014 *Am J Clin Nutr* (green tea → glucose) | Modest. |
| **Fermented dairy** (yogurt, kefir) — 1–2 servings/d | Continuous | Modest CRP ↓ in some trials; supports gut microbiome; estimated PhenoAge ↓ ~0.1–0.3 years | 8–12 weeks | **[Meta]** | Marette 2014 *Adv Nutr*; some inconsistency | |
| **Adequate dietary protein** (especially in low-baseline albumin or undernourished users) | 1.2–1.6 g/kg/d | Albumin ↑ 0.2–0.5 g/dL if low baseline (<4.0 g/dL); estimated PhenoAge ↓ ~0.3–1 year if baseline albumin low | 4–8 weeks | **[RCT in malnourished populations]** | Cawood 2012 *Ageing Res Rev* (protein → albumin in elderly malnourished) | Healthy 20yM eating >100 g protein/d: albumin already high-normal, no further movement. |
| **Coffee** (filtered, 2–4 cups/d) | Continuous | Modest CRP ↓ ~5–15%; some glucose ↓; ALP modest changes; net modest PhenoAge ↓ ~0.1–0.3 years | 8–12 weeks | **[Cohort]** | Loftfield 2018 *J Nutr*; Poole 2017 *BMJ* (coffee → mortality, CRP) | |

---

## 2. Foods that RAISE PhenoAge (via component worsening)

| Food | Dose / pattern | Direction & magnitude (estimated PhenoAge effect) | Time to effect | Evidence (component pathway) | Source | Caveats |
|---|---|---|---|---|---|---|
| **Ultra-processed foods** (NOVA group 4 — sugar-sweetened beverages, packaged snacks, processed meats, ready-meals) | High consumption | CRP ↑ 20–40%; glucose ↑ 3–8 mg/dL; WBC ↑ modest; estimated PhenoAge ↑ ~0.5–2 years | Months | **[Cohort + RCT]** | Hall 2019 *Cell Metab* (NIH ultra-processed RCT — weight ↑, calorie intake ↑); Monteiro 2018; SUN cohort | Largest dietary lever in the wrong direction. |
| **Sugar-sweetened beverages** (soda, sweetened juice, sports drinks, sweetened coffee/tea) | >1 serving/d | Fasting glucose ↑ 2–5 mg/dL chronic; CRP ↑ ~10–25%; WBC ↑ modest; weight ↑; estimated PhenoAge ↑ ~0.3–1.5 years | Months | **[Cohort + RCT]** | Schulze 2004 *JAMA* (Nurses' Health); Aeberli 2011 *AJCN* | |
| **Refined carbohydrates** (white bread, white pasta, white rice, pastries, sweetened cereals) | Daily large portions | Postprandial glucose spikes; chronic insulin resistance; CRP ↑; estimated PhenoAge ↑ ~0.3–1 year | Months | **[Meta]** | Livesey 2019 *Nutrients* (high-GI → CRP); Liu 2002 *AJCN* | |
| **Processed meats** (bacon, sausage, deli meat, hot dogs) | Daily | CRP ↑ ~10–30%; CV mortality ↑; estimated PhenoAge ↑ ~0.3–1 year | Months | **[Meta]** | Micha 2012 *Curr Atheroscler Rep*; Wang 2014 *Public Health Nutr* | |
| **Trans fats** (partially hydrogenated oils — largely banned in US 2018, still in some imported / restaurant) | Any | CRP ↑ 10–20%; LDL ↑; HDL ↓; estimated PhenoAge ↑ ~0.2–0.8 years | Months | **[Meta]** | Mozaffarian 2006 *NEJM* | Mostly historical for US-domestic foods; check imported / restaurant fried items. |
| **Excess alcohol** (>14 drinks/wk men, >7 women) | Heavy chronic | CRP ↑ (heavy drinking); MCV ↑ (macrocytosis from B12/folate impairment + direct toxicity); GGT ↑; ALP modest ↑; albumin ↓ (severe); WBC variable; estimated PhenoAge ↑ ~0.5–2 years (heavy drinkers) | Months–years | **[Meta]** | Imhof 2001 *Lancet* (J-curve for alcohol/CRP — moderate may ↓, heavy ↑); Ronksley 2011 *BMJ* | Light moderate drinking (~1 drink/d) historically associated with J-curve CRP ↓ — but newer MR evidence (Larsson 2020) suggests no causal benefit. |
| **High-sodium ultra-processed meals** | Daily | Hypertension + endothelial dysfunction + CRP ↑ modest; estimated PhenoAge ↑ ~0.1–0.5 years (indirect) | Months | **[Meta]** | He 2013 *BMJ* (Na → BP) | Indirect effect on PhenoAge components. |
| **Crash dieting / very-low-calorie diets / extended fasting in lean adults** | Repeated VLCD or >5-day fasts | Albumin ↓ transiently; lymphocyte % ↓; transient CRP ↑ during refeeding; muscle loss → creatinine ↓ (ironically improves PhenoAge in formula but biologically harmful); estimated PhenoAge effects mixed and confounded | Days–weeks | **[Cohort + 1-Trial]** | Most VLCD data in obese populations; lean-young-adult VLCD data scarce | Counterproductive in lean young adults. |

---

## 3. Supplements

### Lowering / improving (evidence-supported)

| Supplement | Dose | Direction & magnitude (estimated PhenoAge effect) | Time to peak | Evidence (component pathway) | Source | Caveats |
|---|---|---|---|---|---|---|
| **EPA + DHA (fish oil)** | 1–2 g combined EPA+DHA/d | CRP ↓ ~0.2–0.4 mg/L (if elevated baseline); estimated PhenoAge ↓ ~0.2–0.8 years | 8–12 weeks | **[Meta]** | Li 2014 *J Cardiovasc Pharmacol Ther*; AbuMweis 2018 *Clin Nutr* | Floor-limited in lean adults with CRP <0.5 mg/L. See `../omega_fatty_acids/EPA_DHA.md`. |
| **Vitamin D₃** (if 25(OH)D <30 ng/mL) | 1000–2000 IU/d | Modest CRP ↓ ~5–15% if deficient at baseline; some immune-modulation; estimated PhenoAge ↓ ~0.1–0.3 years if correcting deficiency | 8–12 weeks | **[Meta]** | Chen 2014 *J Clin Endocrinol Metab* (vit D → CRP); inconsistent | Replete-only effect; supplementation in already-replete adults shows no benefit. See `../vitamins_minerals/vitamin_D.md`. |
| **Curcumin** (with piperine for bioavailability) | 500–1000 mg/d | CRP ↓ ~0.4 mg/L (in elevated baseline); estimated PhenoAge ↓ ~0.2–0.6 years | 8–12 weeks | **[Meta]** | Sahebkar 2016 *Phytother Res* (curcumin → CRP meta) | Bioavailability poor without piperine / phytosome / nano formulations. Floor-limited. |
| **Soluble fiber** (psyllium, β-glucan) | 5–10 g/d | Glucose ↓ 2–5 mg/dL; LDL ↓; CRP ↓ modest; estimated PhenoAge ↓ ~0.2–0.5 years | 4–8 weeks | **[Meta]** | Whitehead 2014; Brown 1999 | |
| **Magnesium glycinate / citrate** (if dietary intake low) | 200–400 mg/d | Modest CRP ↓ if Mg-deficient; modest BP ↓; estimated PhenoAge ↓ ~0.1–0.3 years if correcting deficiency | 8–12 weeks | **[Meta]** | Simental-Mendia 2017 (Mg → CRP); inconsistent | Replete-only effect. |
| **Multivitamin / B-complex** (if dietary intake inadequate) | RDA-level | If deficient: corrects MCV / RDW abnormalities (folate / B12 deficiency macrocytosis); supports lymphocyte function; estimated PhenoAge ↓ ~0.5–2 years if correcting macrocytic anemia | Months | **[RCT]** | Standard hematology | High leverage IF baseline B12 / folate deficient. No benefit in already-replete adults. See `../vitamins_minerals/B12.md`, `../vitamins_minerals/folate.md`. |
| **Iron (in IDA only)** | 30–65 mg elemental Fe/d | Ferritin ↑; Hgb ↑; MCV ↑ if microcytic; RDW ↓ over time; estimated PhenoAge ↓ ~0.3–1 year if correcting microcytic anemia (RDW component) | 4–12 weeks | **[Meta]** | See `../iron/ferritin.md` | Do NOT supplement without measured deficiency. |

### Lowering / improving (mechanism-only; weak or insufficient evidence)

| Supplement | Marketing claim | Reality | Evidence | Source | Caveats |
|---|---|---|---|---|---|
| **NMN / NR (NAD+ precursors)** | "Reverses biological aging" | Multiple small RCTs raise blood NAD+ ~50–100%; **no PhenoAge or DunedinPACE reduction demonstrated in human RCTs**; one small NR trial in middle-aged adults showed no clock change. | **[Mechanism without clinical endpoint data]** | Martens 2018 *Nat Commun* (NR raises NAD+); Yoshino 2021 *Science* (NMN); Brakedal 2022 (NR Parkinson's) | Heavy marketing far exceeds evidence. |
| **Resveratrol** | "Sirtuin activator, anti-aging" | Modest metabolic effects in some trials; **no PhenoAge reduction demonstrated**; many trials negative. | **[Mechanism only]** | Berman 2017 *Mol Nutr Food Res* meta — modest effects | |
| **Spermidine (wheat germ, fermented soy)** | "Autophagy activator" | Small observational mortality signal (Eisenberg 2016); **no PhenoAge RCT**. | **[Cohort + Mechanism]** | Eisenberg 2016 *Nat Med* | |
| **Astaxanthin** | "Antioxidant anti-aging" | Modest CRP / LDL effects in some trials; no PhenoAge RCT. | **[Mechanism]** | | |
| **Quercetin / fisetin (senolytics)** | "Clears senescent cells" | Mostly animal data; one small human IPF trial (Justice 2019 *EBioMedicine*, n=14); no PhenoAge RCT. | **[Mechanism + 1-Trial in disease]** | Justice 2019; Kirkland & Tchkonia 2020 | Heavy marketing without human aging-clock evidence. |
| **Collagen peptides** | "Anti-aging" | Skin elasticity / joint pain modest effects; no PhenoAge component effects. | **[Off-target for PhenoAge]** | | Not a PhenoAge intervention. |
| **MitoQ / SkQ1 (mitochondrial-targeted antioxidants)** | "Mitochondrial anti-aging" | Some endothelial / VO₂max effects in small trials; no PhenoAge RCT. | **[Mechanism]** | Rossman 2018 *Hypertension* (MitoQ → endothelial function) | |
| **CoQ10 / ubiquinol** | "Mitochondrial anti-aging" | Modest effects in HF / statin myalgia; no PhenoAge effect. | **[Off-target for PhenoAge]** | | |
| **TA-65 (telomerase activator)** | "Lengthens telomeres" | Small observational + 1 RCT showing modest telomere length increase; **no PhenoAge / DunedinPACE / GrimAge effect demonstrated**; safety concerns (theoretical cancer risk). | **[1-Trial for telomeres; not for PhenoAge]** | Salvador 2016 *Rejuvenation Res* | Expensive ($200+/month). |
| "Anti-aging" multi-ingredient formulas (Tru Niagen, Elysium Basis, etc.) | "Comprehensive anti-aging" | None has PhenoAge / aging-clock RCT data. | **[no-evidence for PhenoAge]** | | Marketing-driven. |

### Pharmacotherapy (PRESCRIPTION ONLY)

| Drug | Dose | Direction & magnitude (estimated PhenoAge effect) | Indication | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **GLP-1 receptor agonists** (semaglutide 1–2.4 mg/wk; tirzepatide 5–15 mg/wk) | Per indication | In obese/T2DM: weight ↓ 10–20%; CRP ↓ 30–50%; HbA1c ↓ 1–2%; glucose ↓ 20–40 mg/dL; estimated PhenoAge ↓ ~2–5 years over 12 months | Obesity / T2DM | **[RCT — STEP, SURMOUNT, SELECT]** | Wilding 2021 *NEJM* STEP-1 (semaglutide 2.4 mg → -14.9% weight); Jastreboff 2022 *NEJM* SURMOUNT-1 (tirzepatide -22.5% weight); Kosiborod 2024 *NEJM* SELECT (CV outcomes) | Largest single pharmacotherapy effect on PhenoAge components in obese / T2DM. **Not indicated in lean healthy young adults.** Off-label use in lean adults: muscle loss, sarcopenia risk. |
| **Statins** (atorvastatin 10–80 mg, rosuvastatin 5–40 mg) | Per indication | LDL ↓ 30–55%; CRP ↓ 15–40% (Ridker 2008 JUPITER); estimated PhenoAge ↓ ~0.3–1 year (CRP component, primarily) | Per ASCVD risk / 10y risk ≥7.5% | **[RCT — JUPITER, etc.]** | Ridker 2008 *NEJM* JUPITER (rosuvastatin → CRP ↓ ~37%); see `../cardiovascular/LDL-C.md` | PhenoAge effect modest; primary indication is LDL / CV risk reduction. |
| **Metformin** (500–2000 mg/d) | Per indication | T2DM: HbA1c ↓ 1–2%; modest weight ↓; modest CRP ↓; epidemiologic mortality signal in T2DM cohorts | T2DM / pre-DM (some off-label use for "longevity") | **[RCT for T2DM; Cohort for non-diabetic mortality]** | UKPDS 34; Bannister 2014 *Diabetes Obes Metab* (T2DM on metformin → all-cause mortality slightly LOWER than non-diabetic controls); TAME trial pending | **TAME trial** (Targeting Aging with Metformin, Barzilai et al.): RCT in non-diabetic 65–80yo, primary composite endpoint of CV / cancer / cognitive — results pending as of 2026. **Off-label use in healthy non-diabetic young adults: no evidence; B12 depletion concern with chronic use.** |
| **Rapamycin** (sirolimus, off-label, low-dose intermittent) | Variable (0.5–2 mg/wk in PEARL) | PEARL trial 2024 (Kaeberlein, n=130 healthy adults 50–85, 48 weeks): DunedinPACE slowed ~3% in females (no significant effect in males); PhenoAge effects not established | "Anti-aging" (off-label, no FDA approval) | **[1-Trial — PEARL]** | Mannick et al. 2014 *Sci Transl Med* (everolimus → influenza vaccine response); Kaeberlein PEARL 2024 (preprint; *GeroScience* / *Aging Cell* publication pending) | **Risk profile uncertain in young adults.** Stomatitis, dyslipidemia, thrombocytopenia, infection risk. Long-term safety in healthy adults unknown. **Not currently recommended outside trials.** |
| **Acarbose** (50–100 mg with meals) | Per indication | Postprandial glucose ↓; modest fasting glucose ↓; T2DM mortality reduction in Asian cohorts | T2DM (esp. Asian; Chinese first-line option) | **[RCT]** | UKPDS, Chinese T2DM trials | Acarbose is included in the "geroprotectant" candidate list (ITP rodent studies showed lifespan extension); no PhenoAge RCT in humans. |
| **SGLT2 inhibitors** (dapagliflozin, empagliflozin) | Per indication | T2DM / HF / CKD: glucose ↓; weight ↓; CRP ↓; CV / kidney outcomes improved | T2DM / HFrEF / CKD | **[RCT — DAPA-CKD, EMPA-KIDNEY]** | Heerspink 2020 *NEJM* DAPA-CKD; EMPA-KIDNEY 2023 *NEJM* | Strong CV / renal outcome data. PhenoAge effect indirect via glucose / weight / CRP. |
| **Senolytics** (dasatinib + quercetin combination) | Investigational | Mostly animal data; one small human IPF trial (n=14, Justice 2019); **no PhenoAge RCT**. | Investigational | **[1-Trial in disease]** | Justice 2019 *EBioMedicine*; Hickson 2019 *EBioMedicine* (DKD pilot) | Marketed by some clinics; no evidence base for healthy adults. |
| **Aspirin (low-dose, 81 mg/d)** | Per indication | CRP ↓ ~10–20%; CV / colorectal cancer prevention in selected populations | Per individualized risk-benefit | **[Meta]** | ASPREE 2018 *NEJM* (no benefit for primary prevention in healthy elderly); Rothwell colorectal cancer data | PhenoAge effect modest; bleeding risk must be weighed. Not recommended for primary prevention in healthy young adults. |

---

## 4. Activities & Behaviors

| Activity | Dose / pattern | Direction & magnitude (estimated PhenoAge effect) | Time to effect | Evidence (component pathway) | Source | Caveats |
|---|---|---|---|---|---|---|
| **Smoking cessation** | Stop smoking | WBC ↓ 1–1.5 ×10⁹/L over 7–52 weeks; CRP ↓ 30–50% over 3–12 months; MCV ↓ slight; RDW ↓ slight; estimated PhenoAge ↓ **~1.5–3 years** total | 7 weeks – 12 months | **[Cohort]** | Lavi 2020 *Am J Med*; Saville 2005 *Mayo Clin Proc*; Levine formula coefficients | **Single largest multi-component lifestyle intervention.** WBC ↓ 1 ×10⁹/L alone ≈ PhenoAge ↓ ~1 year. CRP cessation effect adds ~0.5–1.5 years on top. Co-benefits: Cd ↓, Pb modest ↓, lung function preserved, CV mortality ↓. |
| **Aerobic exercise** (moderate–vigorous, 150–300 min/wk) | Weekly | Glucose ↓ 1–3 mg/dL (post-exercise insulin sensitivity); CRP ↓ ~20–30% in overweight (minimal in lean); modest WBC ↓ at rest; estimated PhenoAge ↓ ~0.3–1.5 years | 8–12 weeks | **[Meta]** | Boule 2001 *JAMA*; Hayashino 2012 *Arch Intern Med* (exercise → CRP); Fedewa 2017 *Br J Sports Med* | Floor effects in already-fit lean young adults. |
| **Resistance training** (2–3×/wk) | Weekly | CRP ↓ modest; muscle mass ↑ (creatinine ↑ — paradoxically increases PhenoAge in formula); modest glucose ↓; estimated net PhenoAge effect ~0–0.5 years (creatinine paradox cancels some inflammation benefit) | 8–12 weeks | **[Meta]** | Westcott 2012 *Curr Sports Med Rep* | **Creatinine paradox**: muscular individuals have higher creatinine, which the formula reads as "older." This is a known limitation of PhenoAge — penalizes muscularity. Real biological aging benefit of resistance training is not captured. |
| **HIIT / sprint interval training** | 2–3×/wk | Glucose ↓; insulin sensitivity ↑; CRP modest ↓; VO₂max ↑; estimated PhenoAge ↓ ~0.3–1 year (overlapping with aerobic) | 8–12 weeks | **[Meta]** | Wewege 2017 *Obes Rev* | |
| **Adequate sleep** (7–9 hr/night, regular timing) | Nightly | Glucose ↓ 3–5 mg/dL (vs sleep-deprived state); CRP ↓ ~10–20%; WBC ↓ modest; lymphocyte % normalization; estimated PhenoAge ↓ ~0.5–1.5 years (vs chronic 5h/night state) | Days–weeks | **[RCT]** | Spiegel 2004 *Ann Intern Med* (sleep restriction → glucose ↑); Leproult 2014 *Sleep*; Irwin 2016 *Biol Psychiatry* meta (sleep loss → CRP / IL-6) | **Underappreciated lever.** A young man sleeping 5h/night has measurably worse glucose, CRP, and WBC than the same man sleeping 8h. |
| **Sleep regularity / consistent bedtime** | Nightly | Independent of duration: irregular sleep → CRP ↑, glucose ↑, all-cause mortality ↑ | Weeks | **[Cohort]** | Lunsford-Avery 2018 *Sci Rep*; Huang 2020 *JAMA Netw Open* (Multi-Ethnic Study of Atherosclerosis — sleep regularity → mortality) | Wearable-trackable (Sleep Regularity Index, Oura / Garmin / Apple Health). |
| **Stress reduction / meditation / breathwork** | Daily 10–30 min | CRP ↓ ~10–20% in some MBSR / meditation trials; cortisol pattern improvement; modest WBC ↓; estimated PhenoAge ↓ ~0.2–0.8 years | 8–12 weeks | **[Meta]** | Pascoe 2017 *J Psychiatr Res* (mindfulness → CRP); Black 2016 *Ann N Y Acad Sci* | Floor effects in low-stress baselines. |
| **Caloric restriction (CR, 25%)** | Sustained 1–2 years | CALERIE trial (non-obese adults): DunedinPACE slowed ~2–3%; **PhenoAge / GrimAge effects NOT significant** | 1–2 years | **[RCT — CALERIE]** | Belsky 2023 *Nat Aging* CALERIE PMC10148951; Belsky 2018 *J Gerontol A Biol Sci Med Sci* PMC5861848 | Crucial: 25% CR for 2 years did NOT change PhenoAge significantly. DunedinPACE (a methylation pace-of-aging clock) slowed modestly. PhenoAge is less responsive to CR than methylation clocks. **Not recommended for lean young adults** (muscle loss, hormonal effects). |
| **Time-restricted eating (TRE) / intermittent fasting** | 16:8 or 14:10 | Modest weight ↓ in overweight; modest glucose / CRP improvements in metabolically unhealthy; **no PhenoAge RCT** in healthy young adults; effects in lean adults likely floor-limited or counterproductive | Months | **[1-Trial + small RCTs]** | Lowe 2020 *JAMA Intern Med* TREAT (16:8 in overweight — no significant weight loss vs control) | Trial evidence weaker than marketing suggests. |
| **Sauna** (Finnish dry, 4–7×/wk × 15–30 min) | Weekly | CV mortality ↓ 40% at 4–7×/wk vs 1×/wk (Laukkanen 2015); modest CRP ↓; modest BP ↓; estimated PhenoAge ↓ ~0.2–0.6 years | Months | **[Cohort]** | Laukkanen 2015 *JAMA Intern Med*; Laukkanen 2018 *Mayo Clin Proc* | Strong observational mortality signal; mechanism plausibly via cardiovascular conditioning. |
| **Sun exposure (moderate, for vitamin D)** | 15–30 min daily (mid-day, exposed limbs) | Maintains 25(OH)D >30 ng/mL; modest CRP ↓ if correcting deficiency; estimated PhenoAge ↓ ~0.1–0.3 years if correcting deficiency | 8–12 weeks | **[Cohort]** | Vitamin D / CRP literature | Skin cancer risk balance. |
| **Cold exposure (cold showers, ice baths)** | Daily-weekly | Mostly anecdotal claims; no PhenoAge RCT; modest CRP / inflammation modulation in some small trials | — | **[1-Trial; mostly Mechanism]** | Søberg 2021 *Cell Rep Med* (Wim Hof-style); limited evidence | Marketed but not robustly validated for PhenoAge. |
| **Heavy alcohol consumption** (>14 drinks/wk men) | Heavy chronic | CRP ↑; MCV ↑ (macrocytosis); GGT ↑; ALP modest ↑; albumin ↓ in severe; estimated PhenoAge ↑ ~0.5–2 years (heavy drinkers) | Months–years | **[Meta]** | See "Foods that raise" §2 | Alcohol moderation: PhenoAge ↓ ~0.3–1 year going from heavy to light. |
| **Avoiding chronic infection / treating periodontitis / treating H. pylori** | One-time intervention | Periodontitis is a documented chronic CRP source; treatment ↓ CRP ~0.5–1 mg/L; estimated PhenoAge ↓ ~0.3–1 year if elevated baseline | 3–12 months post-treatment | **[RCT — D'Aiuto]** | D'Aiuto 2018 *Lancet Diabetes Endocrinol* (periodontitis treatment → CRP ↓ in T2DM); Higashi 2008 *Hypertension* (periodontitis treatment → endothelial function ↑) | Underappreciated source of chronic CRP elevation. Dental hygiene / periodontal evaluation is high-leverage. |
| **Treating obstructive sleep apnea (CPAP)** | Nightly CPAP | CRP ↓ ~30%; HbA1c ↓; BP ↓; estimated PhenoAge ↓ ~0.5–2 years if untreated OSA was driving CRP | 3–12 months | **[Meta]** | Baessler 2013 *Sleep Med Rev* (CPAP → CRP); Iftikhar 2014 *Hypertension* | High-leverage if undiagnosed OSA. Many lean young men with PhenoAge acceleration have undiagnosed OSA (esp. SA males with retrognathic mandible — see §7). |

---

## 5. Wearable-Trackable Metric Relationships

PhenoAge components have well-established relationships with wearable metrics — perhaps the strongest of any biomarker covered.

| Wearable metric | Direction of relationship | Magnitude / effect size | Evidence | Source | Caveats |
|---|---|---|---|---|---|
| **VO₂max (estimated by Garmin / Apple / Polar / lab CPET)** | Inverse: higher VO₂max ↔ lower PhenoAge | Each 1 MET (3.5 mL/kg/min) ↑ in CRF associated with ~10–15% lower all-cause mortality (Mandsager 2018 *JAMA*); cross-sectional PhenoAge correlation modest | **[Cohort]** | Mandsager 2018 *JAMA Netw Open*; Kokkinos 2010 *Circulation* | Best wearable-derived "biological fitness" metric. PhenoAge does not include VO₂max but the underlying aging biology aligns. |
| **Resting heart rate (RHR)** | Inverse: lower RHR ↔ lower PhenoAge | Each 10 bpm higher RHR associated with ~10% higher all-cause mortality; PhenoAge correlation via WBC + CRP component | **[Cohort]** | Cooney 2010 *Am Heart J*; Aune 2017 *Nutr Metab Cardiovasc Dis* | Indirect via inflammation / autonomic balance. |
| **HRV (RMSSD / SDNN, Oura / Whoop / Garmin / Polar H10)** | Direct: higher HRV ↔ lower PhenoAge | Higher HRV → lower CRP / WBC → modest PhenoAge ↓; cross-sectional only | **[Cohort]** | Sajadieh 2004 *Eur Heart J* (HRV → CRP) | Indirect; affected by sleep, stress, training load. |
| **Sleep duration (Oura / Whoop / Apple Health / Garmin / Fitbit)** | Inverse U: 7–9 h optimal | Sleep <6 h/night → CRP ↑, glucose ↑, WBC ↑; PhenoAge ↑ ~0.5–1.5 years vs 7–9 h sleeper | **[RCT + Cohort]** | Spiegel 2004; Leproult 2014; Irwin 2016 meta | High-leverage actionable metric. |
| **Sleep regularity (consistent bedtime/wake time, Sleep Regularity Index — Garmin / Apple Health Sleep Schedule)** | Direct: higher regularity ↔ lower PhenoAge | Independent of duration: irregular sleep → CRP ↑, mortality ↑ | **[Cohort]** | Lunsford-Avery 2018 *Sci Rep*; Huang 2020 *JAMA Netw Open* | |
| **Step count (daily, Apple Health / Garmin / Fitbit / Whoop)** | Inverse: higher steps ↔ lower PhenoAge | 7,000–10,000 steps/d associated with mortality ↓ ~50% vs <4,000 (Saint-Maurice 2020 *JAMA*); CRP / glucose effects | **[Cohort]** | Saint-Maurice 2020 *JAMA*; Paluch 2022 *Lancet Public Health* | High-leverage actionable. |
| **Exercise minutes per week (Apple Watch / Garmin "vigorous activity")** | Inverse: higher MVPA ↔ lower PhenoAge | 150–300 min/wk MVPA → CRP ↓, glucose ↓, mortality ↓ | **[Meta]** | Ekelund 2016 *Lancet*; Stamatakis 2022 *JAMA Intern Med* | |
| **Training load / TSS (Whoop / TrainingPeaks / Garmin Training Status)** | Inverse U: moderate optimal; chronic high → CRP ↑ if overtrained | Moderate progressive load → CRP ↓, fitness ↑; chronic overtraining → CRP ↑, lymphocyte ↓, immune dysfunction | **[Cohort]** | Mackinnon 2000 *Med Sci Sports Exerc*; HRV-decay-as-overtraining literature | Personalized; track HRV trend alongside. |
| **Glucose (continuous glucose monitor — Dexcom / Libre)** | Inverse: lower mean glucose ↔ lower PhenoAge | CGM-detected post-prandial glucose excursions in non-diabetics correlate with CV / mortality risk; PhenoAge component glucose direct | **[Cohort + Mechanism]** | DEVOTE / Dexcom population data | Direct measure of one PhenoAge component. |
| **Body composition (DEXA / InBody / smart scale fat %)** | Inverse: higher lean mass ↔ better metabolic health | Higher fat mass → CRP ↑, glucose ↑; muscle mass via creatinine (paradox in PhenoAge formula) | **[Cohort]** | Multiple body comp studies | See "creatinine paradox" caveat above. |
| **Stress score / readiness (Whoop / Oura / Garmin Stress)** | Inverse: lower stress ↔ better immune / inflammatory profile | Indirect via sleep / cortisol / HRV | **[Cohort]** | Stress-CRP literature | |
| **Smoking app log** | Direct: smoking ↔ PhenoAge ↑ | Smokers: PhenoAge ~1.5–3 years higher than non-smokers via CRP / WBC | **[Cohort]** | NHANES smoker analyses; Lavi 2020 | Largest single behavioral input. |

The actionable wearable layer for PhenoAge is **multi-modal**: VO₂max + sleep duration / regularity + step count + exercise minutes + glucose (CGM) + smoking status + body composition. No single wearable metric drives PhenoAge alone.

---

## 6. Synthesis & Highest-Leverage Stack

- **Highest-leverage single intervention:** **Smoking cessation** (PhenoAge ↓ ~1.5–3 years via WBC + CRP). For non-smokers: **address whichever component is most abnormal** (CRP, glucose, WBC, RDW, MCV). There is no universal "best lever" — it is component-specific.
- **Best stack of 3** (for a non-smoker with mildly elevated PhenoAge from CRP / glucose):
  1. **Mediterranean / DASH diet adoption** (CRP ↓ 20–40%, glucose ↓ 3–5 mg/dL, weight ↓ if applicable)
  2. **Adequate sleep (7–9 h, regular timing)** (glucose ↓ 3–5 mg/dL, CRP ↓ 10–20%, WBC normalization)
  3. **150–300 min/wk MVPA + 2–3 resistance sessions** (CRP ↓, glucose ↓, body composition ↑, VO₂max ↑)
  - Combined estimated PhenoAge ↓ ~1.5–3 years over 6 months in someone with elevated baseline.

- **Realistic 12-week delta for a healthy 20yM at near-optimal baseline (PhenoAge ≈ chronological age, all 9 components in healthy range):** Essentially no actionable change. **PhenoAge has a noise floor of ±2–3 years from CRP / WBC / glucose / ALP day-to-day variability** in young adults. Single-day variability in CRP (vaccine, cold, intense workout 24h prior, poor sleep, fasting status) can swing it 2–10×; in WBC ±15–25% diurnal; in glucose by fasting status. **Repeat and trend.**

- **Realistic 12-week delta for someone with elevated baseline (e.g., PhenoAge 28 at chronological 20, driven by CRP 3 mg/L + glucose 100 mg/dL + WBC 8 ×10⁹/L):** Identify the offending component(s):
  - If CRP elevated from periodontitis / undiagnosed sleep apnea / chronic infection / obesity: address root cause → CRP 3 → 0.5 mg/L → PhenoAge ↓ ~1.5 years.
  - If glucose elevated from sleep deprivation / sedentary / refined-carb diet: sleep + exercise + Mediterranean → glucose 100 → 88 mg/dL → PhenoAge ↓ ~2 years.
  - If WBC elevated from smoking: cessation → WBC ↓ 1.5 ×10⁹/L → PhenoAge ↓ ~1 year.
  - **3-month outlook**: PhenoAge ↓ ~1–2 years (one driver fixed).
  - **6-month outlook**: PhenoAge ↓ ~2–3 years (two drivers improved).
  - **12-month outlook**: PhenoAge ↓ ~2–5 years (sustained lifestyle, all modifiable factors optimized).

- **Where pharmacotherapy becomes necessary:**
  - **GLP-1 agonists** (semaglutide / tirzepatide): for **obesity (BMI ≥30) or T2DM**. Largest single pharmacologic intervention on PhenoAge (~2–5 years over 12 months in obese T2DM). NOT indicated for lean healthy young adults — sarcopenia / muscle loss risk.
  - **Statins**: per individualized 10-year ASCVD risk; modest CRP / PhenoAge benefit beyond LDL reduction.
  - **Metformin**: per T2DM indication. **TAME trial pending** for "geroprotection" in non-diabetic 65–80yo. Off-label in healthy young adults: no evidence; B12 depletion concern.
  - **Rapamycin**: PEARL 2024 (modest DunedinPACE effect in 50–85yo females). **Risk profile in healthy young adults unknown; not recommended outside trials.**
  - **CPAP for OSA**: high leverage if undiagnosed OSA is driving CRP / glucose.
  - **Periodontitis treatment**: high leverage if elevated CRP traceable to dental disease.

---

## 7. South Asian / lean-male-specific notes

- **Higher baseline CRP / metabolic risk** at lower BMI: SA males develop insulin resistance and elevated CRP at BMI thresholds 5+ kg/m² lower than European-ancestry males (Razak 2007 *Lancet*; Misra 2009). A lean SA male with BMI 24 may have visceral adiposity / fatty liver / IR profile of a European male at BMI 28–30. This translates to elevated PhenoAge driven by CRP / glucose at apparently "normal" weight.
- **Higher baseline RDW / iron deficiency anemia in SA vegetarian men** with low ferritin → RDW elevated → PhenoAge artifactually elevated. Address ferritin first.
- **Vitamin D deficiency** common in SA populations (~80% prevalence in some studies; less UVB skin synthesis at higher melanin + lower UV-exposure lifestyle). Modest CRP component.
- **Vitamin B12 / folate deficiency** in vegetarian SA males → MCV ↑ (macrocytic anemia) → PhenoAge artifactually elevated. B12 supplementation high-yield.
- **Higher OSA risk** in SA males with retrognathic mandible / smaller upper airway anatomy at lower BMI than European-ancestry; should consider OSA screening (STOP-BANG, home sleep test) earlier in PhenoAge workup.
- **Higher insulin resistance / NAFLD prevalence at lean BMI** → glucose component elevated.
- **Periodontitis prevalence** in SA populations elevated; high-yield CRP source to address.
- **Cultural diet leverage**: traditional SA diet has high-leverage components (legumes, leafy greens, spices like turmeric, fermented dairy) but is also heavy on white rice / refined grain; targeted shift to brown / mixed grains + white basmati + portion control can shift glucose / CRP without abandoning cuisine. (See `arsenic.md` for the rice / iAs trade-off.)

---

## 8. Interactions & Confounders for Recommendation Engine

**The 9-component decomposition is essential — never recommend "lower PhenoAge" abstractly.**

**Genetic modifiers:**
- **CRP**: *CRP* gene variants (rs1205, rs1130864) modify baseline CRP ~20–30%; modest PhenoAge effect; not actionable.
- **Lipid / metabolic SNPs** affect glucose / CRP / weight (FTO, MC4R, TCF7L2, GCKR — see `../metabolic/` files).
- **B12 / folate metabolism** (MTHFR C677T): TT genotype + low folate intake → elevated homocysteine + MCV → PhenoAge ↑.
- **Hemochromatosis (HFE C282Y / H63D)**: elevated iron / ferritin → higher PhenoAge component creatinine + ALP modest changes.
- **APOE ε4**: not in PhenoAge directly, but ε4 carriers have higher inflammatory burden; modest indirect effect.
- **Telomere length SNPs** (TERT, TERC): not in PhenoAge; relevant for methylation clocks but not Levine PhenoAge.

**Drug interactions:**
- **Statins**: CRP ↓ 15–40% (Ridker 2008 JUPITER); ALT can rise modestly (not in PhenoAge but clinical context); affects creatine kinase (also not in PhenoAge).
- **Metformin**: HbA1c / glucose ↓; B12 ↓ over years (chronic use → falsely elevated MCV).
- **PPIs** (chronic): B12 ↓ → MCV ↑ → PhenoAge ↑.
- **GLP-1 agonists**: glucose ↓, weight ↓, CRP ↓; potential muscle loss in lean adults (creatinine paradox).
- **SGLT2 inhibitors**: glucose ↓, weight ↓, modest hematocrit ↑.
- **Corticosteroids** (chronic): glucose ↑, WBC ↑ (demargination), lymphocyte % ↓; PhenoAge ↑ artifactually during use.
- **Chemotherapy / immunosuppressants**: WBC / lymphocyte component severely affected.
- **Biotin** at high dose: interferes with some immunoassays (not directly PhenoAge components but watch for assay artifacts).

**Confounding lifestyle factors:**
- **Acute illness / infection in prior 2 weeks**: CRP / WBC spike → PhenoAge inflated. **Defer testing 2–4 weeks post-illness.**
- **Recent vaccine** (within 3–7 days): CRP transient ↑; PhenoAge inflated. Defer testing 1–2 weeks.
- **Intense exercise within 24–48 h of draw**: CRP ↑ transiently; lymphocyte / neutrophil shifts; muscle damage → modest creatinine ↑.
- **Fasting status**: glucose obviously affected; albumin slightly ↓ in prolonged fast.
- **Time of day**: WBC / lymphocyte / cortisol have diurnal rhythms.
- **Hydration / dehydration**: hemoconcentration affects albumin, RBC indices.
- **Sleep prior night**: glucose / CRP / WBC affected.
- **Recent vaccine (Cd / Pb spike from supplement, contaminated food)**: not PhenoAge directly but watch confounded panels.
- **Pregnancy / lactation** (partners): albumin ↓, ALP ↑ (placenta), WBC ↑ — PhenoAge interpretation unreliable in pregnancy.
- **Menstrual cycle** (partners): CRP / WBC / lymphocyte minor cyclic variation.

**Component-level interpretation pitfalls (the "creatinine paradox" and friends):**
- **Creatinine and muscle mass**: muscular individuals → creatinine ↑ → PhenoAge ↑ (formula reads as "older"); biologically backwards. Lean athletic 20yM with creatinine 1.2 mg/dL gets a PhenoAge bump unrelated to kidney function. **Cystatin C eGFR** is muscle-mass-independent — request if creatinine seems out of context.
- **ALP in young adults**: young males in active bone growth (up through ~25y) can have ALP 90–130 U/L physiologically → PhenoAge ↑ artifactually. **Often resolves on its own** as bone growth completes.
- **MCV from B12 / folate / alcohol**: macrocytosis (MCV >100 fL) → PhenoAge ↑ — verify B12 / folate adequacy and alcohol intake.
- **Lymphocyte % during stress / cortisol**: chronic stress → lymphocyte % ↓ → PhenoAge ↑. May resolve with stress / sleep intervention.
- **CRP — log-transformed**: a CRP drop from 0.5 → 0.3 mg/L is small in PhenoAge terms (<0.3 yr); a drop from 5 → 1 mg/L is large (>1 yr). The actionable range is mostly above CRP 1 mg/L.

**Standardization for accurate trending:**
- Same lab, same time of day, fasting morning draw.
- No acute illness in prior 2–4 weeks; no vaccine in prior 1–2 weeks.
- No intense workout in prior 48 h.
- Stable hydration; no extreme dietary deviation in prior 3 days.
- For component decomposition: pull individual marker values, not just composite PhenoAge.

---

## 9. Open Questions / Weak Evidence

- **"Is PhenoAge worth tracking in a healthy 20yM?"** Marginal value as a single number; **high value as a structured prompt to look at the 9 components.** A negative delta (PhenoAge < chronological) at age 20 is largely artifactual (algorithm trained on older adults; young adults have markers younger than population average by definition). A positive delta is the actionable signal.
- **PhenoAge vs methylation clocks (GrimAge, DunedinPACE)**: Levine PhenoAge has lower test-retest reliability than methylation clocks (~0.5–0.7 vs GrimAge 0.93, DunedinPACE 0.73). Methylation clocks are not what Function Health gives you. Methylation testing (TruDiagnostic, Elysium Index, MyDNAge) is separately available; magnitude of intervention effects on these is also small in young adults.
- **CALERIE trial finding**: 25% caloric restriction for 2 years did NOT change PhenoAge significantly (Belsky 2023 *Nat Aging*). DunedinPACE slowed ~2–3%. PhenoAge is less responsive to CR than methylation clocks. **Marketed "anti-aging" lifestyle interventions often don't move PhenoAge measurably.**
- **PEARL rapamycin trial**: DunedinPACE slowed ~3% in females, no significant effect in males; PhenoAge effects not established. Risk profile in healthy young adults unknown.
- **TAME metformin trial**: pending as of 2026; no PhenoAge results published. Theoretical basis from epidemiologic data in T2DM cohorts; no data in non-diabetic young adults.
- **NMN / NR / resveratrol / spermidine**: raise blood NAD+ / mimic mechanisms; **no PhenoAge reduction demonstrated in human RCTs**.
- **Senolytics (D+Q, fisetin)**: animal data; one small human IPF trial (n=14); no PhenoAge RCT.
- **Telomerase activators (TA-65)**: no PhenoAge effect; marketing-driven.
- **Sauna mortality signal**: Laukkanen 2015 *JAMA Intern Med* observational; no PhenoAge RCT.
- **Stress reduction / meditation effect on CRP**: meta-analyses show modest effect; magnitude in lean low-stress baselines is uncertain.
- **Periodontitis treatment effect on PhenoAge**: D'Aiuto 2018 in T2DM showed CRP ↓ with treatment; no PhenoAge-specific RCT. Underappreciated lever in PhenoAge workup.
- **OSA / CPAP effect on PhenoAge**: well-documented CRP / glucose / BP improvements; no PhenoAge-specific RCT.
- **GLP-1 agonist effect on PhenoAge in obesity**: large CRP / glucose / weight effects predict ~2–5 year PhenoAge ↓; one published analysis confirms in T2DM cohort. Off-label use in lean adults: no evidence + sarcopenia concern.
- **The "creatinine paradox"**: PhenoAge penalizes muscular individuals with high creatinine. Cystatin C-based formulas (the original Levine paper used creatinine; some implementations use cystatin C) handle this better but are not what Function Health uses.
- **Population-mean reference**: PhenoAge translates 9 marker values to "the chronological age at which this combination of markers gives equal mortality risk" using population-mean coefficients. Individual genetic / metabolic context is not adjusted.
- **Calibration in young adults**: Lustgarten reanalysis (2019, Lustgarten blog) found youngest age decile shows mean PhenoAge acceleration of −5.8 years purely as calibration artifact. Negative delta in young adults is not meaningfully predictive of individual mortality benefit.

---

## Source format conventions

- Cited primary literature (PubMed PMID where available); CALERIE / PEARL / TAME / SURMOUNT / SELECT / JUPITER / STEP / DAPA-CKD / EMPA-KIDNEY trial publications; NHANES analyses.
- Did NOT cite: Function Health, supplement marketing, "anti-aging clinic" promotional materials, naturopathic / functional medicine "biological age optimization" blogs.
- Where a marketed intervention has no controlled human evidence on PhenoAge specifically, flagged as **[no-evidence for PhenoAge]** or **[Mechanism only]** with the relevant absent literature noted.

### Key references — PhenoAge algorithm and validation

- Levine ME, Lu AT, Quach A, et al. An epigenetic biomarker of aging for lifespan and healthspan. *Aging (Albany NY)* 2018;10(4):573–591. PMC5940111.
- Liu Z, Kuo PL, Horvath S, Crimmins E, Ferrucci L, Levine M. A new aging measure captures morbidity and mortality risk across diverse subpopulations from NHANES IV: A cohort study. *PLOS Medicine* 2018.
- Belsky DW, Caspi A, Houts R, et al. DunedinPACE, a DNA methylation biomarker of the pace of aging. *eLife* 2022. PMC8853656.
- Belsky DW, Caspi A, Corcoran DL, et al. (CALERIE PhenoAge / DunedinPACE). Effect of long-term caloric restriction on DNA methylation measures of biological aging in healthy adults from the CALERIE trial. *Nat Aging* 2023. PMC10148951.
- Belsky DW, Huffman KM, Pieper CF, et al. Change in the rate of biological aging in response to caloric restriction: CALERIE Biobank Analysis. *J Gerontol A Biol Sci Med Sci* 2018;73(1):4–10. PMC5861848.
- Lustgarten M. Quantifying Biological Age — independent reanalysis of PhenoAge calibration. (Lustgarten blog, 2019.)

### Key references — component intervention RCTs

- Ridker PM, Danielson E, Fonseca FA, et al. (JUPITER). Rosuvastatin to prevent vascular events in men and women with elevated C-reactive protein. *NEJM* 2008;359:2195–2207.
- Wilding JP, Batterham RL, Calanna S, et al. (STEP-1). Once-weekly semaglutide in adults with overweight or obesity. *NEJM* 2021;384(11):989–1002.
- Jastreboff AM, Aronne LJ, Ahmad NN, et al. (SURMOUNT-1). Tirzepatide once weekly for the treatment of obesity. *NEJM* 2022;387:205–216.
- Kosiborod MN, Petrie MC, Borlaug BA, et al. (SELECT subgroup). Semaglutide in patients with obesity-related heart failure and type 2 diabetes. *N Engl J Med* 2024.
- Estruch R, Ros E, Salas-Salvadó J, et al. (PREDIMED). Primary prevention of cardiovascular disease with a Mediterranean diet supplemented with extra-virgin olive oil or nuts. *NEJM* 2018;378:e34.
- Sacks FM, Svetkey LP, Vollmer WM, et al. (DASH-Sodium). Effects on blood pressure of reduced dietary sodium and the Dietary Approaches to Stop Hypertension (DASH) diet. *NEJM* 2001;344:3–10.
- Mannick JB, Del Giudice G, Lattanzi M, et al. mTOR inhibition improves immune function in the elderly. *Sci Transl Med* 2014;6:268ra179.
- Kaeberlein M et al. PEARL trial — rapamycin and biological aging in healthy 50–85yo (preprint 2024 / publication pending).
- Bannister CA, Holden SE, Jenkins-Jones S, et al. Can people with type 2 diabetes live longer than those without? A comparison of mortality in people initiated with metformin or sulphonylurea monotherapy and matched, non-diabetic controls. *Diabetes Obes Metab* 2014;16(11):1165–1173.
- Justice JN, Nambiar AM, Tchkonia T, et al. Senolytics in idiopathic pulmonary fibrosis: results from a first-in-human, open-label, pilot study. *EBioMedicine* 2019;40:554–563.

### Key references — component effects / mechanisms

- Spiegel K, Tasali E, Penev P, Van Cauter E. Brief communication: sleep curtailment in healthy young men is associated with decreased leptin levels, elevated ghrelin levels, and increased hunger and appetite. *Ann Intern Med* 2004;141:846–850.
- Leproult R, Holmbäck U, Van Cauter E. Circadian misalignment augments markers of insulin resistance and inflammation, independently of sleep loss. *Diabetes* 2014;63(6):1860–1869.
- Irwin MR, Olmstead R, Carroll JE. Sleep disturbance, sleep duration, and inflammation: a systematic review and meta-analysis of cohort studies and experimental sleep deprivation. *Biol Psychiatry* 2016;80(1):40–52.
- Lavi S, Bell SE, et al. Leukocytosis and tobacco use — reversible effect on white blood cell count. *Am J Med* 2020.
- Saville CR, et al. Effects of biochemically confirmed smoking cessation on white blood cell count. *Mayo Clin Proc* 2005. PubMed 16092581.
- Hayashino Y, Jackson JL, Hirata T, et al. Effects of exercise on C-reactive protein, inflammatory cytokine and adipokine in patients with type 2 diabetes. *Arch Intern Med* 2012;172:732–741.
- Schwingshackl L, Hoffmann G. Mediterranean dietary pattern, inflammation and endothelial function: a systematic review and meta-analysis of intervention trials. *Nutrients* 2014;6(11):4942–4992.
- Pascoe MC, Thompson DR, Jenkins ZM, Ski CF. Mindfulness mediates the physiological markers of stress: systematic review and meta-analysis. *J Psychiatr Res* 2017;95:156–178.
- Laukkanen T, Khan H, Zaccardi F, Laukkanen JA. Association between sauna bathing and fatal cardiovascular and all-cause mortality events. *JAMA Intern Med* 2015;175(4):542–548.
- D'Aiuto F, Gkranias N, Bhowruth D, et al. Systemic effects of periodontitis treatment in patients with type 2 diabetes (TASTE): a 12-month, single-centre, investigator-masked, randomised trial. *Lancet Diabetes Endocrinol* 2018;6(12):954–965.
- Baessler A, Nadeem R, Harvey M, et al. Treatment for sleep apnea by continuous positive airway pressure improves levels of inflammatory markers - a meta-analysis. *Sleep Med Rev* 2013;17(3):199–208.
- Mandsager K, Harb S, Cremer P, et al. Association of cardiorespiratory fitness with long-term mortality among adults undergoing exercise treadmill testing. *JAMA Netw Open* 2018;1(6):e183605.
- Saint-Maurice PF, Troiano RP, Bassett DR, et al. Association of daily step count and step intensity with mortality among US adults. *JAMA* 2020;323(12):1151–1160.
- Hall KD, Ayuketah A, Brychta R, et al. Ultra-processed diets cause excess calorie intake and weight gain: an inpatient randomized controlled trial of ad libitum food intake. *Cell Metab* 2019;30(1):67–77.

### Key references — South Asian-specific

- Razak F, Anand SS, Shannon H, et al. Defining obesity cut points in a multiethnic population. *Lancet* 2007;370:1929–1938.
- Misra A, Khurana L. Obesity-related non-communicable diseases: South Asians vs White Caucasians. *Int J Obes (Lond)* 2011;35(2):167–187.

### Key references — confounding & calibration

- Lu AT, Quach A, Wilson JG, et al. DNA methylation GrimAge strongly predicts lifespan and healthspan. *Aging (Albany NY)* 2019;11(2):303–327.
- Belsky DW. Quantification of biological aging in young adults. *Proc Natl Acad Sci USA* 2015;112(30):E4104–E4110.

---
