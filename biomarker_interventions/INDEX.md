# Biomarker Interventions — Master Index

Navigation + cross-cutting synthesis for the per-marker intervention research files.

**Corpus stats:** 113 per-biomarker files across 15 panels · ~419,000 words total · all effect sizes carry an evidence tag and primary-literature citation.

**Read first:** [`README.md`](README.md) (folder purpose, format conventions) · [`_TEMPLATE.md`](_TEMPLATE.md) (per-file template every agent followed).

**Sister reference:** [`../effect_sizes_INDEX.md`](../effect_sizes_INDEX.md) — cross-panel quick-look effect-size summary; this folder is the deep per-biomarker version.

---

## How the dashboard's recommendation engine should consume this folder

For a flagged or sub-optimal marker:

1. **Look up the marker file** via the table below.
2. **Pull the food/supplement/activity rows** from §1–4 with the highest evidence tag (`[Meta]` > `[RCT]` > `[Cohort]` > `[Mechanism]`) and largest magnitude.
3. **Filter by the user's known constraints** (vegetarian, lean baseline, drug interactions per §8, genetic data per §8) — drop incompatible recommendations.
4. **Stack the top 3** per §6 of the marker file. Apply the diminishing-returns multiplier (combined effect typically ~60–80% of linear sum, more for elevated baselines, less for already-near-optimum). 
5. **Project the next-draw delta** as a hypothesis, not a guarantee. Mark it with the evidence tag of the source rows so the user can see what's well-established vs mechanistic vs weak.
6. **Surface §8 confounders** with the recommendation so a user with creatine supplementation isn't told their creatinine elevation is kidney disease, etc.
7. **Surface §9 open questions** so the engine doesn't over-promise on weak-evidence interventions.

---

## Full biomarker → file map

### Cardiovascular ([cardiovascular/](cardiovascular/))
| Marker | File |
|---|---|
| Apolipoprotein B | [`ApoB.md`](cardiovascular/ApoB.md) |
| LDL Cholesterol | [`LDL-C.md`](cardiovascular/LDL-C.md) |
| HDL Cholesterol | [`HDL-C.md`](cardiovascular/HDL-C.md) |
| Triglycerides | [`Triglycerides.md`](cardiovascular/Triglycerides.md) |
| Total Cholesterol | [`Total_Cholesterol.md`](cardiovascular/Total_Cholesterol.md) |
| Non-HDL Cholesterol | [`non-HDL-C.md`](cardiovascular/non-HDL-C.md) |
| Total Cholesterol / HDL Ratio | [`TC_HDL_ratio.md`](cardiovascular/TC_HDL_ratio.md) |
| hs-CRP | [`hs-CRP.md`](cardiovascular/hs-CRP.md) |

### Advanced Lipids ([advanced_lipids/](advanced_lipids/))
| Marker | File |
|---|---|
| Lipoprotein(a) | [`Lp(a).md`](advanced_lipids/Lp\(a\).md) |
| LDL Particle Number | [`LDL_particle_number.md`](advanced_lipids/LDL_particle_number.md) |
| LDL Small | [`LDL_small.md`](advanced_lipids/LDL_small.md) |
| LDL Medium | [`LDL_medium.md`](advanced_lipids/LDL_medium.md) |
| LDL Peak Size | [`LDL_peak_size.md`](advanced_lipids/LDL_peak_size.md) |
| LDL Pattern (A/B) | [`LDL_pattern.md`](advanced_lipids/LDL_pattern.md) |
| HDL Large | [`HDL_large.md`](advanced_lipids/HDL_large.md) |
| ApoB / ApoA1 ratio | [`ApoB_ApoA1_ratio.md`](advanced_lipids/ApoB_ApoA1_ratio.md) |

### Metabolic ([metabolic/](metabolic/))
| Marker | File |
|---|---|
| Fasting Glucose | [`fasting_glucose.md`](metabolic/fasting_glucose.md) |
| HbA1c | [`HbA1c.md`](metabolic/HbA1c.md) |
| Fasting Insulin | [`fasting_insulin.md`](metabolic/fasting_insulin.md) |
| HOMA-IR | [`HOMA-IR.md`](metabolic/HOMA-IR.md) |
| Uric Acid | [`uric_acid.md`](metabolic/uric_acid.md) |
| Leptin | [`leptin.md`](metabolic/leptin.md) |

