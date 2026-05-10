# Kidney, Electrolytes & Pancreas Biomarker Reference

**Audience:** Healthy 20-year-old male, Function Health blood draw.
**Scope:** BUN, Creatinine, BUN/Cr ratio, eGFR (CKD-EPI 2021), urine albumin/microalbumin, Na, K, Cl, HCO3 (CO2), Amylase, Lipase. Calcium and Magnesium are deferred — see `nutrients_vitamins_minerals.md`.
**Standards used:** KDIGO 2024 CKD Guideline, CKD-EPI 2021 (Inker NEJM), Atlanta 2012 acute pancreatitis classification, Verbalis 2013 hyponatremia expert panel.

---

## 0. Cross-cutting context (read this first)

### 0.1 Creatine supplementation is the single most important young-male confounder
Creatine monohydrate is converted spontaneously to creatinine. Standard supplementation (3–5 g/day, or higher loading doses) raises **serum creatinine by roughly 0.1–0.4 mg/dL** without any change in measured GFR — i.e. it is a pseudo-elevation, not nephrotoxicity. Multiple meta-analyses show **no change in true GFR** (iohexol/iothalamate clearance) despite the rise in serum creatinine. The eGFR equations were derived in non-supplementing populations, so a creatine-using lifter can drop into "Stage 2 CKD" range purely from supplementation. (de Souza e Silva 2019 *J Renal Nutrition*; Pinto 2020 *J Int Soc Sports Nutr*; Almeida 2020 *Nutr Health* — see also Kreider 2017 ISSN position stand; Persky/Brazaitis safety reviews summarized in Antonio 2021.)
- **Practical rule:** if you supplement creatine, expect serum Cr ~0.15–0.3 mg/dL above your true baseline. Stop creatine for 7–14 days before a draw if you want a clean number.
- **Better marker for muscular individuals:** Cystatin C–based eGFR (eGFR-cys) or the combined eGFR-cr-cys equation (Inker 2021 NEJM). Cystatin C production is largely independent of muscle mass (Baxmann 2008 *CJASN*; Frontiers in Medicine 2022). KDIGO 2024 explicitly recommends cystatin C confirmation when creatinine-based eGFR may be misclassified — including in athletes with high muscle mass. Cystatin C is **not** in the standard Function Health panel; it's the highest-yield add-on if your Cr looks high.

### 0.2 Pseudohyperkalemia from in-vitro hemolysis
The number-one cause of an "elevated K" report in healthy people is **artifact from the blood draw itself** — not real hyperkalemia. Mechanisms:
- **Fist clenching during phlebotomy:** demonstrated to raise measured K by up to ~1.0 mEq/L (Don 1990 *NEJM*).
- **Tourniquet >1 minute:** hemolysis rate jumps from ~1.3% to ~20%; also causes hemoconcentration and pH drift (Mayo Clinic Labs 2018 review).
- **Small-bore needle / vacuum pull / shaken tube:** mechanical lysis releases intracellular K (cells contain ~140 mEq/L vs serum ~4).
- The lab may flag the sample as "hemolyzed"; if not, an isolated K elevation in a healthy person with no symptoms and a normal ECG is presumptively pseudohyperkalemia and should be redrawn before any clinical action. (Asirvatham 2013 *J Clin Med Res*; Sevastos 2006 review.)

### 0.3 Anion gap & MUDPILES
Anion gap (AG) = Na − (Cl + HCO3). Normal **8–12 mEq/L** (varies by lab and albumin). Always calculate AG when HCO3 is low.
- **High AG metabolic acidosis — MUDPILES:** Methanol, Uremia, DKA, Propylene glycol/Paraldehyde, Iron/INH, Lactate, Ethylene glycol, Salicylates. Updated mnemonic **GOLD MARK** (Mehta 2008 *Lancet*): Glycols, Oxoproline, L-lactate, D-lactate, Methanol, Aspirin, Renal failure, Ketoacidosis.
- **Normal AG (hyperchloremic) acidosis:** diarrhea, RTA, large-volume saline, early CKD, ureteral diversion.
- Albumin correction: AG falls by ~2.5 for every 1 g/dL drop in albumin. (StatPearls *Anion Gap and Non-Anion Gap Metabolic Acidosis*.)

### 0.4 ACE inhibitor / ARB effect on creatinine
A creatinine bump of up to **30%** within the first 4 weeks of starting an ACEi/ARB is **expected and acceptable** under KDIGO 2021 BP guideline and KDIGO 2024 CKD guideline. It reflects hemodynamic relief of efferent-arteriole tone — not AKI. Discontinuation is only warranted if the rise exceeds 30%, K rises dangerously, or volume depletion / NSAID co-use is unmasked. (KDIGO 2021 BP Guideline; *Cleveland Clinic J Med* 2019.)

### 0.5 Drugs that block creatinine secretion (raise serum Cr without affecting true GFR)
- **Trimethoprim** (Bactrim) — competitively inhibits OCT2/MATE1 in proximal tubule. Raises plasma Cr ~15–30%, lowers Cr clearance ~20–25%, with **no change in iothalamate GFR** (Berg 1996; Andreev 1999 *J Intern Med*).
- **Cimetidine** — same mechanism; historically used as a research tool to measure pure GFR via CrCl.
- **Dolutegravir, cobicistat, ranolazine, fenofibrate, pyrimethamine** — similar effect.
This is a "pseudo-AKI" pattern: Cr up, BUN unchanged, urine output normal, no symptoms.

