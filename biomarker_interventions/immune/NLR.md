# Neutrophil-to-Lymphocyte Ratio (NLR) — Intervention Research

> NLR = ANC ÷ ALC. Validated mortality and morbidity predictor across cardiovascular, oncologic, infectious, and psychiatric domains. Lower (closer to 1, target <2 in a healthy young adult) is robustly better. Driven by anything that raises neutrophils OR lowers lymphocytes — so smoking, chronic stress, glucocorticoids, obesity, sleep deprivation, sedentary behavior, ultra-processed diet, and acute illness all push NLR up. Lifestyle interventions that lower NLR are largely the same anti-inflammatory stack that lowers WBC and CRP: smoking cessation (NLR ↓ 0.3–0.5), Mediterranean / plant-forward diet (NLR ↓ 0.3–0.6 in inflamed/obese), regular moderate exercise (NLR ↓ 0.2–0.4), weight loss in obesity (NLR ↓ 0.5–1.0), MBSR / chronic stress reduction (NLR ↓ 0.2–0.4), sleep optimization (NLR ↓ small). Single biggest lever: **smoking cessation + 5–10% weight loss in obesity + Mediterranean diet** can drop NLR by 1.0–1.5 units in 12 weeks.

**Cross-link:** Reference biology / clinical interpretation in `../../immune_cbc_differential.md` §7 and `../../effect_sizes_hematology_other.md` §"NLR, LMR, PLR". For the underlying movers see `./neutrophils.md` and `./lymphocytes.md`. This file is INTERVENTION-only and ratio-specific.

---

## Evidence-Grading Legend

| Tag | Meaning |
|---|---|
| **[Meta]** | Replicated meta-analysis of ≥5 RCTs |
| **[RCT]** | Single high-quality RCT |
| **[Cohort]** | Prospective observational |
| **[MR]** | Mendelian randomization |
| **[Mechanism]** | Pharmacology / physiology |
| **[1-Trial]** | Single small trial unreplicated |

Population caveat: most NLR-intervention data come from cardiovascular, oncologic, or metabolic-disease cohorts with elevated baseline NLR (>3). In healthy young adults with NLR 1.5–2.5, floor effects substantially shrink magnitudes.

---

## 0. Why NLR matters — prognostic context

NLR captures the balance of **innate inflammatory** (neutrophil) vs **adaptive regulatory** (lymphocyte) immunity. Higher = more inflammation, less regulatory tone.

- **CV mortality**: Each 1-unit ↑ NLR → HR 1.12 for HF mortality (BMC Cardiovasc Disord 2023 meta of 36 studies); STEMI in-hospital mortality RR 3.52 with high NLR (2024 meta of 35 studies, 28,756 patients).
- **All-cause mortality (general population)**: Forget et al. *BMC Res Notes* 2017 (PMC5217256) established healthy reference 0.78–3.53; populations above threshold show progressively worse mortality.
- **Cancer**: Templeton et al. *J Natl Cancer Inst* 2014 (PMID 24875653) — meta of 100 studies, >40,000 patients with solid tumors: high pretreatment NLR → worse OS HR 1.81. Common cutoff NLR >3.
- **COVID-19**: Simadibrata et al. *PMC* 2022 (PMC9015924) — NLR at admission AUC 0.81 for severity, 0.86 for mortality; each 1-unit ↑ → OR 6.2 for severity, OR 12.6 for all-cause mortality.
- **Depression / psychiatry**: 2025 meta-analysis of 41 studies (>205,000 participants): depressed individuals NLR significantly elevated (SMD 0.35) vs controls; correlates with severity and suicide risk. (Front Psychiatry 2022)
- **Diabetes / prediabetes**: high NLR → all-cause mortality HR 1.82, CV mortality HR 2.07 (Inflammopharmacology 2024).

**Practical NLR interpretation**:
| NLR | Interpretation |
|---|---|
| <1.5 | Excellent — well-regulated immune state |
| 1.5–2 | Normal — healthy young adult target |
| 2–3 | Borderline / subclinical inflammation |
| 3–5 | Elevated — investigate cause |
| >5 | High — strong inflammation; prognostic threshold in CV/cancer literature |
| >9 | Severe — sepsis, severe illness, MPN |

---

## 1. Foods that LOWER NLR (or improve direction)