### Liver ([liver/](liver/))
| Marker | File |
|---|---|
| ALT | [`ALT.md`](liver/ALT.md) |
| AST | [`AST.md`](liver/AST.md) |
| ALP | [`ALP.md`](liver/ALP.md) |
| GGT | [`GGT.md`](liver/GGT.md) |
| Total Bilirubin | [`total_bilirubin.md`](liver/total_bilirubin.md) |
| Albumin | [`albumin.md`](liver/albumin.md) |
| Globulin | [`globulin.md`](liver/globulin.md) |
| Total Protein | [`total_protein.md`](liver/total_protein.md) |
| Albumin / Globulin Ratio | [`albumin_globulin_ratio.md`](liver/albumin_globulin_ratio.md) |

### Male Hormones ([male_hormones/](male_hormones/))
| Marker | File |
|---|---|
| Total Testosterone | [`total_testosterone.md`](male_hormones/total_testosterone.md) |
| Free Testosterone | [`free_testosterone.md`](male_hormones/free_testosterone.md) |
| SHBG | [`SHBG.md`](male_hormones/SHBG.md) |
| Estradiol (E2) | [`estradiol_E2.md`](male_hormones/estradiol_E2.md) |
| LH | [`LH.md`](male_hormones/LH.md) |
| FSH | [`FSH.md`](male_hormones/FSH.md) |
| Prolactin | [`prolactin.md`](male_hormones/prolactin.md) |
| DHEA-S | [`DHEA-S.md`](male_hormones/DHEA-S.md) |
| AM Cortisol | [`cortisol.md`](male_hormones/cortisol.md) |

### Thyroid ([thyroid/](thyroid/))
| Marker | File |
|---|---|
| TSH | [`TSH.md`](thyroid/TSH.md) |
| Free T4 | [`FT4.md`](thyroid/FT4.md) |
| Free T3 | [`FT3.md`](thyroid/FT3.md) |
| Reverse T3 | [`rT3.md`](thyroid/rT3.md) |
| TPO Antibodies | [`TPO_Ab.md`](thyroid/TPO_Ab.md) |
| TgAb | [`TgAb.md`](thyroid/TgAb.md) |

### Vitamins & Minerals ([vitamins_minerals/](vitamins_minerals/))
| Marker | File |
|---|---|
| Vitamin D (25-OH) | [`vitamin_D_25OH.md`](vitamins_minerals/vitamin_D_25OH.md) |
| Vitamin B12 | [`vitamin_B12.md`](vitamins_minerals/vitamin_B12.md) |
| Methylmalonic Acid (MMA) | [`MMA.md`](vitamins_minerals/MMA.md) |
| Folate | [`folate.md`](vitamins_minerals/folate.md) |
| Homocysteine | [`homocysteine.md`](vitamins_minerals/homocysteine.md) |
| Magnesium (RBC) | [`magnesium_RBC.md`](vitamins_minerals/magnesium_RBC.md) |
| Zinc | [`zinc.md`](vitamins_minerals/zinc.md) |
| Copper | [`copper.md`](vitamins_minerals/copper.md) |
| Selenium | [`selenium.md`](vitamins_minerals/selenium.md) |

### Iron ([iron/](iron/))
| Marker | File |
|---|---|
| Ferritin | [`ferritin.md`](iron/ferritin.md) |
| Serum Iron | [`serum_iron.md`](iron/serum_iron.md) |
| TIBC | [`TIBC.md`](iron/TIBC.md) |
| TSAT (Iron % Sat) | [`TSAT.md`](iron/TSAT.md) |

### Omega Fatty Acids ([omega_fatty_acids/](omega_fatty_acids/))
| Marker | File |
|---|---|
| Omega-3 Index / OmegaCheck | [`omega3_index.md`](omega_fatty_acids/omega3_index.md) |
| EPA | [`EPA.md`](omega_fatty_acids/EPA.md) |
| DHA | [`DHA.md`](omega_fatty_acids/DHA.md) |
| DPA | [`DPA.md`](omega_fatty_acids/DPA.md) |
| Arachidonic Acid | [`arachidonic_acid.md`](omega_fatty_acids/arachidonic_acid.md) |
| Linoleic Acid | [`linoleic_acid.md`](omega_fatty_acids/linoleic_acid.md) |
| Omega-6 Total | [`omega6_total.md`](omega_fatty_acids/omega6_total.md) |
| Omega-6:3 Ratio | [`omega6_3_ratio.md`](omega_fatty_acids/omega6_3_ratio.md) |
| AA / EPA Ratio | [`AA_EPA_ratio.md`](omega_fatty_acids/AA_EPA_ratio.md) |