---

## 1. Blood Urea Nitrogen (BUN)

### 1.1 What it is
BUN measures the nitrogen carried in serum urea. **Urea is the end-product of hepatic protein catabolism**: amino-acid amino groups → ammonia → urea (urea cycle, liver) → renal excretion. Most BUN is freely filtered at the glomerulus, but **30–50% is reabsorbed** in the proximal tubule and (under ADH) collecting duct — this is what makes BUN volume-sensitive. Assay: enzymatic urease method on a chemistry analyzer.

### 1.2 Reference range & "optimal"
- **Conventional lab range:** 7–20 mg/dL (adults 18–59); some labs use 6–24. Older adults trend higher (8–23).
- **Optimal in healthy young male:** roughly **10–18 mg/dL**. Below 7 in a non-vegetarian raises a flag for protein deficiency or liver synthetic failure.

### 1.3 High BUN — what it means
- **Prerenal azotemia (most common in young men):** dehydration, vomiting/diarrhea, hemorrhage, CHF, sepsis. ADH-driven urea reabsorption disproportionately raises BUN — **BUN/Cr ratio >20** is the classic prerenal pattern (Clinical Methods, NCBI; LITFL).
- **High protein intake / high-protein diet** (e.g., bodybuilding diet 200+ g/d).
- **GI bleeding** — digested blood is an endogenous protein meal. BUN rises in upper GI bleeds even with normal kidneys.
- **Corticosteroids and tetracyclines** — increase protein catabolism.
- **Renal disease** — when GFR falls, BUN rises (along with Cr).
- **Urinary obstruction (postrenal)** — backpressure reduces filtration.
- **Catabolic states** — burns, severe trauma, fever.

### 1.4 Low BUN — what it means
- **Liver disease** — failing liver makes less urea (urea cycle is hepatic). A low BUN in someone with abnormal LFTs is meaningful.
- **Low protein intake / vegan diet** — common benign cause.
- **SIADH / overhydration** — dilutional.
- **Pregnancy** — increased GFR + plasma volume.
- **Severe malnutrition.**

### 1.5 Direction of "better"
Mid-range. Both extremes are informative; isolated low BUN with normal liver and adequate protein is benign.

### 1.6 Confounders
Hydration (huge), recent protein intake, exercise (catabolic), GI bleed, steroids, age (older = higher), muscle mass (minor).

---

## 2. Creatinine (serum)

### 2.1 What it is
Creatinine is the spontaneous, non-enzymatic dehydration product of phosphocreatine in muscle. Production rate is ~constant per unit of muscle mass (~1.5–2% of total muscle creatine pool turns over to creatinine daily). **Cleared by kidneys: ~85–90% glomerular filtration, ~10–15% proximal tubular secretion** via OCT2/MATE1 transporters. Assay: enzymatic (preferred, IDMS-traceable) or modified Jaffe.

### 2.2 Reference range & "optimal"
- **Conventional lab range, adult males:** 0.7–1.3 mg/dL (some labs 0.6–1.2, depending on reference population).
- **Optimal in a healthy young male:** ~0.8–1.1 mg/dL. A muscular 20-year-old can sit at 1.1–1.3 with completely normal kidneys; this is **physiology, not pathology** if cystatin C and urine ACR are clean.

### 2.3 High creatinine — what it means
1. **Reduced GFR** — true kidney dysfunction (acute or chronic). This is what we don't want to miss.
2. **High muscle mass** — biggest non-pathologic confounder in a 20-year-old male lifter.
3. **Creatine supplementation** — adds 0.1–0.4 mg/dL. **Always disclose to the lab/clinician.** (Section 0.1.)
4. **High meat intake before draw** — cooked meat contains performed creatinine; can raise serum Cr by 20–50% transiently for ~6 hours (Mayersohn 1983; Preiss 2007 *AJKD*). Fasting morning draw mitigates.
5. **Drugs blocking tubular secretion** — trimethoprim, cimetidine, dolutegravir, cobicistat, fenofibrate (Section 0.5). Pseudo-elevation, GFR unchanged.
6. **Rhabdomyolysis** — muscle injury releases creatine and creatinine; CK is the dominant marker but Cr can rise dramatically (BUN/Cr <10 because Cr disproportionately elevated).
7. **Dehydration / prerenal** — modest rise; BUN/Cr >20.
8. **ACEi/ARB** — expected ~10–30% bump (Section 0.4).

### 2.4 Low creatinine — what it means
- **Low muscle mass / sarcopenia / cachexia** — common in elderly, less so in 20-year-olds (would suggest eating disorder, illness).
- **Severe liver disease** — reduced creatine biosynthesis.
- **Pregnancy** — increased GFR and plasma volume.
- **Vegan diet (modest)** — less dietary creatine pool.

### 2.5 Direction of "better"
Lower is generally better **only if interpreted in context of muscle mass.** A bodybuilder at 1.2 mg/dL with normal cystatin C and ACR is healthier than a sedentary person at 0.9 with elevated ACR. Don't chase a low number for its own sake.