| Food | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Mediterranean diet (whole pattern) | PREDIMED-style: EVOO 4 tbsp/d, nuts 30 g/d, fish ≥3×/wk, legumes ≥3×/wk, vegetables ≥2 servings/d | NLR ↓ −0.3 to −0.6 units (in metabolic syndrome / inflamed) | 12 wk – 1 yr | **[RCT]** | Casas et al. *PLOS One* 2014 (PMC4198137) — 1-yr Med diet: granulocyte ↓, lymphocyte stable → NLR ↓; PREDIMED Estruch *Ann Intern Med* 2006 (PMID 16818865) | Effect largest in metabolic syndrome / elevated baseline; minimal in lean healthy young adults at NLR ~1.5 |
| Extra-virgin olive oil | 30–50 mL/d | NLR ↓ −0.1 to −0.3 (via reduced neutrophil activation; lymphocytes stable) | 6–12 wk | **[RCT]** | Aparicio-Soto et al. *Food Funct* 2016 olive oil polyphenols & immune; EUROLIVE Covas *Ann Intern Med* 2006 (PMID 16954359) | Polyphenol-rich EVOO required (>250 mg/kg) |
| Fatty fish / EPA+DHA-rich fish | 2–3 servings/wk | NLR ↓ −0.2 to −0.4 | 8–24 wk | **[Meta]** | Calder *Br J Clin Pharmacol* 2013 omega-3 & inflammation; Yang et al. *Lipids Health Dis* 2013 | Plateau ~1 g/d EPA+DHA from food |
| Whole grains (oats, barley, rye) | ≥48 g whole grain/d | NLR ↓ −0.1 to −0.3 | 6–12 wk | **[Meta]** | Xu et al. *Adv Nutr* 2018 (PMID 29659684) whole grains & inflammation meta | Refined-carb-heavy populations see largest effect |
| Legumes | 1 cup/d cooked | NLR ↓ −0.1 to −0.3; CRP ↓ | 4–12 wk | **[RCT]** | Hosseinpour-Niazi et al. *Diabetes Care* 2015 (PMID 25710924) | Best in metabolic syndrome / T2DM |
| Nuts (walnuts, almonds, pistachios) | 30–60 g/d | NLR ↓ small; CRP ↓ −0.3 mg/L | 4–12 wk | **[Meta]** | Neale et al. *BMJ Open* 2017 (PMID 29101142) | PREDIMED nut arm contributed to reduced inflammation |
| Cruciferous vegetables (broccoli, kale) | ≥1 cup/d | Modest NLR ↓ via sulforaphane Nrf2 activation → reduced NF-κB | 4–12 wk | **[Mechanism]** | Navarro et al. *Cancer Prev Res* 2014 (PMID 24962101) | Direct NLR RCT data sparse |
| Berries (anthocyanin-rich) | ≥1 cup/d | NLR ↓ small; CRP ↓ ~0.3 mg/L | 4–8 wk | **[1-Trial]** | Karlsen et al. *J Nutr* 2007 bilberry & inflammation; Basu et al. *J Nutr* 2010 (PMID 20660279) | Effect modest in healthy subjects |
| Plant-based / vegan diet | Whole pattern | NLR ↓ −0.4 to −0.8 vs Western (largely via neutrophil reduction) | 12+ wk | **[RCT]** | Mishra et al. *Eur J Clin Nutr* 2013 GEICO trial; Haghighatdoost et al. *Public Health Nutr* 2017 vegetarian diets & CRP meta | Largest delta in Western-diet → vegan transitions |
| Coffee (filtered) | 3–4 cups/d | NLR ↓ small; inverse association with WBC and CRP in NHANES | Chronic | **[Cohort]** | Andersen et al. *Am J Clin Nutr* 2006; Loftfield et al. *JAMA Intern Med* 2018 (PMID 29971313) | Coffee-smoking confound |
| Green tea (EGCG-rich) | 3–5 cups/d | NLR ↓ small; reduced neutrophil oxidative burst | 8–12 wk | **[Meta]** | Serban et al. *J Am Heart Assoc* 2015 (PMID 26206733) | Effect modest |
| Turmeric / curcumin (food doses) | 1 tsp/d with black pepper | NLR ↓ small; CRP ↓ | 8–12 wk | **[Meta]** | Sahebkar et al. *J Funct Foods* 2017 curcumin & CRP meta | Bioavailability poor without piperine |
| Yogurt / fermented dairy | 1 serving/d | NLR ↓ small via reduced systemic LPS | 4–12 wk | **[RCT]** | Pei et al. *Br J Nutr* 2017 (PMID 28091333) | Strain-dependent |
| Cocoa flavanols (dark chocolate) | 20–40 g/d (>70%, ~500 mg flavanols) | NLR ↓ small | 4–12 wk | **[Meta]** | Lin et al. *J Nutr* 2016 (PMID 27852870) cocoa & inflammation meta | Effect smaller than Med diet pattern |
| DASH diet | Whole pattern | NLR ↓ −0.2 to −0.4 in hypertensive / metabolic syndrome | 8–12 wk | **[RCT]** | Soltani et al. *Br J Nutr* 2018 DASH & inflammation meta | Similar pattern to Mediterranean |

