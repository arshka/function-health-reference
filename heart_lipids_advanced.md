# Advanced Lipid / Lipoprotein Markers — Reference for a 20-Year-Old Male

A deep-dive interpretation guide for the seven advanced lipid markers reported on Function Health: **LDL-P, LDL Peak Size, LDL Pattern, LDL Small, LDL Medium, HDL Large, and Lipoprotein(a)**. The conventional lipid panel (LDL-C, HDL-C, TG, total cholesterol, non-HDL-C, ApoB) is covered elsewhere; this document is exclusively the *advanced* lipoprotein layer plus Lp(a).

> **Note on provenance.** Quantitative claims are tagged with named sources (author/year/journal or guideline). Where the literature is contested or assays disagree, that is flagged inline. "Optimal" for a healthy 20-year-old male is treated as the lifetime-exposure-minimization target advocated by Sniderman, Attia, and the ESC/EAS — it is more aggressive than population-mean "normal."

---

## 1. Conceptual Foundation: Why Advanced Lipid Testing Exists

### 1.1 The particle-count paradigm

Atherosclerosis is initiated when **apoB-containing lipoprotein particles** (LDL, IDL, VLDL remnants, and Lp(a)) cross the endothelium and become trapped in the subendothelial matrix. **Every** atherogenic particle carries exactly one apoB-100 molecule (Sniderman et al., *Circulation: Cardiovascular Quality and Outcomes* 2011; Behbodikhah et al., *Metabolites* 2021). The driver of risk is therefore not *cholesterol mass inside* the particles (LDL-C), but the *number of particles* delivering apoB to the artery wall.

LDL-C and particle number (LDL-P or apoB) are correlated (~r = 0.7–0.9) but **discordant in 20–30% of individuals** (Otvos et al., *Journal of Clinical Lipidology* 2011). When discordant, **risk tracks the particle count, not the cholesterol** (Cromwell et al., *J Clin Lipidol* 2007 — Framingham Offspring; Otvos et al., *Atherosclerosis* 2014).

### 1.2 The three measurement platforms

| Method | Measures | Vendor | Units |
|---|---|---|---|
| **NMR (LipoProfile)** — used by LabCorp, Function Health, Cleveland HeartLab | Particle concentration of all lipoprotein subclasses from lipid methyl-group NMR signals | LabCorp/LipoScience (Otvos) | nmol/L for LDL-P; mg/dL for LDL-C |
| **Ion mobility (Cardio IQ)** | Gas-phase electrical mobility separation; gives true particle counts and sizes | Quest/Berkeley HeartLab | nmol/L |
| **Vertical Auto Profile (VAP)** | Density-gradient ultracentrifugation, spectrophotometric absorbance | Atherotech (defunct) / regional labs | mg/dL of cholesterol per subclass |

**The methods do not give interchangeable results.** In a head-to-head analysis, three-way concordance for LDL-P, sdLDL, and HDL-P was only 63%, and complete agreement across four LDL-size methods (NMR, GGE, VAP, TGE) was only 8% (Sninsky et al., *Circulation* 2015 abstract 18619). VAP tends to flag small LDL more often; ion mobility tends to under-report large HDL-P. **Conclusion: never compare across labs/methods. Track changes within one method.**

### 1.3 Function Health uses NMR (LabCorp LipoProfile-3)

All seven markers in this report are best interpreted on the LabCorp NMR LipoProfile reference frame. Subclass cutpoints below are NMR cutpoints (Jeyarajah et al., *Clin Lab Med* 2006; Mallol et al., *Frontiers in Nuclear Medicine* 2022).

---

## 2. LDL Particle Number (LDL-P)

### 2.1 What it is

**LDL-P is the total concentration of LDL particles in the blood**, summing all LDL subclasses (large LDL + medium LDL + small LDL + IDL contribution depending on algorithm). Reported in nmol/L. On NMR, it is computed as the sum of subclass particle concentrations derived from the methyl-lipid signal at ~0.84 ppm; concentration scales with particle count rather than cholesterol mass (Jeyarajah, Otvos, *Clin Lab Med* 2006).

LDL-P is conceptually similar to apoB but not identical: apoB counts **all** atherogenic particles (LDL + IDL + VLDL + chylomicron remnants + Lp(a)), whereas LDL-P counts only those classified as LDL by NMR. Their correlation in the Framingham Offspring cohort is ~r² = 0.79 (Cromwell, *J Clin Lipidol* 2007). When ApoB and LDL-P disagree, the most common cause is excess VLDL/IDL or Lp(a) contribution — i.e., insulin resistance (Wilkins et al., *J Clin Lipidol* 2014).

### 2.2 Mechanism / atherogenicity

LDL-P represents the *flux* of apoB particles delivered to the endothelium per unit time. Each particle that enters the intima can be retained by proteoglycans, oxidized, and engulfed by macrophages (foam cells) — the initiating cellular event of atherosclerosis (Borén et al., EAS Consensus, *Eur Heart J* 2020). Particle number, not cholesterol mass, is what determines retention probability.

### 2.3 What HIGH LDL-P means

- **Genetic**: heterozygous familial hypercholesterolemia (HeFH; ~1 in 220 — Hopkins et al., *J Clin Lipidol* 2011), familial combined hyperlipidemia (FCHL — Veerkamp et al., *ATVB* 2003 — small dense LDL + ↑ApoB are *the* signature of FCHL)
- **Insulin resistance / metabolic syndrome / NAFLD**: hepatic VLDL overproduction → TG-rich VLDL → CETP-mediated exchange → small dense LDL particles → high *particle count* even when LDL-C looks normal (Krauss, *Curr Opin Lipidol* 2010)
- **Diet**: high refined carbohydrate intake, alcohol excess, sedentary lifestyle
- **Hypothyroidism** (reduces LDL receptor activity)
- **Discordance with normal LDL-C** is most common when small LDL predominates: each particle carries less cholesterol so total cholesterol looks fine but particle count is high (Otvos, *J Clin Lipidol* 2011)

### 2.4 What LOW LDL-P means

LDL-P below ~700 nmol/L is uniformly protective. There is **no observed floor of harm** in epidemiologic data (Mendelian randomization studies of PCSK9 loss-of-function variants show lifetime LDL-P/apoB ~50% of normal correlates with ~88% lower CHD events — Cohen et al., *NEJM* 2006). Direction is **monotonic: lower is better**.

### 2.5 Reference ranges (LabCorp NMR — used by Function Health)

