# Sex Hormone & HPA Axis Panel — Reference for a 20-Year-Old Male

**Scope:** Total Testosterone, Free Testosterone, SHBG, Estradiol (E2), LH, FSH, Prolactin, DHEA-S, Morning Cortisol.

**Audience:** A healthy 20-year-old male interpreting a Function Health (LabCorp-backend) panel. The endocrine literature for males is dense with motivated noise — TRT clinics, supplement vendors, and "biohacker" framings routinely state ranges that diverge from peer-reviewed consensus. This document tries to cleanly separate Endocrine Society / AUA / JCEM-grade evidence from clinic / enthusiast framing, and to flag where claims are well-supported, where they are extrapolations, and where they are aspirational.

**Provenance tags used below:**
- **[GUIDELINE]** — Endocrine Society, AUA, Pituitary Society, NIDDK consensus.
- **[PRIMARY]** — A specific named study, with cohort and method.
- **[ENTHUSIAST]** — TRT clinic / longevity influencer framing; flagged where it diverges from guideline.
- **[MECHANISM]** — Standard physiology textbook material.

---

## 0. The HPG and HPA axes — one-page mental model

**HPG (Hypothalamic–Pituitary–Gonadal) axis** [MECHANISM]:
1. Hypothalamus secretes **GnRH** in pulses (~every 60–90 min) into the hypophyseal portal system.
2. Anterior pituitary gonadotrophs respond by secreting **LH** and **FSH**.
3. **LH** stimulates Leydig cells (testicular interstitium) to produce **testosterone** from cholesterol via the steroidogenic pathway (StAR → P450scc → 17α-hydroxylase → 17,20-lyase → 17β-HSD).
4. **FSH** stimulates Sertoli cells (seminiferous tubules) to support **spermatogenesis** and produce **inhibin B** (which feeds back negatively on FSH) and androgen-binding protein.
5. Testosterone is converted peripherally by **5α-reductase** to **DHT** (more potent androgen, dominant in skin/prostate/scalp) and by **aromatase (CYP19A1)** to **estradiol** (dominant in adipose, brain, bone).
6. Both T and E2 feed back negatively on hypothalamus and pituitary. **In men, E2 is a particularly important negative-feedback signal on LH** — this is why aromatase inhibitors raise LH and T.

**HPA (Hypothalamic–Pituitary–Adrenal) axis** [MECHANISM]:
1. Hypothalamic **CRH** + **AVP** → pituitary corticotrophs release **ACTH**.
2. ACTH → adrenal cortex zona fasciculata makes **cortisol**; zona reticularis makes **DHEA / DHEA-S** and androstenedione; zona glomerulosa makes aldosterone.
3. Cortisol feeds back on hypothalamus and pituitary.
4. Cortisol has a strong circadian rhythm (peak ~30 min post-wake = "Cortisol Awakening Response", nadir near midnight). DHEA-S has minimal diurnal variation due to its long half-life and large circulating pool.

**SHBG** is a hepatically synthesized glycoprotein that binds T (high affinity), DHT, and E2 (lower affinity) in circulation. About 40–60% of total T is SHBG-bound, ~40–55% is loosely albumin-bound, and ~1–4% is free. Only free + albumin-bound (= "bioavailable") T is generally available to tissue. SHBG production by the liver is downregulated by insulin (hence low SHBG in IR/obesity) and upregulated by thyroid hormone and estrogen.

---

## 1. Total Testosterone

### What it is
A C19 steroid synthesized primarily by Leydig cells (~95%) with a small adrenal contribution. "Total testosterone" = SHBG-bound + albumin-bound + free fractions. Reported in ng/dL (US) or nmol/L (SI; multiply ng/dL by 0.0347).