---

## 2. Foods that RAISE NLR (or worsen direction)

| Food | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Sugar-sweetened beverages | ≥1/d | NLR ↑ +0.2–0.5 | Chronic | **[Cohort]** | de Koning et al. *Circulation* 2012 (PMID 22412070) | Mediated by hepatic DNL → MAFLD inflammation |
| Ultra-processed foods | >50% energy | NLR ↑ +0.3–0.6; CRP ↑ | Chronic | **[Cohort]** | Lopes et al. *Eur J Nutr* 2022 NHANES UPF & inflammation; Martínez-Steele et al. *BMJ Open* 2016 | Independent of total energy, fat, sugar |
| Industrial trans fats | ≥2% energy | NLR ↑ small; CRP ↑ ~30% | 4–12 wk | **[RCT]** | Mozaffarian et al. *J Nutr* 2004 (PMID 15226430) | Largely banned in US since 2018 |
| Processed/cured red meat | ≥50 g/d | NLR ↑ +0.2 (via neutrophil rise + chronic inflammation) | Chronic | **[Cohort]** | Montonen et al. *Eur J Nutr* 2013 (PMID 22538890); Schwingshackl et al. *Br J Nutr* 2017 meta | Heme + nitrites + AGEs |
| Heavy alcohol (chronic) | ≥3 drinks/d | NLR variable: chronic heavy → ↑ neutrophil + ↓ lymphocyte → NLR ↑ +0.3–0.8 | Chronic | **[Cohort]** | Imhof et al. *Eur Heart J* 2004 (PMID 15078742); Pasala et al. *Alcohol Res* 2015 | Light drinking shows neutral or U-shape |
| Acute high-fat meal | Single >50 g fat | NLR ↑ +0.2–0.5 transient (postprandial neutrophilia) | 2–6 h | **[1-Trial]** | Erridge et al. *Am J Clin Nutr* 2007 (PMID 17827268) | Transient; confound for non-fasting draws |
| Western dietary pattern | Habitual | NLR ↑ +0.4–0.8 vs Mediterranean | Chronic | **[RCT]** | PREDIMED control comparison; Esposito *JAMA* 2004 (PMID 15383518) | Pattern-level effect |
| Excess fructose (HFCS) | ≥50 g/d added | NLR ↑; uric acid ↑; CRP ↑ | 4–12 wk | **[RCT]** | Stanhope et al. *J Clin Invest* 2009 (PMID 19381015) | Mechanistic via hepatic ATP depletion |
| Deep-fried / oxidized-oil foods | Several servings/wk | NLR ↑ chronic | Chronic | **[Cohort]** | Cahill et al. *BMJ* 2014 fried food & CHD | |

---

## 3. Supplements

### Lowering / improving

| Supplement | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Omega-3 (EPA+DHA) | 1.5–4 g/d | NLR ↓ −0.2 to −0.5 | 8–24 wk | **[Meta]** | AbuMweis et al. *J Funct Foods* 2018 omega-3 meta; Calder 2013 | Plateau ~3 g/d combined EPA+DHA |
| Curcumin (bioavailable) | 500–1000 mg/d (Meriva, BCM-95, with piperine) | NLR ↓ −0.2 to −0.4; CRP −0.7 to −1.5 mg/L | 4–12 wk | **[Meta]** | Sahebkar et al. *J Funct Foods* 2017 curcumin & CRP meta of 6 RCTs | Plain turmeric powder ineffective |
| Vitamin D₃ (in deficient) | 2000–4000 IU/d | NLR ↓ −0.1 to −0.3 in deficient subjects | 8–16 wk | **[RCT]** | de Oliveira et al. *Nutrients* 2017 vitamin D & WBC; Aranow *J Investig Med* 2011 | No effect in vitamin D-replete [no-effect when sufficient] |
| CoQ10 | 100–200 mg/d | NLR ↓ small; CRP −0.4 mg/L | 8–12 wk | **[Meta]** | Mazidi et al. *Pharmacol Res* 2018 (PMID 28729175) | Mostly CV/metabolic disease |
| Resveratrol | 150–500 mg/d | NLR ↓ small; CRP −0.3 mg/L | 8–12 wk | **[Meta]** | Koushki et al. *Clin Ther* 2018 | Bioavailability poor |
| Probiotics (multi-strain) | 10⁹–10¹⁰ CFU/d | NLR ↓ small via reduced gut LPS | 4–12 wk | **[Meta]** | Mazidi et al. *Pharmacol Res* 2017 (PMID 28442349) | Strain-specific |
| Magnesium (in deficient) | 300–500 mg/d | NLR ↓ small if Mg deficient | 8–24 wk | **[Meta]** | Simental-Mendía et al. *Curr Pharm Des* 2017 | Function of correcting deficiency |
| Garlic (aged extract) | 600–2400 mg/d | NLR ↓ small; CRP ↓ | 8–12 wk | **[Meta]** | Sahebkar et al. *Pharmacol Res* 2016 garlic & CRP meta | Aged garlic > raw |
| Quercetin | 500–1000 mg/d | NLR ↓ small | 8–12 wk | **[Meta]** | Mohammadi-Sartang et al. *Eur J Clin Nutr* 2017 quercetin & CRP meta | Effect small |
| Spirulina | 1–8 g/d | NLR ↓ small (via reduced neutrophil and modest lymphocyte ↑) | 8–12 wk | **[1-Trial]** | Selmi et al. *Cell Mol Immunol* 2011 spirulina & immunity | Limited rigorous trials |
| N-acetylcysteine (NAC) | 600–1200 mg/d | NLR ↓ small; reduced neutrophil ROS | 8–12 wk | **[1-Trial]** | Šalamon et al. *Br J Pharmacol* 2019 NAC & inflammation review | Effect small in healthy adults |