| Category | LDL-P (nmol/L) |
|---|---|
| Optimal | < 1,000 |
| Above optimal | 1,000–1,299 |
| Borderline-high | 1,300–1,599 |
| High | 1,600–2,000 |
| Very high | > 2,000 |

(Source: LabCorp NMR LipoProfile reference document L15035; aligns with NIH ATP-III categorical thresholds).

### 2.6 Optimal for a healthy 20-year-old male

- **Sniderman / Attia view**: < 700 nmol/L (~5th percentile). Attia's verbal target is ApoB ~30–60 mg/dL, which corresponds to LDL-P roughly 700–900 nmol/L (Attia, *AMA #43* 2022).
- **NLA "very high risk" target on therapy**: LDL-P < 1,000 (adapted from ApoB < 80 mg/dL).
- **Pragmatic 20-year-old male target**: < 1,000 nmol/L; ideally < 800. Lifetime cumulative apoB exposure determines plaque burden by age 50–60 (Borén et al., *Eur Heart J* 2020), so the cleanest decade-long trajectory is the most valuable intervention available.

### 2.7 Confounders

- **Statins drop LDL-C more than LDL-P** (Otvos, *J Clin Lipidol* 2011). On a statin, LDL-C may look "at target" while LDL-P remains elevated — this discordance is one of the most clinically actionable findings of NMR testing.
- **Insulin resistance**: high TG → small LDL → discordant high LDL-P relative to LDL-C
- **Acute illness/inflammation** transiently lowers LDL-P
- **Thyroid dysfunction**: hypothyroidism raises LDL-P; hyperthyroidism lowers it

---

## 3. LDL Peak Size

### 3.1 What it is

The **mean diameter (in nm) of the predominant LDL particle population**, measured by NMR LipoProfile (Mallol, *Frontiers in Nuclear Medicine* 2022). It is a *single number* summarizing where the mode of the LDL-size distribution falls.

NMR identifies four LDL subclasses (Jeyarajah, *Clin Lab Med* 2006):
- IDL: ~25 nm
- Large LDL: ~22 nm (range 21.3–22.7)
- Medium LDL ("intermediate"): ~20.5 nm
- Small LDL: ~19 nm (range 18.3–19.7)

### 3.2 Mechanism

Smaller LDL particles are more atherogenic per particle because they:
1. Penetrate the endothelium more efficiently (size-restricted diffusion)
2. Bind arterial wall proteoglycans more tightly (increased negative surface charge, reduced sialic acid — Anber et al.)
3. Are more susceptible to oxidation (lower antioxidant content)
4. Have longer plasma residence time (lower LDL-receptor affinity)

(Reviewed in Hoogeveen et al., *J Lipid Res* 2014; the 2025 *Front Cardiovasc Med* update by Vega et al.)

### 3.3 What SMALL peak size means

Peak size below ~20.5 nm = "small/dense predominant" = **Pattern B**. Driver: insulin resistance / metabolic syndrome (see §5 below).

### 3.4 What LARGE peak size means

