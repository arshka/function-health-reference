# Intervention Effect Sizes — Endocrine (Hormones + HPA + Thyroid)

**Scope:** Quantified intervention data for Total Testosterone, Free Testosterone, SHBG, Estradiol (E2), LH, FSH, Prolactin, DHEA-S, AM Cortisol, TSH, Free T4, Free T3, TPO Antibodies, and TgAb Antibodies. Covers lifestyle, supplements, drugs, and confounders/worseners. Biology, ranges, and clinical significance are in `hormones_male_panel.md` and `thyroid_panel.md`; this file adds only what those files omit: **how much each intervention actually moves the marker.**

---

## Evidence-grading legend

| Tag | Meaning |
|---|---|
| **[Meta]** | Systematic review / meta-analysis |
| **[RCT]** | Randomized controlled trial |
| **[Cohort]** | Prospective or retrospective observational cohort |
| **[MR]** | Mendelian randomization |
| **[Mechanism]** | Established physiology / pharmacodynamics without RCT effect data |
| **[1-Trial]** | Single small RCT; requires independent replication before acting on |

**Critical pre-read — measurement variability warnings**

- **AM serum cortisol:** within-person coefficient of variation (CVI) across days is ~50% for diurnal measurements. A single serum cortisol is unreliable for between-person or longitudinal comparisons without controlling time-of-day, sleep, and stress state. Minimum 3–5 draws on separate mornings for meaningful cortisol trending.
- **LH and FSH:** pulsatile secretion makes a single draw noisy (LH half-life ~30 min). Single values are useful for pattern classification (high/normal/low) but not for fine tracking.
- **Free T3/Free T4:** analog immunoassay platforms show platform-to-platform CV of 15–25%; never compare absolute values across labs or assay changes.
- **Prolactin:** orgasm within 24 h raises prolactin 3–5×; venipuncture stress and sleep timing confound single draws.

**Biotin interference warning (affects multiple markers)**

Modern streptavidin-biotin immunoassays (Roche Cobas, Beckman Coulter, Abbott Architect — the platforms behind most Function Health results) produce false results proportional to circulating biotin concentration. The pattern is mechanistically reproducible and dose-dependent: **sandwich assays (TSH, TPO Ab, TgAb) → falsely LOW; competitive assays (FT4, FT3, total T3/T4) → falsely HIGH.** The classic artifact — suppressed TSH + elevated FT4 + elevated FT3 in a clinically well, non-symptomatic person — is biotin interference until proven otherwise. Hair/skin/nails supplements typically contain 5,000–10,000 µg (5–10 mg) biotin. Even B-complex multivitamins (30–300 µg) may produce subtle interference on some platforms. **Hold biotin ≥ 72 h before any thyroid or hormone panel.** (AACC Guidance Document on Biotin Interference; Trambas 2020 PMC6963918; Cyprus J Med Sci 2025.)

---

## Total Testosterone

**Quick read:** Sleep, body weight, and caloric status are the highest-leverage lifestyle variables. Supplements marketed as "T-boosters" largely fail in replete healthy men; deficiency repletion (zinc, vitamin D) works only if you're genuinely deficient.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Sleep restriction → sleep debt** | 5 h/night × 1 wk vs. 8 h | Total T **−10–15%** (daytime nadir); effect concentrated 2–10 PM | 1 week | [RCT] | Leproult & Van Cauter 2011, *JAMA* 305:2173 (n=10, healthy men age ~24) | n=10; within-person crossover; effect is from sleep DEBT, not sleep augmentation above 8 h in already-rested men |
| **Weight loss via caloric deficit (obese baseline)** | Low-calorie diet; ~10 kg loss | Total T **+2.9 nmol/L (+~84 ng/dL)** per ~10 kg lost; bariatric surgery ~3× larger: +8.7 nmol/L (+~250 ng/dL) | 3–6 months | [Meta] | Grossmann & Matsumoto 2013, *Eur J Endocrinol* 168:829 (44 studies, n>1,700) | Larger gains in heavier, younger, non-diabetic men; effect partly via SHBG up + aromatase down |
| **Low-fat diet (vs. high-fat)** | Shift from high-fat to low-fat isocaloric | Total T **−0.52 SD (~60 ng/dL)** in Western men; overall pooled SMD = −0.38 | 4–12 wk | [Meta] | Whittaker & Wu 2021, *J Steroid Biochem Mol Biol* 210 (6 studies, n=206) | Heterogeneous designs; South/East Asian men showed smaller effect than European ancestry men; direction is real but magnitude uncertain |
| **Resistance training (acute)** | Single bout, high volume (multi-set, compound) | Total T acutely **+20–35%** above rest during/immediately post-exercise | 15–30 min post-exercise | [RCT/Meta] | Vingren et al. 2010, *Sports Med* 40(12):1037 (review) | Transient; **does not elevate baseline fasting T** in healthy eugonadal men even after long-term training programs |
| **High-volume endurance training (chronic)** | >80 km/wk running; "exercise-hypogonadal male condition" | Total T **−30–40%** vs. sedentary controls at rest | Months to years | [Cohort] | Hackney et al. 2003, *Eur J Appl Physiol* 88:619; Hackney 2020 PMC5988228 | Mechanism: functional suppression of HPG axis; partially confounded by energy deficiency (RED-S); not present at moderate training loads |
| **Vitamin D (in deficient men, 25OHD < 50 nmol/L)** | 3,332 IU/day × 12 months | Total T **+25%** (from ~8.6 to ~10.7 nmol/L, +~62 ng/dL) | 12 months | [1-Trial] | Pilz et al. 2011, *Horm Metab Res* 43:223 (n=54; weight-loss program; immunoassay T) | **Single trial.** Effect has NOT replicated in replete men: Lerchbaum 2017 JCEM n=100 replete men → null; Canguven 2017 n=102 mildly deficient → null. Vitamin D → T effect is real only when deficiency is genuine; do NOT extrapolate to replete men. |
| **D-Aspartic acid (DAA)** | 3 g/day | +15% in sedentary men (Topo 2009); **null** in trained men | 12 days (Topo) | [RCT] — but contradicted | Topo 2009 *Reprod Biol Endocrinol* 7:120; Melville 2017 *PLoS One* e0182630 (n=22, 6 g/day, 12 wk → no change) | **Single positive trial vs. multiple null trials in resistance-trained men.** Topo was in sedentary men, small n=23. Melville and Willoughby 2015 both null in trained men. **Do not expect effect in healthy eugonadal trained men.** |
| **Ashwagandha (KSM-66 / Shoden)** | 300–600 mg extract/day | Total T **+~15%** (Lopresti 2019: +14.7% vs. placebo) | 8–16 wk | [1-Trial] | Lopresti et al. 2019, *Am J Mens Health* 13:1557988019835985 (n=57, Shoden, 16 wk crossover; overweight men 40–70); Chauhan 2022 *Health Sci Rep* (KSM-66, +13%) | Small trials with industry-adjacent funding. Mechanism plausible (cortisol reduction → less HPG suppression). Effect likely real but small (~50–75 ng/dL). Not replicated in large independent RCT. |
| **Zinc repletion (zinc-deficient baseline only)** | 459 µmol/day (~30 mg elemental zinc) × 3–6 months | Total T **+92%** in marginally deficient elderly men (8.3 → 16.0 nmol/L; 239 → 461 ng/dL) | 3–6 months | [1-Trial] | Prasad et al. 1996, *Nutrition* 12:344 (n=9 marginally deficient elderly; n=11 zinc-depletion experiment in young men) | Dramatic effect is in **deficient** men only. Young zinc-replete men supplementing zinc see no T benefit. Zinc deficiency in a healthy 20-year-old eating varied diet is uncommon; requires serum/RBC zinc confirmation first. |
| **Boron supplementation** | 10 mg/day × 7 days | Total T **+~28%** in one cohort study | 1 wk | [1-Trial] | Naghii et al. 2011, *Integr Med Insights* 6:11 (n=8 healthy men) | **Single 8-man trial with no control arm.** Mechanistically speculative (SHBG binding modulation). Do not act on this. |
| **Tongkat ali (Eurycoma longifolia)** | 200 mg standardized extract/day | Total T: in LOH men, proportion with normal T increased from 35.5% to 90.8%; meta-analytic SMD = +1.35 (95% CI 0.57–2.14) | 4 weeks | [Meta] | Tambi et al. 2012, *Andrologia* 44:226 (n=76 LOH men); meta-analysis PMC9415500 (2022) | Studies are in **hypogonadal or aging men**; most are pilot/industry-funded trials. Evidence in healthy eugonadal young men is essentially absent. SMD of 1.35 is implausibly large for most supplements — likely driven by hypogonadal baseline effect. |
| **Tribulus terrestris** | 250–1,500 mg/day | **Null** for total T in healthy men; small T increase only in some animal models and hypogonadal clinical cases | — | [Meta] | Santos et al. 2014 *J Ethnopharmacol*; Antonio et al. 2000 *J Strength Cond Res* | **Firmly null in healthy replete men.** Often cited in T-booster marketing; evidence does not support this claim. |
| **Fenugreek extract** | 500–600 mg/day | Total T +2–4 ng/dL in some RCTs; free T +46% in one trial (Wilborn 2010) | 8–12 wk | Mixed | Wilborn 2010 *JISSN*; Wankhede 2016 *J Sport Sci Med* | High heterogeneity; industry-funded trials; the free T finding was via direct immunoassay (unreliable assay method). No strong evidence for clinically meaningful effect. |
| **Shilajit (Primavie extract)** | 250 mg twice daily | Total T **+~20%** vs. placebo (from ~448 to ~549 ng/dL) | 90 days | [1-Trial] | Pandit et al. 2016, *Andrologia* 48:570 (n=75 healthy men 45–55) | Single small trial; older men (45–55); no independent replication in younger men. |
| **Chronic opioid use** | Any long-term opioid (µ-agonists) | Total T **−50%** roughly; mean T in opioid users ~164–265 ng/dL vs. ~449 ng/dL in controls | Weeks to months | [Meta] | Bawor et al. 2015 *Drug Alcohol Depend* (17 studies, n=2,769; MD = −164.78 ng/dL); Rajagopal et al. 2020 *JCEM* 105:1020 (52 studies) | Class effect (all opioids); fentanyl, methadone, oxycodone > hydrocodone; mechanism: µ-receptor inhibition of GnRH pulsatility + hyperprolactinemia |
| **Alcohol (chronic heavy use)** | Chronic heavy drinking / AUD | Total T **−~15–25%** (free T −~10%); E2 elevated | Weeks to months | [Meta] | Santi et al. 2024 *Andrology* (21 studies, n=10,199): total T MD = −4.02 nmol/L; free T MD = −0.17 nmol/L; E2 MD = +7.65 pg/mL | Effect seen in chronic consumption, not acute single-session; conflicting evidence on moderate drinking (< 7 units/week — generally no effect). |
| **Cannabis/marijuana** | Heavy/frequent use | Dose-dependent; infrequent use → slight T increase; chronic heavy use → possible modest T decrease | Unclear | [Cohort] | Thistle et al. 2017 *Andrology* 5:833 (NHANES 2011–12, n=1,577 men); inverse time-since-last-regular-use trend in men 18–29 | Mixed data; at high doses, THC can reduce T; acute light use associated with transient increase; no large RCT; **counsel as probably small net-null at moderate use levels.** |
| **Finasteride (1 mg/day)** | DHT suppression → substrate shift | Total T **+~10–20%** (compensatory); DHT **−65–72%** serum; scalp DHT −56–64% | 4–6 wk | [RCT] | Propecia FDA clinical pharmacology NDA 20788; Kaufman 1998 *JAAD* (n=249, 42-day dose-ranging) | T rises because DHT's negative feedback is reduced; NET androgenic effect is reduced due to DHT loss; free T changes are modest and assay-dependent. |
| **Anabolic steroids / exogenous T (supra-physiologic)** | Any exogenous androgen (TRT, AAS) | Endogenous T production → **near-zero** within weeks; LH + FSH suppressed | 2–6 weeks | [Mechanism] | HPG feedback physiology; confirmed in every TRT suppression study | This is the most important "worsener" to recognize in a young man's panel (high total T + suppressed LH/FSH + low SHBG = likely exogenous). |