### Raising / worsening (or claimed-but-doesn't-work)

| Supplement / drug | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Glucocorticoids (prednisone, dex) | Therapeutic | NLR ↑ +5 to +15 (massive: ANC ↑↑ + ALC ↓↓) | 4–12 h | **[RCT]** | Bishop et al. *Blood* 1968; Olnes et al. *N Engl J Med* 2016 (PMID 27305192) | Universal effect; major confound for any patient on steroids |
| Lithium | 600–1800 mg/d | NLR ↑ +1.5–2.5 (via ANC ↑) | Wk | **[RCT]** | Lapierre et al. *Acta Psychiatr Scand* 1980 | Used therapeutically for clozapine-induced neutropenia |
| G-CSF / GM-CSF | Therapeutic | NLR ↑ profoundly (ANC +10–30) | Days | **[RCT]** | Welte et al. *Blood* 1996 | Pharmacotherapy |
| Anabolic steroids | Variable illicit | NLR ↑ via marrow stimulation | Wk | **[Cohort]** | Bonetti et al. *Int J Sports Med* 2008 | Important confound in young men |
| β-glucan / "immune boosters" | Various | No reliable NLR change [no-effect] | — | **[1-Trial]** | Various | Marketing > evidence |
| Echinacea | 300–900 mg/d | No reliable NLR change [no-effect] | — | **[Meta]** | Karsch-Völk et al. *Cochrane* 2014 | |
| High-dose vitamin C | >2 g/d | No reliable NLR change [no-effect] | — | **[RCT]** | Hemilä & Chalker *Cochrane* 2013 | |

---

## 4. Activities & Behaviors

