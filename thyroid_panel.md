# Thyroid Panel: Comprehensive Reference for a 20-Year-Old Male

**Markers covered:** TSH, Free T4, Free T3, TPO antibodies, Thyroglobulin antibodies (TgAb).

This document is a deep reference compiled from primary literature and society guidelines (ATA, AACE/ACE, ETA, NHANES) plus widely cited "optimization" framings (Function Health, Peter Attia, Optimal DX, Paloma Health). Where mainstream endocrinology and "functional medicine" disagree, both positions are given explicitly.

---

## 0. Quick Orientation: How the System Works

The hypothalamic–pituitary–thyroid (HPT) axis is a classic three-tier negative-feedback loop:

1. **Hypothalamus** → secretes **TRH** (thyrotropin-releasing hormone) into the hypothalamo-hypophyseal portal system.
2. **Anterior pituitary** thyrotrophs → respond to TRH by secreting **TSH** (thyrotropin) into systemic circulation.
3. **Thyroid follicular cells** → respond to TSH by synthesizing thyroglobulin, organifying iodide via thyroid peroxidase (TPO), and releasing **T4** (thyroxine, ~93% of output) and **T3** (triiodothyronine, ~7% of output).
4. Circulating T4/T3 feed back negatively on **both** TRH (hypothalamus) and TSH (pituitary), with the local conversion of T4 → T3 by **type 2 deiodinase (D2)** in the pituitary itself being the dominant feedback signal. This is why TSH is so exquisitely sensitive to thyroid status — it integrates the local T3 generated inside the pituitary.

**Peripheral conversion.** Only ~20% of circulating T3 comes directly from the thyroid; ~80% is generated peripherally by **outer-ring 5'-deiodination of T4** (StatPearls / Bianco; Merck Manual). The three deiodinases:

- **D1** (liver, kidney, thyroid): produces T3 for systemic circulation; also clears rT3.
- **D2** (pituitary, brain, brown fat, skeletal muscle): produces local intracellular T3 — the key feedback signal to the pituitary, and the dominant source of nuclear-receptor-occupying T3 in many tissues.
- **D3** (placenta, fetal tissues, brain): inactivates T3 → T2 and T4 → rT3. Upregulated in non-thyroidal illness syndrome (NTIS).

All three are **selenoenzymes** containing selenocysteine; selenium adequacy is required for normal D1/D2 function. Iodine is the obvious substrate cofactor; zinc is structural in the thyroid hormone *receptor* (TR-α/β zinc fingers) rather than in the deiodinases themselves (though it is sometimes lumped with selenium in the "T4→T3 cofactor" framing in functional-medicine sources — this is partially valid for receptor function but is overstated as a conversion cofactor).

**Half-lives and dynamics:**
- T4: ~6.7 days
- T3: ~0.75–1 day
- TSH: 17–93 minutes; secreted in pulses every 2–3 hours, with a clear circadian rhythm peaking 2–4 AM and reaching nadir 4–8 PM (Roelfsema 2010; Russell 2008; Frontiers in Endocrinology 2021).

This means TSH samples drawn early morning vs. early afternoon can differ by ~25–30%; if you are tracking TSH longitudinally, **always draw at the same time of day** (ideally 7–9 AM, fasting).

---

## 1. Thyroid-Stimulating Hormone (TSH)

### 1.1 What it is

TSH is a glycoprotein heterodimer (α-subunit shared with LH/FSH/hCG, plus a β-subunit unique to TSH) secreted by anterior pituitary thyrotrophs. It binds the TSH receptor (TSHR) on thyroid follicular cells, driving iodide uptake, thyroglobulin synthesis, and T4/T3 release.