### Synthesis

**Highest leverage:** Sleep (10–15% per week of restriction is reversible and dose-dependent); weight loss in overweight men (most robust lifestyle effect in overweight baseline); avoiding opioids; caloric adequacy.

**Oversold — largely null in healthy eugonadal men:** D-aspartic acid (null in trained men), tribulus terrestris (null), ZMA (modest at best; only relevant if zinc/magnesium deficient), vitamin D (null in replete men), most commercial "T-booster" stacks.

**South Asian-specific note:** South Asian men have measurably lower SHBG set-points than European men (lower total T at equivalent free T); the clinical signal is in **free/bioavailable testosterone**, not total T in isolation. (McTernan 2007 PMID 17900299; Bhatt 2010 PMID 20550541.) Insulin resistance is more prevalent in SAs at lower BMI, further suppressing SHBG and total T. Do not over-diagnose "low T" from total T alone without calculating free T (Vermeulen).

**23andMe SNPs relevant to total T:** `rs6258` and `rs12150660` (SHBG locus — affect SHBG set-point and thus free:total T ratio); `CYP19A1` variants (aromatase activity — affect T→E2 conversion rate); `HSD3B2` (steroidogenesis); `CYP17A1` (adrenal/gonadal androgen synthesis — relevant if using topical ketoconazole, which inhibits CYP17A1; `CYP3A4` variants affect cortisol and androgen catabolism rate).

**Pharmacotherapy reference (scale only):**
- Testosterone cypionate 100 mg/wk IM → total T typically ~600–900 ng/dL trough; varies with injection frequency, conversion, SHBG
- Testosterone gel 5–10 g/day → total T ~400–700 ng/dL (high individual variability in absorption)
- Clomiphene (clomid) 25 mg/day → total T +~273 ng/dL (meta-analytic mean; Huijben 2022 *Andrology*); LH +4.7 IU/L; FSH +4.6 IU/L — HPG axis remains intact, fertility preserved
- Enclomiphene (pure trans-isomer) → similar or greater T rise with less estrogenic side effects; FDA rejected NDA for hypogonadism indications; used off-label

**Realistic 3–6 month best-case from suboptimal baseline (20yo lean SA male, T 320–400 ng/dL):**
Sleep to 8 h + weight maintenance + eliminate opioid/alcohol confounders + zinc/D repletion if deficient → realistic gain ~50–150 ng/dL if a modifiable cause existed. If genuinely eugonadal and healthy with no modifiable confounders, lifestyle "optimization" adds little.

---

## Free Testosterone

**Quick read:** Free T moves with the same interventions as total T, but additionally rises whenever SHBG falls (insulin resistance, obesity, exogenous androgens) and falls whenever SHBG rises (hyperthyroidism, weight loss paradox, anticonvulsants). Most "free T optimizer" claims are recycled from total T data; few studies measure free T by equilibrium dialysis.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Weight loss (obese baseline)** | Low-calorie diet; bariatric surgery | Free T: diet +19.9 pmol/L; surgery +58.0 pmol/L | 3–12 months | [Meta] | Grossmann & Matsumoto 2013 (same meta as above) | As T rises and SHBG also rises with weight loss, free T gain is proportionally smaller than total T gain |
| **Improving insulin sensitivity** | Metformin, lifestyle | SHBG rises as insulin falls → free T may paradoxically decrease slightly even as total T rises | Months | [Mechanism/Cohort] | Brand et al. 2010 *Diabetes Care* | This is the "SHBG paradox" of weight loss: total T up, SHBG up, free T net ↑ but less than total T |
| **Sleep restriction** | 5 h/night × 1 wk | Free T likely decreases proportionally to total T (~10–15%) | 1 week | [Extrapolation from RCT] | Leproult & Van Cauter 2011 (free T not separately reported) | Leproult measured total T; free T inference is based on mechanism |
| **Low-fat diet** | As above | Free T: meta-analytic reduction, pooled direction same as total T but smaller individual effect sizes reported | 4–12 wk | [Meta] | Whittaker & Wu 2021 | Fewer trials reported free T; less certain than total T estimate |
| **Finasteride** | 1 mg/day | Free T: modest rise (+5–10%) compensatory with total T rise, offset partly by SHBG changes | 4–12 wk | [Mechanism/RCT] | FDA clinical pharmacology data | Net bioavailable androgens reduced due to DHT loss dominating |
| **Exogenous androgens / AAS** | Any supra-physiologic dose | SHBG falls markedly (exogenous T directly suppresses hepatic SHBG synthesis) → free T fraction rises even more than total T | 2–8 wk | [Mechanism] | Observed in every AAS/TRT cohort study | Pattern: very high total T + very low SHBG + suppressed LH/FSH = diagnostic of exogenous use |

### Synthesis

Free T primarily tracks total T but is modified by SHBG shifts. Key message: **always compute free T (Vermeulen) before concluding low T in a lean SA man**; his total T may be at the lower normal limit while free T is adequate because SHBG is also low. The ISSAM online calculator (issam.ch/freetesto.htm) is the standard tool.

**Pharmacotherapy:**
- Anastrozole 0.5 mg 2–3×/wk → E2 −50%; free T up ~15–20% (via reduced negative E2 feedback on LH → increased LH → more T); used off-label in TRT protocols to manage E2
- **Caution:** AI over-suppression → E2 < 15 pg/mL → fat gain, joint pain, low libido, bone loss (Finkelstein 2013 NEJM proof-of-concept)

---

## SHBG