### Assay considerations
- **Gold standard:** liquid chromatography–tandem mass spectrometry (**LC-MS/MS**), CDC HoSt-standardized. This is the only method that reliably distinguishes monomeric T at low concentrations, doesn't cross-react with androgen metabolites, and is now the basis for harmonized reference ranges. ([CDC HoSt program / Travison 2017, JCEM](https://pubmed.ncbi.nlm.nih.gov/28324103/)) [PRIMARY]
- **Direct immunoassay (chemiluminescent / EIA):** acceptable for adult eugonadal males but inaccurate at low values (women, children, hypogonadal males) and prone to cross-reactivity with DHEA, androstenedione, and DHT. The Endocrine Society 2018 guideline explicitly recommends LC-MS/MS or another "accurate and reliable assay" for diagnostic testing. ([Endocrine Society 2018, JCEM 103(5):1715-44](https://pubmed.ncbi.nlm.nih.gov/29562364/)) [GUIDELINE]
- **Biotin interference:** competitive immunoassays for testosterone can return falsely **elevated** results in patients on high-dose biotin (typical hair/skin/nail supplements contain 5–20 mg, multi-thousand-fold the RDA). Documented case of a "suspected testosterone-producing tumor" workup that was actually biotin interference. Hold biotin ≥ 48 h (some say up to 2 weeks) before draw. ([AACC/ADLM Guidance Document on Biotin Interference](https://myadlm.org/science-and-research/academy-guidance/biotin-interference-in-laboratory-tests)) [GUIDELINE]

### Physiological function
Mediates virilization, libido, erectile function, lean mass / muscle protein synthesis (largely via androgen receptor and via 5α-reduction to DHT), erythropoiesis (raises hematocrit), bone mineral density (largely via aromatization to E2 — see Finkelstein 2013 below), and central effects on mood, motivation, spatial cognition.

### Conventional reference range — the Travison 2017 harmonization
The widely-adopted **264–916 ng/dL** range derives from:

> **Travison TG, Vesper HW, Orwoll E, Wu F, et al. (2017). "Harmonized Reference Ranges for Circulating Testosterone Levels in Men of Four Cohort Studies in the United States and Europe." *J Clin Endocrinol Metab* 102(4):1161–1173.** [PRIMARY]

Pooled data from 4 cohorts (Framingham Heart Study, European Male Aging Study, Osteoporotic Fractures in Men, Male Sibling Study of Osteoporosis), n = 9,054, all measurements harmonized to CDC HoSt LC-MS/MS reference. In healthy nonobese (BMI < 30) men age 19–39, the 2.5th–97.5th percentiles were **264 to 916 ng/dL** (median 531 ng/dL). LabCorp formally adopted this range on **July 17, 2017**, replacing its prior 348–1197 range; the change was driven by CDC harmonization, not a methodological change in the assay itself. ([LabCorp Q&A on testosterone reference interval changes](https://myadlm.org/cln/articles/2017/march/harmonized-normal-reference-range-for-testosterone-in-men-established)) [PRIMARY]

This matters for interpretation because: (a) the lower bound is *meaningfully lower* than older ranges, so what looked "low normal" by old ranges may now be mid-normal; (b) Quest, LabCorp, and most modern reference labs converge on 264–916 for healthy adult males; (c) older literature and TRT clinic marketing materials sometimes still cite 350–1100 ranges.

### What HIGH values indicate
- **Exogenous androgens / TRT / anabolic steroids** — by far the most common cause of supraphysiologic T in a 20-year-old. Hallmark biochemistry: **high T + suppressed LH + suppressed FSH** (because the pituitary thinks the gonads are working hard, so it stops sending signal). This pattern + small testes is essentially diagnostic. Spermatogenesis is suppressed; men typically become azoospermic within 3–6 months of TRT-dose exogenous T. ([Crosnoe 2013 / Desai 2022 review on AAS spermatogenesis suppression](https://pmc.ncbi.nlm.nih.gov/articles/PMC9243576/)) [PRIMARY]
- **Leydig cell tumor** of the testis — rare (~1% of testicular neoplasms), bimodal age distribution (prepubertal boys and 30–60). Steroid-secreting; can produce isolated T elevation, isolated estradiol elevation, or both. Often presents with painless testicular mass or gynecomastia. Workup: scrotal ultrasound; AFP/β-hCG/LDH should be normal (distinguishes from germ cell tumor). ([StatPearls – Leydig cell tumor](https://www.ncbi.nlm.nih.gov/books/NBK549800/)) [PRIMARY]
- **Congenital adrenal hyperplasia (21-OH deficiency)** — non-classical or virilizing forms can present with mildly elevated T and very elevated DHEA-S / 17-OH progesterone; rare to diagnose this de novo at age 20 but possible.
- **Familial / idiopathic** elevation within physiologic range.
- **SHBG elevation** can drive total T up while free T remains normal — see below.

### What LOW values indicate
The Endocrine Society 2018 framework partitions causes by HPG-axis location [GUIDELINE]:

**Primary hypogonadism** (testicular failure → ↑LH, ↑FSH, ↓T):
- Klinefelter syndrome (47,XXY) — most common cause; prevalence ~1/500–1/1000 males; up to 65% never diagnosed; often discovered in workup for infertility. Hallmark: **low T + markedly elevated FSH > LH** + small firm testes + azoospermia. ([StatPearls – Klinefelter syndrome](https://www.ncbi.nlm.nih.gov/books/NBK482314/)) [PRIMARY]
- Cryptorchidism, orchitis (mumps), testicular torsion / trauma, chemo / radiation, varicocele.

**Secondary (central / hypogonadotropic) hypogonadism** (pituitary or hypothalamic → ↓ or inappropriately normal LH/FSH, ↓T):
- **Functional** (most common in young men): obesity (estrogen feedback + inflammation), severe systemic illness, opioids, glucocorticoids, anabolic steroid use *or recovery*, nocturnal hypoxia/OSA, eating disorders / very low energy availability, marijuana (mixed evidence; recent dose-dependent suppression seen in OHSU primate work), severe overtraining.
- **Structural / organic:** prolactinoma (or any large pituitary adenoma compressing gonadotrophs), Kallmann syndrome (congenital GnRH deficiency + anosmia, prevalence ~1/8000 males), other forms of congenital hypogonadotropic hypogonadism, hemochromatosis (iron deposition in pituitary), traumatic brain injury, pituitary apoplexy, craniopharyngioma, sarcoidosis, hypophysitis.

**Specific lifestyle/medication causes well-documented in young men:**
- **Sleep restriction:** Leproult & Van Cauter (2011, JAMA): 10 healthy men, age ~24, sleep restricted 5 h/night × 1 week → **10–15% drop in daytime T**, with the effect concentrated in afternoon/evening hours. ([Leproult & Van Cauter 2011, JAMA 305(21):2173–4](https://pubmed.ncbi.nlm.nih.gov/21632481/)) [PRIMARY]
- **Opioid-induced hypogonadism:** ε-receptor inhibition of GnRH pulsatility → secondary hypogonadism within days–weeks of starting chronic opioids; meta-analysis confirms class effect. ([JCEM 2020 systematic review of opioids and endocrine effects](https://academic.oup.com/jcem/article/105/4/1020/5568226)) [PRIMARY]
- **Obesity:** SHBG ↓ (insulin suppresses hepatic SHBG → drops total T mathematically), and adipose aromatase ↑ (more T → E2 → more central feedback → ↓ LH → ↓ T). Bidirectional cycle. ([Lowered testosterone in male obesity: mechanisms, morbidity and management. PMC3955331](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955331/)) [PRIMARY]
- **Glucocorticoids** (oral, intra-articular, topical at high enough dose) suppress GnRH.
- **Marijuana:** evidence is mixed; older reports of suppression, more recent NHANES data showing modest *increases* with infrequent use and possible *decreases* with high-dose chronic use. ([Marijuana use and serum testosterone concentrations among U.S. males. PMC5660879](https://pmc.ncbi.nlm.nih.gov/articles/PMC5660879/)) [PRIMARY] Counsel as "probably small effect, dose-dependent, and recency-dependent."

### Diagnostic thresholds: Endocrine Society 2018 vs AUA 2018 vs Travison

| Source | Threshold for "low T" | Population basis |
|---|---|---|
| **Endocrine Society 2018 [GUIDELINE]** | Below the lower limit of the harmonized range (~264 ng/dL); requires symptoms PLUS two morning fasting confirmations. ([Bhasin et al. 2018 JCEM](https://pubmed.ncbi.nlm.nih.gov/29562364/)) | Travison 2017 cohort |
| **AUA 2018 [GUIDELINE]** | **< 300 ng/dL** as a "reasonable cutoff," again requiring symptoms + at least two early-morning measurements at the same lab using the same assay. ([Mulhall et al. 2018 J Urol](https://pubmed.ncbi.nlm.nih.gov/29601923/)) | Best-evidence consensus |
| **Travison harmonized 2.5th percentile [PRIMARY]** | 264 ng/dL | Healthy nonobese 19–39 |

**Both guidelines agree on three things [GUIDELINE]:**
1. Diagnosis of hypogonadism requires **clinical symptoms** (not just a number).
2. **Two separate morning (8–10 AM) fasting samples** — because ~30% of men with one "low" reading have a normal value on retest, due to diurnal/day-to-day variation.
3. Use a CDC-traceable accurate assay (LC-MS/MS preferred).

### Direction of "better"
**U-shaped relationship with mortality.** Yeap et al. individual-participant-data meta-analysis (2024, *Annals of Internal Medicine* and JCEM updates) of prospective cohorts with mass-spec T showed nonlinear associations: increased all-cause and CV mortality below ~213 ng/dL (7.4 nmol/L), and signs of increased risk at very high DHT. ([Yeap individual-participant meta-analysis JCEM 2024/2025](https://academic.oup.com/jcem/advance-article/doi/10.1210/clinem/dgaf622/8321888)) [PRIMARY] So both very low and very high are bad; mid-to-upper-normal is associated with the best outcomes.

For a healthy 20-year-old, **upper-half-of-normal is probably ideal** — i.e. roughly 500–900 ng/dL. The Travison median for healthy 19–39-year-olds was 531 ng/dL [PRIMARY]. There is **not** rigorous RCT evidence that a healthy young man with a T of 600 ng/dL benefits from getting to 900 ng/dL — that claim is widespread in the TRT/longevity ecosystem (Attia, Huberman, various clinics) but is largely *extrapolation* from association data and from Finkelstein's dose-response work in *suppressed* men. [ENTHUSIAST]

### Confounders & pre-test conditions
- **Time of day:** T peaks 5:30–8:00 AM, drops 25–30% by evening in young men. **Always draw before 10 AM** ([Bremner 1983 / Diver 2003](https://pubmed.ncbi.nlm.nih.gov/19088162/)). [PRIMARY]
- **Fasting:** glucose/insulin transiently lower T 10–25%; fasting morning sample is standard.
- **Recent illness, fever, surgical stress** can transiently suppress T 30–50%.
- **Acute exercise:** modest transient rise; chronic overtraining/under-fueling drops T.
- **Recent ejaculation:** small effect, generally ignored.
- **Biotin** (see above).

---

## 2. Free Testosterone

### What it is
The unbound fraction (~1–4% of total) free in plasma; together with albumin-bound (loosely bound, dissociates in capillary bed) makes up "bioavailable testosterone."

### Why measure it
SHBG variation can dissociate total from bioavailable. Examples in young men:
- High SHBG (hyperthyroid, low BMI, chronic illness, anorexia) → total T can be in mid-normal range while free T is functionally low and the patient is symptomatic.
- Low SHBG (insulin resistance, obesity, NAFLD) → total T appears low, but free T may be normal-ish; the "low T" diagnosis based on total T alone is misleading.

The Endocrine Society 2018 recommends measuring free T when total T is borderline or when SHBG is suspected to be abnormal. [GUIDELINE]

### Assay considerations — this is where most clinical interpretation goes wrong

**Methods, ranked by reliability:**

1. **Equilibrium dialysis** (gold standard). Physically separates free T from protein-bound T using a dialysis membrane, then measures the dialysate by LC-MS/MS. Slow, expensive, low-throughput. Available as a send-out at major reference labs (LabCorp 070282, Quest specialty). ([LabCorp Test 140226 / 070282](https://www.labcorp.com/tests/070282)) [PRIMARY]

2. **Calculated free T (Vermeulen equation)** — uses measured total T, SHBG, and albumin (assumed 4.3 g/dL if not measured), with empirically derived association constants (Ka,SHBG ≈ 1.0 × 10⁹ L/mol; Ka,alb ≈ 3.6 × 10⁴ L/mol). Validated in Vermeulen, Verdonck, Kaufman 1999 *JCEM* against equilibrium dialysis (r ≈ 0.92). This is the calculation **most reputable clinicians use**. ([Vermeulen 1999 JCEM 84(10):3666–72](https://academic.oup.com/jcem/article/84/10/3666/2660660)) [PRIMARY] Free online calculators exist (ISSAM); the formula slightly *over*estimates free T at extremes but is the most robust simple method.
   - Newer Fiers/Kaufman LC-MS/MS direct-equilibrium-dialysis re-derivation (2018) gave updated constants and slightly different absolute numbers but did not displace Vermeulen as the standard for clinical calculation. ([Fiers et al. 2018 JCEM 103(6):2167](https://pubmed.ncbi.nlm.nih.gov/29618085/)) [PRIMARY]

3. **Direct (analog) immunoassay** — what many panels (including some Function Health–reported "Free Testosterone (Direct)" readings) actually run. Produces results that correlate with equilibrium dialysis but with substantially different absolute numbers (often 4–5× lower). The Endocrine Society 2018 explicitly recommends *against* the direct analog method when accurate free T is required [GUIDELINE]. Useful only for tracking within-patient change with a single assay, not for diagnostic thresholds.

**Practical guidance:** if your Function Health report shows a "Free Testosterone (Direct)" with units like 9–26 pg/mL, that is the direct analog assay. For decision-making, you want either calculated free T (Vermeulen) using your measured total T + SHBG + albumin, or send-out equilibrium dialysis. The Issam ISSAM calculator (https://www.issam.ch/freetesto.htm) is the simplest way to do this yourself.

### Reference ranges (key — these depend heavily on method)

| Method | Adult male range | Source |
|---|---|---|
| **Equilibrium dialysis (LC-MS/MS)** | ~50–210 pg/mL | LabCorp 070282 / specialty refs |
| **Calculated (Vermeulen)** | ~70–235 pg/mL (2.5–97.5 percentile, age 19–40); median ~134 pg/mL | [Reference intervals JCEM 2023 (PMID 36251328)](https://pubmed.ncbi.nlm.nih.gov/36251328/) [PRIMARY] |
| **Direct immunoassay** | ~9–26 pg/mL (LabCorp); ~35–155 pg/mL (other labs) | Lab-specific; **don't compare across methods** |

Free T is approximately **2–3% of total T** when SHBG is normal.

### What HIGH free T means
Same as high total T (exogenous, tumor, idiopathic), OR low SHBG with normal total T (i.e. normal absolute T but more of it is unbound). Low SHBG by itself usually flags insulin resistance, not androgen excess — see SHBG section.

### What LOW free T means
Same causes as low total T (primary or secondary hypogonadism), OR high SHBG with normal total T (functional androgen deficiency — reasonably common in lean very-healthy or hyperthyroid young men). High SHBG can produce a "low free T with normal total T" picture — Vermeulen calculation reveals this.

### Optimal for a 20-year-old male
By the calculated/Vermeulen method, **150–250 pg/mL** is the upper half of the young-male reference range. Below ~70 pg/mL by Vermeulen is the conventional cutoff for biochemical hypogonadism in symptomatic men [GUIDELINE].

---

## 3. Sex Hormone–Binding Globulin (SHBG)

### What it is
A 90 kDa homodimeric glycoprotein synthesized by the liver. Binds T (highest affinity), DHT, and E2. Its expression is regulated by hepatic nuclear factor-4α (HNF-4α), which is suppressed by insulin and induced by thyroid hormone. SHBG can also be locally produced in testis (where it functions as androgen-binding protein, ABP).

### Why it's clinically important
SHBG is one of the **earliest and most sensitive markers of insulin resistance**. Mendelian randomization and multiple prospective cohort studies show low SHBG predicts incident type 2 diabetes and metabolic syndrome *independently* of testosterone, BMI, and other measured insulin resistance markers. ([Diabetes Care 2010 — Brand et al. — meta-analysis SHBG and metabolic syndrome](https://diabetesjournals.org/care/article/33/7/1618/39422/Association-of-Testosterone-and-Sex-Hormone)) [PRIMARY]

For a 20-year-old male without classical risk factors, an SHBG in the lowest decile is a *real* signal of likely insulin resistance / nascent metabolic syndrome and warrants a deeper metabolic workup (fasting insulin, HOMA-IR, lipid panel, possibly OGTT). It often precedes overt fasting glucose changes by years. ([Lakshman 2010 JCEM and follow-up cohort work](https://pubmed.ncbi.nlm.nih.gov/20368409/)) [PRIMARY]

### Reference range
**LabCorp adult males 20–49 yr: 16.5–55.9 nmol/L** (age 50+: 19.3–76.4 nmol/L — note that SHBG *rises* with normal aging, partially explaining why older men with the same total T have lower free T). [PRIMARY]

### What HIGH SHBG indicates
- **Hyperthyroidism** — thyroid hormone induces hepatic SHBG production. SHBG is sometimes used as a peripheral indicator of thyroid hormone action (e.g. checking thyroid hormone resistance). ([Selva 2009 J Mol Endocrinol on thyroid–SHBG mechanism](https://jme.bioscientifica.com/view/journals/jme/43/1/19.xml)) [PRIMARY]
- **Liver disease** — chronic hepatitis, cirrhosis (paradoxically — synthesis is preserved relatively well, while metabolic clearance falls and estrogenization rises).
- **Anorexia / very low BMI / low energy availability** — classic in male athletes with relative energy deficiency.
- **Hypogonadism** — both primary and secondary (less estrogen and androgen feedback to hepatocytes).
- **Anticonvulsants** (phenytoin, carbamazepine), **estrogens**, **HIV/HAART**, **aging**, **SSRIs** (modest).

### What LOW SHBG indicates
- **Insulin resistance / metabolic syndrome** (the headline clinical signal in young men).
- **Obesity / NAFLD** (mechanism: same — hyperinsulinemia + hepatic fat).
- **Hypothyroidism**.
- **Glucocorticoids**.
- **Exogenous androgens** (testosterone, anabolic steroids — they directly suppress hepatic SHBG synthesis).
- **Acromegaly / GH excess**.

### Direction of "better"
**U-shaped.** Very low (< 15 nmol/L in a young man) flags IR; very high (> 60 nmol/L in a young man) suggests hyperthyroidism, low energy availability, or hidden liver issue. The "sweet spot" for a 20-year-old male is **roughly 25–45 nmol/L**. This is the range where free T is well-buffered, IR is unlikely, and thyroid signaling is normal. [ENTHUSIAST framing — but biologically defensible based on the IR association at the low end and the symptomatic high-SHBG phenotype at the high end.]

### Conditions SHBG can help flag
- Pre-clinical insulin resistance.
- Subclinical hyper/hypothyroidism (combine with TSH/FT4).
- NAFLD risk.
- Eating disorders / RED-S in athletic males.
- Subtle exogenous androgen use (would be expected as a screening flag along with suppressed LH/FSH).

---

## 4. Estradiol (E2) — sensitive vs standard assay matters enormously

### What it is
The dominant circulating estrogen, an 18-carbon steroid produced in men by **aromatization of testosterone** by CYP19A1 (aromatase) in adipose tissue, brain, bone, and Leydig cells, plus some direct testicular E2 secretion (~20%). Healthy men have circulating E2 of ~10–40 pg/mL — about 1/5th to 1/10th the level seen in cycling premenopausal women in mid-follicular phase, and at the very low end of the range that traditional immunoassays can resolve.

### Assay considerations — critical
- **"Sensitive estradiol"** by **LC-MS/MS** (e.g. LabCorp 140244 — Estradiol, Sensitive, LC/MS) is the appropriate test for men, low-estradiol women, postmenopausal women, men on aromatase inhibitors, and pediatric patients. Reliable down to ~1 pg/mL. ([LabCorp 140244 — Estradiol, Sensitive, LC/MS](https://www.labcorp.com/tests/140244/estradiol-sensitive-lc-ms)) [PRIMARY]
- **Standard direct immunoassay E2** is reasonably accurate above ~50 pg/mL but **systematically overestimates and produces noisy results below that** — exactly the male physiologic range. ([Limitations of Direct Immunoassays for Measuring Circulating Estradiol — Cancer Epidemiol Biomarkers Prev 2010](https://aacrjournals.org/cebp/article/19/4/903/68242/)) [PRIMARY]
- This is the single biggest interpretation pitfall in male hormone panels. Many "high E2" diagnoses in TRT clinics that lead to anastrozole prescriptions are based on standard immunoassay values that are simply unreliable. **If your Function Health report does not specify "sensitive" or LC-MS/MS, the absolute value is unreliable for clinical decisions in a man.**

### Physiological function in men
- Bone: dominant regulator of bone mineral density in men. Men with aromatase deficiency or estrogen receptor mutations get severe osteoporosis despite normal/high T.
- Cardiovascular: lipid effects, endothelial function.
- Libido and erectile function: independent contribution beyond T (proven by Finkelstein 2013).
- Bone epiphyseal closure at puberty (men with aromatase deficiency keep growing).
- Negative feedback at hypothalamus on GnRH/LH (often more important than T's own feedback).

### The Finkelstein 2013 NEJM study — why E2 in men matters

> **Finkelstein JS, Lee H, Burnett-Bowie SAM, et al. (2013). "Gonadal Steroids and Body Composition, Strength, and Sexual Function in Men." *N Engl J Med* 369(11):1011–1022.** [PRIMARY]

Design: 400 healthy men age 20–50 received goserelin (suppresses endogenous gonadal steroid production), then were randomized to placebo or one of four testosterone gel doses (1.25/2.5/5/10 g/day). One cohort (n = 198) ran without anastrozole — so endogenous aromatization to E2 was preserved. The second cohort (n = 202) added anastrozole, blocking T → E2 conversion, allowing isolation of T-only vs T+E2 effects.

**Key findings:**
- **Lean mass, muscle area, strength** depended on T (independent of E2).
- **Fat accumulation** depended on **E2** — anastrozole-treated men gained substantially more fat at every T dose.
- **Sexual function** (libido, erectile function) depended on **both** T and E2 — even men with normal T saw libido decline when E2 was suppressed by anastrozole.
- Threshold T for fat accumulation onset (intact aromatization): ~300–350 ng/dL. Threshold T for lean mass / strength loss: ~200 ng/dL.

This is the single best evidence-based proof that estradiol is a critical hormone for men in its own right, and that **suppressing E2 with aromatase inhibitors in a man with normal-to-high T is a bad idea** (causes fat gain, libido loss, joint pain, and bone loss). The relationship is **U-shaped**.

### Reference range (sensitive assay, men)
LabCorp Sensitive E2 (LC/MS): **≤ 39 pg/mL** for adult men (laboratory-specific). The lab does not always publish a meaningful lower bound because the question for men is usually "is it too high" — but levels < 10 pg/mL are associated with bone loss. ([LabCorp 140244](https://www.labcorp.com/tests/140244/estradiol-sensitive-lc-ms)) [PRIMARY]

### What HIGH E2 indicates (in a man)
- **Excess aromatization:** obesity (adipose-rich aromatase), heavy alcohol use (impairs hepatic E2 clearance + induces aromatase), aging.
- **Exogenous testosterone or anabolic steroid use** — high T substrate → high E2 product (hence the use of AIs by bodybuilders).
- **Liver disease** (impaired clearance).
- **Aromatizable AAS** (notably methandrostenolone, testosterone esters).
- **Estrogen-secreting tumors:** Leydig cell tumor, Sertoli cell tumor, adrenal tumor, hCG-secreting germ cell tumor (testis or extragonadal).
- **Hyperthyroidism**, marijuana (modest).

### What LOW E2 indicates (in a man)
- **Aromatase inhibitor use** (anastrozole, letrozole, exemestane) — usually iatrogenic from a TRT clinic that's misinterpreting standard-immunoassay E2.
- **Low testosterone** (less substrate) — proportionally low.
- **Very low body fat** (less aromatase tissue) — common in lean ultra-athletes / RED-S.
- **Genetic aromatase deficiency** (rare).

Clinically: **E2 < ~20 pg/mL in a man is associated with accelerated bone loss, joint pain, low libido, worsening lipids.** [PRIMARY: Finkelstein 2013 + bone density studies — see refs.]

### Optimal for a 20-year-old male
**~20–35 pg/mL by sensitive assay** is the practical "young, lean, healthy" range. Men in the Finkelstein placebo arms (no goserelin) had baseline E2 in the high-teens to low-30s pg/mL. [ENTHUSIAST/clinical] There's no proof that 25 vs 35 pg/mL matters; the more important thing is **don't be < 20 and don't be > 40**.

---

## 5. Luteinizing Hormone (LH)

### What it is
A pituitary glycoprotein (heterodimer α + β subunits; β confers specificity, identical α to FSH/TSH/hCG). Pulsatile secretion (~every 90 min) under hypothalamic GnRH control. Half-life ~30 min. Bound to LH/CG receptors on Leydig cells → cAMP → cholesterol mobilization → testosterone synthesis.

### Reference range
Adult men: **~1.7–8.6 mIU/mL** (LabCorp). Lab-specific. Pulsatile so single random measurement has appreciable noise.

### What HIGH LH indicates
- **Primary hypogonadism / testicular failure** — Leydig cells aren't responding, so the pituitary keeps signaling harder. Causes: Klinefelter (most common; LH and FSH both up, FSH usually higher), bilateral cryptorchidism, post-orchitis, post-testicular trauma/torsion, post–chemo/radiation, anorchia.
- **GnRH analogs paradoxically:** acute administration causes a flare (LH spike), which is why GnRH agonists for prostate cancer suppress only after a transient surge.
- **Androgen receptor insensitivity / partial AIS** — high T, high LH, phenotypically male-but-undervirilized.

### What LOW LH indicates
- **Secondary (central) hypogonadism** — pituitary or hypothalamic disease/dysfunction. Same list as for low T (secondary): obesity, opioids, glucocorticoids, illness, hyperprolactinemia, prolactinoma, other pituitary mass, Kallmann, congenital HH.
- **Exogenous androgens** — LH is suppressed because the gonads' product is already high (negative feedback). This is the **single best biochemical signature of anabolic steroid use** in a young man with a normal physical exam: high T + suppressed LH + suppressed FSH + suppressed SHBG.
- **Severe hyperprolactinemia** (suppresses GnRH).

### Direction of "better"
Mid-normal range. Either elevation (primary failure) or suppression (secondary failure or exogenous) is pathologic.

### Confounders
- Pulsatility — single value can be at the trough.
- Recent acute stress slightly raises LH.
- Diurnal: small AM peak, generally less prominent than T's diurnal pattern.

---

## 6. Follicle-Stimulating Hormone (FSH)

### What it is
Glycoprotein structurally similar to LH (shared α subunit). Stimulates Sertoli cells to support spermatogenesis and inhibin B production. Half-life ~3–4 h (longer than LH). Less pulsatile-noisy than LH on a single sample.

### Reference range
Adult men: **~1.5–12.4 mIU/mL** (LabCorp). Lab-specific.

### What HIGH FSH indicates
- **Primary testicular failure with seminiferous tubule damage / Sertoli cell dysfunction.** FSH rises *more* than LH when the testicular damage is predominantly tubular (germ cell loss) because **inhibin B**, which negatively feeds back on FSH but not LH, is no longer being made.
- **Klinefelter syndrome** — markedly elevated FSH > LH. ([StatPearls Klinefelter](https://www.ncbi.nlm.nih.gov/books/NBK482314/)) [PRIMARY]
- Post-chemo/radiation, post-orchitis (especially mumps).
- Sertoli-cell-only syndrome.
- Y-chromosome microdeletions causing azoospermia.

### What LOW FSH indicates
- Same as low LH: secondary hypogonadism, exogenous androgens (FSH is actually *more deeply* suppressed by exogenous T than LH in most men), hyperprolactinemia, pituitary disease, Kallmann.

### Why FSH is especially useful clinically
- Best single marker of **spermatogenic function** — high FSH = bad sign for fertility even with normal T.
- Differentiates testicular vs hypothalamic-pituitary failure when paired with LH.
- For a 20-year-old, an isolated high FSH with normal T and normal LH is a flag for occult Sertoli cell / seminiferous tubule pathology and warrants semen analysis ± urology referral.

### Direction of "better"
Mid-normal. Same logic as LH.

---

## 7. Prolactin

### What it is
A 23 kDa polypeptide hormone secreted by anterior pituitary lactotrophs. Unique among pituitary hormones in being primarily under **tonic inhibition by hypothalamic dopamine**; everything else is stimulated by hypothalamic releasing factors. This is why **dopamine antagonists (antipsychotics, metoclopramide) raise prolactin** and **dopamine agonists (cabergoline, bromocriptine) lower it** — the most clinically important pharmacology of this hormone.

### Reference range
Adult men: **~4.0–15.2 ng/mL** (LabCorp). [PRIMARY] Most labs cap upper-normal at 15–20 ng/mL.

### What HIGH prolactin indicates
**Pathologic causes [GUIDELINE — Endocrine Society 2011 Hyperprolactinemia guideline](https://academic.oup.com/jcem/article/96/2/273/2709487):**
- **Prolactinoma** (most concerning). In men, ~60% present as macroadenomas (> 1 cm) due to delayed diagnosis; symptoms are hypogonadism (low libido, ED, fatigue from low T), headache, visual field deficits (bitemporal hemianopia from optic chiasm compression), and rarely galactorrhea.
- **Other pituitary masses with stalk effect** — anything that compresses the pituitary stalk reduces dopamine inhibition → prolactin rises. Modestly (usually < 100 ng/mL).
- **Drugs:** antipsychotics (especially risperidone, paliperidone, haloperidol), metoclopramide / domperidone, methyldopa, verapamil, opioids, SSRIs (modest), TCAs, estrogens.
- **Hypothyroidism** — high TRH cross-stimulates lactotrophs.
- **Renal failure** (impaired clearance).
- **Chronic chest wall stimulation** (post-thoracic surgery, herpes zoster).
- **PCOS** in females; not applicable here.

**Physiologic causes (transient elevations):**
- Stress (including anticipatory anxiety about a blood draw)
- Sleep / nocturnal peak (4–7 AM)
- Recent meal (small effect)
- Recent intercourse / orgasm — prolactin can rise up to **5-fold for ≥ 60 min after orgasm** and may still be modestly elevated the next day. ([Hyperprolactinemia StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537331/)) [PRIMARY]
- Nipple stimulation
- Vigorous exercise
- Seizure

### Diagnostic thresholds (Endocrine Society 2011 + Pituitary Society 2023) [GUIDELINE]
- **Mild elevation (16–~40 ng/mL):** check medications, repeat fasting, screen for hypothyroidism, and **request macroprolactin assay** if asymptomatic.
- **30–200 ng/mL:** could be drug-induced, microprolactinoma, stalk effect, or other pituitary mass. MRI usually warranted.
- **> 150–200 ng/mL:** almost always due to a prolactin-secreting tumor (prolactinoma).
- **> 500 ng/mL:** very high specificity for macroprolactinoma.
([Pituitary Society Consensus Statement 2023, Nat Rev Endocrinol](https://www.nature.com/articles/s41574-023-00886-5)) [GUIDELINE]

### The macroprolactin pitfall — critical
**Macroprolactin** is biologically inactive prolactin bound to IgG (a large complex with prolonged half-life). Standard immunoassays cannot distinguish it from monomeric (active) prolactin. **10–46% of patients with apparent hyperprolactinemia actually have macroprolactinemia, not true bioactive elevation.** ([Macroprolactin: A Frequent Cause of Misdiagnosed Hyperprolactinemia, PMC3719302](https://pmc.ncbi.nlm.nih.gov/articles/PMC3719302/)) [PRIMARY]

**Practical rule:** If your prolactin comes back mildly elevated (15–50 ng/mL) and you have **no symptoms** (no ED, no low libido, no headache, no visual changes, no galactorrhea), **request a macroprolactin (PEG precipitation) assay** before any imaging or dopamine agonist. If post-PEG recovery is < 40%, it's macroprolactinemia and requires no treatment.

### What LOW prolactin indicates
- Rare; clinically usually irrelevant in men.
- Severe hypopituitarism (would have other deficits — TSH, ACTH, gonadotropins all low).
- Dopamine agonist therapy.

### Direction of "better"
Generally **lower-end-of-normal is fine** in men. There is no established benefit of "higher prolactin" in men. **Optimal for a 20-year-old male: < 15 ng/mL** is consistent with a well-functioning HPG axis. [ENTHUSIAST/clinical]

### Confounders
- Stress of venipuncture itself can raise prolactin (Endocrine Society 2011 guideline notes excessive venipuncture stress as a confounder; one calm draw is preferred). [GUIDELINE]
- Recent orgasm (within 24 h).
- Sleep timing (rises in night, peaks 4–7 AM, declines by mid-morning).
- Nipple stimulation in the prior hours.
- Macroprolactin (above).
- Many drugs (above).

---

## 8. DHEA-Sulfate (DHEA-S)

### What it is
Sulfated form of dehydroepiandrosterone, the most abundant circulating steroid in humans. **Almost exclusively adrenal in origin** (zona reticularis), especially after age ~5 ("adrenarche"). The sulfated form has a half-life of hours (vs minutes for unsulfated DHEA), is non-pulsatile, and shows little diurnal variation — making it a stable marker of adrenal androgen output. DHEA-S itself has minimal direct hormonal activity but is a peripheral reservoir that can be desulfated and converted to androstenedione → testosterone or estradiol in target tissues.

### Reference range and age dependence — KEY point for a 20-year-old
**DHEA-S has the most dramatic age dependence of any hormone on this panel.** Production peaks in the **early 20s** and falls roughly 1–4% per year ("adrenopause"), reaching 10–20% of peak by age 70–80. ([Endotext "Adrenal Androgens and Aging"](https://www.ncbi.nlm.nih.gov/sites/books/NBK279006/)) [PRIMARY]

**A 20-year-old is at the lifetime peak.** Use age-stratified ranges, not adult-male ranges.

LabCorp adult male DHEA-S reference ranges (typical):
- 20–29 years: **211–492 µg/dL**
- 30–39 years: 110–510 µg/dL (drops with age)
- 40–49 years: 110–370 µg/dL
- 60–69 years: 30–260 µg/dL
- (Function Health reports also use age-banded ranges — confirm yours says age 19–29 or similar)

For a 20-year-old, an "age-appropriate optimal" sits in the upper portion of the 20–29 reference range — perhaps **350–500 µg/dL**, reflecting peak adrenal androgen output. [ENTHUSIAST framing for "optimal," but biologically defensible — values in the lower part of the age 20–29 range may reflect chronic stress, glucocorticoid use, or beginning adrenal insufficiency.]

### Physiological function
- Precursor for ~50% of androgens in adult males and the bulk of androgens in adult females (in females the ovary makes most circulating T directly post-puberty).
- Anti-glucocorticoid effects (functional antagonist of cortisol at multiple loci) — basis for the cortisol/DHEA-S ratio as a "stress balance" / vitality marker.
- Substrate for peripheral aromatization to estrogens.
- Receptors in CNS — neurosteroid effects on mood, cognition.

### What HIGH DHEA-S indicates
- **Adrenal tumor (DHEA-S-secreting adenoma or carcinoma)** — markedly elevated DHEA-S (often > 700 µg/dL or rising over time) is a classic flag for adrenal cortical neoplasm; prompt imaging warranted.
- **Congenital Adrenal Hyperplasia (CAH)** — classical or non-classical 21-hydroxylase deficiency causes accumulation of 17-OH progesterone, which spills into the androgen pathway and elevates DHEA, androstenedione, T. ([CAH StatPearls / GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1171/)) [PRIMARY] Confirm with morning 17-OH progesterone ± ACTH stimulation.
- **PCOS** — relevant in females, not here.
- **Exogenous DHEA supplementation** — doses of 25–200 mg/day raise DHEA-S substantially; be sure to ask about supplements, "adrenal support" products, and pro-hormones.
- **Stress / adrenal hyperplasia / Cushing's** — DHEA-S can rise modestly with ACTH-driven adrenal stimulation but is more often *low* in Cushing's because the steroidogenic pathway is shunted toward cortisol. Not a primary Cushing's marker.

### What LOW DHEA-S indicates
- **Aging** (the dominant cause; not relevant at age 20).
- **Adrenal insufficiency (Addison's, secondary AI from pituitary disease, tertiary AI from chronic exogenous glucocorticoid use)** — DHEA-S is one of the earliest markers to fall in adrenal cortical insufficiency.
- **Chronic glucocorticoid therapy** — even moderate doses (oral, inhaled, topical at sufficient potency) suppress ACTH and the adrenal androgen pathway.
- **Chronic illness, severe stress, malnutrition** — "burnout" / "adrenal fatigue" framing in functional medicine; the clinical correlate for a 20-year-old is RED-S, eating disorder, severe overtraining, or chronic underfueling.
- **Hyperprolactinemia** (modestly suppresses adrenal androgens).
- **Hypopituitarism** with low ACTH.

### Direction of "better"
**Higher-within-normal is generally considered "youthful."** Cortisol/DHEA-S ratio rising with age is associated with epigenetic age acceleration (Hannum, Horvath2, PhenoAge clocks). ([Cortisol/DHEAS and epigenetic age, Biogerontology 2025](https://link.springer.com/article/10.1007/s10522-025-10307-x)) [PRIMARY] But **DHEA supplementation in healthy young men with normal DHEA-S has no proven benefit** — the RCT in young men (Brown 2003, healthy men age 18–42, 6 months 50–200 mg/day) raised DHEA, DHEA-S, and DHT metabolites but raised concerns about androgenic effects on the prostate. ([Brown 2003 — Pharmacokinetics of DHEA in healthy young men](https://www.sciencedirect.com/science/article/pii/S0015028203030127)) [PRIMARY] DHEA supplementation has clear benefit only in *primary or secondary adrenal insufficiency*. [GUIDELINE-adjacent.]

### Specific conditions DHEA-S can flag
- Non-classical CAH (esp 21-OH deficiency) — non-trivial frequency in some populations (1/100 in Ashkenazi Jews; ~1/1000 general).
- Adrenal cortical tumor.
- Addison's disease / chronic exogenous glucocorticoid exposure.
- "Adrenal androgen deficiency" pattern in functional hypogonadism (debatable clinical entity).

### Confounders
- Age (huge — see ranges above).
- Hour of day (minimal — DHEA-S long half-life dominates).
- Recent ACTH stimulation (test, infection, surgery) raises transiently.
- DHEA supplementation (raises markedly).
- Glucocorticoid therapy (suppresses).

---

## 9. Cortisol (Morning Serum)

### What it is
Glucocorticoid synthesized in adrenal cortex zona fasciculata, secreted in pulses with strong circadian rhythm under control of pituitary ACTH (which is under control of hypothalamic CRH + AVP). Bound in circulation 80–90% to corticosteroid-binding globulin (CBG / transcortin), 5–10% to albumin, and ~5% free (the bioactive fraction). Total serum cortisol assays measure the bound + free pool.

### The diurnal rhythm — critically important for interpretation
- **Peak ~30 min after waking** (the **Cortisol Awakening Response, CAR**); typical magnitude is a 50–75% rise from waking value over 30–45 min.
- Falls steadily through the day; ~50–70% of morning value by mid-afternoon.
- Nadir near midnight (often < 5 µg/dL).
- A blood draw at 8 AM captures near-peak; at 4 PM, expect ~33–66% of the 8 AM value. ([Endocrine.com / Medscape Cortisol Reference Range overview](https://emedicine.medscape.com/article/2088826-overview)) [PRIMARY]
- Therefore **timing of draw is the single biggest confounder of cortisol interpretation** — a "low" cortisol at 2 PM may be entirely physiologic.

### Reference range
**Morning (~8 AM) serum cortisol: ~5–25 µg/dL (138–690 nmol/L).** Most commonly cited as **6.7–22.6 µg/dL** or **10–20 µg/dL** in healthy adults. ([Cleveland Clinic / Medscape / standard endocrinology references](https://emedicine.medscape.com/article/2088826-overview)) [PRIMARY]

**Clinically useful thresholds [PRIMARY/GUIDELINE]:**
- AM cortisol **> 14–15 µg/dL** essentially rules out adrenal insufficiency.
- AM cortisol **< 3 µg/dL** is highly suggestive of adrenal insufficiency.
- AM cortisol **3–14 µg/dL** with symptoms → ACTH stim test.
- After 1 mg dexamethasone (overnight DST), AM cortisol **< 1.8 µg/dL** rules out Cushing syndrome (sensitivity ~95%). ([Endocrine Society Cushing's Guideline](https://www.ncbi.nlm.nih.gov/books/NBK542317/)) [GUIDELINE]

### What HIGH cortisol indicates
- **Cushing syndrome** (pathologic hypercortisolism) — endogenous (Cushing disease = ACTH-secreting pituitary adenoma; ectopic ACTH from neuroendocrine tumors like small-cell lung; primary adrenal hypercortisolism from adrenal adenoma/carcinoma) or exogenous (most common — chronic high-dose glucocorticoid use). Screen with: 1 mg overnight DST, late-night salivary cortisol × 2, or 24-h urine free cortisol × 2. Random morning serum cortisol alone is *not* a Cushing's screening test.
- **Acute physiologic stress:** illness, surgery, severe pain, hypoglycemia, MI — all transiently elevate cortisol. A single high cortisol in an acutely ill patient is often non-specific.
- **Chronic psychological stress / depression** — modest elevations and (more importantly) flattening of the diurnal slope. ~40–60% of depressed patients have HPA axis abnormalities. ([HPA axis in depression, PMC5313380](https://pmc.ncbi.nlm.nih.gov/articles/PMC5313380/)) [PRIMARY]
- **Alcohol use disorder** — pseudo-Cushing's pattern.
- **Pregnancy** (raised CBG → raised total cortisol; free cortisol mostly preserved).
- **Severe sleep deprivation** — flattens and elevates evening cortisol.
- **Estrogen therapy / oral contraceptives** — raise CBG → raise total cortisol with normal free cortisol (relevant in women but mentioned for completeness).

### What LOW cortisol indicates
- **Primary adrenal insufficiency (Addison's disease)** — autoimmune adrenalitis (~75% in developed countries), TB / fungal adrenalitis, adrenal hemorrhage, congenital. Hallmark: low cortisol + **high ACTH** + hyponatremia/hyperkalemia. Classic clinical features: hyperpigmentation (high ACTH/MSH), salt craving, orthostatic hypotension, nausea, weight loss.
- **Secondary adrenal insufficiency** (pituitary disease — low ACTH → low cortisol; no electrolyte changes since aldosterone is preserved via renin-angiotensin).
- **Tertiary adrenal insufficiency** — hypothalamic disease OR (much more common) **chronic exogenous glucocorticoid suppression of CRH/ACTH**. Even moderate-dose oral steroids for several weeks, or long courses of inhaled / intra-articular / topical steroids, can suppress the HPA axis and produce low morning cortisol.
- **Severe hypopituitarism** (would have multiple deficits).
- **Critical illness–related corticosteroid insufficiency (CIRCI)** — relevant in ICU patients.

### Direction of "better"
**U-shaped.** Both pathologically high and pathologically low cortisol are bad. A robust **morning cortisol of ~10–20 µg/dL** with a normal diurnal decline is the marker of a healthy HPA axis. [Both endocrinology consensus and reasonable clinical interpretation; not enthusiast-specific.]

The functional medicine framing of "cortisol slope" / cortisol awakening response / DUTCH test as a "stress phenotype" tool [ENTHUSIAST] can be useful but: (a) salivary cortisol and DUTCH test results are not validated for diagnosing pathologic Cushing's or adrenal insufficiency; (b) the "adrenal fatigue" diagnosis is **not recognized by mainstream endocrinology** (Endocrine Society explicitly rejected it as a clinical entity in a 2016 statement).

For a 20-year-old healthy male with normal energy/sleep, a single AM serum cortisol in the 10–20 µg/dL range tells you: HPA axis is intact, no Addison's, no exogenous-steroid suppression. It does **not** by itself diagnose chronic stress or "burnout"; assessing those requires multiple measurements (e.g. salivary CAR + diurnal slope) or clinical context.

### Conditions cortisol can flag
- Cushing syndrome (need confirmatory testing).
- Addison's disease / primary adrenal insufficiency.
- Iatrogenic / exogenous-steroid-induced HPA suppression.
- Pituitary disease (when paired with ACTH and other anterior pituitary hormones).
- Pseudo-Cushing's: alcohol, depression, severe obesity, OSA.

### Confounders — substantial
- **Time of draw** (biggest single factor).
- Recent acute stress (psychological or physical) — venipuncture itself can transiently raise cortisol.
- Sleep deprivation, shift work, jet lag — alter the diurnal pattern.
- Estrogens (OCPs, pregnancy) — raise total cortisol via CBG; check free or use salivary.
- Infection / illness.
- Caffeine intake within 2–4 h (modest rise).
- Hypoglycemia (rises).
- Strenuous exercise within prior hour (rises).
- Glucocorticoid drugs — can suppress endogenous production for weeks after stopping.

---

## 10. Putting it all together: pattern recognition for a 20-year-old male

**Patterns and their interpretations** (assumes appropriate AM fasting draw, normal biotin status):

| Pattern | Most likely explanation |
|---|---|
| Total T low, LH low, FSH low | Secondary hypogonadism: workup obesity, opioid/cannabis/glucocorticoid use, prolactin, exogenous androgen use, severe stress / RED-S, MRI pituitary if persistent |
| Total T low, LH high, FSH high (FSH > LH) | Primary hypogonadism — **rule out Klinefelter (47,XXY) with karyotype** |
| Total T low, LH normal, FSH high | Isolated Sertoli-cell / spermatogenic dysfunction — get semen analysis, urology referral |
| Total T high, LH low, FSH low, SHBG low | **Exogenous androgen / TRT / anabolic steroid use** — pattern is essentially diagnostic |
| Total T mid-normal, **prolactin elevated**, LH/FSH normal-low | Prolactinoma or stalk effect — repeat prolactin, request macroprolactin if mild + asymptomatic, MRI pituitary if confirmed |
| Total T low/normal, **SHBG very low** | Early insulin resistance / metabolic syndrome — fasting insulin, HOMA-IR, lipid panel, HbA1c |
| Total T low, **SHBG very high** | Hyperthyroidism, anorexia / RED-S, liver disease — TSH/FT4, nutritional history |
| **DHEA-S very high** | Rule out CAH (17-OH progesterone), exogenous DHEA, adrenal tumor (imaging) |
| **DHEA-S very low** | Adrenal insufficiency (check 8 AM cortisol + ACTH), exogenous glucocorticoids, chronic illness |
| **AM cortisol < 5 µg/dL** | Highly suggestive of adrenal insufficiency or HPA suppression — ACTH stim test; check for exogenous steroid exposure |
| **AM cortisol > 25 µg/dL** | Acute stress most likely; if persistent or with symptoms, screen Cushing's (DST, late-night salivary, 24-h UFC) |
| **E2 elevated** (sensitive assay) without exogenous T | Obesity, alcohol, liver disease, occult Leydig/Sertoli tumor (rare; imaging if persistent) |
| **E2 < 15 pg/mL** (sensitive assay) without AI use | Functional hypothalamic deficiency, very low body fat, low T proportionally; address underlying cause — bone density consideration |

---

## 11. Sources cited (curated, with notes on trustability)

**Top-tier — guidelines and major studies:**
- [Bhasin S et al. (2018). Testosterone Therapy in Men with Hypogonadism: An Endocrine Society Clinical Practice Guideline. *JCEM* 103(5):1715–1744.](https://pubmed.ncbi.nlm.nih.gov/29562364/) — Authoritative diagnostic framework.
- [Mulhall JP et al. (2018). Evaluation and Management of Testosterone Deficiency: AUA Guideline. *J Urol* 200:423–432.](https://pubmed.ncbi.nlm.nih.gov/29601923/) — AUA position with 300 ng/dL cutoff.
- [Travison TG et al. (2017). Harmonized Reference Ranges for Circulating Testosterone Levels in Men of Four Cohort Studies in the United States and Europe. *JCEM* 102(4):1161–1173.](https://pubmed.ncbi.nlm.nih.gov/28324103/) — Source of the 264–916 ng/dL range.
- [Finkelstein JS et al. (2013). Gonadal Steroids and Body Composition, Strength, and Sexual Function in Men. *NEJM* 369:1011–1022.](https://www.nejm.org/doi/full/10.1056/NEJMoa1206168) — Definitive evidence for independent role of E2 in male physiology.
- [Vermeulen A et al. (1999). A Critical Evaluation of Simple Methods for the Estimation of Free Testosterone in Serum. *JCEM* 84:3666–3672.](https://academic.oup.com/jcem/article/84/10/3666/2660660) — Vermeulen calculation.
- [Melmed S et al. (2011). Diagnosis and Treatment of Hyperprolactinemia: An Endocrine Society Clinical Practice Guideline. *JCEM* 96:273–288.](https://academic.oup.com/jcem/article/96/2/273/2709487) — Prolactin/prolactinoma.
- [Petersenn S et al. (2023). Diagnosis and management of prolactin-secreting pituitary adenomas: a Pituitary Society international Consensus Statement. *Nat Rev Endocrinol*.](https://www.nature.com/articles/s41574-023-00886-5) — Updated 2023 prolactinoma consensus.
- [Leproult R, Van Cauter E (2011). Effect of 1 Week of Sleep Restriction on Testosterone Levels in Young Healthy Men. *JAMA* 305(21):2173–2174.](https://pubmed.ncbi.nlm.nih.gov/21632481/) — Definitive sleep–T study.

**Reference / mechanism:**
- [Endotext: Adrenal Androgens and Aging.](https://www.ncbi.nlm.nih.gov/sites/books/NBK279006/) — DHEA-S age trajectory.
- [StatPearls: Klinefelter syndrome.](https://www.ncbi.nlm.nih.gov/books/NBK482314/) — Primary hypogonadism reference.
- [StatPearls: Kallmann syndrome.](https://www.ncbi.nlm.nih.gov/books/NBK538210/) — Congenital HH reference.
- [StatPearls: Hyperprolactinemia.](https://www.ncbi.nlm.nih.gov/books/NBK537331/) — Physiologic and pathologic causes.
- [StatPearls: Leydig Cell Cancer of the Testis.](https://www.ncbi.nlm.nih.gov/books/NBK549800/) — Hormonally active testicular tumors.

**Assay / lab references:**
- [LabCorp 070282 — Testosterone, Free and Weakly Bound, with Total, LC/MS-MS.](https://www.labcorp.com/tests/070282) — Equilibrium dialysis send-out.
- [LabCorp 140244 — Estradiol, Sensitive, LC/MS.](https://www.labcorp.com/tests/140244/estradiol-sensitive-lc-ms) — Sensitive E2.
- [AACC/ADLM Guidance: Biotin Interference in Laboratory Tests.](https://myadlm.org/science-and-research/academy-guidance/biotin-interference-in-laboratory-tests) — Pre-analytical pitfall.

**Clinical mechanism reviews (good signal):**
- [Lowered testosterone in male obesity (PMC3955331).](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955331/) — Aromatase / SHBG mechanism.
- [Macroprolactin: A Frequent Cause of Misdiagnosed Hyperprolactinemia (PMC3719302).](https://pmc.ncbi.nlm.nih.gov/articles/PMC3719302/) — The macroprolactin pitfall.
- [Yeap BB et al. (2024/2025). Endogenous Testosterone, Testosterone Treatment, and Cardiovascular Health Outcomes in Men. *JCEM*.](https://academic.oup.com/jcem/advance-article/doi/10.1210/clinem/dgaf622/8321888) — IPD meta-analysis with non-linear / U-shaped mortality findings.

**Caveats on lower-trust sources:**
- TRT clinic websites (Defy Medical, regenxhealth, Lamkin Clinic) and longevity-influencer ranges (Function Health "optimal" tiers, Attia/Huberman framings) were used in this report only for *enthusiast-tier "optimal range"* cues and are explicitly tagged [ENTHUSIAST]. Their incentive structure rewards aggressive interpretation of borderline values. When their framing diverges from Endocrine Society / AUA / JCEM consensus, the consensus governs.

---

## 12. Quick decision rules for a 20-year-old male reading his own results

1. **Confirm time and conditions of draw.** Was it before 10 AM, fasting, no biotin in last 48 h, no recent intense exercise, not in an acute illness? If not, the panel is preliminary at best.
2. **Total T < 264 ng/dL or borderline?** Repeat AM fasting (per Endocrine Society 2018) before any further action. ~30% of "low" first reads are normal on retest.
3. **Total T high AND LH/FSH suppressed AND SHBG low?** This is the exogenous androgen pattern. There is no other common explanation in a 20-year-old without a testicular mass.
4. **Always pair Total T with SHBG** and calculate free T (Vermeulen, ISSAM calculator) before concluding anything about androgen status. A "low T" with very low SHBG often masks normal free T.
5. **Insist on sensitive E2 (LC-MS/MS).** Standard immunoassay E2 is unreliable in men. Don't treat an immunoassay E2 number as if it were precise.
6. **Mildly elevated prolactin without symptoms?** Get a macroprolactin assay before pituitary MRI. 10–46% of these are macroprolactin (clinically meaningless).
7. **Very low SHBG in a lean-appearing 20-year-old?** Flag it — it's an early IR signal independent of BMI. Get fasting insulin / HOMA-IR.
8. **AM cortisol < 5 or > 25?** Don't ignore. Low → workup adrenal insufficiency; high → check for exogenous steroid exposure or repeat for Cushing's screen.
9. **DHEA-S age-band:** at 20 you should be near peak; values in the lower part of the 20–29 range deserve a "why" — chronic stress, RED-S, glucocorticoid exposure, beginning AI.
10. **Anything outside reference range without clear explanation gets repeated** before you act on it.