### CBC ([cbc/](cbc/))
| Marker | File |
|---|---|
| Hemoglobin | [`hemoglobin.md`](cbc/hemoglobin.md) |
| Hematocrit | [`hematocrit.md`](cbc/hematocrit.md) |
| RBC Count | [`RBC_count.md`](cbc/RBC_count.md) |
| MCV | [`MCV.md`](cbc/MCV.md) |
| MCH | [`MCH.md`](cbc/MCH.md) |
| MCHC | [`MCHC.md`](cbc/MCHC.md) |
| RDW | [`RDW.md`](cbc/RDW.md) |
| Platelets | [`platelets.md`](cbc/platelets.md) |

### Immune CBC Differential ([immune/](immune/))
| Marker | File |
|---|---|
| WBC Count | [`WBC_count.md`](immune/WBC_count.md) |
| Neutrophils | [`neutrophils.md`](immune/neutrophils.md) |
| Lymphocytes | [`lymphocytes.md`](immune/lymphocytes.md) |
| Monocytes | [`monocytes.md`](immune/monocytes.md) |
| Eosinophils | [`eosinophils.md`](immune/eosinophils.md) |
| Basophils | [`basophils.md`](immune/basophils.md) |
| NLR (Neut/Lymph Ratio) | [`NLR.md`](immune/NLR.md) |

### Kidney / Electrolytes / Pancreas ([kidney_electrolytes_pancreas/](kidney_electrolytes_pancreas/))
| Marker | File |
|---|---|
| Creatinine | [`creatinine.md`](kidney_electrolytes_pancreas/creatinine.md) |
| BUN | [`BUN.md`](kidney_electrolytes_pancreas/BUN.md) |
| eGFR | [`eGFR.md`](kidney_electrolytes_pancreas/eGFR.md) |
| Urine Albumin / Cr Ratio (uACR) | [`uACR.md`](kidney_electrolytes_pancreas/uACR.md) |
| Sodium | [`sodium.md`](kidney_electrolytes_pancreas/sodium.md) |
| Potassium | [`potassium.md`](kidney_electrolytes_pancreas/potassium.md) |
| Chloride | [`chloride.md`](kidney_electrolytes_pancreas/chloride.md) |
| Bicarbonate (CO₂) | [`bicarbonate.md`](kidney_electrolytes_pancreas/bicarbonate.md) |
| Calcium (serum) | [`calcium_serum.md`](kidney_electrolytes_pancreas/calcium_serum.md) |
| Phosphorus | [`phosphorus.md`](kidney_electrolytes_pancreas/phosphorus.md) |
| Amylase | [`amylase.md`](kidney_electrolytes_pancreas/amylase.md) |
| Lipase | [`lipase.md`](kidney_electrolytes_pancreas/lipase.md) |

### Heavy Metals & PhenoAge ([heavy_metals_phenoage/](heavy_metals_phenoage/))
| Marker | File |
|---|---|
| Lead (blood) | [`lead_blood.md`](heavy_metals_phenoage/lead_blood.md) |
| Mercury (blood) | [`mercury_blood.md`](heavy_metals_phenoage/mercury_blood.md) |
| Arsenic | [`arsenic.md`](heavy_metals_phenoage/arsenic.md) |
| Cadmium | [`cadmium.md`](heavy_metals_phenoage/cadmium.md) |
| PhenoAge (Levine) | [`phenoage.md`](heavy_metals_phenoage/phenoage.md) |

### Autoimmunity & PSA ([autoimmunity_psa/](autoimmunity_psa/))
| Marker | File |
|---|---|
| ANA | [`ANA.md`](autoimmunity_psa/ANA.md) |
| Rheumatoid Factor | [`RF.md`](autoimmunity_psa/RF.md) |
| Anti-dsDNA | [`anti_dsDNA.md`](autoimmunity_psa/anti_dsDNA.md) |
| Anti-CCP | [`anti_CCP.md`](autoimmunity_psa/anti_CCP.md) |
| PSA Total | [`PSA_total.md`](autoimmunity_psa/PSA_total.md) |
| PSA Free | [`PSA_free.md`](autoimmunity_psa/PSA_free.md) |
| PSA Free % | [`PSA_free_percent.md`](autoimmunity_psa/PSA_free_percent.md) |