### 2.6 Confounders (summary)
Muscle mass, creatine supplementation, recent cooked meat, hydration, drugs (TMP, cimetidine), rhabdo, assay method (Jaffe vs enzymatic differ ~5–10%).

### 2.7 Better tests if available
- **Cystatin C (CysC):** filtered freely, not muscle-dependent; superior in athletes (Baxmann 2008 *CJASN*; Frontiers in Medicine 2022). The 2024 KDIGO guideline recommends combined eGFR-cr-cys in adults when confirmation of CKD is needed.
- **Measured GFR (mGFR)** with iohexol or iothalamate — research-grade, rarely needed.

---

## 3. BUN / Creatinine Ratio

### 3.1 What it is
Numerical ratio of BUN to serum Cr (both in mg/dL). Useful for parsing the cause of azotemia.

### 3.2 Normal range
**10–20:1** (some sources 10–15:1; LITFL CCC DDx). Mid-teens typical.

### 3.3 High ratio (>20:1) — prerenal pattern
- **Dehydration, hypovolemia** — most common cause in healthy young men (workout dehydration, GI losses, fasting before draw).
- **GI bleed** — extra protein load + prerenal volume contraction.
- **Heart failure** — reduced renal perfusion.
- **High-protein diet.**
- **Corticosteroid use.**
- **Urinary tract obstruction** (early phase).

### 3.4 Low ratio (<10:1)
- **Liver disease** (low BUN — urea production fails).
- **Low protein intake / vegan diet.**
- **SIADH** (BUN diluted, Cr less so).
- **Rhabdomyolysis** (Cr disproportionately high).
- **Pregnancy.**
- **Malnutrition.**
- **Hemodialysis** (urea is small, dialyzed efficiently).

### 3.5 Direction of "better"
A ratio in the **10–15:1 range** in a well-hydrated, normally-fed person is reassuring. Outside this range needs the matched clinical context.

### 3.6 Confounders
Hydration status at draw is dominant. A 20-year-old who fasted, didn't drink water, and lifted before the draw can easily push >20:1 without disease.

---

## 4. eGFR (CKD-EPI 2021, creatinine-based)

### 4.1 What it is
A statistical estimate of measured GFR derived from serum creatinine, age, and sex (the 2021 update **removed race**). Reported in mL/min/1.73 m².

**Equation (Inker LA et al., NEJM 2021;385:1737–1749):**

eGFRcr = 142 × min(Scr/κ, 1)^α × max(Scr/κ, 1)^−1.200 × 0.9938^Age × 1.012 [if female]

where κ = 0.9 (male) or 0.7 (female); α = −0.302 (male) or −0.241 (female); Scr in mg/dL.

The 2021 race-free equation was endorsed by the joint NKF/ASN Task Force and is the current standard for US clinical labs (NKF Lab Engagement Working Group 2021; CAP 2022).

### 4.2 Reference range & staging (KDIGO 2024)
| Stage | eGFR (mL/min/1.73 m²) | Description |
|---|---|---|
| G1 | ≥90 | Normal or high |
| G2 | 60–89 | Mildly decreased |
| G3a | 45–59 | Mild–moderate |
| G3b | 30–44 | Moderate–severe |
| G4 | 15–29 | Severely decreased |
| G5 | <15 | Kidney failure |

CKD requires the abnormality to be **present for ≥3 months** AND associated with structural/functional markers (e.g., albuminuria) — not just one low reading. KDIGO 2024 also adds a CGA staging that combines Cause + GFR (G1–G5) + Albuminuria (A1 <30, A2 30–300, A3 >300 mg/g). Color-coded risk: green/yellow/orange/red.

### 4.3 What "optimal" looks like for a 20-year-old male
- Expected eGFR-cr in a healthy 20-year-old is **>90 (often 100–130)**. The CKD-EPI equation tends to plateau / flat-line around 120 in young people regardless of true GFR, so an exact value above 90 isn't very informative — it's the trend and ACR that matter more.
- An eGFR of **60–90 in a 20-year-old male is a yellow flag** but in a muscular lifter — especially one on creatine — is most often a **false low** from elevated serum Cr. The right next step is **cystatin C** (Inker 2021 showed eGFR-cr-cys outperforms either alone; KDIGO 2024 grade 1B for CKD confirmation in equivocal cases).

### 4.4 What HIGH eGFR means
- **Hyperfiltration** (>120 in adults) is associated with very early diabetic nephropathy and obesity-related glomerulopathy. In healthy lean young men, it is mostly noise.
- May reflect undermuscled state (low Cr → high estimated GFR).

### 4.5 What LOW eGFR means
- True CKD if confirmed >3 months with kidney damage marker (ACR).
- High muscle mass with creatinine elevation (false low).
- Dehydration (transient prerenal).
- Drugs blocking Cr secretion (TMP, cimetidine).
- Recent creatine load or cooked-meat meal.

### 4.6 Direction of "better"
Higher is better, but the equation saturates ~120. In a 20-year-old, anything ≥90 with a normal ACR is fine.

### 4.7 Confounders
Same as creatinine (Section 2.6) plus the equation's own limitations: validated in adults ≥18, designed for steady-state, not accurate in AKI, less accurate at extremes of body composition.