| Activity | Dose / pattern | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Smoking cessation | Stop combustion + vaping | NLR ↓ −0.3 to −0.5 (via ANC ↓ and modest ALC ↓) | 4–52 wk | **[Cohort]** | Lavi et al. *Am J Med* 2020; Saville et al. *Mayo Clin Proc* 2005 (PMID 16092581) | Single largest reversible NLR lever |
| Smoking (current) | 1+ pack/d | NLR ↑ +0.2–0.5 above non-smoker baseline | Wk-mo | **[Cohort]** | Higuchi et al. *Atherosclerosis* 2016; Schwartz & Weiss *Am J Epidemiol* 1991 | Smoking raises both ANC and ALC, but ANC more |
| Vaping (e-cigarettes) | Daily | NLR ↑ smaller magnitude than combustion smoking | Wk | **[Cohort]** | Reidel et al. *Am J Respir Crit Care Med* 2018; Hickman *Tob Control* 2022 | Long-term data emerging |
| Acute exercise (vigorous, 60+ min) | Single bout | NLR biphasic: ↓ immediately post (ALC mobilization); then ↑ 1–24 h post (lymphopenia + sustained neutrophilia from cortisol) | Min–24 h | **[RCT]** | McCarthy & Dale *Sports Med* 1988 (PMID 3293015); Pedersen & Hoffman-Goetz *Physiol Rev* 2000; Walsh et al. *Exerc Immunol Rev* 2011 | Major draw confound; avoid hard exercise <24 h before lab |
| Chronic aerobic training | 150+ min/wk moderate | Resting NLR ↓ −0.2 to −0.4 (in sedentary baseline); minimal in already trained | 8–24 wk | **[Meta]** | Bahls et al. *Atherosclerosis* 2018 exercise & NLR meta; Wang et al. *Mediators Inflamm* 2017; Mathur & Pedersen *Scand J Med Sci Sports* 2008 | Trained athletes have lower resting NLR |
| Resistance training (chronic moderate) | 2–3×/wk | NLR ↓ small; less data than aerobic | 8–24 wk | **[1-Trial]** | Tomeleri et al. *Exp Gerontol* 2018 | |
| HIIT | 3×/wk × 8–12 wk | Resting NLR ↓ comparable to moderate aerobic | 8–12 wk | **[1-Trial]** | Ramos-Campo et al. *Eur J Sport Sci* 2021 | Acute spike larger; chronic adaptation similar |
| Chronic excessive exercise (overtraining) | >20 h/wk endurance | NLR ↑ via ALC ↓ (overtraining lymphopenia) + mild ANC ↑ | Mo | **[Cohort]** | Mackinnon *Int J Sports Med* 2000 overtraining & immune; Nieman 2019 J-curve | Athlete-specific |
| Step count ≥7000/d | Sustained | NLR ↓ small; CRP ↓ ~0.3 mg/L per +2000 steps | 12+ wk | **[Cohort]** | Loprinzi *Health Promot Pract* 2015 NHANES | Sedentary baseline → larger effect |
| Sleep (chronic restriction → adequate) | <6 h → 7–9 h | NLR ↓ −0.2 to −0.4 when restored | 4–12 wk | **[Cohort]** | Born et al. *J Immunol* 1997; Irwin et al. *Best Pract Res Clin Endocrinol Metab* 2010 | Acute sleep deprivation ↑ NLR transiently |
| Acute sleep deprivation | 1 night | NLR ↑ +0.3–0.6 next morning (ANC ↑ + ALC ↓) | 24 h | **[1-Trial]** | Born et al. 1997 | Reverses with recovery sleep |
| Sleep regularity (consistent bedtime) | ±30 min nightly | NLR ↓ small; reduced HPA dysregulation | Mo | **[Cohort]** | Lunsford-Avery et al. *Sci Rep* 2018 sleep regularity & cardiometabolic risk | Independent of duration |
| Stress reduction (MBSR / mindfulness) | 8-wk MBSR | NLR ↓ −0.2 to −0.4 (in chronically stressed); reduced cortisol-driven neutrophil mobilization | 8–16 wk | **[RCT]** | Creswell et al. *Brain Behav Immun* 2012 (PMID 22820409); Black et al. *Ann N Y Acad Sci* 2016 meditation & inflammation | Effect modest in healthy controls; larger in chronic stress |
| Yoga (regular practice) | 2–3 sessions/wk | NLR ↓ small to modest; reduced cortisol and CRP | 12 wk | **[1-Trial]** | Yadav et al. *J Altern Complement Med* 2012 yoga & inflammation; Kohli et al. *J Asthma* 2015 yoga & atopy | |
| Sauna (Finnish) | 2–7×/wk, 15–20 min @ 80–90 °C | NLR ↓ small over months; chronic adaptation lowers hsCRP | 6–24 mo | **[Cohort]** | Laukkanen et al. *JAMA Intern Med* 2015 (PMID 25705824); Kunutsor et al. *Eur J Epidemiol* 2018 sauna & inflammation | Acute session → transient ANC ↑ → NLR ↑ briefly |
| Cold exposure (cold-water immersion) | 2–3×/wk, 5–10 min | Acute NLR ↑ (catecholamine demargination of ANC and ALC); chronic effect mixed | Acute / chronic | **[1-Trial]** | Šrámek et al. *Eur J Appl Physiol* 2000; Buijze et al. *PLOS One* 2016 | Limited rigorous chronic NLR data |
| Heavy alcohol cessation (in heavy drinker) | Stop drinking | NLR ↓ −0.3 to −0.7 (via ANC ↓ + ALC restoration) | Wk-mo | **[Cohort]** | Latvala et al. *Alcohol* 2004; Pasala et al. *Alcohol Res* 2015 | Chronic alcoholic baseline can have NLR >3 |
| Caffeine (acute) | 200–400 mg | Transient NLR ↑ small via catecholamine | 1–4 h | **[Mechanism]** | Walker et al. *Eur J Appl Physiol* 2007 | |
| Hydration (correct dehydration) | 2–3 L/d | Hemoconcentration corrected; NLR slight change | Hours | **[Mechanism]** | Maw et al. *Clin Sci* 1997 | |
| Time-restricted eating / IF | 16:8 daily | NLR ↓ small; mostly via weight loss + reduced inflammation | 8–12 wk | **[1-Trial]** | Sutton et al. *Cell Metab* 2018 eTRF; Moro et al. *J Transl Med* 2016 | Effect mostly indirect |
| Weight loss (in obesity) | −5–10% body weight | NLR ↓ −0.5 to −1.0 | 3–12 mo | **[RCT]** | Look AHEAD *N Engl J Med* 2013 (PMID 23796131); Jung & Choi *Ann Intern Med* 2014 | Largest non-smoking lifestyle lever in obese; NLR responds well |
| Bariatric surgery | RYGB / sleeve | NLR ↓ −0.7 to −1.5 over 12 mo | 6–12 mo | **[Cohort]** | Illán-Gómez et al. *Obes Surg* 2012 | Includes both ANC ↓ and ALC normalization |
| Periodontal treatment (in periodontitis) | Scaling + root planing | NLR ↓ −0.3 to −0.5 if periodontitis driving inflammation | 2–6 mo | **[RCT]** | Tonetti et al. *N Engl J Med* 2007 (PMID 17314338) | Hidden inflammation source |
| Acute psychological stress | Single major stressor | NLR ↑ +0.5–2.0 within 1 h (ANC ↑ via catecholamine + ALC ↓ via cortisol redistribution) | 30 min – 24 h | **[1-Trial]** | Dimitrov et al. *J Immunol* 2010 (PMID 19948948); Dhabhar 2012 (PMC3412918) | Standardize draw conditions |
| Chronic psychological stress | Months of chronic stress | NLR ↑ +0.5–1.5 sustained | Mo | **[Cohort]** | Cohen et al. *PNAS* 2012; Steptoe & Kivimäki *Annu Rev Public Health* 2013 | Cortisol + SNS-mediated |
| Active acute infection | During illness | NLR ↑ +5 to +30 (bacterial > viral); severe sepsis: NLR >9 | Days–wk | **[Cohort]** | Standard infection literature; Simadibrata 2022 COVID-19 NLR | Resolves with infection clearance |