**Quick read:** SHBG is tightly regulated by insulin and thyroid hormone. The biggest movers are metabolic state (insulin resistance → SHBG down) and thyroid status (hyperthyroid → SHBG up, hypothyroid → SHBG down). Most supplement claims for SHBG modulation are secondary effects of T changes, not direct.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Weight loss / improved insulin sensitivity** | 10 kg weight loss in obese men | SHBG **+5–10 nmol/L** (rises as insulin falls) | 3–6 months | [Meta/Cohort] | Various weight-loss RCTs; Grossmann 2013 review | Paradox: SHBG rising after weight loss partially offsets free T gain |
| **Caloric restriction / fasting** | Severe caloric restriction (eating disorder, extreme cut) | SHBG **↑** (hepatic synthesis upregulated with low insulin/IGF-1) | Days–weeks | [Mechanism/Cohort] | Anorexia/eating disorder literature; RED-S studies | Can produce high total T / low free T phenotype even in underweight men |
| **Levothyroxine (T4) therapy → hyperthyroid** | Excess levothyroxine → TSH < 0.1 | SHBG **+5–20%** (thyroid hormone induces hepatic SHBG production) | 4–8 wk | [Mechanism] | Selva 2009 *J Mol Endocrinol* | Bidirectional: overt hyperthyroid → high SHBG; hypothyroid → low SHBG |
| **High-fat, low-carb diet (ketogenic)** | Isocaloric KD | SHBG: modest **rise** in some RCTs (improved insulin sensitivity effect) | 4–12 wk | Mixed | Limited RCTs; Whittaker 2021 shows T rises on high-fat, with SHBG changes inconsistent | Net effect on free T can be positive due to T rise outweighing SHBG rise |
| **Exogenous testosterone / AAS** | Any supra-physiologic androgen | SHBG **↓** 30–50% (androgens directly suppress hepatic SHBG) | 2–6 wk | [Mechanism/Cohort] | Observed universally in AAS users; is a diagnostic flag | Low SHBG in presence of high total T = exogenous androgen signature |
| **SSRIs** | Chronic use | SHBG **modest ↑** (~2–5 nmol/L in some series) | 4–8 wk | [Cohort] | Observational data; mechanism unclear (serotonin → hepatic HNF-4α?) | Small effect; primarily noted in women; not a clinically significant driver in young men |
| **Creatine supplementation** | 5 g/day × 3 wk | DHT **↑~56%** above baseline (Van der Merwe 2009); SHBG effect not separately reported | 3 wk | [1-Trial] | Van der Merwe et al. 2009 *Clin J Sport Med* (n=20 rugby players, college age) | **Single trial, single cohort.** The DHT rise (via creatine → more substrate for 5α-reductase, or creatine → DHT pathway) was not replicated. Do not over-interpret. |

### Synthesis

**SNPs:** `rs6258` (SHBG Ser156Thr → lower SHBG) and `rs12150660` (intron 1 of SHBG gene → affects SHBG set-point) are the two most clinically validated SHBG-modifying SNPs; if you carry lower-SHBG alleles, your SHBG will normally track lower and your free T interpretation baseline shifts accordingly.

**SA-specific:** South Asian men have a population-level lower SHBG set-point, partly explained by higher insulin resistance and ectopic adiposity. A SHBG of 18 nmol/L in a lean SA man may not reflect metabolic pathology; context matters.

---

## Estradiol (E2)

**Quick read:** E2 in men is primarily a function of testosterone substrate × aromatase activity (fat mass, CYP19A1 genotype, alcohol). The most important message is bidirectional: too low E2 (from AI over-suppression or very low T) damages bone, increases fat, and impairs libido — as clearly shown by Finkelstein 2013. The "E2 is bad for men" framing in TRT clinic culture is not supported by the evidence.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Weight loss (obese baseline)** | 10 kg fat loss | E2 **↓10–20%** (less aromatase substrate × less adipose aromatase) | 3–6 months | [Cohort/Mechanistic] | Consistent across weight-loss trials; exact % varies by fat distribution | Central fat has higher aromatase density; visceral fat loss → largest E2 drop |
| **Alcohol (chronic heavy use)** | Heavy intake / AUD | E2 **+7.65 pg/mL** (meta-analytic mean) | Weeks–months | [Meta] | Santi et al. 2024 *Andrology* | Mechanism: alcohol impairs hepatic E2 clearance (CYP3A4 competition) + induces aromatase; gynecomastia is the clinical correlate |
| **Anabolic steroids / high-dose T** | Supra-physiologic T | E2 **markedly elevated** (proportional to T substrate); absolute level depends on AI use | 2–8 wk | [Mechanism] | AAS users routinely measured E2 40–100+ pg/mL (sensitive assay) | Aromatizable AAS (testosterone esters, methandrostenolone) → more aromatization; non-aromatizable (oxandrolone, stanozolol) → less |
| **Anastrozole** | 0.5 mg 2–3×/wk | E2 **−50%** | 4–8 wk | [RCT/Cohort] | Standard AI pharmacodynamic data; confirmed in TRT cohorts | Over-suppression (E2 < 15 pg/mL) → fat gain, joint pain, libido loss, bone loss (Finkelstein 2013 data) |
| **Letrozole** | 2.5 mg/day | E2 **−90–95%** | 4 wk | [RCT] | Used in oncology/fertility; very potent | Far too aggressive for physiologic optimization; reserved for documented gynecomastia or fertility workup |
| **Finasteride** | 1 mg/day | E2 decreases slightly (less DHT substrate for aromatase? — actually modest); net effect usually **minimal** | 4–12 wk | [Mechanism/RCT] | Various finasteride RCTs; small direct E2 effect | DHT is aromatized to 3α-diol (weak estrogen) in some tissues; finasteride slightly lowers this pathway |
| **Tamoxifen** | 20 mg/day | E2 **not dramatically changed** systemically; blocks ER at breast and pituitary; raises LH/T via anti-feedback at pituitary | 4–8 wk | [RCT] | Standard SERM pharmacology | Used for gynecomastia treatment; raises T similar to clomid but with fewer estrogen partial-agonist effects |

### Synthesis

**The Finkelstein 2013 NEJM evidence:** 400 men, goserelin + graded T doses ± anastrozole. With anastrozole blocking E2: fat mass increased significantly in the E2-suppressed arm at every T dose level. Libido impaired with E2 suppression independent of T. This is the highest-quality data proving E2 mediates fat regulation and sexual function in men. **Do not suppress E2 without documented indication.**

**Assay reminder:** Standard direct immunoassay E2 is unreliable below ~50 pg/mL (the entire male physiologic range). All E2 interpretation in men requires LC-MS/MS (LabCorp 140244 "Estradiol, Sensitive").

---

## LH

**Quick read:** LH is an output marker of HPG axis integrity, not a target for lifestyle intervention per se. Its clinical value is as a pattern discriminator. The main interventions that move LH are SERMs (up), exogenous androgens (down), and dopamine agonists (indirect, via prolactin normalization).

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Clomiphene citrate** | 25 mg/day | LH **+4.7 IU/L** above baseline (meta-analytic) | 4–8 wk | [Meta] | Huijben et al. 2022 *Andrology* 10:384 (multiple RCTs) | In hypogonadal men; effect in eugonadal men not studied in RCTs |
| **Exogenous androgens (TRT, AAS)** | Any exogenous T | LH → **near-zero** (suppressed within 1–3 wk) | 2–4 wk | [Mechanism] | Standard HPG feedback; reproduced in every TRT/AAS study | Recovery after cessation: weeks to months; HCG + clomid used for recovery |
| **Prolactin normalization (cabergoline)** | 0.25 mg 2×/wk | If hyperprolactinemia was suppressing GnRH → LH recovers to normal with prolactin normalization | 4–12 wk | [RCT/Mechanism] | Standard prolactinoma treatment data | LH rise magnitude depends on baseline hyperprolactinemia severity |
| **Sleep restriction** | 5 h/night × 1 wk | LH pulse amplitude likely reduced (mechanistic inference from GnRH-LH coupling during sleep) | 1 wk | [Mechanism] | Leproult 2011 didn't isolate LH; mechanism from sleep–GnRH coupling literature | Not directly quantified in that trial |
| **Opioids** | Chronic use | LH → **suppressed** (µ-opioid inhibition of GnRH pulsatility = secondary hypogonadism pattern) | Weeks | [Meta] | Rajagopal et al. 2020 *JCEM* | Clinically presents as low T + low/normal LH + low FSH |

### Synthesis

No lifestyle intervention reliably raises LH in healthy eugonadal young men in a clinically meaningful way. LH is a diagnostic marker. SERMs are the main pharmacologic movers upward; exogenous androgens/opioids are the main suppressors.

---

## FSH

**Quick read:** FSH tracks similarly to LH in response to HPG-axis manipulations, but is more sensitive to spermatogenic damage (elevated FSH with low LH = tubular injury, not Leydig failure). The clinical use of FSH as a target for intervention is limited; it's primarily a diagnostic marker for spermatogenic function.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Clomiphene / SERMs** | 25 mg/day clomid | FSH **+4.6 IU/L** above baseline (meta-analytic) | 4–8 wk | [Meta] | Huijben 2022 *Andrology* | FSH rises alongside LH; spermatogenesis effect takes 60–90 days to manifest |
| **Exogenous testosterone (TRT, AAS)** | Any dose | FSH → **near-zero** (often more deeply suppressed than LH) | 2–4 wk | [Mechanism] | Reproduced in every TRT/AAS series | Azoospermia typically within 3–6 months of TRT-dose exogenous T |
| **Testosterone + HCG (combination TRT)** | HCG 500–1,000 IU 2–3×/wk with T | FSH remains **suppressed** (HCG mimics LH, not FSH); FSH-specific recovery requires FSH itself (Gonal-F, Menopur) for spermatogenesis induction | — | [Mechanism/Cohort] | Standard fertility treatment data | Important nuance: HCG preserves intratesticular T and Leydig cell function but does NOT preserve FSH-driven spermatogenesis |