**Assay.** Modern clinical TSH measurement uses **third-generation chemiluminescent sandwich immunoassays** with functional sensitivity of ~0.01 mIU/L — sufficient to distinguish suppressed (Graves'/exogenous thyroid) from low-normal (Spectra Labs technical bulletin; Medscape 2024). First-generation assays could only reach ~1 mIU/L sensitivity and could not reliably distinguish low from low-normal; this is mostly of historical interest now but is why some older textbooks describe TSH as "less useful at the low end."

### 1.2 Physiological function

TSH is the dominant integrator of thyroid status. The classic log-linear relationship — a doubling of free T4 produces a ~100-fold drop in TSH — means TSH amplifies small free-hormone changes into a large, easy-to-measure signal. This is why TSH alone is the recommended primary screen in iodine-replete populations with intact pituitary function (AACE/ATA 2012; Garber et al., *Endocrine Practice* 2012).

### 1.3 Reference ranges (assay-dependent — read your lab's printed range)

| Range type | Value | Source |
|---|---|---|
| Conventional NHANES III–derived | **0.45–4.12 mIU/L** | Hollowell 2002, *JCEM* |
| Common lab convention | **0.4–4.5 mIU/L** | Multiple |
| Quest / LabCorp typical | 0.4 (or 0.45) – 4.5 mIU/L | Lab websites |
| AACE 2003 proposed (largely abandoned) | 0.3–3.0 mIU/L | AACE |
| Optimization framings | 0.5–2.5 mIU/L | Attia *Outlive*; Function Health; Optimal DX |
| Lowest-mortality nadir (IPD meta-analysis, 2023) | TSH 1.9–2.9 mIU/L (60th–80th percentile) | Xu et al., *Lancet Diabetes Endocrinol* 2023 |

The **upper-limit debate** is unresolved. Wartofsky and Spencer argued in 2005 that excluding antibody-positive subjects from NHANES III brings the upper 97.5th percentile down to ~2.5 mIU/L; Surks countered (Surks & Hollowell, *JCEM* 2007) that TSH distribution shifts upward with age, and applying a 2.5 cutoff would mislabel up to 35% of older adults as "subclinical hypothyroid" with no evidence of benefit. The mainstream consensus (ATA, AACE, ETA) has stayed close to ~4.0–4.5 mIU/L, with age-specific upward drift acknowledged.

### 1.4 What HIGH TSH means

| TSH (mIU/L) | Free T4 | Interpretation |
|---|---|---|
| 4.5–10 | normal | **Subclinical hypothyroidism** (most common pattern) |
| >10 | low | **Overt primary hypothyroidism** |
| Elevated | normal/elevated | **Thyroid hormone resistance (RTHβ)** — rare; THRB mutation; ~1 in 19,000–40,000 (Frontiers Endocrinol 2021); also TSH-secreting pituitary adenoma |
| Elevated | very low + symptoms | Recovery phase of thyroiditis; lab artifact (heterophile antibody, anti-streptavidin IgM) |

Most common cause in iodine-replete countries: **Hashimoto's (chronic autoimmune) thyroiditis**, with TPO antibodies positive in ~95% of cases and TgAb in ~60–80% (Caturegli 2014; StatPearls).

### 1.5 What LOW TSH means

| TSH | Free T4 / Free T3 | Interpretation |
|---|---|---|
| Suppressed (<0.1) | high FT4/FT3 | Overt **thyrotoxicosis** — Graves' (most common in young adults, ~70–80% of cases), toxic adenoma, multinodular goiter, thyroiditis (early phase), exogenous T4/T3 ingestion |
| Low (0.1–0.4) | normal | Subclinical hyperthyroidism |
| Low/normal | low FT4 | **Central hypothyroidism** — pituitary or hypothalamic disease; up to 35% of central-hypo patients have *normal-range* TSH and 5–10% are slightly elevated, because the secreted molecule is bioinactive (Persani, *Endocr Connect* 2019) |
| Low | low normal T3, normal/high rT3 | **Non-thyroidal illness syndrome (NTIS / euthyroid sick)** — present in ~75% of ICU patients (StatPearls) |
| Spurious low | spurious high FT4 | **Biotin interference** on streptavidin-biotin assays (see §6) |

In a healthy 20-year-old male, a low TSH demands investigation. The leading differential is Graves' disease (peak incidence 30–50, but plenty under 25), and the diagnostic confirmation is **TSH-receptor antibody (TRAb) or thyroid-stimulating immunoglobulin (TSI)** — note that TRAb/TSI is **NOT** in the Function Health panel. TRAb sensitivity for Graves' is ~92–96%, specificity ~96–99% (Frontiers in Endocrinology 2024; PMC10290220). If TSH is suppressed and FT4/FT3 are high, TRAb is the reflex test of choice; if TRAb is negative, consider radioactive iodine uptake scan to distinguish Graves' from thyroiditis.

### 1.6 "Better" direction — U-shaped, not linear

TSH is **not "lower is better"**. Multiple cohort analyses show a U-shaped or J-shaped association with all-cause and cardiovascular mortality:

- **Whickham 20-year follow-up** (Vanderpump 1995): incident overt hypothyroidism 4.3%/yr if TSH >2 + TPO+, vs ~0.6%/yr if TSH normal + TPO–.
- **NHANES III longitudinal** and **Thyroid Studies Collaboration IPD meta-analysis** (Xu et al., *Lancet Diabetes Endocrinol* 2023, n>134,000 across 22 cohorts): nadir of CVD and all-cause mortality at TSH **~1.9–2.9 mIU/L** (60th–80th percentile of normal range). Risk increases above and below this band.
- TSH ≥7 mIU/L: increased CHD mortality; TSH ≥10: increased CHD events (Rodondi et al., *JAMA* 2010 IPD meta-analysis).
- **Suppressed TSH** (<0.1) is associated with increased atrial fibrillation (Sawin 1994 *NEJM*), osteoporotic fractures, and all-cause mortality.

**Practical interpretation for a 20yM**: target TSH roughly 1.0–2.5 mIU/L with FT4/FT3 mid-normal. Don't chase a TSH of 0.5 — there is no mortality benefit and the lower-bound risks are real (though small at TSH 0.4–1.0).

### 1.7 Optimal range for a 20-year-old male

- **Mainstream conservative (ATA)**: anywhere within lab range (0.4–4.5) is acceptable absent symptoms or antibodies.
- **Function Health / Optimal DX / Paloma framings**: 0.5–2.5 mIU/L.
- **Attia (*Outlive*, 2023)**: prefers 0.5–2.5 mIU/L; emphasizes pairing with FT4, FT3, and (in his framing) rT3.
- **Mortality-nadir data (Xu 2023)**: ~1.9–2.9 mIU/L is empirically lowest-risk in pooled cohorts.

There is no good evidence that pushing TSH below ~1.0 in an asymptomatic euthyroid 20yM has any benefit — if anything, mortality data trends back upward in the very-low-normal band in older populations. **Mid-normal (1.0–2.5) is the defensible target.**

---

## 2. Free Thyroxine (Free T4)

### 2.1 What it is

T4 (3,5,3',5'-tetraiodothyronine) is synthesized in the thyroid follicle by iodination of tyrosine residues on thyroglobulin, catalyzed by thyroid peroxidase (TPO) using iodide and H₂O₂. ~99.97% of circulating T4 is bound to thyroxine-binding globulin (TBG, ~70%), transthyretin (~20%), and albumin (~10%); only the ~0.03% **free fraction** is biologically active. Free T4 measurement attempts to capture this active pool.

**Assays:**
- **Equilibrium dialysis (ED) ± LC-MS/MS** — gold standard, separates free hormone from binding proteins before quantification. Expensive, slow, mostly reference-lab only (Mayo Clinic Laboratories, Quest Diagnostics for FT4D).
- **Analog (one-step) immunoassay** — the typical clinical FT4 result. Convenient, automated, but susceptible to artifacts when binding proteins are abnormal (pregnancy, severe illness, drugs, dysalbuminemic hyperthyroxinemia) (Mayo Clin Lab; Clinical Chemistry 2022).
- Function Health (and most direct-to-consumer panels) use platform analog assays (Roche Cobas, Beckman, Abbott Architect) — adequate for screening healthy ambulatory adults.

### 2.2 Physiology

T4 is best understood as a **pro-hormone reservoir**. It has very low intrinsic affinity for the nuclear thyroid hormone receptor (TR) — its biological action depends almost entirely on local conversion to T3 by D1/D2 in target tissues. The 6.7-day half-life makes serum levels stable and gives T4 the "buffer" role — the body preserves T3 production by drawing on the T4 pool.

### 2.3 Reference ranges

- **Conventional**: 0.8–1.8 ng/dL (10–23 pmol/L); slight assay variation
- **Adults, lab-typical**: 0.9–1.7 ng/dL
- **Sex difference (Korean NHANES IV, 2018)**: mean FT4 in males 1.29 ± 0.003 ng/dL vs. females 1.20 ± 0.005 ng/dL — males run slightly higher (Kim et al., *PLOS One* 2018).
- **Optimization framing (Function Health, Optimal DX)**: 1.4–1.77 ng/dL (i.e., upper-mid range)

### 2.4 Interpretation matrix

| FT4 | TSH | Likely pattern |
|---|---|---|
| Low | High | Overt primary hypothyroidism |
| Low | Low or normal | Central hypothyroidism (rare); NTIS (severe/prolonged illness) |
| Low | Normal | Mild central hypo; recent levothyroxine initiation; transient |
| Normal | High | Subclinical hypothyroidism |
| Normal | Low | Subclinical hyperthyroidism; T3 toxicosis (check FT3) |
| High | Low/suppressed | Overt hyperthyroidism (Graves', toxic nodule, thyroiditis) |
| High | Normal/high | TSH-secreting adenoma; **Resistance to Thyroid Hormone β (RTHβ)**; **biotin interference** (very common artifact!); FDH (familial dysalbuminemic hyperthyroxinemia) |

### 2.5 "Better" direction

Mid-normal is the defensible target. **Low-normal FT4** has been associated with increased risk of incident depression (PMC10387582), reduced cognitive performance, and (in pregnancy) fetal neurodevelopmental concerns. **High-normal FT4** within the reference range has been associated with atrial fibrillation, bone loss, and all-cause mortality in some elderly cohorts.

For a healthy 20yM, mid-range — roughly **1.1–1.5 ng/dL** — is the practical target with no evidence to justify chasing the upper or lower end.

### 2.6 Optimal range for a 20-year-old male

- **Mainstream**: anywhere in lab range (0.8–1.8 ng/dL).
- **Function Health / Optimal DX**: 1.4–1.77 ng/dL.
- **Reasonable synthesis**: 1.1–1.5 ng/dL with TSH 1–2.5 and FT3 mid-normal — i.e., a coherent picture, not chasing any single number.

---

## 3. Free Triiodothyronine (Free T3)

### 3.1 What it is

T3 (3,5,3'-triiodothyronine) is the **biologically active** thyroid hormone — it binds nuclear TR-α and TR-β with ~10–15× higher affinity than T4. About 20% of circulating T3 comes directly from thyroid secretion; **~80% is generated peripherally** from T4 by outer-ring deiodination, predominantly by D1 (liver/kidney) and D2 (locally in target tissues).

Like T4, T3 circulates ~99.7% protein-bound; ~0.3% is the free, active fraction. Free T3 is measured by analog immunoassay or, less commonly, equilibrium dialysis.

### 3.2 Reference ranges

- **Adults**: 2.3–4.1 pg/mL (Cleveland Clinic), or 2.0–4.4 pg/mL (lab-typical, e.g., LabCorp, Quest); units sometimes given in pmol/L (3.5–6.5 pmol/L).
- **Optimization framing**: 3.2–4.4 pg/mL (Optimal DX); 3.8–4.4 (Function Health framing per Paloma/Optimal DX).

### 3.3 Why FT3 is informative even though TSH "covers it"

In iodine-replete healthy outpatients with intact pituitary function, TSH is tightly correlated with intracellular pituitary T3 and is generally a sufficient screen — this is the AACE/ATA 2012 position. But FT3 adds information in specific scenarios:

1. **T3-predominant thyrotoxicosis** ("T3 toxicosis"): suppressed TSH with normal FT4 and elevated FT3 — seen in ~5% of Graves', more in toxic nodules and iodine-deficient regions.
2. **NTIS / fasting / chronic illness**: low FT3 is the earliest finding (selective D1 downregulation, D3 upregulation). FT4 and TSH may be normal initially.
3. **Conversion concerns**: in patients on T4 monotherapy, ~10–15% have low-normal FT3 despite normal FT4 and TSH and report persistent hypothyroid symptoms — the basis of the long-running T4-monotherapy vs T4+T3 combination debate (Bianco; Attia *Drive* podcast #373 with Bianco; Jonklaas et al., *Thyroid* 2014 ATA guidelines).
4. **Selenium / iodine / chronic stress**: severe selenium deficiency can impair D1 activity and lower T3.

### 3.4 The Free T3 / Reverse T3 framework — what to know

**Reverse T3 (rT3, 3,3',5'-T3)** is the "wrong" deiodination product: D3 removes the inner-ring iodine of T4 to make rT3, an inactive metabolite. rT3 has hundreds-fold lower affinity for TR than T3.

- **Functional medicine framing** (Westin Childs / Optimal DX / Rupa Health): a free T3 / rT3 ratio >20 (with FT3 in pg/mL and rT3 in ng/dL) is "optimal." Low ratios are interpreted as evidence of "T4-pooling" or impaired conversion driven by stress, fasting, illness, low selenium, or iron deficiency.
- **ATA / mainstream endocrinology position**: rT3 testing is **not recommended**. The 2014 ATA hypothyroidism treatment guidelines (Jonklaas et al., *Thyroid* 2014) and subsequent commentary (Halsall & Oddy, *Annals of Clinical Biochemistry* 2021) state that "evidence that the analysis of serum rT3 concentration can aid further modifications to treatment such as T3 therapy is currently lacking, and the use of rT3 in this manner cannot be recommended." rT3 *is* useful in one validated context: distinguishing NTIS (high rT3) from central hypothyroidism (low/normal rT3) in hospitalized patients.
- **Honest synthesis**: rT3 reliably increases in NTIS, fasting, glucocorticoid use, β-blocker use (propranolol inhibits D1), and severe illness. The interpretive question — does an elevated rT3 in an *ambulatory healthy* person predict future clinical events or respond to intervention? — has not been answered by RCT-quality data. Treat the FT3/rT3 framework as biologically plausible but unvalidated for healthy-population optimization.

rT3 is **NOT** in the Function Health panel by default; it's an add-on. If you have unexplained low FT3 with normal TSH/FT4 and persistent hypothyroid-like symptoms (cold intolerance, fatigue, slow recovery), a one-time rT3 to confirm whether you're in a low-FT3-high-rT3 NTIS-like state can be diagnostically informative — but the evidence base for treating it is weak.

### 3.5 Optimal range for a 20yM

- **Mainstream**: any value in lab range (2.3–4.1 pg/mL) is acceptable.
- **Function Health / Optimal DX**: 3.2–4.4 pg/mL (upper-mid).
- **Reasonable synthesis**: mid-to-upper normal (3.0–4.0 pg/mL) suggests adequate conversion. Persistently low-normal FT3 (<2.8 pg/mL) with normal TSH/FT4 warrants checking ferritin, selenium status, and considering caloric deficit / overtraining as reversible causes.

---

## 4. Thyroid Peroxidase Antibodies (TPO Ab / Anti-TPO / Anti-microsomal Ab)

### 4.1 What it is

TPO antibodies are autoantibodies (predominantly IgG, especially IgG1 and IgG4) against thyroid peroxidase, the enzyme that catalyzes iodination of tyrosines on thyroglobulin and the coupling reaction that produces T4 and T3 within the thyroid follicle. TPO is a transmembrane protein on the apical surface of thyrocytes; the immune attack against TPO is the most reliable serological marker of **autoimmune thyroid disease (AITD)**.

**Assay.** Quantitative chemiluminescent immunoassay or ELISA against recombinant TPO. Cutoffs are *not standardized across platforms* — read your lab's report:

| Lab | TPO Ab cutoff |
|---|---|
| LabCorp | <34 IU/mL |
| Quest Diagnostics | <9 IU/mL (some assays); <34 with older ICMA |
| Many platforms | <35–60 IU/mL |

Function Health uses Quest Diagnostics for most assays; check your report for the exact reference threshold.

### 4.2 What positivity means

- **Sensitive marker for Hashimoto's thyroiditis** (~90–95% sensitivity)
- **Less sensitive for Graves'** but still positive in ~60–80%
- **Background positivity in healthy population** (Hollowell 2002, NHANES III, n=17,353):
  - Overall: 11.3% ± 0.4%
  - Whites: 12.3% ± 0.5%
  - Blacks: 4.5% ± 0.3%
  - Mexican Americans: ~10–11%
  - Higher in females; rises with age
  - **In a 20yM, baseline expected positivity is ~6–8%**

### 4.3 Risk of progression to overt disease

The Whickham 20-year follow-up (Vanderpump 1995) and subsequent work establish:

- **TSH normal + TPO+**: ~2%/year incidence of overt hypothyroidism
- **TSH elevated + TPO+**: ~4–5%/year incidence
- Combined elevated TSH and TPO+ in women: 4.3%/year vs. 2.6%/year for either alone
- Adding TgAb positivity to TPO positivity roughly **doubles** the progression rate
- Among patients with positive TPO and normal TSH, ~20–30% develop overt Hashimoto's hypothyroidism within 5 years; ~80%+ progression in highest-titer subgroups (Paloma; Wentz; reflecting Vanderpump 1995 methodology)

### 4.4 Titers vs. binary positive

The titer **does** carry information beyond simple positive/negative:

- Borderline (<60 IU/mL): may reflect occult AITD, but progression rate lower; ~20% revert to negative on repeat
- Moderately elevated (60–500 IU/mL): consistent with active Hashimoto's
- Very high (>500 IU/mL): strongly associated with active autoimmune destruction; faster progression to hypothyroidism

That said, *trends* (rising or stable across years) are at least as informative as absolute titer. TPO Ab levels can also fluctuate with infection, pregnancy, and (controversially) gluten exposure / vitamin D / selenium status.

### 4.5 What to do with isolated TPO positivity, normal TSH

If you are an asymptomatic 20yM with TPO+ and TSH 1.5, FT4/FT3 normal:

- **ATA / endocrine consensus**: monitor — annual TSH; sooner if symptoms develop. No treatment indicated.
- **Functional/integrative**: investigate gluten sensitivity, vitamin D (target 40–60 ng/mL), selenium 200 μg/day (Selenium Trial in Pregnancy and Negro 2007 showed reduction in TPO Ab titers), iron, cortisol, environmental toxin load. *Note*: most of these interventions have weak or no RCT evidence for delaying progression; selenium 200 μg/day has the best evidence (modest TPO titer reduction in a few small trials, no proven effect on clinical progression).

Some autoimmunity-stratified longevity panels would also recommend baseline thyroid ultrasound if persistently positive, since Hashimoto's confers a small lifetime increase in thyroid lymphoma risk (~67-fold relative but ~0.5% absolute over decades).

### 4.6 "Optimal" range

- **Mainstream**: below the lab's positivity cutoff is reassuring; anything detectable above the cutoff warrants follow-up.
- **Functional medicine**: undetectable (≤2 IU/mL) is "optimal" — i.e., no autoimmune signal at all. Realistic for most 20yMs in a non-autoimmune family history.

---

## 5. Thyroglobulin Antibodies (TgAb / Anti-Tg)

### 5.1 What it is

TgAb is an autoantibody against thyroglobulin, the large (~660 kDa) iodinated glycoprotein that serves as the matrix and storage form of thyroid hormone within the follicular colloid. TgAb is also predominantly IgG and is measured by chemiluminescent immunoassay; cutoffs differ across platforms (LabCorp <0.9 IU/mL with one assay, <4.0 IU/mL with another).

### 5.2 Two distinct clinical contexts for TgAb

**Context A — autoimmune thyroid disease (AITD) screening** (relevant to a healthy 20yM panel):
- Less specific than TPO Ab.
- Background positivity in NHANES III: **10.4% ± 0.5%** (Hollowell 2002).
- Higher in women, increases with age; lower in Black Americans.
- **Importantly: Hollowell 2002 found that *isolated* TgAb positivity (TgAb+ / TPO–) was NOT statistically associated with current thyroid dysfunction.** TPO+ was. This is the central interpretive caveat.
- In overt Hashimoto's, TgAb+ in ~60–80%; in Graves', ~25–50%.

**Context B — surveillance after thyroidectomy for differentiated thyroid cancer** (not relevant to a healthy 20yM):
- TgAb interferes with serum thyroglobulin (Tg) measurement, causing falsely low Tg values that can mask recurrence.
- In this setting TgAb itself is monitored as a *surrogate tumor marker*; rising TgAb post-thyroidectomy is concerning.
- ATA 2015 thyroid cancer guidelines mandate that every Tg measurement include a simultaneous quantitative TgAb measurement (Spencer; Haugen et al., *Thyroid* 2016).

### 5.3 Interpretation in your context

For a 20yM in a screening panel:

- **TgAb+ alone (TPO–), normal TSH/FT4/FT3**: low specificity for clinical thyroid disease. Likely background autoimmunity; monitor annually. Consider checking TPO Ab again in 6–12 months — TPO sometimes appears later, converting "isolated TgAb+" into full Hashimoto's serology.
- **TgAb+ AND TPO+, normal TSH**: clear AITD signal; risk of progression to hypothyroidism roughly **doubles** vs. either antibody alone (~4–5%/year).
- **TgAb+ AND elevated TSH**: subclinical or overt Hashimoto's; treat if symptomatic or TSH >10.

### 5.4 Titers and trends

As with TPO, very high titers (often >100–500 IU/mL) suggest more active disease. Trends matter. TgAb titers tend to decline over years if the autoimmune process burns out (some Hashimoto's patients become "atrophic" with low TgAb but continued thyroid hypofunction).

### 5.5 "Optimal" range

- **Mainstream**: below the lab's positivity cutoff.
- **Functional medicine**: undetectable.
- **Honest synthesis**: in the absence of any other signal (normal TSH/FT4/FT3, no symptoms, no family history), an isolated low-positive TgAb in a 20yM is *probably* clinically irrelevant per Hollowell 2002, but warrants annual TSH and a TPO Ab recheck.

---

## 6. Confounders & Lab Artifacts (CRITICAL)

### 6.1 Biotin interference — by far the most common artifact

Many modern immunoassays (Roche Cobas, Beckman, Abbott Architect, Ortho — covering most clinical labs including those used by Function Health) use **streptavidin-biotin** capture chemistry. Exogenous biotin in the patient's blood saturates the streptavidin sites and produces:

| Assay type | Marker | Biotin effect |
|---|---|---|
| Sandwich (large analytes) | TSH | **Falsely LOW** |
| Competitive (small analytes) | FT4, FT3 | **Falsely HIGH** |
| Sandwich | TPO Ab, TgAb | Falsely low (can mask autoimmunity) |
| Competitive | T3, total T4 | Falsely high |

The classic "factitious Graves' disease" pattern: suppressed TSH + high FT4 + high FT3, but **clinically euthyroid** and not on thyroid replacement — this is a biotin artifact until proven otherwise (Barbesino, *Thyroid* 2016 *JCEM* case report; AACC 2017 guidance).

**Practical guidance:** stop biotin **at least 48 hours** before any thyroid panel (most sources, Mayo Clinic). For high-dose biotin (≥10 mg/day, common in MS/biotinidase therapy or "hair/skin/nails" supplements that often contain 5,000–10,000 μg = 5–10 mg), wait **72 hours** or longer (Cyprus J Med Sci 2025; AACC Academy guidance). Many multivitamins and B-complex products contain 30–300 μg biotin which can also interfere; check labels.

This is the single most likely artifact to mislead a 20yM optimizer who takes a "hair, skin, and nails" or pre-workout/B-complex supplement.

### 6.2 Time of day — TSH circadian variation

- TSH peaks 02:00–04:00, nadirs 16:00–20:00 (Russell 2008; Roelfsema 2014).
- Magnitude: ~24–30% lower at noon vs. 8 AM; can reach 65% in some individuals.
- Implication: **draw at the same time of day each test** (ideally 7–9 AM, fasting). A 9 AM TSH of 2.8 vs. a 2 PM TSH of 2.0 may reflect identical biology.
- FT4 has milder diurnal variation; FT3 follows TSH partially.

### 6.3 Acute illness, stress, fasting

- **Fasting (>24h)**: drops T3, raises rT3, TSH usually unchanged. Considered an adaptive energy-conservation response. Don't test thyroid function during a prolonged fast or strict caloric restriction.
- **Acute infection / surgery / trauma**: NTIS pattern within 24–48h.
- **Sleep deprivation**: blunts the nocturnal TSH surge; modest effect.
- **Heavy endurance training**: low-T3-syndrome–like pattern in chronically over-trained athletes (RED-S / overtraining syndrome).

### 6.4 Medications

| Drug | Effect |
|---|---|
| **Lithium** | Inhibits thyroid hormone release → hypothyroidism (~20–30% chronic users) |
| **Amiodarone** | High iodine content (37% by weight); inhibits D1 (peripheral T4→T3 conversion); causes either hypo (AIT type 1, "Wolff-Chaikoff") or hyper (AIT type 2, destructive thyroiditis); TSH rises within 48h, peaks ~10 days at ~2.7× baseline (PMC 2018; ETA 2018) |
| **Glucocorticoids** | Suppress TSH (acute), inhibit D1 (lower T3, raise rT3); high-dose prednisone is a classic NTIS mimic |
| **Dopamine / dopamine agonists** | Suppress TSH directly; common in ICU |
| **Estrogens (OCP, HRT)** | ↑ TBG → ↑ total T4/T3, free fractions usually unchanged |
| **Heparin** | In vitro liberates fatty acids → falsely high FT4 by some assays |
| **Beta-blockers (esp. propranolol)** | Inhibit D1 → mildly lower T3, raise rT3 |
| **Metformin** | Modestly lowers TSH (mechanism unclear); ~0.4 mIU/L drop in some studies |
| **Iron, calcium, PPIs, soy** | Interfere with absorption of levothyroxine (relevant if treated, not for native lab values) |
| **Tyrosine kinase inhibitors (sunitinib etc.)** | Drug-induced hypothyroidism in ~50% |
| **Iodine excess** (kelp, seaweed, povidone-iodine, contrast media) | Wolff-Chaikoff effect — transient hypothyroidism |
| **Heterophile antibodies / HAMA / anti-streptavidin IgM** | Endogenous interference; cannot be "washed out"; requires assay change or dilution studies |

### 6.5 Pregnancy / sex hormones (less relevant to your context but for completeness)

Pregnancy raises TBG, lowers free fractions, TSH suppressed in T1 by hCG cross-reactivity at TSHR — pregnancy-specific reference ranges should be used (ATA 2017 pregnancy guidelines).

---

## 7. Differential Diagnosis Cheat Sheet

| Pattern | Most likely diagnoses |
|---|---|
| ↑TSH, ↓FT4 | **Overt primary hypothyroidism** — usually Hashimoto's |
| ↑TSH, normal FT4 | **Subclinical hypothyroidism** — Hashimoto's, recovery from thyroiditis, NTIS recovery |
| ↑TSH, ↑FT4 | RTHβ; TSH-secreting adenoma; assay artifact (heterophile Ab) |
| ↓TSH, ↑FT4 ± ↑FT3 | **Overt hyperthyroidism** — Graves' (check TRAb), toxic nodule/MNG, thyroiditis, exogenous T4 |
| ↓TSH, normal FT4 | **Subclinical hyperthyroidism**; T3 toxicosis (check FT3); biotin artifact |
| ↓TSH, ↓FT4 | **Central hypothyroidism**; severe NTIS |
| Normal TSH, ↓FT4 | Mild central hypo; biotin artifact (less common); analog assay artifact |
| Normal TSH, ↓FT3, normal FT4, ↑rT3 | **NTIS**; fasting; severe stress; selenium deficiency |
| Normal TSH/FT4, +TPO ± +TgAb | **Subclinical autoimmunity** — Hashimoto's "in waiting"; ~2%/year progression |
| Suppressed TSH + high FT4 + high FT3 in clinically well person not on T4 | **Biotin interference** until proven otherwise |

---

## 8. Special Topics

### 8.1 When to treat subclinical hypothyroidism

This is one of the most-debated questions in endocrinology. Synthesizing AACE/ATA 2012 (Garber), ATA 2014 (Jonklaas), ETA 2013 (Pearce), and the Thyroid Studies Collaboration IPD meta-analyses:

| Scenario | Recommendation |
|---|---|
| TSH 4.5–10 + symptoms suggestive of hypothyroidism | Trial of levothyroxine reasonable; reassess after 6–12 weeks (ATA 2014) |
| TSH 4.5–10 + TPO Ab+ | Lower threshold for treatment; high progression risk |
| TSH 4.5–10 + cardiovascular risk factors / dyslipidemia | Consider treatment, esp. age <65 |
| TSH 4.5–10 + age <65, no symptoms, antibody negative | Watchful waiting; recheck 3–6 months |
| TSH 4.5–10 + age >65–70 | Generally do not treat; raise target TSH to 4–6 in the elderly (ATA 2014) |
| TSH 4.5–10 + age >80–85 | Avoid treatment — observational data show survival advantage with mildly elevated TSH (Cleveland Clinic J Med 2025) |
| TSH >10 (any age) | Treat, with caveats for the very old |
| Pregnancy or planning | Treat per ATA 2017 pregnancy guidelines (target TSH <2.5 in T1) |

For a 20-year-old: TSH 4.5–7 with normal FT4 and negative antibodies, asymptomatic — most endocrinologists would not treat, but would repeat in 2–3 months at the same time of day. If antibodies come back positive, the case for treatment strengthens.

### 8.2 Why both Free T4 AND Free T3 matter

Even though TSH integrates both, FT4 and FT3 add information:

- Confirms the *direction* of dysfunction when TSH is borderline.
- Identifies T3-predominant thyrotoxicosis (~5% of Graves', more with toxic nodules) — TSH suppressed, FT4 normal, FT3 high.
- Surfaces conversion problems (low-normal FT3 with normal/high FT4 in chronic illness, severe caloric restriction, or — controversially — selenium / iron / cortisol issues).
- Identifies central hypothyroidism (low FT4 with non-suppressed TSH).

For a 20yM, the value-add of FT3 in addition to TSH+FT4 is modest in the typical case (~5–10% of clinically meaningful diagnoses change when FT3 is added). It's reasonable to test once and then drop to TSH+FT4 monitoring if normal.

### 8.3 The TSH-only vs. full-panel debate

AACE/ATA 2012 explicitly endorses **TSH alone as the screening test of choice** in iodine-replete populations with intact pituitary function (Garber et al.). The full panel makes sense:

- At baseline (one-time comprehensive look)
- When TSH is abnormal (reflex FT4, FT3, antibodies)
- When pituitary dysfunction is suspected
- When biotin interference or assay artifact is suspected
- For longitudinal optimization tracking, where the *trend* across markers is informative

---

## 9. Action Plan Synthesis for a 20-Year-Old Male

**Pre-test prep:**
1. Stop biotin and any "hair, skin, and nails" / B-complex supplements **at least 72 hours** before draw.
2. Draw 7–9 AM, fasting (also matters for lipids/glucose; thyroid is less sensitive to fasting itself but co-test consistency matters).
3. Do not test during acute illness or in the first 1–2 weeks after recovery from significant illness.
4. Do not test during prolonged caloric deficit, heavy endurance overtraining, or after a multi-day fast.
5. Test at the same time of day for serial comparisons.

**Reasonable target band (synthesis of mainstream + optimization framings):**

| Marker | Conservative range | Optimization target | Notes |
|---|---|---|---|
| TSH | 0.4–4.5 mIU/L | **1.0–2.5 mIU/L** | Mortality nadir ~1.9–2.9 (Xu 2023) |
| Free T4 | 0.8–1.8 ng/dL | **1.1–1.5 ng/dL** | Mid-normal |
| Free T3 | 2.3–4.4 pg/mL | **3.0–4.0 pg/mL** | Mid-to-upper normal |
| TPO Ab | < lab cutoff | **Undetectable / lowest** | Background positivity ~6–8% in young men |
| TgAb | < lab cutoff | **Undetectable / lowest** | Isolated TgAb+ less specific than TPO+ |

**If everything is normal and antibodies are undetectable:** TSH alone every 1–3 years is reasonable for a healthy 20yM. Full panel every ~5 years to recheck antibody status.

**If antibodies are positive:** TSH + FT4 every 6–12 months; full panel + ultrasound consideration if progression evident.

**If pattern is abnormal:** confirm with a repeat draw 4–8 weeks later (and **first** rule out biotin and timing artifacts), then refer to endocrinology with FT4, FT3, TPO, TgAb, and (for low TSH) TRAb / TSI.

---

## Sources

### Primary literature
- Hollowell JG, Staehling NW, Flanders WD, et al. **Serum TSH, T(4), and thyroid antibodies in the United States population (1988 to 1994): NHANES III.** *J Clin Endocrinol Metab* 2002;87(2):489–499. — TPO 11.3%, TgAb 10.4% prevalence; race/sex breakdowns. https://academic.oup.com/jcem/article/87/2/489/2846568
- Surks MI, Hollowell JG. **Age-specific distribution of serum thyrotropin and antithyroid antibodies in the U.S. population: implications for the prevalence of subclinical hypothyroidism.** *J Clin Endocrinol Metab* 2007;92(12):4575–4582. https://academic.oup.com/jcem/article/92/12/4575/2596923
- Vanderpump MPJ, Tunbridge WMG, et al. **The incidence of thyroid disorders in the community: a twenty-year follow-up of the Whickham Survey.** *Clin Endocrinol* 1995. (Reanalysis: Razvi 2010 *J Clin Endocrinol Metab*.) https://pubmed.ncbi.nlm.nih.gov/20150579/
- Xu Y, Derakhshan A, Hysaj O, et al. **The optimal healthy ranges of thyroid function defined by the risk of cardiovascular disease and mortality: systematic review and individual participant data meta-analysis (Thyroid Studies Collaboration).** *Lancet Diabetes Endocrinol* 2023;11(10):743–754. — Mortality nadir TSH 1.9–2.9 mIU/L. https://pmc.ncbi.nlm.nih.gov/articles/PMC10866328/
- Rodondi N, et al. Subclinical hypothyroidism and CHD events/mortality IPD meta-analysis. *JAMA* 2010.
- Sawin CT, Geller A, Wolf PA, et al. **Low serum thyrotropin concentrations as a risk factor for atrial fibrillation in older persons.** *N Engl J Med* 1994;331:1249–1252.

### Guidelines
- Garber JR, Cobin RH, Gharib H, et al. **Clinical Practice Guidelines for Hypothyroidism in Adults: Cosponsored by AACE and ATA.** *Endocr Pract* 2012. https://www.endocrinepractice.org/article/S1530-891X(20)43030-7/fulltext
- Jonklaas J, Bianco AC, Bauer AJ, et al. **Guidelines for the Treatment of Hypothyroidism: ATA Task Force on Thyroid Hormone Replacement.** *Thyroid* 2014;24(12):1670–1751. https://journals.sagepub.com/doi/full/10.1089/thy.2014.0028
- Pearce SHS, Brabant G, Duntas LH, et al. **2013 ETA Guideline: Management of Subclinical Hypothyroidism.** *Eur Thyroid J* 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3923601/
- Alexander EK, Pearce EN, Brent GA, et al. **2017 Guidelines of the American Thyroid Association for the Diagnosis and Management of Thyroid Disease During Pregnancy and the Postpartum.** *Thyroid* 2017;27(3):315–389. https://pubmed.ncbi.nlm.nih.gov/28056690/
- Haugen BR et al. **2015 ATA Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer.** *Thyroid* 2016. — TgAb mandatory with every Tg.
- Bartalena L et al. **2018 European Thyroid Association Guidelines for the Management of Amiodarone-Associated Thyroid Dysfunction.** *Eur Thyroid J* 2018. https://etj.bioscientifica.com/view/journals/etj/7/2/ETJ486957.xml
- **2024 ETA Guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action.** https://pmc.ncbi.nlm.nih.gov/articles/PMC11301568/

### Reviews / authoritative chapters
- Persani L et al. **The diagnosis and management of central hypothyroidism in 2018.** *Endocr Connect* 2019. https://ec.bioscientifica.com/view/journals/ec/8/2/EC-18-0515.xml
- Caturegli P, De Remigis A, Rose NR. **Hashimoto thyroiditis: Clinical and diagnostic criteria.** *Autoimmun Rev* 2014.
- **Euthyroid Sick Syndrome — StatPearls.** https://www.ncbi.nlm.nih.gov/books/NBK482219/
- **The Non-Thyroidal Illness Syndrome — Endotext.** https://www.ncbi.nlm.nih.gov/books/NBK285570/
- **Hashimoto Thyroiditis — StatPearls.** https://www.ncbi.nlm.nih.gov/books/NBK459262/
- **Subclinical Hypothyroidism — StatPearls.** https://www.ncbi.nlm.nih.gov/books/NBK536970/
- **Physiology of the Hypothalamic-Pituitary-Thyroid Axis — Endotext.** https://www.ncbi.nlm.nih.gov/books/NBK278958/
- Bianco AC, Salvatore D, Gereben B, et al. **Biochemistry, cellular and molecular biology, and physiological roles of the iodothyronine selenodeiodinases.** *Endocr Rev* 2002 (and updates 2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6668716/
- **Resistance to Thyroid Hormone Beta: A Focused Review** — *Front Endocrinol* 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8044682/
- Halsall DJ, Oddy S. **Clinical and laboratory aspects of 3,3′,5′-triiodothyronine (reverse T3).** *Ann Clin Biochem* 2021. https://journals.sagepub.com/doi/full/10.1177/0004563220969150
- Frontiers in Endocrinology 2024 — TRAb vs TSI in Graves'. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1487490/full
- Fitzgerald SP et al. **Within-Person Variation in Serum Thyrotropin Concentrations.** *Front Endocrinol* 2021. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2021.619568/full

### Lab artifacts / biotin
- AACC Academy. **Biotin Interference in Laboratory Tests — Guidance Document.** https://myadlm.org/science-and-research/academy-guidance/biotin-interference-in-laboratory-tests
- Barbesino G. **Misdiagnosis of Graves' Disease with Apparent Severe Hyperthyroidism in a Patient Taking Biotin Megadoses.** *Thyroid* 2016.
- Trambas C et al. **Biotin Interference in Immunoassays — review.** *PMC* 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC6963918/
- Cyprus J Med Sci 2025 — biotin interference review with washout times. https://cyprusjmedsci.com/articles/an-overview-of-biotin-interference-impact-on-immunoassays/cjms.2025.2024-71

### Optimization framings
- Attia P. **Outlive: The Science and Art of Longevity** (2023); Peter Attia Drive podcast #256 (Endocrine system) and #373 (Bianco — thyroid). https://peterattiamd.com/antoniobianco/
- Function Health public-facing biomarker pages (optimal range framing). 
- Optimal DX. **Free T3 and Free T3:Reverse T3 Ratio.** https://www.optimaldx.com/blog/free-t3-reverse-t3-ratio
- Paloma Health. **Normal Thyroid Levels.** https://www.palomahealth.com/learn/what-are-normal-thyroid-levels
- Lamkin Clinic. **TPO Antibodies / Thyroglobulin Antibodies — Optimal Levels.** https://lamkinclinic.com/tpo-antibodies/, https://lamkinclinic.com/thyroglobulin-antibodies/

### Lab reference ranges (assay-specific)
- LabCorp test catalog (006676 TPO Ab, 006685 TgAb, 010389 Free T3): https://www.labcorp.com/tests/006676/, /006685/, /010389/
- Mayo Clinic Laboratories — FRT4D (Free T4 by dialysis): https://www.mayocliniclabs.com/test-catalog/overview/8859
- Quest Diagnostics test directory.

### Provenance note
- Quantitative claims (e.g., NHANES TPO 11.3%, TSH mortality nadir 1.9–2.9, biotin washout 48–72h, NHANES TSH 0.45–4.12) are taken from the cited primary or guideline sources above and verified across multiple references where possible.
- "Optimization" ranges (Function Health, Optimal DX, Paloma, Attia) are clearly labeled as such and not endorsed by ATA/AACE/ETA — they represent reasonable practitioner consensus targets but lack the RCT evidence base of the conventional ranges.
- Where mainstream and functional-medicine views diverge (rT3, antibody "optimal = undetectable", narrow TSH targets), both positions are presented; the reader should weight them according to their own clinical context.