### Urinalysis ([urinalysis/](urinalysis/))
| Marker | File |
|---|---|
| Urine pH | [`urine_pH.md`](urinalysis/urine_pH.md) |
| Specific Gravity | [`urine_specific_gravity.md`](urinalysis/urine_specific_gravity.md) |
| Urine Protein | [`urine_protein.md`](urinalysis/urine_protein.md) |
| Urine Glucose | [`urine_glucose.md`](urinalysis/urine_glucose.md) |
| Urine Ketones | [`urine_ketones.md`](urinalysis/urine_ketones.md) |
| Urine Blood (occult / RBCs) | [`urine_blood.md`](urinalysis/urine_blood.md) |
| Urine Bilirubin | [`urine_bilirubin.md`](urinalysis/urine_bilirubin.md) |
| Urine Nitrites | [`urine_nitrites.md`](urinalysis/urine_nitrites.md) |
| Leukocyte Esterase | [`urine_leukocyte_esterase.md`](urinalysis/urine_leukocyte_esterase.md) |
| Color & Appearance | [`urine_appearance_color.md`](urinalysis/urine_appearance_color.md) |
| Microscopy (casts/cells/crystals) | [`urine_microscopy.md`](urinalysis/urine_microscopy.md) |

---

## Cross-cutting synthesis: highest-leverage interventions across all markers

The "game plan" engine in the dashboard should privilege interventions that move *many* markers simultaneously. Below is the marker-set each top intervention moves, drawn from §1–4 of the per-marker files. Magnitudes are summarized — the per-file row is authoritative.

### Tier 1 — Multi-system levers (move 10+ markers materially)

#### **Weight loss (5–10% body weight, sustained)**
Biggest cross-system impact. From the per-marker files, moves: ApoB ↓, LDL-C ↓, TG ↓, HDL-C ↑, hs-CRP ↓, HbA1c ↓, fasting glucose ↓, insulin ↓, HOMA-IR ↓, uric acid ↓, ALT ↓ (esp. MASLD), AST ↓, GGT ↓, total T ↑ (in obese), SHBG ↑, E2 ↓ (in obese), leptin ↓, BP ↓, uACR ↓, hs-CRP ↓, NLR ↓, WBC ↓, ferritin ↓ (in MASLD-driven elevation), free T4/3 modest, PhenoAge ↓.
**Caveat:** Most magnitudes shrink to near-zero at BMI <22. This is a TIER 1 lever for elevated baseline only.

#### **Sleep extension to 7.5–8h with regularity**
Moves: Total T ↑ (Leproult 2011), AM cortisol pattern normalization, fasting insulin ↓ 20–30% (Spiegel 1999), HbA1c ↓ (chronic short-sleep correction), BP ↓, hs-CRP ↓, WBC ↓, HRV ↑, leptin ↑ (counterintuitive — short sleep DROPS leptin per Spiegel 2004), ghrelin ↓, NLR ↓.
**Caveat:** ceiling at ~8h; further extension shows no additional benefit.

#### **Aerobic / Zone 2 endurance training (≥150 min/wk)**
Moves: HDL-C ↑ modestly, TG ↓, ApoB minor, HbA1c ↓ (mostly in T2D), insulin sensitivity ↑↑ (+25–40%), ALT ↓ (esp. MASLD; Hallsworth 2011), VO₂max ↑↑, RHR ↓, BP ↓, hs-CRP ↓, NLR ↓, WBC chronic baseline ↓.
**Critical confound:** APPARENTLY drops Hgb/Hct 0.5–1.5 g/dL via plasma volume expansion in 2–6 wk WITHOUT true RBC mass change. RBC count is the stable anchor; recommendation engine MUST surface this confound when an aerobic-trained user sees "low Hgb."

#### **Resistance training (3–5 sessions/wk progressive)**
Moves: insulin sensitivity ↑ (+20–30%), HbA1c ↓ (T2D), liver fat ↓ (Hallsworth 2011, MASLD), lean mass ↑, bone density ↑, glucose disposal ↑.
**Critical confounds:** Acute spike in CK, ALT (muscle origin), AST (muscle origin), creatinine (creatine + meat); recommendation engine MUST flag a recent novel resistance session before alerting on these.

#### **Smoking cessation**
Moves: hs-CRP ↓ (−30–50%), WBC ↓ (−1.0–1.5 K/µL), neutrophils ↓, monocytes ↓, Hgb/Hct ↓ (CO-driven false elevation), HDL-C ↑, fibrinogen ↓, BP modest, RF/anti-CCP risk ↓ (esp. with HLA-DRB1 SE), cadmium body burden ↓ (smoking is dominant Cd source), urine bilirubin neutral, FEV1 trajectory normalization.