---

## Prolactin

**Quick read:** SSRIs, antipsychotics, and sleep timing are the main movers in healthy young men. The most important clinical action is recognizing that mild elevations are often macroprolactin (biologically inactive) or pre-analytical confounders, not true hyperprolactinemia.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **SSRIs (paroxetine, fluoxetine, sertraline)** | Standard antidepressant doses | Prolactin **+~2–5 ng/mL** on average; hyperprolactinemia (>20 ng/mL) in ~10–35% of users | 4–12 wk | [Cohort] | Knegtering et al. 2003 *Psychoneuroendocrinology*; Kuruvilla et al. 2013 *Psychiatry Investig* | Paroxetine > sertraline > fluoxetine in terms of prolactin elevation; population-based data suggest less effect than clinical series |
| **Atypical antipsychotics (risperidone, paliperidone)** | Standard doses | Prolactin **+30–100 ng/mL**; most marked hyperprolactinemia of any drug class | Days–weeks | [RCT] | Prolactin pharmacology for each agent (standard psychiatry data) | Clinically significant; causes hypogonadism, gynecomastia; switch to quetiapine/aripiprazole if problematic |
| **Metoclopramide / domperidone** | Standard antiemetic doses | Prolactin **+20–50 ng/mL** (dopamine antagonist) | Hours–days | [Mechanism/RCT] | Pharmacology data | Acute elevation with each dose; can persist with chronic use |
| **Opioids** | Chronic use | Prolactin **elevated** (µ-opioid stimulate prolactin secretion; mechanism via reduced dopamine tone) | Weeks | [Meta] | Rajagopal 2020 *JCEM* | Contributes to opioid-induced hypogonadism syndrome alongside LH suppression |
| **Orgasm** | Single episode | Prolactin **3–5× baseline** for ≥ 60 min post-orgasm | Minutes | [Cohort] | Kruger et al. 2003 *Neuropsychobiology* | Still modestly elevated at 24 h; disclose recent sexual activity before prolactin draw |
| **Cabergoline** | 0.25 mg 2×/wk | Prolactin → **normalized** (typically < 20 ng/mL) in most prolactinomas within 1–3 months | 4–12 wk | [RCT/Meta] | Verhelst & Abs 2003 review; standard prolactinoma treatment data | First-line therapy for prolactinoma; 80–90% normalization rate |
| **Bromocriptine** | 2.5 mg/day (titrated) | Prolactin **normalized** but with more side effects (nausea, orthostasis) | 4–8 wk | [RCT] | Original dopamine agonist for hyperprolactinemia | Cabergoline is now preferred for both efficacy and tolerability |
| **Hypothyroidism correction** | Levothyroxine to normalize TSH | Prolactin **normalized** if originally elevated from TRH cross-stimulation of lactotrophs | 4–8 wk | [Mechanism/Case series] | TRH → lactotroph PRL secretion; standard thyroid pathophysiology | Always rule out hypothyroidism as a cause before attributing prolactin elevation to pituitary disease |

### Synthesis

**Macroprolactin caveat is paramount:** 10–46% of apparent hyperprolactinemia (15–50 ng/mL range) is biologically inactive macroprolactin (IgG-bound prolactin). Insist on PEG precipitation test before MRI referral for mild asymptomatic elevation.

---

## DHEA-S

**Quick read:** DHEA-S is tightly controlled by ACTH. The main suppressors in a healthy 20-year-old are exogenous glucocorticoids (including inhaled/intranasal at high doses and topical ketoconazole). DHEA supplementation in eugonadal young men with normal DHEA-S has no demonstrated benefit and may elevate androgenic metabolites.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Exogenous glucocorticoids (oral)** | Prednisone 5–20 mg/day for ≥ 2 weeks | DHEA-S **↓ 40–80%** (ACTH suppression → adrenal androgen pathway shut down) | Days–weeks | [Mechanism/Cohort] | Standard HPA suppression data; Gordon 1994 *Clin Endocrinol* | Even low-dose inhaled steroids (high-potency, high-dose, years of use) can measurably suppress DHEA-S; systemic oral → larger effect |
| **Intranasal fluticasone (standard dose)** | 200–400 µg/day | DHEA-S: **minimal to no effect** at recommended doses (no measurable HPA suppression at standard dosing in most studies) | — | [RCT] | Howland 2004 *J Allergy Clin Immunol* (n=healthy volunteers, 28 days, FP 200 µg vs 400 µg twice daily → no HPA effect) | At high doses (400 µg twice daily, above label), some studies show borderline ACTH suppression. Long-term use warrants occasional DHEA-S monitoring. |
| **Topical ketoconazole (scalp/skin)** | 2% shampoo / cream; scalp application | Systemic absorption is low from shampoo; topical cream → small but measurable ketoconazole blood levels. Mechanism: CYP17A1 inhibition → DHEA-S **↓** dose-dependently if systemic levels are appreciable. | Weeks | [Mechanism] | Feldmann & Maibach 1970 percutaneous absorption data; ketoconazole CYP17A1 IC50 data | Standard scalp shampoo (2 min contact, rinsed off) → probably negligible systemic effect. Leave-on cream to large body surface area → more risk. Monitor DHEA-S if using extensively and values are trending low. |
| **DHEA supplementation (25–200 mg/day)** | Oral DHEA | DHEA-S **rises markedly** (dose-dependent); androgens ↑; BUT endogenous DHEA-S production **suppressed** via ACTH feedback | 4–8 wk | [RCT] | Brown 2003 *Fertil Steril* (n= healthy men 18–42, 6 months); Morales 1994 *J Clin Endocrinol Metab* | DHEA supple in healthy young men with normal DHEA-S: no longevity benefit demonstrated; potential androgenic side effects (acne, prostate growth); guidelines do not endorse in young eugonadal men. |
| **Chronic overtraining / energy deficiency** | RED-S equivalent; severe caloric restriction | DHEA-S **↓** (chronic ACTH dysregulation + adrenal androgen pathway suppression) | Weeks–months | [Cohort] | Male RED-S and eating disorder literature (parallel to adrenarche suppression) | DHEA-S is one of the first markers to fall with chronic underfueling in young male athletes |
| **Hyperprolactinemia** | Elevated prolactin (any cause) | DHEA-S modest **↓** (prolactin modulates adrenal androgen sensitivity) | Variable | [Cohort] | Small observational studies; mechanism partially via altered ACTH-adrenal signaling | Modest effect; prolactin normalization (cabergoline) → DHEA-S partial recovery |

### Synthesis

In a healthy 20yo SA male at peak DHEA-S age: **do not supplement DHEA if values are in the normal age-stratified range.** Values in the lower half of the 20–29 range (< 300 µg/dL) warrant asking: exogenous glucocorticoid exposure? Chronic energy deficit? Chronic illness? These are the actionable targets, not DHEA exogenous replacement.

**Drug note:** Ketoconazole (oral, therapeutic doses 400–1200 mg/day) is a powerful CYP17A1 inhibitor used to treat Cushing's. Topical scalp application for seborrheic dermatitis at standard shampoo doses does not produce the same systemic effect — but this context is noted for your ketoconazole exposure record.

---

## AM Cortisol