---

## 5. Albumin / Microalbumin (urine)

### 5.1 What it is
Urinary albumin excretion measured on a spot urine sample, normalized to urinary creatinine — the **albumin-to-creatinine ratio (uACR)**, expressed in mg/g. Reflects glomerular barrier integrity and systemic endothelial health. Often the **earliest detectable marker of kidney injury**, before eGFR drops.

Assay: immunoturbidimetric or immunonephelometric albumin; Jaffe or enzymatic creatinine.

### 5.2 Reference categories (KDIGO 2024)
| Category | uACR (mg/g) | Description |
|---|---|---|
| A1 | <30 | Normal to mildly increased |
| A2 | 30–300 | Moderately increased ("microalbuminuria") |
| A3 | >300 | Severely increased ("macroalbuminuria") |

### 5.3 "Optimal" in a healthy 20-year-old male
- Within the A1 (<30) band, **lower is better and the relationship is linear / continuous**. Hemmelgarn 2010 *JAMA* (Alberta cohort, ~1M patients) showed cardiovascular and all-cause mortality climbs progressively across all uACR strata, including within "normal."
- **Healthy young-adult ACR quartiles (Inoue 2018 *Kidney Int Rep*, NHANES):** men 2.7 / 4.2 / 5.9 mg/g for the 25th/50th/75th percentiles. Rises **above the median (~4 mg/g)** in young adults independently associate with future mortality.
- **Aim:** **<10 mg/g**, ideally near or below 5 mg/g for a healthy 20-year-old male.

### 5.4 Causes of high uACR
- **Diabetic nephropathy** (earliest sign).
- **Hypertensive nephropathy.**
- **Glomerulonephritis** (IgA nephropathy is the most common in young men globally — typically presents with hematuria + proteinuria, often after URI).
- **Obesity / metabolic syndrome.**
- **Cardiovascular disease** — endothelial dysfunction marker; predicts CV events independent of GFR (Hemmelgarn 2010; AHA 2024 *J Am Heart Assoc* review).
- **Pre-eclampsia, autoimmune disease (lupus nephritis), HIV-associated nephropathy.**

### 5.5 Confounders (very important — most "isolated" elevations in young men are benign)
- **Recent vigorous exercise** — transient post-exercise proteinuria within 24–48 h. Don't draw within 24 h of a hard workout.
- **Fever / acute illness / UTI.**
- **Menstruation** (contamination).
- **Orthostatic (postural) proteinuria** — affects 2–5% of adolescents and young men. Protein excretion is normal supine but increased upright. Diagnosed by collecting a **first-morning void** (after lying down all night). If first-morning ACR is normal, the daytime "proteinuria" is benign and prognosis at 20–50 y follow-up is excellent (StatPearls *Orthostatic Proteinuria*; Robinson series, 17–24 y old men). In a young male with isolated mild proteinuria, **always do the first-morning void test** before accepting a kidney workup.
- **Dehydration** — concentrates albumin.
- **Low muscle mass / very low Cr in urine** — denominator effect; ACR overestimated when urine Cr is low (e.g., elderly, sarcopenic — *Hypertension* 2006). In young males with high muscle mass, opposite (slight underestimate).
- **High blood pressure on day of draw.**

### 5.6 Direction of "better"
Lower is better, with the caveat that the assay floor and biologic noise put a practical lower limit ~3–5 mg/g.

---

## 6. Sodium

### 6.1 What it is
Dominant extracellular cation; primary determinant of plasma osmolality. Tightly regulated by ADH/thirst (water control) and aldosterone/RAAS (Na control). Assay: ion-selective electrode (ISE) on chemistry analyzer.

### 6.2 Reference range & "optimal"
- **Lab range:** 135–145 mmol/L (some use 136–146).
- **Optimal:** mid-range, **138–142 mmol/L**.

### 6.3 High Na (hypernatremia, >145)
Almost always means **water deficit > Na deficit**, i.e., relative dehydration. Pure salt poisoning is rare.
- **Pure water loss:** insensible losses (fever, hot environment), inadequate intake (institutionalized, infants, comatose).
- **Diabetes insipidus** (central — pituitary; nephrogenic — lithium, hypercalcemia).
- **Osmotic diuresis** — uncontrolled diabetes (glucosuria), mannitol.
- **Hypotonic fluid loss** — sweating, GI losses.
- **Rare:** primary hyperaldosteronism, Cushing's, hypertonic saline iatrogenic.