#### **Saturated fat reduction (15% → <7% kcal, replace with PUFA/MUFA)**
Moves: LDL-C ↓ −15–25 mg/dL (Mensink 2003), ApoB ↓ proportional, non-HDL-C ↓, total cholesterol ↓, HDL-C marginal ↓.
**Lp(a) reverses direction:** SFA reduction RAISES Lp(a) by 10–25% (GET-READI). This is the "honest no-free-lunch" exception — a fundamental conflict the engine must surface for users with elevated Lp(a).

#### **Soluble fiber increase (psyllium 10–12 g/d, β-glucan 3–5 g/d)**
Moves: LDL-C ↓ −0.20–0.35 mmol/L, ApoB ↓, HbA1c ↓ in T2D, postprandial glucose ↓, hs-CRP modest ↓, satiety / weight, microbiome SCFAs.
Tolerated by most; minimal interaction. High-confidence engine recommendation.

#### **Mediterranean diet (PREDIMED-style)**
Moves: hs-CRP ↓, WBC ↓, NLR ↓, ApoB / non-HDL ↓ modest, HbA1c ↓, ALT ↓ (Properzi 2018), TG ↓, BP ↓, insulin sensitivity ↑, omega-3 / omega-6 favorable shifts (depending on fish content). Cardiovascular event reduction (PREDIMED).

#### **Alcohol cessation / reduction**
Moves: GGT ↓↓ (−30–50%), MCV ↓ over 10–16 wk, ALT ↓ (if elevated), TG ↓, HDL-C ↓ (alcohol RAISES HDL — cessation drops it), uric acid ↓ (heavy drinkers), BP ↓, total T ↑ in heavy drinkers, E2 ↓, folate / Mg / B-vitamin repletion.

### Tier 2 — Targeted high-leverage (move 3–8 markers materially)

#### **Vitamin D supplementation (replete to ≥30–40 ng/mL)**
Moves: 25-OH vit D ↑↑, PTH ↓ if deficient, calcium modest ↑, total T ↑ in deficient men only (Pilz 2011 [1-Trial]; Lerchbaum 2017 null in replete), TPO Ab ↓ modest in Hashimoto's, hs-CRP modest in deficient. SA-specific: 72–94% deficient, requires 2000–4000 IU/d.

#### **Sodium reduction (>4g → ~2.3 g/d)**
BP ↓ (−5–10 mmHg in HTN; −2–5 normotensive); uACR ↓ in salt-sensitive.

#### **EPA+DHA supplementation (2 g/d, 4–6 mo)**
Omega-3 Index ↑ to ≥8% (target), TG ↓ −15–30%, AA:EPA ↓↓, hs-CRP modest, BP modest, RHR ↓, HRV ↑.
**Outcome divergence:** REDUCE-IT (icosapent ethyl 4g/d, EPA-only) showed CV benefit; STRENGTH (EPA+DHA carboxylic acid) did not. Engine should privilege EPA-rich formulations for CV-focused users.

#### **Coffee consumption (3–4 cups/d, especially filtered)**
ALT ↓, GGT ↓, HCC risk ↓ (per AASLD), uric acid ↓ slightly, T2D risk ↓, HbA1c modest. Caveat: unfiltered coffee (French press, espresso) RAISES LDL-C +6–15 mg/dL via cafestol/kahweol.

#### **Selenium 200 µg/d (or 1–2 Brazil nuts/d)**
TPO Ab ↓ −20–55% (Toulis 2010 meta) — but no clinical progression benefit demonstrated. SELECT (Klein 2011) FAILED for prostate cancer prevention; do not recommend for that indication.

#### **Iron repletion (alternate-day Stoffel protocol)**
Ferritin ↑, TSAT ↑, Hgb ↑, MCV ↑, MCH ↑, RDW transient ↑ during repletion (then ↓), RBC ↑.
**Form selection:** ferrous bisglycinate or alternate-day ferrous sulfate; with vit C, away from calcium / coffee / tea / dairy.

#### **B12 (oral high-dose 500–1000 µg/d cyanocobalamin)**
B12 ↑, MMA ↓, homocysteine ↓ modest, MCV ↓ if macrocytic. Methylcobalamin = cyanocobalamin clinically (no proven advantage in healthy adults). High-dose oral works as well as IM in non-pernicious deficiency (Cochrane).

#### **Magnesium repletion (300–400 mg/d glycinate, citrate, or threonate)**
RBC Mg ↑ (slow), PPI users at risk of deficiency, modest BP effect, sleep modest, HRV modest. Forms: glycinate (best tolerated), citrate (mild laxative), oxide (poor absorption — avoid), threonate (CNS-targeted, industry-funded evidence).

### Tier 3 — Single-marker workhorses (highest-evidence per-marker leverage)