**Quick read:** Single-point AM cortisol has CVI ~50% — it is reliable for ruling out adrenal insufficiency (< 3 µg/dL) or Cushing's (>25 µg/dL) but not for fine "optimization" tracking. The main modifiable interventions are sleep, alcohol, and glucocorticoid avoidance.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Sleep deprivation** | Partial sleep deprivation (< 6 h/night) | Evening/late cortisol **elevated** (+50–100% vs. rested); AM cortisol less reliably different; diurnal slope **flattened** | 1–2 wk | [RCT/Cohort] | Spiegel et al. 1997 *Sleep*; multiple subsequent studies confirming flattened cortisol slope with sleep restriction | AM serum cortisol may not change significantly; the pathology is in the evening nadir rising and slope flattening, better captured by salivary cortisol × 4 timepoints |
| **Morning bright light / sun exposure** | 10–30 min outdoor light within 1 h of wake | Cortisol Awakening Response (CAR) **augmented** (~10–20%); acute component sharpened | Minutes → days | [RCT/Cohort] | Scheer & Buijs 1999; Tsai et al. 2004 *Physiol Behav*; multiple salivary CAR studies | Effect is on the CAR (30–45 min post-wake arc), not on total daily cortisol output; best measured by salivary cortisol at wake, +30, +60 min |
| **Acute psychological stress / anxiety** | Anticipatory or procedural stress | Cortisol **acutely +50–150%** above baseline | Minutes | [RCT] | Kirschbaum TSST studies; physiological stress response literature | Single-point serum cortisol is highly vulnerable to draw-related stress; standard pre-draw guidance: 20–30 min seated rest |
| **Alcohol (acute)** | Single intoxicating dose | Cortisol **acutely rises** (~+50% in some studies) → disrupts subsequent sleep architecture → sustained HPA dysregulation with chronic use | Hours | [RCT] | Wand & Dobs 1991 *J Clin Endocrinol Metab* | Acute cortisol rise post-alcohol followed by rebound drop; chronic heavy use → pseudo-Cushing's pattern with AM cortisol chronically elevated |
| **Chronic oral glucocorticoids** | Prednisone ≥ 5 mg/day × weeks | Endogenous AM cortisol **suppressed** (feedback suppression of CRH/ACTH); can persist weeks after cessation | Weeks; persists weeks after stopping | [Mechanism] | HPA suppression data; standard endocrine pharmacology | The most common cause of "low AM cortisol" in young men is prior/ongoing exogenous glucocorticoid exposure (including some inhaled steroids at high potency/dose) |
| **Magnesium supplementation** | 300–500 mg/day elemental magnesium | Evening salivary cortisol modestly **reduced** in some small trials; AM total serum effect less clear | 4–8 wk | Mixed | Held et al. 2002 *Pharmacopsychiatry* (small RCT, sleep quality + cortisol in elderly); limited data in young men | Data are in elderly subjects with poor Mg status; effect in healthy young replete men is uncertain. |
| **Ashwagandha** | 300–600 mg KSM-66 extract | Serum cortisol **−14–28%** vs. placebo in chronically stressed subjects | 8–12 wk | [RCT] | Chandrasekhar et al. 2012 *Indian J Psychol Med* (n=64, KSM-66, −14.5%); Lopresti 2019 also shows cortisol reduction | Studies in self-reported "stressed" subjects; magnitude in healthy low-stress 20-year-olds likely smaller |

### Synthesis

**Measurement caveat:** Single AM serum cortisol CVI = ~50%. Do not read trend from one draw to the next without controlling for identical pre-draw conditions. To assess HPA axis dynamics meaningfully: 4-point salivary cortisol (wake, +30 min, noon, bedtime) is far more informative for the cortisol awakening response and slope.

**Drug notes:** Any exogenous glucocorticoid (oral, intra-articular, high-dose inhaled, extensive topical) can suppress AM cortisol. Fluticasone (intranasal) at recommended dosing generally does not suppress the HPA axis; fluticasone at high doses or extensive topical application can. If using topical ketoconazole and/or intranasal fluticasone (Flonase), monitoring DHEA-S and AM cortisol longitudinally is appropriate.

---

## TSH