### 6.4 Low Na (hyponatremia, <135) — categorize by volume status
This is the **electrolyte abnormality with the most mechanistic depth**. Verbalis 2013 algorithm: assess tonicity → urine osmolality → urine Na → ECF volume.
- **Hypovolemic hyponatremia (Na loss > water loss):** vomiting, diarrhea, diuretics (esp. thiazides), Addison's (mineralocorticoid deficiency), salt-wasting nephropathy.
- **Euvolemic hyponatremia (water excess, no Na change):**
  - **SIADH** (Schwartz–Bartter criteria: euvolemic, hypotonic, urine osm >100, urine Na >30, no adrenal/thyroid disease, no diuretic). Causes: small-cell lung cancer, CNS disease (stroke, hemorrhage, meningitis), pulmonary disease (pneumonia, TB — relevant in young adults), drugs (SSRIs, carbamazepine, oxcarbazepine, MDMA/ecstasy, cyclophosphamide), pain, nausea, post-op.
  - **Hypothyroidism** (severe).
  - **Glucocorticoid deficiency.**
  - **Primary polydipsia** — water intake exceeds renal free-water clearance (~12–15 L/day); urine osm <100. Common in psychiatric patients, occasionally in fitness culture ("must drink a gallon").
  - **Exercise-associated hyponatremia (EAH)** — well-documented and sometimes fatal. ~13% of 2002 Boston Marathon runners had Na ≤135; 0.6% had Na ≤120 (Almond 2005 *NEJM*). Driven by overdrinking + non-osmotic AVP release during prolonged exercise. Risk factors: race time >4 h, weight gain during race, fluid intake every mile, low BMI extremes, female sex. **Wilderness Medical Society 2020 update: drink to thirst, not on a fixed schedule** (AAFP 2021 summary).
- **Hypervolemic hyponatremia:** CHF, cirrhosis, nephrotic syndrome, advanced CKD — all states of effective arterial underfilling that drive ADH.

### 6.5 Direction of "better"
Mid-range. Low end of normal in a young endurance athlete is worth a second look — over-hydration is plausible.

### 6.6 Confounders
- **Pseudohyponatremia** from severe hyperlipidemia or hyperproteinemia (when measured by older indirect ISE; modern direct ISE is unaffected).
- **Translocational hyponatremia** from severe hyperglycemia (correct: add 1.6–2.4 mEq/L Na per 100 mg/dL glucose >100).
- Recent water bolus, exercise, draw timing.

---

## 7. Potassium

### 7.1 What it is
Major intracellular cation (~140 mEq/L inside cells, ~4 mEq/L in serum). The serum-cellular gradient sets resting membrane potential — small swings have outsized cardiac consequences. Regulated by aldosterone (renal excretion), insulin/β-adrenergic tone (cellular shift), and acid–base status. Assay: ISE.

### 7.2 Reference range & "optimal"
- **Lab range:** 3.5–5.0 mmol/L.
- **Optimal:** **4.0–4.5 mmol/L**. Mortality and arrhythmia data (Goyal 2012 *JAMA*; Krogager 2017 *Eur Heart J*) show U-shaped relationship — even within "normal," K <3.7 or >4.7 carries higher event rates in cardiovascular populations. Aim mid-band.

### 7.3 High K (hyperkalemia, >5.0) — first ask: real or pseudo?
**Pseudohyperkalemia is the most common cause in healthy people.** See Section 0.2. Look for:
- Lab note about hemolysis.
- Isolated K elevation, no other electrolyte issues.
- Asymptomatic, no ECG change.
- Tube was drawn with tight tourniquet, fist clenching, small needle, or sat too long.

If real:
- **Reduced excretion:** CKD, AKI, **K-sparing diuretics (spironolactone, eplerenone, amiloride), ACEi/ARB, NSAIDs, trimethoprim** (blocks ENaC).
- **Adrenal insufficiency / hypoaldosteronism / Addison's** — classically Na↓, K↑.
- **Cellular release:** rhabdomyolysis, tumor lysis, hemolysis, severe burns, massive transfusion.
- **Metabolic acidosis** — H+ moves into cells, K shifts out (~0.6 mEq/L K rise per 0.1 pH drop, varies).
- **Insulin deficiency / DKA** — both shift K extracellular (offsets total-body K depletion).
- **Non-selective β-blockers** (mild).
- **Familial periodic paralysis (hyperkalemic).**