| Marker | Single-best lifestyle | Single-best supplement | When pharmacotherapy is needed |
|---|---|---|---|
| ApoB | SFA reduction + soluble fiber + weight loss | Plant sterols 2 g/d + psyllium 10 g/d | High-intensity statin / ezetimibe / PCSK9i for >−25% ApoB |
| LDL-C | Same as ApoB | Same as ApoB | Same as ApoB |
| Lp(a) | (Honest: nothing meaningful — flax / niacin small) | Niacin 1–2g (modest, watch SE) | Pelacarsen / olpasiran / lepodisiran (Phase 3) |
| HDL-C | Aerobic + smoking cessation | (No intervention raises HDL with proven CV benefit — do NOT chase) | None — failed pharma class |
| Triglycerides | Carb / alcohol / weight loss | EPA+DHA 2–4g/d | Icosapent ethyl 4g/d; fibrates if very high |
| hs-CRP | Weight loss + Mediterranean + smoking cessation | Omega-3 modest | Statin (incidental); canakinumab / colchicine (CIRT failed for MTX) |
| HbA1c | Weight loss + walking after meals + carb composition | Berberine (mostly Chinese trials) | Metformin → GLP-1 → SGLT2i |
| Fasting glucose | Walking after meals + sleep + weight loss | Berberine, ALA | Metformin |
| Fasting insulin | Weight loss + carb reduction + exercise | None evidence-based | Metformin (modest), GLP-1 |
| Uric acid | Alcohol / fructose reduction + weight loss | Cherry juice (modest) | Allopurinol; HLA-B*5801 screen in SA before allopurinol |
| ALT | Weight loss (MASLD) + Mediterranean | Vitamin E 800 IU (controversial — PIVENS) | Pioglitazone, semaglutide, resmetirom |
| GGT | Alcohol cessation + coffee | Omega-3 modest | (Underlying disease tx) |
| Total T | Sleep + weight loss (in obese) + adequate dietary fat | Zinc / Mg if deficient; vit D if deficient | Clomiphene / hCG / TRT (specialist) |
| TPO Ab | (Nothing strong — gluten elimination IF celiac) | Selenium 200 µg/d (titer ↓ but no progression benefit) | Levothyroxine if hypothyroid |
| Vitamin D | Sun exposure (3-5× less efficient in pigmented skin) | D3 2000–4000 IU/d (SA dosing) | Loading dose 50,000 IU/wk × 8 wk |
| B12 | Animal foods | Oral cyanocobalamin 500–1000 µg/d | IM if pernicious anemia / absorption-impaired |
| Ferritin | Iron-rich foods + vit C; alcohol cessation if elevated | Ferrous bisglycinate alternate-day | IV ferric carboxymaltose (FCM) for severe deficiency |
| Omega-3 Index | Fatty fish 2–3×/wk | EPA+DHA 2 g/d (algal for vegans) | Icosapent ethyl 4g/d |
| Hgb / Hct | Iron / B12 / folate adequacy + altitude | Iron if deficient | EPO (medical only) |
| WBC / NLR | Smoking cessation + Mediterranean + weight loss | Omega-3 modest | (Disease-specific) |
| eGFR / uACR | Sodium reduction + glycemic control + BP control | None | ACEi / ARB / SGLT2i / GLP-1 / finerenone |
| K | High-K foods (banana / leafy greens / potato / avocado / dairy) | KCl supplementation (caution) | MRA / SGLT2i raise K; loop / thiazide drop K |
| Lead | Source elimination + Ca / Fe sufficiency | Periodic blood donation | EDTA chelation only at BLL ≥45 µg/dL (not lower) |
| Mercury | Predator-fish substitution | Selenium / Brazil nuts (tissue protection only) | DMSA / DMPS only if symptomatic |
| PSA | Avoid ejaculation / cycling 48h before draw; limit animal fat | None proven | 5α-reductase inhibitors (× 2 PSA correction) |

### Tier 4 — Aggressively flagged null / fraudulent / oversold interventions

The recommendation engine should NOT surface these as positive recommendations. Documented in the per-marker files with [no-effect] / [conflicting] / negative-trial citations.