**Quick read:** TSH is the most sensitive thyroid marker; it is not a direct intervention target but reflects underlying thyroid disease and assay artifacts. The main modifiable lifestyle effects (stress, sleep, caloric restriction, selenium) are modest and rarely produce changes outside the reference range in healthy individuals. The main interventions that move TSH are thyroid hormone drugs and the biotin artifact.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Biotin (high-dose supplement)** | ≥ 5,000 µg/day | TSH **falsely suppressed** (magnitude varies by platform): at 500 ng/mL plasma biotin → TSH suppressed to near-undetectable on Roche Elecsys; at lower doses, 7–10% suppression per 6–15 ng/mL biotin | Hours (peak biotin) | [Mechanism/In vitro] | AACC Guidance; Trambas 2020 *PMC6963918*; Cyprus J Med Sci 2025 | This is artifact, not biological. Stop biotin ≥ 72 h before draw. |
| **Levothyroxine (L-T4)** | Starting dose ~1.6 µg/kg/day; titrate | TSH falls to target (0.5–2.5 mIU/L for most indications); **every 0.5 µg/kg dose change → ~2–4-fold TSH shift** (log-linear relationship) | 4–8 wk (new steady state) | [RCT] | Standard levothyroxine pharmacodynamics; Garber et al. 2012 *Endocr Pract* | Overcorrection → iatrogenic subclinical hyperthyroidism (suppressed TSH → AF risk, bone loss) |
| **Liothyronine (L-T3) addition** | 5–25 µg/day added to L-T4 | TSH falls substantially (T3 is more potent feedback signal at pituitary) → must reduce L-T4 dose | 1–2 wk | [RCT] | Combination T4+T3 trials (Bunevicius 1999 *NEJM*; Jonklaas 2014 ATA guidelines review) | T3 addition is not routinely recommended by ATA; T4 monotherapy remains standard; combination considered for persistent symptoms on T4 with DIO2 Thr92Ala genotype |
| **Selenium 200 µg/day (Hashimoto's)** | Selenomethionine 200 µg/day × 6 months | TSH: **minimal direct effect** (selenium primarily reduces TPO Ab titers, not TSH directly, in most trials) | — | [Meta] | Toulis 2010 *Thyroid* 20:1163; Huwiler 2024 *Thyroid* | Selenium reduces TPO Ab but does not consistently alter TSH, FT4, or clinical progression to overt hypothyroidism |
| **Iodine excess** | Kelp supplements, high-dose iodine | TSH **transiently ↑** (Wolff-Chaikoff effect: iodine excess inhibits thyroid hormone synthesis acutely → feedback rise in TSH) | Days–weeks | [Mechanism] | Pharmacology of iodine; case series with kelp/seaweed ingestion | Usually transient in normal thyroid; can precipitate hypothyroidism in autoimmune thyroid disease |
| **Amiodarone** | Therapeutic dose (anti-arrhythmic) | TSH **rises sharply** within 48 h, peaks ~10× above baseline at ~10 days; then may settle (Type 1 AIT = persistent hypothyroidism vs. Type 2 = destructive thyroiditis) | Days–weeks | [RCT/Meta] | Bartalena 2018 ETA guidelines; PMC 2018 amiodarone review | High iodine content (37% by weight) + D1 inhibition → complex TSH dynamics; requires endocrinology management |
| **Beta-blockers (propranolol)** | Standard doses | TSH: **unchanged**; but T3 **↓** (D1 inhibition → reduced T4→T3 conversion) → rT3 rises | 1–2 wk | [Mechanism/RCT] | Standard pharmacology; confirmed in propranolol trials | The T3/rT3 change is real; TSH does not change because pituitary D2-generated T3 is relatively preserved |
| **Metformin** | Standard doses (500–2,000 mg/day) | TSH modestly **↓** (~0.4 mIU/L) in some hypothyroid patients on levothyroxine; mechanism unclear | Months | [Cohort] | Multiple observational studies; not seen in all trials | Effect appears in treated hypothyroid patients, not clearly in euthyroid subjects; clinically minor |
| **Severe caloric restriction / fasting (>24h)** | Extended fasting or prolonged severe deficit | TSH: **unchanged or slightly reduced**; T3 **↓** (D1 downregulation → less T4→T3); rT3 **↑** | Hours–days | [RCT] | Fasting studies (Vagenakis 1975; multiple starvation-hypothyroid-phenotype papers) | Fasting effects on thyroid are adaptive; do not test thyroid during a fast or severe caloric restriction |
| **TRUST trial (levothyroxine for mild SCH in elderly)** | 50–200 µg/day targeting TSH 0.4–2.5 in SCH (mean baseline TSH 6.4 mIU/L) | TSH normalized to 3.6 vs. 5.5 in placebo at 1 year; **zero symptom benefit** on hypothyroid symptom or tiredness scores | 1 year | [RCT] | Stott et al. 2017, *NEJM* 376:2534 (n=737, mean age 74.4 yr) | Study population was older (mean 74.4); mild SCH (TSH 4.5–20, median ~6.4); results may not fully generalize to symptomatic patients or young adults with TSH > 10. |

---

## Free T4

**Quick read:** FT4 is stable (T4 half-life ~7 days) and resistant to acute perturbations. Main movers are levothyroxine, TBG-modifying states (pregnancy, estrogen — less relevant here), and biotin artifact. In a euthyroid young man, FT4 tracks slowly with thyroid disease progression or treatment changes.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Biotin (high-dose)** | ≥ 5,000 µg/day | FT4 **falsely elevated** (competitive immunoassay artifact); magnitude platform-dependent: Roche Elecsys → 1146% false positive at 400 ng/mL biotin; lower doses → smaller effect | Hours | [Mechanism/In vitro] | Trambas 2020; AACC guidance | The most common artifact causing spuriously high FT4 in a young male optimizer |
| **Levothyroxine** | 25 µg dose increment | FT4 **+0.1–0.2 ng/dL** per 25 µg dose increment (approximate; individual variability high) | 4–8 wk (T4 half-life ~7 days) | [RCT] | Standard clinical pharmacokinetics; Garber 2012 guidelines | TSH is a far more sensitive titration endpoint than FT4 itself |
| **Selenium 200 µg/day (Hashimoto's)** | 6 months | FT4: **minimal direct change** in most trials | 6 months | [Meta] | Toulis 2010; Huwiler 2024 | Selenium reduces antibody titers; does not consistently alter FT4 |
| **Heparin** | Therapeutic IV or SC | FT4 **falsely elevated** in vitro (heparin activates lipoprotein lipase → frees fatty acids → displace T4 from TBG) | Minutes | [Mechanism] | Physiologic in vitro phenomenon; reproducible across labs | Not relevant for standard outpatient draw; relevant if anti-coagulated |

---

## Free T3

**Quick read:** FT3 is the biologically active hormone and the most sensitive to acute perturbations of conversion (selenium status, illness, fasting, beta-blockers, glucocorticoids). Low FT3 with normal TSH and FT4 is the "conversion problem" phenotype that is real but controversial regarding intervention.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Selenium repletion (deficient)** | 200 µg/day selenomethionine | FT3 **modestly ↑** (D1 is a selenoenzyme; repletion restores D1 activity); estimated +5–15% in deficient individuals | 4–12 wk | [Mechanism/Small RCT] | Bianco 2019 *Endocr Rev* (deiodinase biochemistry); limited human RCT evidence for healthy subjects | Effect clearest in documented selenium deficiency; unclear benefit in selenium-replete individuals |
| **Severe caloric restriction / fasting** | Extended fast; very low calorie diet | FT3 **↓ 20–40%** (adaptive D1 downregulation + D3 upregulation → less T4→T3, more T4→rT3) | 24–72 h | [RCT] | Vagenakis 1975; multiple fasting studies | Fully reversible on refeeding; do not test thyroid during a prolonged fast |
| **Beta-blockers (propranolol)** | Standard doses | FT3 **↓ ~10–20%** (D1 inhibition; selective β-blockers less effect than propranolol) | 1–2 wk | [RCT] | Pharmacology literature; Wiersinga 1982 | TSH unchanged; rT3 rises |
| **High-dose glucocorticoids** | Prednisone ≥ 20 mg/day or equivalent | FT3 **↓** (D1 inhibition; similar mechanism to beta-blockers) → rT3 ↑ | Days | [Mechanism] | NTIS analog pharmacology | Seen in supraphysiologic doses; standard therapeutic doses have less effect |
| **Acute illness / surgery** | NTIS pattern | FT3 **↓ 25–50%** as part of non-thyroidal illness syndrome | Hours–days | [Cohort] | Chopra 1997; Euthyroid Sick StatPearls | TSH may be normal or low; do not initiate T3/T4 therapy for NTIS — treatment does not improve outcomes (RCT data) |
| **Iron repletion (iron-deficient)** | Ferrous sulfate to replete ferritin | FT3 may modestly **improve** if iron deficiency was impairing thyroid peroxidase activity or erythropoiesis | 3–6 months | [Mechanism/Cohort] | Zimmermann 2002 *Am J Clin Nutr* (children); limited adult data | Iron is a cofactor for TPO; deficiency can impair thyroid hormone synthesis; relevant if ferritin < 30 ng/mL |
| **T4 monotherapy (levothyroxine)** | Standard replacement | FT3: **normal or low-normal** in ~10–15% of treated patients despite adequate T4/TSH; these patients show persistent symptoms | — | [RCT/Cohort] | Gullo et al. 2011 *J Clin Endocrinol Metab*; Bianco 2019 review | Basis of the ongoing T4-monotherapy debate; DIO2 rs225014 Thr92Ala carriers at increased risk of impaired T4→T3 conversion |

### Synthesis

**DIO2 rs225014 (Thr92Ala):** The Ala/Ala genotype (homozygous) is associated with lower serum T3:T4 ratio, impaired intracellular T3 generation (particularly in pituitary and brain), worse psychological well-being on T4 monotherapy, and greater response to combination T3 therapy. (Peeters 2017 *JCEM*; 2009 *JCEM* 94:1623.) However: the association is inconsistent across populations, and the rs225014 Ala allele frequency is ~36% in European populations (many people carry it without symptoms). **Do not start combination T4+T3 therapy based on genotype alone without clear clinical symptoms of T4 monotherapy inadequacy.**

**Reverse T3 note:** rT3 reliably rises in NTIS, fasting, propranolol use, and high-dose glucocorticoids — these are validated contexts. The "FT3/rT3 ratio < 20" framework as a trigger for T3 supplementation in otherwise healthy outpatients is **biologically plausible but not supported by RCT outcome data.** (Halsall & Oddy 2021 *Ann Clin Biochem*.) rT3 testing adds value when NTIS vs. central hypothyroidism must be distinguished in hospitalized patients; its use in healthy optimization settings is not guideline-endorsed.

---

## TPO Antibodies

**Quick read:** TPO antibodies reflect autoimmune activity; they don't respond robustly to lifestyle in most trials. Selenium is the best-evidenced intervention, reducing titers ~20–55% without proven effect on clinical progression to overt hypothyroidism. The most "intervention" that works is identifying and eliminating triggers (iodine excess, smoking), not supplements.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Selenium 200 µg/day (selenomethionine)** | 6 months | TPO Ab **↓ 20–55%** from baseline; absolute reduction varies greatly by baseline titer | 3–6 months | [Meta] | Toulis et al. 2010 *Thyroid* 20:1163 (meta-analysis, 4 studies; weighted mean difference −271.09 IU/mL); Gärtner 2002 showed −63.6% TPO at 3 months in selenium vs. −88% in placebo (i.e., 46% delta); Negro 2007 confirmed in pregnant women | **Does not reduce progression to overt hypothyroidism** in controlled trials; Huwiler 2024 meta-analysis confirms antibody reduction without clinical endpoint benefit. Mechanistically plausible (selenoprotein GPx4 reduces oxidative stress at thyroid). |
| **Iodine excess** | Kelp, high-dose iodine (> 1 mg/day) | TPO Ab may **increase** or trigger Hashimoto's flare | Days–weeks | [Cohort/Mechanism] | Multiple geographic studies; Teng 2006 *NEJM* (iodine excess → increased autoimmune thyroid disease in China) | Avoid iodine megadosing (> 500 µg/day) in TPO+ individuals |
| **Vitamin D repletion (25OHD < 50 nmol/L)** | 1,000–4,000 IU/day D3 | TPO Ab: **modest reduction** in some observational studies; effect ~10–20%; inconsistent in RCTs | 3–6 months | Mixed | Mazokopakis 2015 *Hormones*; Simsek 2016 — RCTs inconclusive; observational data shows inverse correlation | Association is real (TPO+ patients have more vitamin D deficiency); whether correcting D directly lowers TPO Ab mechanistically is not proven. Replete D anyway for other reasons. |
| **Gluten-free diet** | Complete gluten elimination | TPO Ab: some case reports and small series show reduction; **no high-quality RCT** | 6–12 months | [Cohort — weak] | Sategna-Guidetti 2001 *J Endocrinol Invest* (celiac + AIT); Shor 2012 review | **Only justified in confirmed celiac disease.** No evidence for benefit of gluten elimination in TPO+ individuals without celiac or gluten sensitivity. |
| **Smoking cessation** | Stop tobacco | TPO Ab: current smokers have **lower** TPO positivity rates (paradoxically — nicotine is immunosuppressant); cessation may be associated with transient increase | Months | [Cohort] | Strieder 2003 *Eur J Endocrinol*; NHANES observational data | Smoking is not protective in any clinically useful sense — the immunosuppression is harmful overall. Do not use this finding to justify smoking. |

### Synthesis

**SNPs and selenium:** `SELENOP` (SEPP1) variants (particularly rs7579, rs3877899) affect selenoprotein P levels, the main selenium transport protein to the thyroid. Lower-SELENOP variants may require higher selenium intake to achieve equivalent intra-thyroidal selenium concentration. Clinical impact: if a patient fails to show TPO Ab reduction after 6 months of 200 µg selenium, SELENOP genotype is one possible explanation (though not routinely tested). The evidence base for SELENOP genotype-guided dosing is mechanistic, not yet trial-proven.

**SA-specific:** Some South Asian regional populations have higher Hashimoto prevalence (particularly South Indian, Sri Lankan cohorts); genetic data are limited but HLA-DR3/DR5 associations with Hashimoto's are similar across ancestries. Vitamin D deficiency is extremely common in SA populations even in temperate climates (darker skin + limited sun exposure) and may contribute to autoimmune susceptibility — this is a legitimate lifestyle target regardless of TPO Ab status.

**Pharmacotherapy reference:**
- Selenium 200 µg/day selenomethionine → TPO Ab −20–55% over 6 months; no effect on progression to overt hypothyroidism (Huwiler 2024 meta, confirmed)
- Levothyroxine in overt Hashimoto's (TSH > 10 or symptomatic) → treatment normalizes TSH; does not significantly reduce TPO Ab titers
- Inositol 600 mg + selenium 83 µg (Nordio 2017 *Eur Rev Med Pharmacol Sci*, n=86) → TPO Ab further reduced vs. selenium alone; preliminary data only

---

## TgAb Antibodies

**Quick read:** TgAb follows similar intervention responses to TPO Ab but is less specific for clinical thyroid disease when occurring in isolation (TgAb+ / TPO– is not statistically associated with current thyroid dysfunction per Hollowell 2002). Most intervention data are from mixed AITD populations where TPO+ and TgAb+ co-occur.

### Effect size table

| Intervention | Dose/Protocol | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| **Selenium 200 µg/day** | As above for TPO Ab | TgAb: **less consistent reduction than TPO Ab** in most trials (Toulis 2010 meta: no significant TgAb effect in primary analysis) | 3–6 months | [Meta] | Toulis 2010 *Thyroid* — TgAb weighted mean difference not statistically significant in original meta | Some newer trials show TgAb reduction; effect is smaller and less reliable than for TPO Ab |
| **Vitamin D repletion** | As for TPO Ab | TgAb: observational inverse correlation; RCT evidence weak | — | Mixed | As for TPO Ab | Same caveats as TPO Ab section |
| **Thyroidectomy (for completeness)** | Total or near-total thyroidectomy | TgAb: may persist for years post-operatively; rising TgAb post-thyroidectomy is used as a cancer recurrence marker (second clinical context) | Years | [Mechanism/Cohort] | ATA 2015 thyroid cancer guidelines (Haugen *Thyroid* 2016) | Only relevant if thyroid cancer history; not applicable to screening context |

### Synthesis

TgAb in isolation (no TPO+, normal TSH) requires only annual monitoring, not intervention. If TgAb+ co-occurs with TPO+, treat as Hashimoto's. The 2× increased progression risk with dual antibody positivity is the main clinical message.

---

## Cross-Marker Patterns

### Weight loss

Effect runs through multiple markers simultaneously: total T ↑ (less aromatase substrate, less insulin-driven SHBG suppression), SHBG ↑ (insulin sensitivity improves → hepatic HNF-4α de-repressed), free T ↑ (less than total T because SHBG also rises), E2 ↓ (less aromatase activity in reduced adipose), DHEA-S stable or ↑ slightly, AM cortisol unchanged or slightly ↓ (reduced cortisol-cortisone recycling in adipose). Net hormonal improvement is real and consistent; it is the single highest-leverage lifestyle intervention for overweight men.

### Sleep deprivation

Total T ↓ 10–15% within one week; evening cortisol ↑ and diurnal slope flattens; prolactin patterns shift (reduces nocturnal peak duration); LH pulse amplitude likely decreases. All effects reverse with sleep restoration. Sleep is the cheapest and most evidence-supported "testosterone optimization" tool available.

### Alcohol

Total T ↓ (chronic), SHBG complex (acute increases, chronic heavy use reduces), E2 ↑ (impaired hepatic clearance + aromatase induction), LH paradoxically suppressed (alcohol inhibits GnRH), AM cortisol acutely ↑. Prolactin may rise acutely. Pattern of heavy chronic alcohol: feminizing hormone profile (low T, high E2, low LH) + gynecomastia.

### Exogenous/inhaled corticosteroids

DHEA-S ↓ (dose-dependent ACTH suppression → adrenal androgen pathway shutdown); AM cortisol ↓ with prolonged use; SHBG ↓ slightly (glucocorticoids suppress hepatic SHBG somewhat); total T ↓ via central HPG suppression at high doses. Inhaled fluticasone at standard doses: minimal HPA effect; high-dose or long-duration use warrants monitoring.

### Biotin artifact pattern

TSH falsely ↓ + FT4 falsely ↑ + FT3 falsely ↑ + TPO Ab falsely ↓ (masked) → pattern mimics hyperthyroidism but patient is clinically well. Stop biotin 72 h and repeat. This is the most common single source of false positives in a health-optimizing young male's thyroid panel.

### Topical ketoconazole + intranasal fluticasone (Flonase)

Ketoconazole (CYP17A1 inhibitor): at systemic concentrations (from extensive topical use or oral dosing) → DHEA-S ↓, cortisol ↓ (via CYP11B1/CYP17A1 inhibition). Standard scalp shampoo use: systemic absorption low, effect probably negligible. Fluticasone (Flonase) at recommended intranasal doses: no detectable HPA suppression in controlled studies; at high doses or extensive body-surface topical use → DHEA-S ↓, AM cortisol ↓ possible. **If using either chronically: periodic DHEA-S + AM cortisol monitoring is prudent. Look for trend, not a single value.**

---

## Drug Class Reference Table

| Drug | Dose | Primary marker effects | Key caveats |
|---|---|---|---|
| **Testosterone cypionate (TRT)** | 100 mg/wk IM | Total T 600–900 ng/dL trough; LH → 0; FSH → 0; SHBG ↓ 30–50%; E2 ↑ (aromatization); DHEA-S unchanged; hematocrit ↑ | Spermatogenesis suppressed (azoospermia within 3–6 months); requires post-TRT recovery protocol (HCG + SERM) for fertility restoration |
| **HCG (human chorionic gonadotropin)** | 500–1,000 IU 2–3×/wk | LH-mimetic → intratesticular T ↑; total serum T ↑; preserves testis size; FSH remains suppressed | Does not substitute for FSH in spermatogenesis; used with TRT to preserve fertility |
| **Clomiphene citrate (clomid)** | 25–50 mg/day or EOD | LH +4.7 IU/L; FSH +4.6 IU/L; total T +~250–300 ng/dL (meta-analytic); E2 also rises (ER blockade at pituitary releases LH → more T substrate for aromatase); SHBG unaffected | HPG axis intact; fertility preserved; estrogenic effects (mood, visual) from the cis-isomer (zuclomiphene) |
| **Enclomiphene** | 12.5–25 mg/day | Similar T/LH/FSH increases as clomid; less estrogenic (pure trans-isomer) | Off-label; FDA rejected NDA for hypogonadism |
| **Anastrozole (AI)** | 0.5 mg 2–3×/wk | E2 ↓ ~50%; free T ↑ modestly (+15–20% via reduced negative E2 feedback on LH); total T ↑ modestly | Over-suppression → E2 < 15 pg/mL → fat gain, joint pain, bone loss, libido loss (Finkelstein 2013); use only with documented E2 excess on sensitive assay |
| **Tamoxifen (SERM)** | 20 mg/day | LH ↑; FSH ↑; total T ↑; used for gynecomastia treatment; E2 levels unchanged systemically | Less E2 partial agonism than clomid; preferred for gynecomastia; similar fertility-preserving HPG stimulation |
| **Cabergoline** | 0.25–0.5 mg 2×/wk | Prolactin → normalized in ~80–90% of microprolactinoma and drug-induced hyperprolactinemia; secondary T/LH/FSH recovery with prolactin normalization | First-line for prolactinoma; dopamine agonist adverse effects: nausea, orthostasis, cardiac valve risk at very high doses (Parkinson's doses, not endocrine doses) |
| **Levothyroxine (L-T4)** | ~1.6 µg/kg/day (adult average); titrate to TSH | TSH → target range (0.5–2.5 for most); FT4 ↑; FT3 depends on D2 conversion; SHBG ↑ (thyroid hormone → hepatic SHBG induction) | Overcorrection → suppressed TSH → AF, osteoporosis; absorption affected by iron, calcium, PPIs, soy (take on empty stomach) |
| **Methimazole** | 10–40 mg/day (hyperthyroid) | Inhibits TPO → T4/T3 production ↓; TSH ↑; E2/SHBG normalize as hyperthyroid state resolves | Agranulocytosis 0.1–0.5% (monitor CBC); liver toxicity rare; preferred over PTU in non-pregnant adults |
| **Selenium 200 µg/day** | Selenomethionine 200 µg/day × 6 months (Hashimoto's) | TPO Ab ↓ 20–55%; TgAb less consistent; TSH, FT4, FT3 unchanged; no progression benefit proven | Upper tolerable limit for selenium is 400 µg/day; selenosis above that (nail brittleness, garlic breath, GI); 200 µg/day is safe and is the studied dose |

---

## Sources

### Sleep and exercise
- Leproult R, Van Cauter E. **Effect of 1 Week of Sleep Restriction on Testosterone Levels in Young Healthy Men.** *JAMA* 2011;305(21):2173–2174. PMID 21632481. PMC4445839. (n=10, 5h vs 8h, total T −10–15%)
- Hackney AC, Szczepanowska E, Viru AM. **Basal testicular testosterone production in endurance-trained men is suppressed.** *Eur J Appl Physiol* 2003;89:198–201. (Confirmed in: Hackney 2020 PMC5988228 — "Exercise-hypogonadal male condition")
- Vingren JL, Kraemer WJ, Ratamess NA, et al. **Testosterone Physiology in Resistance Exercise and Training: The Up-Stream Regulatory Elements.** *Sports Med* 2010;40(12):1037–1053. (Acute spike; no baseline elevation in replete men)

### Diet and supplements
- Whittaker J, Wu K. **Low-fat diets and testosterone in men: Systematic review and meta-analysis of intervention studies.** *J Steroid Biochem Mol Biol* 2021;210:105878. PMID 33741447. (6 studies, n=206; SMD −0.52 in Western men)
- Pilz S, Frisch S, Koertke H, et al. **Effect of Vitamin D Supplementation on Testosterone Levels in Men.** *Horm Metab Res* 2011;43:223–225. PMID 21154195. (n=54, deficient men, +25% T — single trial; null in replete men: Lerchbaum 2017 JCEM)
- Prasad AS, Mantzoros CS, Beck FW, et al. **Zinc status and serum testosterone levels of healthy adults.** *Nutrition* 1996;12(5):344–348. PMID 8875519. (Zinc-deficient elderly → T +92% with repletion; zinc restriction in young men → T −73%)
- Lopresti AL, Drummond PD, Smith SJ. **A Randomized, Double-Blind, Placebo-Controlled, Crossover Study Examining the Hormonal and Vitality Effects of Ashwagandha (Withania somnifera) in Aging, Overweight Males.** *Am J Mens Health* 2019;13. PMC6438434. (+14.7% T vs. placebo; Shoden extract, n=57)
- Melville GW, Siegler JC, Marshall PW. **The effects of d-aspartic acid supplementation in resistance-trained men over a three month training period: A randomised controlled trial.** *PLoS One* 2017. PMC5571970. (Null at 6 g/day × 12 wk in trained men)
- Topo E, Soricelli A, D'Aniello A, et al. **The role and molecular mechanism of D-aspartic acid in the release and synthesis of LH and testosterone in humans and rats.** *Reprod Biol Endocrinol* 2009;7:120. (Positive in sedentary men — single trial, n=23)
- Naghii MR, Mofid M, Asgari AR, et al. **Comparative effects of daily and weekly boron supplementation on plasma steroid hormones and proinflammatory cytokines.** *Integr Med Insights* 2011;6:11–18. (Boron, n=8 — single uncontrolled trial)
- Tambi MI, Imran MK, Henkel RR. **Standardised water-soluble extract of Eurycoma longifolia, Tongkat ali, as testosterone booster for managing men with late-onset hypogonadism?** *Andrologia* 2012;44:226–230. PMID 21671978.
- Pandit S, Biswas S, Jana U, et al. **Clinical evaluation of purified Shilajit on testosterone levels in healthy volunteers.** *Andrologia* 2016;48:570–575. PMID 26395129. (n=75 men 45–55, +~20% total T)
- Van der Merwe J, Brooks NE, Myburgh KH. **Three weeks of creatine monohydrate supplementation affects dihydrotestosterone to testosterone ratio in college-aged rugby players.** *Clin J Sport Med* 2009;19(5):399–404. (DHT +56%; single trial)

### Weight loss
- Grossmann M. **Low testosterone in men with type 2 diabetes: significance and treatment.** *J Clin Endocrinol Metab* 2011;96:2341–2353. (Diet +2.9 nmol/L T per 10 kg; bariatric +8.7 nmol/L)
- Camacho EM, et al. **Body weight loss reverts obesity-associated hypogonadotropic hypogonadism: a systematic review and meta-analysis.** *Eur J Endocrinol* 2013;168:829–843. PMID 23482592.

### Opioids and alcohol
- Bawor M, Dennis BB, Bhalerao A, et al. **Testosterone suppression in opioid users: a systematic review and meta-analysis.** *Drug Alcohol Depend* 2015. (17 studies, n=2,769; T MD −164.78 ng/dL)
- Rajagopal A, Vassilopoulou-Sellin R, Palmer JL, et al. **Opioids and Their Endocrine Effects: A Systematic Review and Meta-analysis.** *JCEM* 2020;105(4):1020. PMC7054712.
- Santi D, et al. **The chronic alcohol consumption influences the gonadal axis in men: Results from a meta-analysis.** *Andrology* 2024;12:626. (21 studies, n=10,199; total T MD −4.02 nmol/L, E2 MD +7.65 pg/mL)

### South Asian-specific testosterone/SHBG data
- McTernan CL, McTernan PG, Harte AL, et al. **Migration is associated with lower total, but not free testosterone levels in South Asian men.** *Horm Metab Res* 2007. PMID 17900299.
- Bhatt SP, Nigam P, Misra A, et al. **Reduced total testosterone concentrations in young healthy South Asian men are partly explained by increased insulin resistance but not by altered adiposity.** *Metab Syndr Relat Disord* 2010. PMID 20550541. (Total T lower in SAs; free T comparable to European men due to lower SHBG)

### Finkelstein 2013
- Finkelstein JS, Lee H, Burnett-Bowie SAM, et al. **Gonadal Steroids and Body Composition, Strength, and Sexual Function in Men.** *N Engl J Med* 2013;369:1011–1022. PMID 24024838. (E2 mediates fat mass; both T and E2 mediate sexual function; anastrozole → fat gain + libido loss)

### Thyroid and selenium
- Toulis KA, Anastasilakis AD, Tzellos TG, et al. **Selenium Supplementation in the Treatment of Hashimoto's Thyroiditis: A Systematic Review and a Meta-analysis.** *Thyroid* 2010;20(10):1163–1173. (TPO Ab weighted mean difference −271 IU/mL; no TgAb or TSH effect)
- Huwiler VV, Maissen-Abgottspon S, Stanga Z, et al. **Selenium Supplementation in Patients with Hashimoto Thyroiditis: A Systematic Review and Meta-Analysis of Randomized Clinical Trials.** *Thyroid* 2024. PMC10951571. (Confirms antibody reduction; no clinical progression benefit)
- Stott DJ, Rodondi N, Kearney PM, et al. **Thyroid Hormone Therapy for Older Adults with Subclinical Hypothyroidism (TRUST trial).** *N Engl J Med* 2017;376:2534–2544. PMID 28402245. (n=737, mean age 74.4; levothyroxine → TSH normalized; zero symptom benefit)
- Xu Y, Derakhshan A, Hysaj O, et al. **The optimal healthy ranges of thyroid function defined by the risk of cardiovascular disease and mortality: systematic review and individual participant data meta-analysis (Thyroid Studies Collaboration).** *Lancet Diabetes Endocrinol* 2023;11(10):743–754. PMC10866328. (TSH mortality nadir 1.9–2.9 mIU/L)
- Hollowell JG, Staehling NW, Flanders WD, et al. **Serum TSH, T(4), and thyroid antibodies in the United States population (1988–1994): NHANES III.** *JCEM* 2002;87(2):489–499. (TPO 11.3%; TgAb 10.4% population prevalence)

### DIO2 and conversion
- Peeters RP, et al. **DIO2 Thr92Ala Reduces Deiodinase-2 Activity and Serum-T3 Levels in Thyroid-Deficient Patients.** *JCEM* 2017;102(5):1623. (rs225014 Ala/Ala → impaired local T4→T3; worse outcomes on T4 monotherapy)
- Bianco AC, Dumitrescu A, Gereben B, et al. **Paradigms of Dynamic Control of Thyroid Hormone Signaling.** *Endocr Rev* 2019;40(4):1000–1047. PMC6668716.

### SERMs and pharmacology
- Huijben M, et al. **Clomiphene citrate for men with hypogonadism: a systematic review and meta-analysis.** *Andrology* 2022;10:384–394. (LH +4.7 IU/L; FSH +4.6 IU/L; total T +273 ng/dL vs. placebo)

### Biotin interference
- Trambas CM, Sikaris KA, Lu ZX. **Chemistry of Biotin-Streptavidin and the Growing Concern of an Emerging Biotin Interference in Clinical Immunoassays.** *PMC6963918*. 2020.
- AACC/ADLM Guidance Document on Biotin Interference in Laboratory Tests. https://myadlm.org/science-and-research/academy-guidance/biotin-interference-in-laboratory-tests
- Cyprus J Med Sci 2025. **An Overview of Biotin Interference Impact on Immunoassays.** doi:10.2399/cjms.2025.2024-71

### Finasteride
- Propecia FDA NDA 20788 clinical pharmacology (DHT −65–72% serum; scalp DHT −56–64%; T +~15–20% compensatory at 1 mg/day)
- Kaufman KD, Olsen EA, Whiting D, et al. (1998) Finasteride dose-ranging study in AGA; Kaufman *JAAD* 1998;39(4):578–589.

### Cannabis
- Thistle JE, Graubard BI, Braunlin M, et al. **Marijuana use and serum testosterone concentrations among US males.** *Andrology* 2017;5(5):833–840. PMC5660879. (NHANES 2011–12, n=1,577; dose-response for time since last regular use in men 18–29)

### Cortisol variability
- Smyth JM, et al. **Variability and reliability of diurnal cortisol in younger and older adults.** PMC4165809. (CVI ~50% for diurnal cortisol; single draw reliability = 0.22)

### Miscellaneous
- Vanderpump MPJ et al. **Incidence of thyroid disorders: 20-year follow-up of the Whickham Survey.** *Clin Endocrinol* 1995. (TPO+ → ~2%/yr overt hypothyroidism; dual positive → ~4–5%/yr)
- Bartalena L et al. **2018 ETA Guidelines: Amiodarone-Associated Thyroid Dysfunction.** *Eur Thyroid J* 2018.
- Selva DM, Hogeveen KN, Innis SM, Hammond GL. **Monosaccharide-induced lipogenesis regulates the human hepatic sex hormone-binding globulin gene.** *J Clin Invest* 2007;117:3979–3987. (Insulin suppresses SHBG via HNF-4α pathway)

---

*This file documents effect sizes only. For marker biology, reference ranges, and clinical significance, see `hormones_male_panel.md` and `thyroid_panel.md`.*