---

## 5. Wearable-Trackable Metric Relationships

| Wearable metric | Direction of relationship | Magnitude / effect size | Evidence | Source | Caveats |
|---|---|---|---|---|---|
| VO₂max ↑ | Inverse with NLR | Each 1 MET ↑ → NLR ↓ ~0.05–0.1 | **[Cohort]** | Aspenes et al. *Med Sci Sports Exerc* 2011 fitness & inflammation; Kullo et al. *J Cardiopulm Rehabil* 2007 | Confounded by adiposity, smoking |
| HRV (RMSSD/SDNN) ↑ | Higher HRV → lower NLR | r ~ −0.20 to −0.30 in cohort data | **[Cohort]** | Williams et al. *Brain Behav Immun* 2019 (PMID 31195092) HRV & inflammation meta | Vagal tone & cholinergic anti-inflammatory pathway (Tracey *Nature* 2002) |
| Resting HR ↓ | Inverse with NLR | Both reflect parasympathetic tone | **[Cohort]** | Whelton et al. *Ann Intern Med* 2014 | Indirect downstream of fitness/training |
| Step count ≥7000/d | Inverse with NLR | +2000 steps → NLR ↓ small | **[Cohort]** | Loprinzi 2015 NHANES | Sedentary baseline → larger effect |
| Sleep duration 7–9 h | Inverse U-shape with NLR | <6 h → NLR ↑ +0.3–0.5; >9 h → also ↑ | **[Cohort]** | Patel et al. *Sleep* 2009; Born 1997 | Both extremes raise NLR |
| Sleep regularity (low SD bedtime) | Inverse with NLR | Modest but consistent | **[Cohort]** | Lunsford-Avery 2018 | Independent of duration |
| Exercise minutes/wk (150–300 moderate) | Inverse with NLR | Doses above 300 min/wk show plateau or J-curve | **[Cohort]** | Pedersen *Eur J Clin Invest* 2017 | Overtraining → ↑ NLR |
| Training load (acute spike) | Acute ↑ NLR | Single hard session → NLR ↑ +1–3 at 1–24 h post | **[RCT]** | McCarthy & Dale 1988; Walsh 2011 | Major draw confound |
| Body composition (lower fat %) | Inverse with NLR | −5% body fat → NLR ↓ −0.2 to −0.4 | **[Cohort]** | Visser et al. *JAMA* 1999 (PMID 10591383); Furuncuoğlu et al. *Eur Rev Med Pharmacol Sci* 2016 BMI & NLR | Adipose IL-6 production |
| Stress score (HRV + subjective) | Positive with NLR | Modest correlation | **[Cohort]** | Cohen 2012; Steptoe 2013 | Wearable proxy |
| Sleep efficiency / quality | Inverse with NLR | Higher quality → lower NLR | **[Cohort]** | Irwin 2010 | |
| Continuous glucose monitor — high glucose variability | Positive with NLR | Higher variability → ↑ NLR via inflammation | **[Cohort]** | Monnier et al. *JAMA* 2006 — glucose variability & oxidative stress | Indirect |
| Alcohol intake (logged) | Positive with NLR (heavy) | Heavy chronic intake → ↑ NLR | **[Cohort]** | Pasala 2015 | U-shape at light intake |