- **Testosterone "boosters"**: D-aspartic acid, tribulus, fenugreek, ZMA, chrysin, maca, stinging nettle — all null in RCTs in eugonadal men.
- **Saw palmetto for BPH/PSA**: STEP / CAMUS null.
- **Selenium for cancer prevention**: SELECT failed (Klein 2011).
- **Vitamin E for cancer/CVD prevention**: SELECT showed HARM (HR 1.17 for prostate cancer in healthy men).
- **B-vitamin Hcy lowering for CV events**: HOPE-2, NORVIT, VITATOPS, Clarke 2010 meta — null for CV outcomes despite lowering Hcy.
- **Heavy metal "detox" supplements**: chlorella, cilantro, oral glutathione, zeolite, modified citrus pectin — all [no-evidence] for systemic Hg/Pb/As lowering. Source elimination > all else.
- **HDL-raising drugs**: torcetrapib, dalcetrapib, evacetrapib, anacetrapib, niacin (AIM-HIGH, HPS2-THRIVE) — all null or harmful for CV events.
- **Pomegranate for PSA**: Pantuck 2006 single-arm vs Pantuck 2015 placebo-controlled NULL.
- **Cinnamon / chromium for glycemic control**: largely null in modern meta-analyses.
- **Echinacea / high-dose vitamin C / β-glucan for WBC/immunity**: null effects for outcomes.
- **Berberine** (non-Chinese populations): real ApoB / glucose effects in Chinese trials, transportability uncertain.
- **Bergamot polyphenol** (single-group Italian trial dependency).
- **"Lean mass hyperresponder" keto-defended LDL-C elevations**: no outcome trial; engine should NOT excuse elevated ApoB on this basis.
- **Saunas / chelators for "metal sweat" excretion**: minor pathway, not clinically meaningful.

---

## Cross-cutting confounder map (apply BEFORE generating recommendations)

These are the "would make a default recommendation wrong" filters. Surface them on the dashboard alongside any flagged marker. Each per-marker file's §8 has the full list; this is the highest-yield subset.

| Confound | Marker(s) affected | Default fix |
|---|---|---|
| Biotin (≥1 mg/d) | TSH falsely ↓, FT4/FT3 falsely ↑, troponin falsely ↓, PSA, sex hormones — assay-wide interference | Hold biotin 48–72 h before draw |
| Recent novel resistance training (24–48 h) | CK ↑↑, ALT ↑ (muscle), AST ↑ (muscle), creatinine ↑ (creatine + meat) | Defer non-urgent draws; differentiate via AST:ALT ratio + CK |
| Aerobic-trained user with low Hgb/Hct | Hgb ↓, Hct ↓ — plasma volume expansion artifact (not anemia) | Check RBC count + ferritin; do NOT recommend iron unless ferritin/TSAT also low |
| Creatine monohydrate supplementation | Creatinine ↑ +0.1–0.4 mg/dL, eGFR ↓ (no true GFR change) | Measure cystatin C if eGFR concern persists |
| Recent ejaculation (<48 h) or cycling (<48 h) | PSA ↑ +0.4–0.8 ng/mL | Reschedule draw |
| Recent UTI / prostatitis | PSA ↑↑ (transient large rise) | Defer PSA draw 4–6 wk post-infection |
| Iron repletion in progress | RDW ↑ (transient — reticulocyte mixing) | Expected; will normalize as repletion completes |
| Acute illness / vaccination (recent <2 wk) | hs-CRP ↑↑, ferritin ↑↑, WBC ↑, albumin ↓ | Defer non-urgent draws |
| Smoking | WBC ↑, neutrophils ↑, monocytes ↑, Hgb/Hct ↑ (CO), hs-CRP ↑, cadmium ↑ | Cessation > all else; mark elevations as smoking-driven |
| Heavy alcohol (recent) | GGT ↑, MCV ↑, AST:ALT >2, TG ↑, HDL ↑ (paradoxical), uric acid ↑, B-vitamin / Mg deficiency | Cessation + B-vitamin / Mg repletion |
| MASLD / lean MASLD (esp. SA) | ALT ↑, GGT ↑, ferritin ↑, uric acid ↑, ApoB ↑, HOMA-IR ↑ | Weight loss + Mediterranean; coffee modestly protective |
| PPI use | Mg ↓, B12 ↓, iron absorption ↓ | Periodic Mg / B12 / Fe screening |
| Metformin use | B12 ↓ (10–30%) | Periodic B12 / MMA screening |
| GLP-1 use (semaglutide / tirzepatide) | Amylase ↑, lipase ↑, weight ↓↓, A1c ↓↓, ApoB ↓, hs-CRP ↓, eGFR initial dip | Expected; differentiate from acute pancreatitis via symptoms + magnitude |
| SGLT2i use | Glycosuria (expected), eGFR initial dip, K modest, urate ↓, phosphate ↑ modest, modest ketonuria | Expected; not pathologic |
| Diuretic use | K ± (loop/thiazide ↓; MRA ↑), Na ±, Cr ↑ if volume-depleted | Adjust intake / monitor electrolytes |
| First-morning vs random urine | uACR (much more accurate first-morning); proteinuria (orthostatic vs persistent) | Always specify timing |
| 23andMe modifiers (APOE, FADS1/2, MTHFR, HFE, TMPRSS6, SLCO1B1, PNPLA3, GCKR, CYP1A2, ALDH2, GC vit-D, DIO2, SHBG SNPs, HOXB13, BRCA1/2, HLA-B*5801, ACKR1/Duffy, G6PD, HBB) | Cross-marker — see `effect_sizes_INDEX.md` §SNP Modifiers + per-file §8 | Apply genetic-aware recommendation overlay |