Peak size above ~21.2–21.5 nm = "large LDL predominant" = **Pattern A**. Generally favorable, but a high *count* of large LDL particles still drives risk (LDL-P matters more than size — Mora et al., *Circulation* 2009 from the Women's Health Study; *the relation of LDL-P to events is mediated by small and intermediate LDL contribution*).

### 3.5 Direction of "better"

**Larger is better — but the magnitude of the effect is small once LDL-P is accounted for.** Peak size is mostly a *marker* for the metabolic state (insulin sensitivity), not an independent driver beyond particle count. In MESA, after adjustment for LDL-P, LDL size lost most independent association with carotid IMT (Mora et al., *Atherosclerosis* 2007 — MESA).

### 3.6 Reference range (NMR)

| Category | LDL Peak Size (nm) |
|---|---|
| Pattern A (large) | > 20.5 (some labs: > 20.6 or 21.2) |
| Pattern A/B intermediate | 20.5–20.6 |
| Pattern B (small) | < 20.5 |

(LabCorp NMR LipoProfile cutpoints; Otvos et al.)

### 3.7 Optimal for 20-year-old male

> 21.0 nm — corresponding to a metabolically clean state with low TG, normal insulin, and dominant large LDL.

### 3.8 Confounders

- **Triglycerides** are the strongest non-genetic determinant: TG > 130 mg/dL drives the small-LDL phenotype via CETP-mediated TG/CE exchange (Krauss).
- **Adiposity** — Krauss et al. showed 81% of Pattern B men converted to Pattern A when BMI dropped below 25 (*Atherosclerosis* 2010 / earlier work).
- **Postprandial state** transiently increases small LDL precursor production.

---

## 4. LDL Pattern (A vs. B)

### 4.1 What it is

A categorical summary of LDL size distribution, originally defined by Krauss & Burke (*J Lipid Res* 1982) using gradient gel electrophoresis. NMR adapts the categorization based on peak size.

- **Pattern A** = predominantly large, buoyant LDL (peak diameter > 20.5 nm). Lower atherogenicity per particle.
- **Pattern B** = predominantly small, dense LDL (peak diameter ≤ 20.5 nm). 3-fold higher CVD risk than Pattern A *independent of LDL-C* in early Krauss-era studies (Austin, Krauss et al., *Circulation* 1990).
- **Pattern A/B (intermediate)** = mixed.

### 4.2 Genetics and metabolic drivers

- Heritability ~35–60% (twin studies). The **ATHS (atherogenic lipoprotein phenotype)** clusters: high TG + low HDL + Pattern B + insulin resistance — sometimes called the "lipid triad" of metabolic syndrome.
- In familial combined hyperlipidemia (FCHL), small dense LDL + elevated apoB are the *unifying signature* across the three FCHL phenotypes (Veerkamp et al., *ATVB* 2003).
- Pattern B is one of the four NCEP ATP-III emerging risk factors and is part of the 2005 IDF/AHA metabolic syndrome construct (though not a defining criterion).

### 4.3 What HIGH risk (Pattern B) means

- Insulin resistance, T2D, prediabetes, NAFLD, central obesity, metabolic syndrome
- Diet pattern dominated by refined carbohydrates / sugar
- Postprandial hypertriglyceridemia
- Genetic FCHL or polygenic insulin-resistance risk
- ~3-fold CVD risk increase vs. Pattern A *before adjustment for particle number* (Austin, Krauss, *Circulation* 1990)

### 4.4 Direction of "better"

**Pattern A > Pattern A/B > Pattern B.** But again, modern view (Otvos, Sniderman): once LDL-P/apoB is measured, the marginal value of "Pattern" alone is modest. Pattern B is most useful as a **flag for insulin resistance** that should prompt fasting insulin, HOMA-IR, HbA1c, and TG/HDL ratio review.

### 4.5 Modifiability

Highly modifiable. Krauss group demonstrated that weight loss, low-saturated-fat / low-refined-carb diets, and exercise can convert Pattern B → A within months. ~80% conversion when BMI normalizes to < 25 (Krauss et al.).

### 4.6 Optimal for 20-year-old male

**Pattern A**, with peak size > 21.0 nm. If Pattern B at age 20: investigate insulin resistance immediately — fasting insulin, HbA1c, TG, ALT/AST for NAFLD, waist circumference. Pattern B at 20 is a near-guaranteed precursor to T2D unless reversed.

---

## 5. LDL Small (small dense LDL particles, sdLDL)

### 5.1 What it is

Concentration of LDL particles with diameter approximately 18.3–19.7 nm, measured by NMR (units: nmol/L). On Quest/Cardio IQ, sdLDL-C is reported in mg/dL of cholesterol contained in small dense LDL — these are different units measuring different things (count vs. cholesterol mass). On Function Health (LabCorp NMR), Small LDL-P is the **count**.

### 5.2 Mechanism

The most atherogenic LDL subclass (Hoogeveen, *J Lipid Res* 2014). Mechanisms:
1. **Enhanced endothelial penetration** — smaller particles diffuse across the endothelial barrier more readily
2. **Increased proteoglycan binding** — modified surface chemistry (lower sialic acid, higher negative charge, reduced phospholipid) increases retention in the intima
3. **Greater oxidation susceptibility** — lower endogenous antioxidant content (vitamin E, ubiquinol-10)
4. **Reduced LDL-receptor affinity** — leads to longer plasma residence (~5 days vs. ~2 days for large LDL), more time to be modified
5. **Preferential uptake by macrophage scavenger receptors** — directly fuels foam cell formation
(Reviewed in Krauss, *Curr Opin Lipidol* 2010; Sniderman et al.)

### 5.3 What HIGH small LDL means

The hallmark of **insulin resistance**. Pathway:
- Hepatic VLDL overproduction (high TG)
- CETP transfers TG from VLDL onto LDL → TG-enriched LDL
- Hepatic lipase hydrolyzes the TG → smaller, denser LDL remnant
- Net result: shift of LDL distribution toward small/dense

This is why high small LDL almost always co-travels with: ↑ TG, ↓ HDL-C, ↑ fasting insulin, ↑ ALT (NAFLD), waist circumference, and HbA1c creep.

Also seen in: FCHL (Veerkamp, *ATVB* 2003), uncontrolled T2D, hypothyroidism, chronic kidney disease.

### 5.4 What LOW small LDL means

Protective. **Monotonic — lower is better.** Optimal small LDL-P is essentially at the assay floor.

### 5.5 Reference range (LabCorp NMR)

| Category | Small LDL-P (nmol/L) |
|---|---|
| Optimal | < 527 |
| Borderline-high | 528–744 |
| High | ≥ 745 |

(LabCorp/LipoScience reference; OptimalDx aggregations)

### 5.6 Optimal for 20-year-old male

**< 200 nmol/L** is what a metabolically pristine 20-year-old looks like; < 527 is the formal "optimal" cutoff. Anything > 500 at age 20 is a strong insulin-resistance flag even if BMI looks normal — TOFI ("thin outside fat inside") phenotype.

### 5.7 Confounders

- **TG levels** are the dominant driver (TG > 130 mg/dL → small LDL).
- **Recent dietary carbohydrate load** transiently raises sdLDL.
- **Statins lower large LDL more than small LDL** — patients on statins can show "discordance" with small LDL persistently elevated (Krauss, *J Clin Lipidol* 2008).
- **Fibrates and pioglitazone** preferentially lower small LDL.

---

## 6. LDL Medium

### 6.1 What it is

LDL subclass particles of approximately 20.5 nm diameter (range 20.0–20.8), reported in nmol/L. NMR LipoProfile-3 separates medium LDL from small and large LDL based on its distinct lipid methyl signal.

### 6.2 Clinical significance

Medium LDL is often described as **"intermediate atherogenicity"** — between small and large. In the NMR-based studies of incident CVD, the *combined* contribution of medium + small LDL accounts for most of the LDL-P attributable risk (Mora et al., *Circulation* 2009 — Women's Health Study).

Medium LDL on its own has received much less attention than small LDL or peak size. It does not have its own Mendelian randomization or large-cohort meta-analysis; its primary clinical use is **as a component of LDL-P** and as a sensitive marker of *transition* between Pattern A and Pattern B states.

### 6.3 Direction of "better"

In isolation: **lower is better, monotonically**, but the effect size is modest after adjusting for total LDL-P. There is no defined "floor" of harm.

### 6.4 Reference range

NMR labs (LabCorp/LipoScience) typically do not publish a dedicated optimal cutoff for medium LDL alone. Population median is approximately 200–400 nmol/L. Labcorp reports it in the LipoProfile graphical breakdown but does not categorize it as optimal/borderline/high in the way Small LDL-P or LDL-P are categorized.

### 6.5 Optimal for 20-year-old male

Total LDL-P < 1,000 with proportional medium LDL < ~300 nmol/L is consistent with a Pattern A profile in a young, lean, insulin-sensitive male. Treat the **total LDL-P + small LDL** as the actionable numbers; medium LDL is informational.

### 6.6 Confounders

Same as Small LDL: TG, insulin resistance, statin therapy (statins reduce medium LDL more than small LDL).

---

## 7. HDL Large (large HDL particles)

### 7.1 What it is

The concentration of large HDL particles (~9.4–14.0 nm diameter on NMR; HDL2 subclass on density-gradient ultracentrifugation), reported in μmol/L. Includes HDL2a and HDL2b. Cholesterol-rich, lipid-loaded mature HDL particles.

NMR LipoProfile reports total HDL-P (μmol/L) and its three subclass concentrations: large, medium, small (Jeyarajah, *Clin Lab Med* 2006).

### 7.2 Mechanism — and why it's the most contested marker

The traditional model: large HDL = mature HDL = cholesterol-loaded by ABCA1/LCAT, ready to deliver cholesterol back to the liver via SR-BI = the *protective* form. Small HDL = nascent / pre-β = pickup form. Reverse cholesterol transport (RCT) is the central function.

But the past 15 years overturned this clean picture:

1. **CETP inhibitor failures**: Torcetrapib (ILLUMINATE, 2007), dalcetrapib (dal-OUTCOMES, 2012), evacetrapib (ACCELERATE, 2017) all *raised* HDL-C dramatically (30–130%) without reducing CVD events — and torcetrapib *increased* mortality. This decoupled "raising HDL-C / large HDL" from clinical benefit (Barter et al., *NEJM* 2007; Schwartz et al., *NEJM* 2012; Lincoff et al., *NEJM* 2017). **Anacetrapib** (REVEAL, 2017) showed a marginal benefit but was not commercialized. **Obicetrapib** (Phase 3 BROOKLYN/BROADWAY, 2025) shows ~37% LDL-C reduction and ~37% Lp(a) reduction with HDL-C ~+135%, and a pooled analysis suggested cardiovascular benefit (Nicholls et al., *JACC* 2025) — but the benefit is now attributed to the LDL-C and Lp(a) reductions, *not* HDL-C raising.

2. **Niacin failures**: AIM-HIGH (2011) and HPS2-THRIVE (2014) found niacin (which raises HDL-C ~25%) did not reduce events on top of statin therapy.

3. **Mendelian randomization** (Voight et al., *Lancet* 2012) showed genetic variants raising HDL-C are *not* associated with lower MI risk, while LDL-C–raising variants are. **HDL-C is not causal.**

4. **Dysfunctional HDL** (Heinecke and colleagues, *J Clin Invest* and follow-on work): HDL function — particularly **cholesterol efflux capacity (CEC)** — predicts CVD better than HDL-C. CEC is impaired in CAD, T2D, CKD, and inflammation, even when HDL-C is normal or high. Khera et al., *NEJM* 2011; Rohatgi et al., *NEJM* 2014 (Dallas Heart Study) — CEC inversely associated with incident events independent of HDL-C.

5. **JUPITER analyses** (Mora, Ridker et al., *Circulation* 2013): On potent statin therapy, HDL-C lost predictive value for residual risk. **HDL particle number** (HDL-P) — not HDL-C, not HDL size — remained the strongest inverse predictor. CEC was *also* predictive (Khera, *NEJM* 2017 JUPITER analysis).

6. **JUPITER CEC analysis** (Khera et al., *NEJM* 2017): impaired CEC predicted events; HDL-C did not.

### 7.3 So is large HDL good or bad?

Mixed and population-dependent:

- In **MESA** (Mackey et al., *JACC* 2012; subsequent kidney-function-stratified analyses), large HDL-P was inversely associated with CVD events.
- In a Chinese CAD cohort (Tian et al., *Medicine* 2016), **large HDL-C** was the *only* HDL subfraction associated with CAD severity and outcomes — inversely. Large HDL-C, not HDL-C, tracked with risk.
- In the GENES study (*Sci Rep* 2020), HDL particle number (total) was independently associated with prognosis after CAD — an *inverse* association.
- However, in **heart failure** populations, *larger HDL particle size* has been associated with *worse* outcomes (paradoxical) — possibly reflecting impaired RCT/maturation pathology rather than abundance of healthy mature HDL (Hunter et al., other HF studies).
- **Some recent work** suggests small/medium HDL has direct anti-inflammatory and anti-oxidative actions (protecting LDL from oxidation) that large HDL lacks — i.e., size and function are dissociable.

### 7.4 Direction of "better": NOT MONOTONIC

This is the single most important takeaway:
- **HDL-C: not causal, not a treatment target.** Raising HDL-C pharmacologically has failed in 5 large outcome trials.
- **Large HDL: probably U-shaped.** Higher is associated with lower risk in *most* observational studies, but *very* high HDL-C (>80–90 mg/dL) has been associated with paradoxically increased mortality and infection risk in some cohorts (Madsen et al., *Eur Heart J* 2017 — Copenhagen General Population Study).
- **HDL particle number (total HDL-P): probably the best summary** — inversely associated with risk in JUPITER and MESA.
- **Cholesterol efflux capacity (functional HDL): the most predictive measure**, but not on routine panels.

### 7.5 What HIGH large HDL means

Genetic CETP loss-of-function variants, genetic high HDL-C, alcohol intake (small-to-moderate), high-fat diets (esp. monounsaturated), exercise, premenopausal female sex hormones, weight loss. Most of these are favorable contexts. But high HDL-C in the context of inflammation, kidney disease, or genetic SR-BI mutation can paradoxically *not* be protective.

### 7.6 What LOW large HDL means

Insulin resistance, metabolic syndrome, T2D, obesity, smoking, anabolic steroid use, chronic inflammation. CETP-mediated TG enrichment of HDL → hepatic lipase remodeling → small HDL with rapid catabolism → low total HDL-P and low large HDL.

### 7.7 Reference range (LabCorp NMR)

LabCorp reports HDL Large in μmol/L. Typical population reference is approximately:
- **Total HDL-P optimal**: > 30 μmol/L (men); > 35 μmol/L (women) — Mayo Clinic Labs, NMR LipoProfile reference
- **HDL Large**: > 6.7 μmol/L often cited as favorable; population mean ~5–7 μmol/L

These are approximate — there is no single agreed-on "optimal."

### 7.8 Optimal for a 20-year-old male

**Total HDL-P > 35 μmol/L** with **HDL Large > 7 μmol/L**, in the context of a normal HDL-C (40–60 mg/dL), low TG (< 80 mg/dL), and normal apoB. *Do not pharmacologically chase HDL elevation.* The five trials of HDL-raising drugs collectively cost ~$5 billion and produced no benefit. Treat HDL Large as a marker of metabolic health, not a treatment target.

### 7.9 Confounders

- Alcohol — raises HDL-C and large HDL; not a reason to drink more
- Exercise raises HDL-P
- Anabolic steroids dramatically *suppress* HDL — relevant if user lifts and supplements
- Chronic inflammation (CRP, IL-6) impairs HDL function even if HDL-C is preserved (acute phase)
- Statins minimally affect HDL-P; fibrates raise it modestly

---

## 8. Lipoprotein(a) — Lp(a)

> **The most important section of this report.** Lp(a) is the most underdiagnosed, most strongly genetic, and now most actively druggable major cardiovascular risk factor. Approximately 20–25% of the population has elevated Lp(a) (~1.4 billion globally), and most do not know it. For a 20-year-old, this is a once-in-a-lifetime measurement with disproportionate downstream value.

### 8.1 What Lp(a) is — the structure

Lp(a) is an LDL-like particle with a single apolipoprotein(a) — **apo(a)** — covalently linked via a single disulfide bond to apoB-100 on the LDL surface (Reyes-Soffer et al., *ATVB* 2022 — AHA Scientific Statement; Marcovina, Koschinsky).

Apo(a) is a plasminogen homolog. It contains:
- A protease-like (but inactive) domain
- One **kringle V (KV)** domain
- Multiple **kringle IV (KIV)** domains, sub-classified into KIV-1 through KIV-10

The number of **KIV-2 repeats is highly variable** (3 to >40 copies), creating apo(a) isoforms ranging from ~300 to >800 kDa (Lackner et al., *J Clin Invest* 1991; Marcovina et al.).

**Critical inverse relationship**: fewer KIV-2 repeats → smaller apo(a) isoform → higher plasma Lp(a) concentration. The mechanism is that smaller apo(a) is secreted faster and degraded less efficiently. Carriers of small isoforms (≤22 KIV repeats) have ~3-fold higher CHD risk (Erqou et al., *JAMA* 2009; Saleheen et al., *PROMIS*).

The LPA gene on chromosome 6q26-27 controls plasma Lp(a) levels with **~80–90% heritability** — essentially Mendelian for a quantitative trait. Lp(a) levels at age 5 are nearly identical to levels at age 75. This is a *fixed genetic risk factor*.

### 8.2 What is being measured — and why standardization is a mess

There are two ways to report Lp(a):

1. **Mass-based (mg/dL)**: measures the total mass of the Lp(a) particle, including apo(a). Because apo(a) mass varies 3-fold across isoforms, mass assays are **isoform-sensitive** — they over-estimate when apo(a) is large and under-estimate when apo(a) is small (or vice versa, depending on the calibration). Older Lp(a) mg/dL assays missed the most dangerous small-isoform / high-concentration phenotype.

2. **Molar (nmol/L) — particle number**: counts the number of Lp(a) particles. Modern monoclonal-antibody-based assays (e.g., the Denka assay) use antibodies against epitopes outside the variable KIV-2 region and are therefore **isoform-insensitive**. The IFCC (Internationla Federation of Clinical Chemistry) Working Group has developed a mass spectrometry reference measurement procedure expressing results in nmol/L (Cobbaert et al., *Clin Chem* 2024).

**The mg/dL ↔ nmol/L conversion is NOT a fixed factor.** A common rule-of-thumb is 1 nmol/L ≈ 0.4 mg/dL, but the actual ratio varies from 1.82 to 3.64 depending on isoform (Tate et al.; Marcovina). The NLA explicitly recommends **against using a fixed conversion factor** (Wilson et al., 2024 NLA focused update, *J Clin Lipidol*).

**Practical consequence**: if your result is in nmol/L, do not multiply by 0.4 to get mg/dL or vice versa. Track within the same assay. Function Health (Quest backend) typically reports nmol/L using the Denka isoform-insensitive assay — confirm on the report.

### 8.3 Mechanism / atherogenicity — three converging pathways

Lp(a) drives disease through three mechanisms (Reyes-Soffer 2022 AHA Scientific Statement):

1. **Atherogenesis (LDL-like)**: Lp(a) carries an apoB-100-containing LDL particle that penetrates the intima and contributes to plaque formation. Mass-for-mass, Lp(a) is *more* atherogenic than LDL because of mechanism #2.

2. **Oxidized phospholipid (OxPL) carrier**: Lp(a) is the **predominant carrier of oxidized phospholipids in plasma**. OxPLs covalently bind to apo(a) (KIV-10 domain especially). OxPL-apoB and OxPL-apo(a) are pro-inflammatory and pro-calcific — they activate monocyte trafficking, induce arterial wall inflammation, and drive valvular calcification (Tsimikas, Witztum; *Circulation* 2017 — van der Valk et al.; *J Lipid Res* 2024). This is *why* Lp(a) drives **calcific aortic valve stenosis** specifically — Lp(a) deposits in valve tissue, OxPL drives osteogenic differentiation of valvular interstitial cells.

3. **Antifibrinolysis / prothrombosis**: apo(a) is structurally homologous to plasminogen but enzymatically inactive. It competes with plasminogen for binding to fibrin and cell surfaces, *inhibiting* fibrinolysis and promoting thrombosis. This contributes to acute thrombotic events on top of Lp(a)-driven plaque (Boffa, Koschinsky).

### 8.4 Causality — the Mendelian randomization story

The case for Lp(a) causality in coronary disease is among the strongest in cardiology:

- **Kamstrup et al., *JAMA* 2009** (Copenhagen City Heart Study): observational + genetic data showed extreme Lp(a) (top 5%, > ~120 mg/dL) → 3-4-fold MI risk. Genetic variants in *LPA* causing high Lp(a) showed the same effect → causal.
- **Clarke et al., *NEJM* 2009** (PROCARDIS): two SNPs in *LPA* (rs10455872, rs3798220) associated with smaller apo(a) isoform, higher Lp(a), and CHD with OR ~1.7-1.9.
- **Burgess et al., *JAMA Cardiology* 2018**: comprehensive MR analysis confirmed dose-response — each 10 mg/dL absolute increase in Lp(a) corresponds to ~5.8% relative increase in CHD risk over a lifetime.
- **Trinder et al., *Nature Medicine* 2024** and broader phenome-wide MR: confirmed causal effects on CHD, ischemic stroke, peripheral artery disease, and aortic stenosis. Suggestive but not confirmed for venous thromboembolism.

### 8.5 Lp(a) and aortic stenosis — a unique disease association

Lp(a) is the *only* established **causal risk factor for calcific aortic valve disease (CAVD)** — even more specifically than for coronary disease.

- **Thanassoulis et al., *NEJM* 2013**: GWAS identified rs10455872 in *LPA* → 60–68% per-allele increase in aortic stenosis risk; Mendelian randomization confirmed causality.
- **Kamstrup et al., *JACC* 2014**: in the Copenhagen General Population Study, Lp(a) > 90 mg/dL → ~3-fold aortic stenosis risk vs. < 5 mg/dL.
- **Mechanism**: Lp(a) and OxPL accumulate in valvular tissue → osteogenic transformation of valvular interstitial cells → calcification.

**Implication for a 20-year-old with elevated Lp(a)**: lifetime risk of aortic stenosis is non-trivial; warrants a baseline echocardiogram by age 35–40 if Lp(a) is markedly elevated, with serial follow-up.

### 8.6 What HIGH Lp(a) means

The cause is **almost always genetic** (~80–90%). Non-genetic modifiers are minor:
- Estrogen (post-menopausal women see increases)
- Renal disease (CKD raises Lp(a))
- Acute inflammation can transiently elevate
- Hypothyroidism raises modestly
- Niacin lowers ~20% (variable, up to 40%)
- PCSK9 inhibitors lower ~20–30% (Watts et al., evolocumab and alirocumab data)

There is NO strong lifestyle modifier. Diet, exercise, weight loss, smoking cessation — none meaningfully change Lp(a). This is genetics.

**~20–25% of the population has Lp(a) > 50 mg/dL (~125 nmol/L)** (Reyes-Soffer 2022 AHA). The distribution is non-Gaussian and extremely right-skewed.

**Ethnic variation** is large (Tsimikas, Steffen, MESA; Patel et al., *Circulation* 2021):
- Median Lp(a) (nmol/L): Chinese ~16, White ~19, South Asian ~31, Black ~75 — roughly 4-fold range
- Black individuals have the highest median; Asian individuals the lowest
- The 50 mg/dL threshold is set against a Caucasian reference and may need ethnic adjustment

### 8.7 What LOW Lp(a) means

Protective. **Direction is monotonic — there is NO known floor of harm for low Lp(a).** This is in contrast to LDL-C (where extreme low values may have neurologic edge concerns) and HDL-C (U-shaped). In the entire MR literature, no detrimental effect of low Lp(a) has been identified. Loss-of-function *LPA* variants are not associated with disease.

### 8.8 Risk thresholds and reference ranges

Multiple guideline cutoffs exist; they are not perfectly harmonized:

| Source | Risk threshold |
|---|---|
| 2019 NLA / 2024 NLA focused update (Wilson et al., *J Clin Lipidol*) | High risk: ≥ 125 nmol/L (≥ 50 mg/dL); intermediate: 75–125 nmol/L (30–50 mg/dL); low: < 75 nmol/L (< 30 mg/dL) |
| 2019 EAS Consensus (Mach et al., *Eur Heart J*) | ≥ 50 mg/dL (corresponds to ~80th percentile in Caucasians) |
| 2022 AHA Scientific Statement (Reyes-Soffer) | "High" ≥ 50 mg/dL (~125 nmol/L); "very high" ≥ 100 mg/dL (~250 nmol/L) |
| 2025 ESC/EAS Focused Update | Elevated > 50 mg/dL or > 105 nmol/L |
| Family Heart Foundation | "Optimal" < 30 mg/dL (~75 nmol/L) |
| Tsimikas / many lipidologists | Truly low risk: < 30 nmol/L (~12 mg/dL) |

### 8.9 Optimal for a 20-year-old male

**< 30 nmol/L (~< 14 mg/dL)** is what you'd hope for — bottom quintile, lifetime low-risk. **< 75 nmol/L (~< 30 mg/dL)** is the formal NLA "low risk" cutoff. Anything above 125 nmol/L (~50 mg/dL) is a high-risk genotype warranting:

1. **Confirm with a second test** in a different lab — assay variability, although Lp(a) is otherwise stable
2. **Aggressive control of all modifiable risk factors**: target apoB ≤ 60 mg/dL (Attia threshold; Sniderman view), BP < 120/80, no smoking, normal HbA1c, regular cardio + resistance training
3. **Cascade screen first-degree relatives** (NLA recommendation)
4. **Coronary calcium scan at age 35–40** (or earlier if family history of premature CVD)
5. **Discuss future Lp(a)-targeted therapy** (see §8.11)

### 8.10 Test once, test correctly

The 2024 NLA focused update and 2019 EAS consensus both recommend **measuring Lp(a) at least once in every adult** (including at age 20+) — for risk stratification.

- **Not fasting required.** Lp(a) is essentially unaffected by meals (varies 17 vs. 19 mg/dL fasting vs. fed in studies).
- **Stable across the lifespan from age ~5.** Intra-individual variability is <10% in most adults.
- **Recent challenges to absolute stability** (Schmidt et al., STAR-Lp(a), 2024): in some patients, Lp(a) varied >20% over years. Periodic reassessment is reasonable in patients near the decision threshold.
- **Repeat testing indications**: kidney disease, post-menopause (women), acute inflammatory illness, after large dietary/weight change.

### 8.11 Treatment landscape

**Currently FDA-approved targeted Lp(a) therapy: NONE (as of 2024–2025).**

**Modest-effect, non-targeted therapies**:
- PCSK9 inhibitors (evolocumab, alirocumab): lower Lp(a) ~20–30% (insufficient as standalone Lp(a) therapy, but useful adjunctive). Mechanism: probably increased apoE-mediated clearance, since Lp(a) does not engage the LDL receptor strongly.
- Niacin: ~20% reduction (up to 40% in some patients), but failed in outcome trials. Not first-line.
- Lipoprotein apheresis (FDA-approved for Lp(a) > 60 mg/dL with established CVD): ~60–70% per-session reduction, weekly or biweekly. Last-resort.
- Statins: do **not** lower Lp(a); some data suggest a modest *increase* on statin therapy.
- Inclisiran (PCSK9 siRNA): similar Lp(a) reduction profile to monoclonal PCSK9i.

**Pipeline — targeted Lp(a) therapeutics** (Phase 2/3 active 2024–2025):
- **Pelacarsen (TQJ230)** — antisense oligonucleotide (ASO) against *LPA* mRNA, monthly subcutaneous injection. Phase 2 showed ~80% Lp(a) reduction. Phase 3 outcomes trial: **Lp(a)HORIZON** (NCT04023552), 8,323 patients with prior CVD and Lp(a) ≥ 70 mg/dL. Results expected late 2025 or 2026 (Tsimikas et al., *NEJM* 2020 phase 2; Yeang et al., trial design in *Am Heart J* 2025).
- **Olpasiran** — siRNA, every-12-week dosing, ~95% Lp(a) reduction at peak. Phase 2 OCEAN(a)-DOSE published in *NEJM* 2022 (Nissen et al.) showed ~95% reduction at 36 weeks. Phase 3 outcomes trial: **OCEAN(a)** (NCT05581303), results expected 2027.
- **Lepodisiran** — siRNA, in phase 2 ALPACA (presented at ACC.25, 2025): single 400 mg dose → 93.9% Lp(a) reduction at day 180, > 90% reduction persisting at day 360. Phase 3: **ACCLAIM-Lp(a)**, enrolling.
- **Zerlasiran** — GalNAc-conjugated siRNA, phase 2 (Nissen et al., *JAMA* 2024) showed ~80–90% reductions.
- **Muvalaplin** — small-molecule oral inhibitor of apo(a)–apoB covalent linkage assembly. Phase 2 (Nicholls et al., *JAMA* 2024) — first oral Lp(a) drug, ~70% reduction.

**The unanswered question**: how much Lp(a) reduction is needed for clinical benefit? Mendelian randomization suggests **65–100 mg/dL absolute reduction** is required for a clinically meaningful (~22% over 5 years) CHD risk reduction (Burgess et al., *JAMA Cardiol* 2018; Madsen et al.). This is a higher absolute reduction bar than for LDL-C and is why trials enroll patients with Lp(a) > 70 mg/dL — anything lower can't be reduced enough in absolute terms to demonstrate outcome benefit.

### 8.12 Direction of "better" for Lp(a)

**Strictly monotonic. Lower is better. No floor of harm.** This is essentially unique among cardiovascular biomarkers in being so cleanly directional. The contrast with HDL-C (U-shaped) or even LDL-C (where very low values raise theoretical concerns) is stark.

### 8.13 Confounders

- **Assay**: nmol/L (isoform-insensitive) vs. mg/dL (isoform-sensitive) reporting can mis-classify by 1.5–3.5x. Always check the assay.
- **Apo(a) isoform**: small isoform → higher concentration *and* higher per-mg risk (independent effect). If your lab reports KIV-2 repeat number, smaller (< 22 repeats) is worse.
- **Renal disease**: raises Lp(a) ~2-fold
- **Postmenopausal**: raises ~10–20%
- **Pregnancy**: raises 2-fold transiently
- **Acute inflammation/sepsis**: transient elevation
- **Hypothyroidism**: modest elevation; treatment normalizes

---

## 9. Putting It Together — A Decision Framework for a 20-Year-Old Male

### 9.1 The hierarchy of importance

For a healthy 20-year-old male evaluating these 7 markers, prioritize attention as follows:

1. **Lp(a)** — once-in-a-lifetime test, fixed genetic risk, irreplaceable information
2. **LDL-P** (and equivalently apoB if reported) — actionable lifetime particle exposure
3. **Small LDL-P + LDL Pattern** — flag for insulin resistance even at normal weight
4. **LDL Peak Size** — partly redundant with Pattern, useful trend tracker
5. **HDL Large** — informational; do not pharmacologically treat to a target
6. **LDL Medium** — primarily a component of LDL-P, informational
7. (LDL-P beats all single-subclass measures for prognostic value — Otvos)

### 9.2 The "all good" young-male profile

| Marker | Optimal target |
|---|---|
| LDL-P | < 1,000 nmol/L (Attia: < 800) |
| LDL Peak Size | > 21.0 nm |
| LDL Pattern | A |
| LDL Small | < 200 nmol/L (formal optimal < 527) |
| LDL Medium | < ~300 nmol/L |
| HDL Large | > 7 μmol/L (in context of total HDL-P > 35 μmol/L) |
| Lp(a) | < 30 nmol/L (~< 14 mg/dL) |

### 9.3 Action triggers

- **Lp(a) ≥ 125 nmol/L (≥ 50 mg/dL)**: confirm; treat all other CV risks aggressively; cascade-screen family; CAC scan at 35–40; track Lp(a) drug pipeline.
- **LDL-P > 1,300 nmol/L** at age 20 with normal LDL-C: rule out FCHL (apoB, family lipid history), check insulin/HbA1c, evaluate diet.
- **LDL-P > 1,800 nmol/L** at age 20 with very high LDL-C (>190): rule out heterozygous FH (Dutch Lipid Clinic Network criteria; consider genetic testing for *LDLR*, *APOB*, *PCSK9*).
- **Pattern B at age 20**: investigate insulin resistance — fasting insulin, HbA1c, ALT, TG/HDL ratio, waist circumference. Pattern B at 20 is a near-guaranteed precursor to T2D unless reversed by lifestyle.
- **HDL Large low + small LDL high + TG high**: classic atherogenic dyslipidemia of metabolic syndrome.

### 9.4 The non-obvious points worth internalizing

1. **Lp(a) measured once is enough — but actually do it.** The 1-in-5 chance of finding elevated Lp(a) is the highest-value information per dollar in preventive cardiology for someone your age.
2. **LDL-C alone is insufficient.** Statin therapy can lower LDL-C to "target" while leaving LDL-P (particle count) elevated — a known and clinically actionable discordance pattern.
3. **HDL is not a treatment target.** Five negative outcome trials make this clear. Use HDL as a marker of metabolic health, not a number to optimize.
4. **Pattern B at age 20 is the metabolic-syndrome bat signal.** Even if BMI is normal — a young, lean Pattern B male is the textbook TOFI phenotype and is on a clear T2D / NAFLD / CVD trajectory.
5. **The cleanest decade-long apoB trajectory available is the highest-leverage cardiovascular intervention you have — and you have it now.** Borén et al. (EAS Consensus 2020): cumulative apoB exposure × time = atherosclerotic plaque burden. An extra 30 years at low apoB matters more than any drug started at 50.

---

## 10. Sources

### 10.1 Primary peer-reviewed literature (selected)

- Reyes-Soffer G, Ginsberg HN, Berglund L, et al. **Lipoprotein(a): A Genetically Determined, Causal, and Prevalent Risk Factor for Atherosclerotic Cardiovascular Disease: A Scientific Statement From the American Heart Association.** *Arterioscler Thromb Vasc Biol.* 2022;42(1):e48-e60. doi:10.1161/ATV.0000000000000147
- Wilson DP, Jacobson TA, Jones PH, et al. **A focused update to the 2019 NLA scientific statement on use of lipoprotein(a) in clinical practice.** *J Clin Lipidol.* 2024;18(3):e308-e319.
- Kamstrup PR, Tybjaerg-Hansen A, Steffensen R, Nordestgaard BG. **Genetically elevated lipoprotein(a) and increased risk of myocardial infarction.** *JAMA.* 2009;301(22):2331-9.
- Clarke R, Peden JF, Hopewell JC, et al. (PROCARDIS Consortium). **Genetic variants associated with Lp(a) lipoprotein level and coronary disease.** *N Engl J Med.* 2009;361(26):2518-28.
- Burgess S, Ference BA, Staley JR, et al. **Association of LPA Variants With Risk of Coronary Disease and the Implications for Lipoprotein(a)-Lowering Therapies: A Mendelian Randomization Analysis.** *JAMA Cardiol.* 2018;3(7):619-627.
- Thanassoulis G, Campbell CY, Owens DS, et al. **Genetic associations with valvular calcification and aortic stenosis.** *N Engl J Med.* 2013;368(6):503-12.
- Kamstrup PR, Tybjaerg-Hansen A, Nordestgaard BG. **Elevated Lipoprotein(a) and Risk of Aortic Valve Stenosis in the General Population.** *J Am Coll Cardiol.* 2014;63(5):470-7.
- Tsimikas S, Karwatowska-Prokopczuk E, Gouni-Berthold I, et al. **Lipoprotein(a) Reduction in Persons with Cardiovascular Disease (pelacarsen).** *N Engl J Med.* 2020;382(3):244-255.
- Nissen SE, Wolski K, Balog C, et al. **Single Ascending Dose Study of a Short Interfering RNA Targeting Lipoprotein(a) Production (Olpasiran).** Reported in *NEJM* 2022 and follow-up extension in *JACC* 2024.
- Sniderman AD, Williams K, Contois JH, et al. **A meta-analysis of low-density lipoprotein cholesterol, non–high-density lipoprotein cholesterol, and apolipoprotein B as markers of cardiovascular risk.** *Circ Cardiovasc Qual Outcomes.* 2011;4(3):337-45.
- Otvos JD, Mora S, Shalaurova I, Greenland P, Mackey RH, Goff DC. **Clinical implications of discordance between low-density lipoprotein cholesterol and particle number.** *J Clin Lipidol.* 2011;5(2):105-13.
- Cromwell WC, Otvos JD, Keyes MJ, et al. **LDL Particle Number and Risk of Future Cardiovascular Disease in the Framingham Offspring Study.** *J Clin Lipidol.* 2007;1(6):583-92.
- Mora S, Otvos JD, Rifai N, Rosenson RS, Buring JE, Ridker PM. **Lipoprotein particle profiles by nuclear magnetic resonance compared with standard lipids and apolipoproteins in predicting incident cardiovascular disease in women.** *Circulation.* 2009;119(7):931-9.
- Mora S, Glynn RJ, Ridker PM. **High-Density Lipoprotein Cholesterol, Size, Particle Number, and Residual Vascular Risk After Potent Statin Therapy** (JUPITER analysis). *Circulation.* 2013;128(11):1189-97.
- Khera AV, Cuchel M, de la Llera-Moya M, et al. **Cholesterol efflux capacity, high-density lipoprotein function, and atherosclerosis.** *N Engl J Med.* 2011;364(2):127-35.
- Rohatgi A, Khera A, Berry JD, et al. **HDL cholesterol efflux capacity and incident cardiovascular events.** *N Engl J Med.* 2014;371(25):2383-93.
- Voight BF, Peloso GM, Orho-Melander M, et al. **Plasma HDL cholesterol and risk of myocardial infarction: a Mendelian randomisation study.** *Lancet.* 2012;380(9841):572-80.
- Krauss RM. **Lipoprotein subfractions and cardiovascular disease risk.** *Curr Opin Lipidol.* 2010;21(4):305-11.
- Austin MA, King MC, Vranizan KM, Krauss RM. **Atherogenic lipoprotein phenotype. A proposed genetic marker for coronary heart disease risk.** *Circulation.* 1990;82(2):495-506.
- Veerkamp MJ, de Graaf J, Hendriks JC, Demacker PN, Stalenhoef AF. **Nomogram to diagnose familial combined hyperlipidemia on the basis of results of a 5-year follow-up study.** *Arterioscler Thromb Vasc Biol.* 2003;23(7):1242-7.
- Borén J, Chapman MJ, Krauss RM, et al. **Low-density lipoproteins cause atherosclerotic cardiovascular disease: pathophysiological, genetic, and therapeutic insights: a consensus statement from the European Atherosclerosis Society Consensus Panel.** *Eur Heart J.* 2020;41(24):2313-2330.
- van der Valk FM, Bekkering S, Kroon J, et al. **Oxidized phospholipids on lipoprotein(a) elicit arterial wall inflammation and an inflammatory monocyte response in humans.** *Circulation.* 2016;134(8):611-624.
- Tsimikas S. **A Test in Context: Lipoprotein(a): Diagnosis, Prognosis, Controversies, and Emerging Therapies.** *J Am Coll Cardiol.* 2017;69(6):692-711.

### 10.2 Guidelines

- Mach F, Baigent C, Catapano AL, et al. **2019 ESC/EAS Guidelines for the management of dyslipidaemias.** *Eur Heart J.* 2020;41(1):111-188.
- 2025 Focused Update of the 2019 ESC/EAS Guidelines for the management of dyslipidaemias. *Eur Heart J.* 2025.
- 2026 ACC/AHA/AACVPR/etc. Guideline on the Management of Dyslipidemia. *Circulation.* 2026.
- Wilson DP et al. (NLA), 2024 Focused Update on Lp(a). *J Clin Lipidol.*
- Grundy SM et al., 2018 AHA/ACC Cholesterol Guideline. *Circulation.* 2019.

### 10.3 Public-facing references and Function Health context

- LabCorp NMR LipoProfile reference document L15035 (LDL-P, subclass cutpoints)
- Mayo Clinic Labs NMR LipoProfile catalog (HDL-P reference ranges)
- Family Heart Foundation, "Reading Your Lipid and Lipoprotein(a) Test Results"
- Cleveland HeartLab / Quest Cardio IQ technical documents
- Peter Attia, *AMA #43: Understanding apoB, LDL-C, Lp(a), and insulin* (peterattiamd.com)
- Empirical Health, "Lp(a): the strongest hereditary risk factor for heart disease"
- Lp(a) Foundation (lipoproteinafoundation.org)

### 10.4 Evidence-quality tags used in this report

- **Well established**: LDL-P/apoB causality for ASCVD; Lp(a) causality for CHD and aortic stenosis; HDL-C non-causality
- **Emerging / debated**: HDL function (efflux capacity) clinical use; obicetrapib outcomes interpretation; isoform-specific Lp(a) risk modification beyond plasma concentration; periodic Lp(a) re-testing in patients near thresholds
- **Open**: optimal Lp(a) reduction magnitude for outcome benefit (Lp(a)HORIZON, OCEAN(a) results pending)