---

## 6. Synthesis & Highest-Leverage Stack

- **Highest-leverage single intervention**: **Smoking cessation** (NLR ↓ −0.3 to −0.5) for smokers; **5–10% weight loss** (NLR ↓ −0.5 to −1.0) for obese subjects. In a non-smoking lean person, no single lifestyle intervention dominates — diet pattern + exercise + sleep stack incrementally.
- **Best stack of 3** (additive but with diminishing returns ~70–80% of linear sum):
  1. **Smoking cessation + 5–10% weight loss** (if applicable; combined NLR ↓ −0.7 to −1.5)
  2. **Mediterranean / plant-forward diet pattern** (NLR ↓ −0.3 to −0.6)
  3. **Chronic moderate exercise (150–300 min/wk) + sleep optimization (7–9 h regular) + MBSR for chronic stress** (combined NLR ↓ −0.3 to −0.5)
- **Realistic 12-week delta for healthy 20yM with NLR 1.5–2.0**: essentially flat (±0.2 noise). Floor effects — no reliable way to push NLR much below 1 by lifestyle, and NLR ≈ 1 may not be more "optimal" than 1.5–2 in a healthy young adult.
- **Realistic 12-week delta for elevated baseline (NLR 3.5+ from smoking + obesity + poor sleep + sedentary)**: −1.0 to −2.0 units achievable with simultaneous smoking cessation + 5–10% weight loss + diet + exercise + sleep.
- **Realistic 12-week delta for chronic stress / depression with NLR 3 (no smoking/obesity)**: −0.3 to −0.6 units with MBSR + sleep + exercise; SSRI response may improve or worsen depending on remission of underlying inflammation.
- **Where pharmacotherapy becomes necessary**:
  - NLR sustained >5 without acute illness → workup for chronic infection, autoimmune disease, malignancy, hematologic disorder
  - Prognostically high NLR in CV/cancer context: anti-IL-1β (canakinumab, CANTOS Ridker *NEJM* 2017 PMID 28845751) lowers IL-6/CRP and indirectly NLR; statins lower CD16+ monocyte fraction and modestly NLR; colchicine 0.5 mg/d lowers CRP and CV events in stable CAD (LoDoCo2)
  - Severe chronic depression with elevated NLR: SSRI/SNRI may modestly lower NLR in responders; anti-inflammatory adjuncts being studied

---

## 7. South Asian / lean-male-specific notes

- South Asian men have higher NLR per unit BMI compared to NW European peers, reflecting the "lean-but-inflamed" South Asian phenotype with greater visceral adiposity at lower total BMI (Indian Migration Study related analyses; INTERHEART). Use waist circumference and trunk fat % alongside NLR interpretation.
- ACKR1/Duffy-null is rare in South Asians — BEN as a low-NLR-via-low-ANC explanation generally does **not** apply.
- Cultural diet pattern in SA: traditional plant-forward / legume-rich diets (idli, dal, vegetable curries) tend to be lower NLR; urban Western-style adoption (refined wheat, fried foods, sugar-sweetened beverages) raises NLR. Lifestyle dietary recommendations should align with culturally familiar options (lentils, brown rice, leafy greens, fish where available).

---

## 8. Interactions & Confounders for Recommendation Engine

- **Genetic modifiers**:
  - **ACKR1 rs2814778 (Duffy-null)** — common in African-ancestry, rare in others. Constitutionally lower ANC → lower NLR baseline (often <1). Not actionable; don't recommend NLR-lowering interventions.
  - **CXCL8 / CXCR2 polymorphisms** — minor effects on neutrophil trafficking.
  - **IL-6 -174G>C polymorphism** — affects chronic inflammation; carriers may show slightly higher NLR.
  - **TNF-α -308 polymorphism** — modest inflammation modifier.