---

## SA-specific cross-cutting (apply for South Asian users)

Drawn from per-file §7 sections. Default thresholds shift in this population.

- **Vit D deficiency near-universal** in SA / pigmented skin populations (~72–94% in UK SA cohorts); larger oral D3 doses (2000–4000 IU/d) needed for repletion.
- **Lean MASLD / TOFI phenotype:** ALT, GGT, ferritin, uric acid, HOMA-IR, ApoB elevated at apparently-normal BMI. Do not dismiss based on BMI alone.
- **ApoB > LDL-C** for SA risk stratification. SA lipid phenotype: lower HDL, higher TG, higher ApoB/ApoA1; LDL-C alone systematically undertreats. NLA 2021 statement.
- **Lp(a) baseline distribution shifted higher** in SA. Measure once.
- **B12 deficiency very common** in vegetarian SA (up to 75% in some Indian cohorts). Oral 500–1000 µg/d cyanocobalamin.
- **Iron-handling complications:** TMPRSS6 variants common in SA; affect oral iron response. HFE C282Y rarer in SA (~0.3% vs 6% European).
- **FADS2 advantage** for ω3 conversion (~70% SA carry rs66698963 insertion); still insufficient for Omega-3 Index ≥8% without direct supplementation.
- **SHBG set-point lower** in SA → total T runs lower but free T parity maintained.
- **Higher T2D risk at lower A1c.** Lower intervention thresholds. HOMA-IR threshold drops to >1.5 (vs >2.7 standard).
- **HLA-B*5801 screen before allopurinol** in SA (severe cutaneous reactions).
- **Higher ABCG2 risk allele frequency** → higher baseline urate; less responsive to dietary purine reduction.
- **Mercury exposure higher** in Asian Americans (Caldwell 2014 NHANES) — fish-source audit higher yield.
- **NLR baseline differences** by ancestry; ACKR1/Duffy-null benign neutropenia in African ancestry (not SA but worth flagging).

---

## What's still missing (next research priorities for the dashboard team)

In ranked order (per audit conversation):

1. **Within-person biological variability (CVI) / Reference Change Values (RCV) per marker** — to interpret semi-annual draw deltas as signal vs. noise. Westgard database has CVI for ~600 analytes.
2. **23andMe linkage per marker formalized into recommendation overlays.** Currently the SNP modifiers are listed in §8 of each file but not yet structured as engine-readable rules.
3. **CGM data integration.** Many metabolic interventions (food order, vinegar pre-meal, postprandial walking) are best tracked / personalized via CGM.
4. **Wearable-correlate quantification.** §5 of each file documents the qualitative direction; quantified change-on-change models (e.g., "+10 min Z2/day → −0.1 mg/dL hs-CRP at 12 wk") are mostly absent in the literature.
5. **Combined-stack diminishing-returns curves.** §6 uses the rule-of-thumb 60–80% of linear sum; per-marker quantification would allow more precise next-draw projection.
6. **Within-day timing models.** Some interventions (caffeine timing for cortisol, training timing for HRV recovery, fasting window for IF) need timing-aware models, not just dose-aware.
7. **Female-specific re-calibration.** Most evidence is male / mixed-sex; female cycle-phase, perimenopause, and pregnancy cutoffs need separate treatment if expanding beyond the male user base.

---

## Sister files for cross-reference

- [`../README.md`](../README.md) — repo-level overview
- [`../effect_sizes_INDEX.md`](../effect_sizes_INDEX.md) — cross-panel intervention summary (this folder is the deeper per-marker version)
- [`../biomarker_confounds_reference.md`](../biomarker_confounds_reference.md) — pre-analytical confounds master reference
- Panel reference files at repo root (`heart_lipids_basic.md`, `metabolic_panel.md`, etc.) — biology and clinical interpretation context