### 7.4 Low K (hypokalemia, <3.5)
- **GI losses:** diarrhea (large volume), vomiting (more via renal mechanism — see below), laxative abuse.
- **Renal losses:** loop & thiazide diuretics, hyperaldosteronism (primary — Conn's, secondary — RAS), Cushing's, Bartter/Gitelman, RTA type 1 & 2, hypomagnesemia.
- **Cellular shift:** insulin (refeeding syndrome, DKA treatment), β-2 agonists (albuterol, epinephrine — common in asthmatics), alkalosis, **periodic paralysis (hypokalemic)**, theophylline, caffeine in large doses.
- **Inadequate intake** (rare alone — kidney is good at conserving K).
- **Hypomagnesemia → refractory hypokalemia** — Mg blocks ROMK channels in the distal nephron; without intracellular Mg, K leaks into urine continuously, and oral/IV K alone won't fix it (Huang & Kuo 2007 *J Am Soc Nephrol*; *JAMA Intern Med* "Refractory Potassium Repletion"). **Always check Mg before treating persistent hypokalemia.**

### 7.5 Direction of "better"
4.0–4.5 mmol/L is the sweet spot. Borderline-low K in a healthy 20-year-old who drinks a lot of coffee, takes a pre-workout with high caffeine, or just used albuterol is usually a benign β-2 / cellular-shift artifact.

### 7.6 Confounders
- Pseudohyperkalemia from in-vitro hemolysis (#1).
- Recent caffeine, β-2 agonist (asthma inhaler), heavy meal with insulin response.
- Severe leukocytosis or thrombocytosis can cause "reverse pseudohyperkalemia" if processed in serum (clot releases K from platelets; plasma sample resolves).
- Hours-long delay between draw and centrifugation (cold storage causes K leak from RBCs).

---

## 8. Chloride

### 8.1 What it is
Dominant extracellular anion; tracks Na in most settings. Filtered and reabsorbed by kidney; involved in acid-base via the chloride shift in RBCs and renal H+/HCO3- handling. Assay: ISE.

### 8.2 Reference range & "optimal"
- **Lab range:** 98–107 mmol/L (some labs 95–105).
- **Optimal:** mid-range, ~100–104.

### 8.3 High Cl (hyperchloremia)
- **Dehydration** (parallels hypernatremia).
- **Hyperchloremic (normal-AG) metabolic acidosis** — diarrhea (loss of HCO3, retain Cl), RTA, ureteral diversion, large-volume normal-saline infusion (Cl 154 mEq/L >> physiologic; iatrogenic acidosis well-documented — *PMC* 1550953).
- **Saline-related dilutional acidosis.**
- Resolving DKA with Cl-rich fluids.

### 8.4 Low Cl (hypochloremia)
- **Vomiting / NG suction** — gastric secretions are HCl-rich; loss → hypochloremic metabolic alkalosis.
- **Diuretics** (loop, thiazide).
- **CHF, SIADH** — dilutional, parallels low Na.
- **Mineralocorticoid excess** (hyperaldosteronism — Cl wasting + alkalosis).
- **Cystic fibrosis** (sweat — but serum Cl typically normal).

### 8.5 Direction of "better"
Mid-range. Used mostly as input for anion gap.

### 8.6 Confounders
- Bromide and other halides falsely raise Cl on some assays (rare, mostly historical).
- Recent IV fluid resuscitation with normal saline.

---

## 9. Bicarbonate / Carbon Dioxide (CO2 total)

### 9.1 What it is
"Total CO2" or "venous bicarbonate" on a chemistry panel reflects predominantly **HCO3- (~95%)** plus small amounts of dissolved CO2 and carbamino compounds. It is the **metabolic component of acid–base balance** (the renal contribution). Pair with anion gap, and ideally with arterial blood gas if abnormal.

### 9.2 Reference range & "optimal"
- **Lab range:** 22–29 mmol/L.
- **Optimal:** ~24–28.

### 9.3 High CO2 (>29) — metabolic alkalosis or compensated respiratory acidosis
- **Vomiting / NG suction** (loss of HCl).
- **Diuretics** (loop, thiazide — contraction alkalosis + K, H loss).
- **Hyperaldosteronism, Cushing's, licorice ingestion** (mineralocorticoid excess).
- **Excessive bicarbonate intake** (sodium bicarb supplements, antacid abuse).
- **COPD with chronic CO2 retention** — kidneys retain HCO3 to compensate.
- **Bartter / Gitelman syndromes.**

### 9.4 Low CO2 (<22) — metabolic acidosis or compensated respiratory alkalosis
Always **calculate anion gap** here.
- **High AG:** DKA, lactic acidosis (sepsis, ischemia, metformin in renal failure), uremia, toxic ingestion (methanol, ethylene glycol, salicylates), starvation/alcoholic ketoacidosis. (MUDPILES — Section 0.3.)
- **Normal AG:** diarrhea, RTA (types 1, 2, 4), early CKD, ureteral diversion, large-volume saline.
- **Compensated respiratory alkalosis** (chronic hyperventilation — anxiety, high altitude, pregnancy, chronic liver disease) — kidney excretes HCO3 to compensate.

### 9.5 Direction of "better"
Mid-range. Low CO2 in an asymptomatic 20-year-old is often **chronic hyperventilation** (anxiety, mouth breathing) or laboratory artifact (delayed centrifugation lets CO2 escape). A repeat draw and arterial blood gas clarify.

### 9.6 Confounders
- **Sample handling artifact** — total CO2 falls if the tube sits open: CO2 escapes from solution. Often quoted as the most common reason for a slightly low CO2 in healthy patients.
- **Tourniquet ischemia** can produce mild lactic acid release.
- Recent vomiting, intense exercise (lactate surge), high-altitude residence.

---

## 10. Calcium *(deferred — see `nutrients_vitamins_minerals.md`)*

Brief note: total Ca (8.5–10.5 mg/dL) is albumin-dependent; ionized Ca is the physiologically active fraction. PTH–vitamin D axis is the dominant regulator. Persistently high calcium → primary hyperparathyroidism, malignancy. Persistently low → vitamin D deficiency, hypoparathyroidism, severe malabsorption. Full coverage in nutrients file.

## 11. Magnesium *(deferred — see `nutrients_vitamins_minerals.md`)*

Brief note: serum Mg measures only ~1% of body Mg pool — **insensitive marker**, intracellular deficit common despite normal serum. RBC Mg or Mg-loading test more accurate. Low Mg drives refractory hypokalemia and contributes to arrhythmia. Full coverage in nutrients file.

---

## 12. Amylase

### 12.1 What it is
α-1,4-glucan hydrolase; cleaves starch. Two major isoenzymes:
- **P-type** — pancreas (~40–45% of total).
- **S-type** — salivary glands (~55–60%).
- Trace from ovary, fallopian tube, lung tumors.

Assay: enzymatic activity (substrate hydrolysis, kinetic IFCC method) on a chemistry analyzer.

### 12.2 Reference range & "optimal"
- **Lab range:** ~30–110 U/L (varies; some labs 25–125; Function Health typically reports 30–110).
- **Optimal:** mid-range. Low end is fine; very low is rarely pathologic.

### 12.3 High amylase
- **Acute pancreatitis** — classic >3× ULN within hours of onset; rises in 6–12 h, peaks 24–48 h, normalizes 3–5 d (sooner than lipase).
- **Salivary disease** — mumps, parotitis, sialadenitis, Sjögren's, salivary stones.
- **Macroamylasemia** — amylase forms complexes with IgA/IgG too large to be renally cleared. Benign. Diagnose via **amylase-to-creatinine clearance ratio (ACCR <1%)**. Important to recognize so the patient isn't worked up for pancreatitis.
- **Diabetic ketoacidosis** — salivary-type elevation, often without pancreatitis.
- **Chronic alcohol use, chronic pancreatitis (variable).**
- **Bowel infarction / mesenteric ischemia, perforated ulcer, intestinal obstruction.**
- **Ovarian cyst rupture, ectopic pregnancy** (women).
- **Renal failure** — reduced clearance; both amylase and lipase rise (Section 13.4).
- **Post-ERCP**, head trauma, post-operative.
- **Lung tumors** (rare ectopic source).

### 12.4 Low amylase
Usually not clinically significant. Possible in:
- Severe pancreatic destruction (advanced chronic pancreatitis, cystic fibrosis with exocrine insufficiency).
- Some forms of liver disease.
- **Not** a useful screening test for chronic pancreatitis on its own.

### 12.5 Direction of "better"
Mid-range. Mildly elevated isolated amylase in an asymptomatic young man is most often macroamylasemia or salivary in origin, not pancreatitis. **Lipase + clinical context resolves.**

### 12.6 Confounders
- Recent ERCP, abdominal trauma.
- Macroamylasemia (lab tip-off: high amylase, normal lipase, no symptoms).
- CKD (mild rise).
- Salivary gland inflammation from any cause (mumps, sialolith, oral surgery).
- Drugs: opiates (sphincter of Oddi spasm — usually transient), thiazides, valproate, GLP-1 agonists (semaglutide etc. — well documented).

---

## 13. Lipase

### 13.1 What it is
Pancreatic triglyceride lipase; hydrolyzes triglycerides to monoglycerides + free fatty acids. **More specific to the pancreas than amylase** (some lipases come from gastric, lingual, hepatic sources but the assay is calibrated to pancreatic). Cleared by glomerular filtration + renal tubular reabsorption/degradation.

### 13.2 Reference range & "optimal"
- **Lab range:** 0–160 U/L (varies; some labs 10–140; older adults shift higher).
- **Optimal:** mid-range; very low is rarely pathologic.

### 13.3 Atlanta 2012 acute pancreatitis criteria
Diagnosis requires **2 of 3**:
1. Abdominal pain consistent with pancreatitis.
2. **Lipase (or amylase) >3× ULN.**
3. Characteristic findings on contrast-enhanced CT, MRI, or US.

(Banks PA, Bollen TL, Dervenis C, et al. *Gut* 2013;62:102–111.)

Lipase sensitivity at ≥3× ULN: 64–100%; specificity: 87–99.4% (Ismail 2017 *Pancreatology*; *Dig Dis Sci* 2025 review).

### 13.4 High lipase
- **Acute pancreatitis** — gallstones (most common), alcohol, hypertriglyceridemia (>1000 mg/dL), drugs, ERCP, post-traumatic, autoimmune, idiopathic, viral.
- **Chronic pancreatitis** — variable; can be normal, mildly elevated, or low.
- **Pancreatic cancer.**
- **GI:** intestinal obstruction, mesenteric ischemia, perforation, peptic ulcer.
- **Renal disease** — significant. Up to ~3% of hemodialysis patients have lipase ≥2× ULN without pancreatitis (Goba Hospital cohort, *Diabetes Metab Syndr Obes* 2022). 20% of pancreatic enzymes are renally cleared.
- **DKA, ketoacidosis** (similar to amylase, sometimes mimics pancreatitis).
- **Post-ERCP** — common, expected; lipase rises in most patients after ERCP.
- **Drugs:** GLP-1 receptor agonists (semaglutide, liraglutide, tirzepatide — increasingly common in young men using off-label for body composition), thiazides, valproate, azathioprine, didanosine, sulfasalazine, statins (rare), pentamidine.
- **Idiopathic / familial benign hyperlipasemia** — described but rare.

### 13.5 Low lipase
Not typically pathologic. May be seen in:
- Advanced chronic pancreatitis with exocrine failure.
- Severe pancreatic destruction.
- Cystic fibrosis (variable).

### 13.6 Direction of "better"
Mid-range. **Isolated mild lipase elevation (<3× ULN) with no abdominal pain and no risk factors is usually NOT pancreatitis** (Hameed 2015 *HPB*; Muniraj 2015 *Dig Dis Sci*). Common alternatives in a healthy 20-year-old: post-meal, vigorous exercise, mild GI virus, GLP-1 agonist, or assay variation. Repeat fasting + clinical correlation is the right move before imaging.

### 13.7 Confounders
- Recent meal (usually minor).
- GLP-1 agonists (very common confounder in 2025–2026 — note prominently if using).
- Renal impairment.
- Recent ERCP / abdominal procedure.
- Macrolipasemia (analogous to macroamylasemia, much rarer).

---

## 14. Putting it together — interpretation patterns relevant to a 20-year-old male

| Pattern | Likely cause |
|---|---|
| BUN/Cr >20, normal Cr, mild Na elevation | Dehydration on day of draw |
| Cr 1.2–1.4, eGFR 70–85, normal ACR, lifter, on creatine | Pseudo-CKD from creatine + muscle mass — get cystatin C |
| Isolated K 5.2, no symptoms, normal ECG (if checked) | Pseudohyperkalemia (hemolysis/fist clenching) — redraw |
| Low CO2 22, no AG, normal everything | Chronic hyperventilation or sample gassing-off |
| Mild proteinuria on random urine, asymptomatic young man | Orthostatic — repeat first-morning void |
| Isolated amylase 150, lipase normal, no symptoms | Macroamylasemia or salivary; benign |
| Cr bumps 15–25% after starting ACEi | Expected hemodynamic effect, not AKI |
| Lipase 220 U/L on semaglutide, no pain | Drug effect; not pancreatitis (still flag if rising) |
| BUN 4, normal Cr, vegan, lean | Low protein intake — benign |
| Na 132 in marathon finisher | Exercise-associated hyponatremia |

## 15. Key references (numbered)
1. **Inker LA, Eneanya ND, Coresh J, et al.** New creatinine- and cystatin C–based equations to estimate GFR without race. *N Engl J Med* 2021;385:1737–1749.
2. **KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD.** *Kidney Int* 2024;105(4S):S117–S314.
3. **KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in CKD.** *Kidney Int* 2021;99(3S):S1–S87.
4. **Banks PA, Bollen TL, Dervenis C, et al.** Classification of acute pancreatitis—2012: revision of the Atlanta classification and definitions by international consensus. *Gut* 2013;62:102–111.
5. **Verbalis JG, Goldsmith SR, Greenberg A, et al.** Diagnosis, evaluation, and treatment of hyponatremia: expert panel recommendations. *Am J Med* 2013;126(10 Suppl 1):S1–S42.
6. **Hemmelgarn BR, Manns BJ, Lloyd A, et al.** Relation between kidney function, proteinuria, and adverse outcomes. *JAMA* 2010;303:423–429.
7. **Don BR, Sebastian A, Cheitlin M, et al.** Pseudohyperkalemia caused by fist clenching during phlebotomy. *N Engl J Med* 1990;322:1290–1292.
8. **Almond CSD, Shin AY, Fortescue EB, et al.** Hyponatremia among runners in the Boston Marathon. *N Engl J Med* 2005;352:1550–1556.
9. **Huang CL, Kuo E.** Mechanism of hypokalemia in magnesium deficiency. *J Am Soc Nephrol* 2007;18:2649–2652.
10. **Andreev E, Koopman M, Arisz L.** A rise in plasma creatinine that is not a sign of renal failure: which drugs can be responsible? *J Intern Med* 1999;246:247–252.
11. **Inoue K, Streja E, Tsujimoto T, et al.** Renal albumin excretion in healthy young adults and its association with mortality risk in the US population. *Kidney Int Rep* 2018.
12. **Kreider RB, Kalman DS, Antonio J, et al.** International Society of Sports Nutrition position stand: safety and efficacy of creatine supplementation in exercise, sport, and medicine. *J Int Soc Sports Nutr* 2017;14:18.
13. **Persky AM, Brazeau GA.** Clinical pharmacology of the dietary supplement creatine monohydrate. *Pharmacol Rev* 2001;53:161–176.
14. **de Souza e Silva A et al.** Effects of creatine supplementation on renal function: a systematic review and meta-analysis. *J Renal Nutrition* 2019.
15. **Wilderness Medical Society 2020 Update — Exercise-Associated Hyponatremia.** Summarized in *AAFP* 2021.
16. **NKF Laboratory Engagement Working Group.** Recommendations for implementing the CKD-EPI 2021 race-free equations. *AJKD* 2021;79:268–288.
17. **Mehta AN, Emmett JB, Emmett M.** GOLD MARK: an anion gap mnemonic for the 21st century. *Lancet* 2008;372:892.
18. **StatPearls** chapters: *Anion Gap*, *Hypokalemia*, *Hyperkalemia*, *Hyperamylasemia*, *Orthostatic Proteinuria*, *Hyperchloremic Acidosis*.
19. **Mayo Clinic Laboratories.** Top Gun Phlebotomy: Pseudohyperkalemia (2018).
20. **Frontiers in Medicine 2022.** Establishment of muscle mass-based indications for the cystatin C test in renal function evaluation.

---

*Compiled May 2026. Reference ranges drawn from current US clinical lab standards and guideline documents 2020–2025. Always interpret in clinical context; this is an interpretation reference, not medical advice.*