- **Drug interactions / iatrogenic** (very large effects):
  - **Glucocorticoids** (any): NLR ↑ +5 to +15 within hours via ANC ↑↑ + ALC ↓↓. Massive confound.
  - **Lithium**: NLR ↑ +1.5–2.5.
  - **G-CSF**: NLR ↑ profoundly.
  - **β-blockers**: blunt acute exercise/stress NLR rise.
  - **Statins**: NLR ↓ small via reduced CD16+ monocytes and reduced systemic inflammation; meta-analyses show modest NLR reduction in CV patients.
  - **ACEi/ARB**: small NLR ↓ via reduced inflammation in CV cohorts.
  - **Anti-IL-6 (tocilizumab)**: NLR ↓ in autoimmune patients.
  - **Anti-IL-1β (canakinumab)**: NLR ↓ in CANTOS-type populations.
  - **Colchicine**: NLR ↓ small.
  - **Chemotherapy**: ALC ↓↓ (may transiently ↑ NLR before nadir).
  - **Anti-CD20 (rituximab)**: ALC ↓ → NLR ↑.
  - **HIV antiretrovirals**: NLR ↓ as CD4 recovers.
  - **Fingolimod**: ALC ↓ profoundly → NLR ↑ markedly.
  - **Anabolic steroids**: NLR ↑.
- **Lifestyle confounders**:
  - **Hard exercise within 24 h**: NLR ↑ +1–3 (delayed-phase post-exercise lymphopenia + persistent neutrophilia). Major false positive.
  - **Acute psychological stress within 1 h**: NLR ↑ +0.5–2.
  - **Acute sleep deprivation (1 night)**: NLR ↑ +0.3–0.6 next morning.
  - **Active infection within 2 wk**: NLR distorted in either direction (bacterial → ↑↑; viral → variable).
  - **Recent vaccination (1–7 d)**: variable NLR.
  - **Heavy alcohol day prior**: variable.
  - **Hemoconcentration from dehydration**: NLR slight change (both numerator and denominator affected).
  - **Pregnancy**: NLR physiologically elevated to 3–6 in 3rd trimester.
- **Timing artifacts**:
  - **Diurnal**: NLR follows neutrophil peak (late afternoon 4–8 PM); morning NLR ~25–30% lower than afternoon. (Sennels et al. *Scand J Clin Lab Invest* 2011 PMID 21247230)
  - **Postprandial fat-rich meal**: small NLR ↑ within 4–6 h via postprandial neutrophilia.
  - **Menstrual cycle (in females)**: variation through cycle.

For a clean serial baseline: morning, fasted, no exercise within 24 h, no acute illness within 2 wk, no vaccine within 1–2 wk, normal prior-night sleep, no recent corticosteroid.

---

## 9. Open questions / weak evidence

- **Optimal NLR target in healthy young adults** — most prognostic literature is from disease cohorts; the lifetime mortality benefit of pushing NLR from 2.0 to 1.2 in a healthy 20-year-old is unknown and may be near zero.
- **NLR as serial biomarker of intervention response** — proposed but not formally validated; CRP and hsCRP have stronger validation as inflammation tracking biomarkers.
- **Mendelian randomization for NLR** — limited; most causal inference is from observational cohorts.
- **Population-specific NLR reference ranges** — Forget et al. 2017 used predominantly European-ancestry cohort; Asian, African, and South Asian-specific normative data are emerging but reference ranges not fully harmonized.
- **NLR cutoffs across diseases** — vary widely (2.5–5.0); no single agreed clinical decision threshold.
- **Anti-inflammatory pharmacotherapy specifically for elevated NLR in healthy people** — not indicated; NLR is a downstream marker, not a treatment target outside of disease context.
- **Cold exposure / sauna chronic NLR data** — sparse.
- **Probiotic strain specificity** — strain-by-strain heterogeneity for NLR reduction.
- **Time-restricted eating independent of weight loss** — unclear whether autophagy / inflammation mechanism modifies NLR beyond weight effect.
- **Caloric restriction (CALERIE-style) and NLR** — Spadaro et al. *Science* 2022 (PMID 35143240) showed reduced inflammaging biomarkers; NLR specifically not the primary endpoint but reduction reported.
- **Plant-based vs Mediterranean head-to-head for NLR** — both lower NLR; relative magnitude unclear.
- **Vagal nerve stimulation / breathwork (slow breathing 6 breaths/min)** — modulates HRV and theoretically NLR via cholinergic anti-inflammatory pathway (Tracey *Nature* 2002 PMID 12490958); direct NLR RCTs scarce.
- **Air pollution (PM2.5, NO₂) and NLR** — emerging cohort data show positive association; intervention via air filtration plausible but not directly tested for NLR endpoint.
