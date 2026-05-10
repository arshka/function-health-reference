# Intervention Effect Sizes — Master Index & Cross-Cutting Synthesis

This index ties together five panel-specific effect-size files. Use it when an intervention you're considering moves markers across multiple panels, or when you want to know which intervention has the highest coupled-leverage across the system.

**The five panel files:**

| File | Markers covered |
|---|---|
| `effect_sizes_cardiovascular.md` | ApoB · LDL-C · HDL-C · non-HDL-C · TC · TG · TC/HDL · ApoB/ApoA1 · Lp(a) · hs-CRP |
| `effect_sizes_metabolic_liver.md` | Fasting glucose · HbA1c · fasting insulin · HOMA-IR · uric acid · ALT · AST · ALP · GGT · total bilirubin · albumin · globulin · A/G ratio · total protein |
| `effect_sizes_endocrine.md` | Total T · Free T · SHBG · E2 · LH · FSH · prolactin · DHEA-S · AM cortisol · TSH · FT4 · FT3 · TPO Ab · TgAb |
| `effect_sizes_nutrients.md` | Ferritin · iron · TSAT · TIBC · 25-OH vit D · B12 · MMA · folate · homocysteine · serum Mg · zinc · calcium · Omega-3 Index |
| `effect_sizes_hematology_other.md` | Hgb · Hct · RBC · MCV · MCH · MCHC · RDW · Plt · MPV · WBC + 5-part diff · NLR · Na · K · Cl · HCO3 · Ca · BUN · Cr · eGFR · uACR · Pb · Hg · PhenoAge |

**Total reference corpus**: ~54,000 words across 5 files. ~84 markers. Each effect size is tagged with provenance — **[Meta]** (replicated meta-analysis), **[RCT]** (single high-quality trial), **[Cohort]** (observational), **[MR]** (Mendelian randomization), **[Mechanism]** (biochemical extrapolation, not direct human RCT), **[1-Trial]** (single-trial finding worth knowing but not yet replicated).

---

## How to read these files

1. **They are reference, not personal.** No marker interpretation, no "what to do for you" framing. Personal interpretation lives in the existing per-panel research files (`heart_lipids_basic.md`, etc.) and in dashboard verdicts.
2. **They quantify what existing research files only narrate.** The audit gap that drove their creation: zero quantified intervention effect sizes across the prior 17 files.
3. **Population caveat is everywhere.** Most cited RCTs/meta-analyses are NW European, age 50+, with overt disease (T2D, MetS, ASCVD, CKD). Effect sizes in a healthy lean 20-year-old SA male will often be **smaller** (floor effects — markers already near optimum have less room to move) and the SA-specific multipliers are noted where data exists.
4. **Provenance over consensus.** Where evidence is mixed, both sides are reported. Where a "well-known" intervention lacks RCT support (HDL-raising drugs, homocysteine lowering for CV, milk thistle for MASLD, T-boosters), it is flagged as such rather than smoothed.

---

## Cross-cutting interventions: which markers each moves

The single highest-leverage observation: a few interventions move markers across nearly every panel simultaneously. Optimizing them captures more system-wide variance than any per-marker tweak. Effect-size details for each marker live in the panel files — this table is the cross-marker map.

### 1. Weight loss (5–10% body weight) — highest cross-system coupling

| Marker | Direction & magnitude per ~5% loss | Time | File |
|---|---|---|---|
| ApoB | −5–10 mg/dL | 12 wk | CV |
| LDL-C | −5–10 mg/dL | 12 wk | CV |
| Triglycerides | −15–30% | 8–12 wk | CV |
| HDL-C | +2–5 mg/dL | 12–24 wk | CV |
| hs-CRP | −20–30% | 12–24 wk | CV |
| HbA1c | −0.5 to −0.8% (T2D); −0.2 to −0.4% (non-DM) | 12–24 wk | Metab/Liver |
| Fasting insulin | −20–35% | 8–12 wk | Metab/Liver |
| HOMA-IR | −25–40% | 8–12 wk | Metab/Liver |
| ALT | −5 to −10 U/L (MASLD baseline); large in lean MASLD | 12–24 wk | Metab/Liver |
| GGT | −10–25% | 12 wk | Metab/Liver |
| Uric acid | −0.3 to −0.7 mg/dL | 12 wk | Metab/Liver |
| Total T | +30–100 ng/dL (in obese; minimal in lean) | 12–24 wk | Endocrine |
| SHBG | +5–15 nmol/L | 12–24 wk | Endocrine |
| E2 | −15–30% (in obese aromatase-driven E2) | 12–24 wk | Endocrine |
| AM cortisol | Variable (acute restriction → up; sustained loss → normalization) | 8–24 wk | Endocrine |
| Systolic BP | −3–6 mmHg per 5 kg | 4–12 wk | Hema/Other |
| uACR | −20–35% (in obese with elevated uACR) | 12–24 wk | Hema/Other |
| eGFR | Initial preserved; long-term protection | months | Hema/Other |

**Caveat**: at lean baseline (BMI <22), most of these magnitudes shrink toward zero — floor effects dominate. Weight-loss leverage is for elevated baseline, not for already-lean optimization.

### 2. Sleep extension / quality (5–6h → 7.5–8h actual sleep)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| Total T | +10–15% (Leproult 2011 [RCT]) | 1 wk | Endocrine |
| AM cortisol | Pattern normalization (AUC ↓, slope steeper) | 1–2 wk | Endocrine |
| Fasting insulin | −20–30% (Spiegel 1999 [RCT]) | days | Metab/Liver |
| Insulin sensitivity (HOMA / clamp) | +30% | 1 wk | Metab/Liver |
| HbA1c | −0.1 to −0.3% (chronic short-sleep → normal) | 8–12 wk | Metab/Liver |
| Systolic BP | −2 to −5 mmHg | 2–4 wk | Hema/Other |
| hs-CRP | −10–20% | 4–8 wk | CV |
| WBC | Normalization of chronic-sleep-loss elevation | weeks | Hema/Other |
| HRV | Increase (rough, noisy) | days–weeks | non-blood |
| Hgb | Modest in chronic apnea reversal (CPAP) | months | Hema/Other |

**Caveat**: extending above ~8h has no documented additional benefit; the curve is concave with diminishing returns. The effect is on sleep DEBT, not sleep luxury.

### 3. Alcohol cessation (from regular drinking → none)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| GGT | −30–50% | 4–8 wk | Metab/Liver |
| ALT | −10–30% (if elevated) | 4–8 wk | Metab/Liver |
| MCV | −3–8 fL | 10–16 wk (RBC turnover) | Hema/Other |
| Triglycerides | −10–30% (in heavy drinkers) | 2–4 wk | CV |
| HDL-C | −5–10 mg/dL (alcohol RAISES HDL — moderate drinking) | 4 wk | CV |
| Total T | +5–15% in heavy drinkers; minimal in light | 4–8 wk | Endocrine |
| E2 | −10–20% in heavy drinkers | 4–8 wk | Endocrine |
| SHBG | Decrease (heavy alcohol → SHBG up; cessation → down) | 4–12 wk | Endocrine |
| Uric acid | −0.5 to −1.0 mg/dL (in heavy drinkers) | 2–4 wk | Metab/Liver |
| Systolic BP | −2 to −5 mmHg | 2–4 wk | Hema/Other |
| Folate | Repletion (alcohol blocks absorption) | 4–12 wk | Nutrients |
| Magnesium | Repletion (alcohol → renal Mg loss) | 4–12 wk | Nutrients |
| B12 / thiamine | Repletion in heavy drinkers | weeks | Nutrients |

**Note**: cessation is asymmetric with light vs heavy baseline — meta-analytic effects scale roughly with prior intake. The HDL-falling effect of cessation is real but probably not protective (HDL-raising drugs failed in RCTs; see CV file).

### 4. Aerobic / Zone 2 endurance training (5–10 hr/wk)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| Hgb | **APPEARS −0.5 to −1.5 g/dL** (plasma volume expansion artifact) | 2–6 wk | Hema/Other |
| Hct | −2 to −5% (same artifact) | 2–6 wk | Hema/Other |
| RBC mass | Actually +5–15% (true measurement requires Cr-51) | weeks–months | Hema/Other |
| HDL-C | +3–6 mg/dL | 8–12 wk | CV |
| Triglycerides | −15–25% | 8–12 wk | CV |
| LDL/ApoB | Modest (−3–8 mg/dL); much smaller than dietary effect | 12–24 wk | CV |
| HbA1c | −0.3 to −0.6% (in T2D); −0.1 to −0.2% (healthy) | 12–24 wk | Metab/Liver |
| Insulin sensitivity | +25–40% | 4–8 wk | Metab/Liver |
| ALT (in MASLD) | −20–30% with reduction in liver fat ~10–13% (Hallsworth 2011 [RCT]) | 8–12 wk | Metab/Liver |
| Resting HR | −5–10 bpm | 4–12 wk | non-blood |
| BP (hypertensive) | −5–8 mmHg systolic | 4–12 wk | Hema/Other |
| hs-CRP | −10–25% | 12–24 wk | CV |
| Total T | Neutral or modest +; high-volume endurance can suppress (Hackney 2003) | months | Endocrine |
| AM cortisol | Acutely up post-exercise; chronic pattern improves | months | Endocrine |
| WBC | Transient post-exercise rise; chronic baseline drop in trained | months | Hema/Other |

### 5. Resistance training (3–5 sessions/wk, progressive)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| Insulin sensitivity | +20–30% | 8–12 wk | Metab/Liver |
| HbA1c | −0.3 to −0.5% (T2D) | 12–24 wk | Metab/Liver |
| Liver fat (MASLD) | −13% (Hallsworth 2011 [RCT]) — without weight change | 8 wk | Metab/Liver |
| Total T baseline | No change in eugonadal trained men (Vingren 2010) | — | Endocrine |
| Lean mass | +1–3 kg | 12–24 wk | non-blood |
| Bone density | +1–3% (lumbar / femoral) | 6–12 mo | non-blood |
| ALT | Transient acute rise (muscle vs liver origin — discriminate via AST:ALT and CK) | days | Metab/Liver |
| CK | Acute spikes 2–10× ULN post-novel session | 1–3 days | Hema/Other |
| Creatine kinase / myoglobin | Confound for AKI panic if not contextualized | days | Hema/Other |
| Cortisol | Acute spike; chronic pattern unchanged in well-recovered | sessions | Endocrine |

**Practical surprise**: at 20yM with replete eugonadal status, resistance training does NOT raise baseline T despite acute post-session spikes. Lift for body composition / insulin sensitivity / bone, not for testosterone.

### 6. Saturated fat reduction (15% → <7% of kcal, replacing with PUFA/MUFA)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| LDL-C | −15–25 mg/dL (Mensink 2003 [Meta]) | 8–12 wk | CV |
| ApoB | −10–20 mg/dL | 8–12 wk | CV |
| Non-HDL-C | −15–25 mg/dL | 8–12 wk | CV |
| HDL-C | −3 to −5 mg/dL (PUFA replacement; SFA RAISES HDL → cessation drops it slightly) | 8–12 wk | CV |
| Triglycerides | Variable (depends on replacement carb vs fat) | 8–12 wk | CV |

**Surprise**: ketogenic / very-high-SFA diets can RAISE LDL-C dramatically in lean individuals (KETO trial, JACC Adv 2024) — the effect is not symmetric with the reduction effect, and lean people are particularly sensitive. APOE4 carriers respond more strongly to SFA in both directions (Minihane 2007).

### 7. Soluble fiber increase (psyllium, beta-glucan, oats; 5–15 g/d)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| LDL-C | −5–10 mg/dL per 5 g/d added soluble fiber | 4–8 wk | CV |
| ApoB | −3–8 mg/dL | 4–8 wk | CV |
| HbA1c | −0.2 to −0.4% (in T2D) | 12 wk | Metab/Liver |
| hs-CRP | Modest decrease | 8–12 wk | CV |
| Bile acid loss | Mechanism for LDL effect | weeks | — |

### 8. Dietary sodium reduction (>4g → ~2.3 g/d)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| Systolic BP (hypertensive) | −5 to −10 mmHg (Sacks 2001 DASH-Sodium [RCT]) | 30 d | Hema/Other |
| Systolic BP (normotensive) | −2 to −5 mmHg | 30 d | Hema/Other |
| Serum Na | Minimal change in healthy (kidney compensates) | — | Hema/Other |
| K | Minimal direct (depends on diet substitution) | — | Hema/Other |
| uACR | Reduction in salt-sensitive | weeks | Hema/Other |

**Caveat**: PURE J-curve controversy is real. Population-level reduction has stronger evidence than ultra-low-Na (<1.5 g/d) where some cohorts show worse outcomes. See Hema/Other file for full discussion.

### 9. Smoking cessation

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| hs-CRP | −30–50% | 4–12 wk | CV |
| WBC | −1.0 to −1.5 K/µL (smokers run elevated) | 4–12 wk | Hema/Other |
| Hgb / Hct | −0.5 to −1.0 g/dL (smokers run elevated CO-driven) | 4–12 wk | Hema/Other |
| HDL-C | +3–5 mg/dL | 4–12 wk | CV |
| Fibrinogen | −10–20% | 4–12 wk | — |
| Pulmonary FEV1 trajectory | Slope normalization (decline rate matches non-smoker) | months–years | non-blood |
| Lp(a) | Smoking has no documented effect; cessation neutral | — | CV |

### 10. Sun exposure / vitamin D supplementation

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| 25-OH vit D | +1 ng/mL per 100 IU/d at steady state (non-linear; smaller increment at higher baseline) | 8–12 wk | Nutrients |
| PTH | Decrease in vitamin-D-deficient | 8–24 wk | Nutrients |
| Calcium | Mild increase | 8–24 wk | Nutrients |
| Total T | +10–25% in deficient men (Pilz 2011 [1-Trial]); null in replete (Lerchbaum 2017) | 12 wk | Endocrine |
| TPO Ab | Possibly modest reduction in Hashimoto's with repletion (mixed) | 6 mo | Endocrine |
| hs-CRP | Modest decrease in deficient | weeks–months | CV |
| Insulin sensitivity | Mixed; possibly modest in deficient | weeks–months | Metab/Liver |

**SA-specific**: 72–94% of UK SAs are deficient regardless of season (per nutrients file). Skin pigmentation reduces UVB-driven D3 synthesis ~3–5×. Pigmented populations require larger oral doses (typically 2000–4000 IU/d for repletion).

### 11. Stress reduction / meditation / vagal training

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| AM cortisol | Pattern normalization (slope steeper, AUC modest) | weeks | Endocrine |
| Systolic BP | −3 to −5 mmHg (mostly in hypertensives) | 8–12 wk | Hema/Other |
| hs-CRP | Modest reduction | weeks–months | CV |
| HRV | Increase | weeks | non-blood |
| HbA1c | Minimal direct | — | Metab/Liver |

### 12. Caffeine reduction / cessation

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| AM cortisol | Modest reduction (caffeine acutely raises cortisol) | days | Endocrine |
| Systolic BP | −2 to −3 mmHg | days | Hema/Other |
| Sleep architecture (REM, deep %) | Improved with afternoon-cutoff | days | non-blood |
| Iron absorption | Increased (coffee/tea inhibit non-heme iron) | weeks | Nutrients |
| GGT | Mild increase (coffee LOWERS GGT — cessation reverses) | weeks | Metab/Liver |
| ALT | Mild increase (same — coffee is mildly hepato-protective) | weeks | Metab/Liver |

**Surprise**: coffee specifically (independent of caffeine) lowers ALT/GGT in MASLD per AASLD guidelines — cessation can transiently bump them.

### 13. Periodic blood donation (every 8–16 weeks, men)

| Marker | Direction & magnitude | Time | File |
|---|---|---|---|
| Ferritin | −30–60 µg/L per donation | 4–8 wk | Nutrients |
| TSAT | Decrease, then re-equilibrate | 4–8 wk | Nutrients |
| Hgb | −0.5 to −1.0 g/dL acute, recovers | 4–8 wk | Hema/Other |
| Blood Pb | Modest reduction (lead partitions to RBCs) | per donation | Hema/Other |
| Cardiovascular events (HFE+) | Decrease in C282Y carriers (Karlsson 2019) | years | — |

### 14. Pharmacotherapy reference (for scale only — see panel files for full tables)

| Drug class | Headline effect size | File |
|---|---|---|
| Statin (high-intensity) | LDL −50%, ApoB −45%, hs-CRP −15–35%, Lp(a) +5–15% | CV |
| Ezetimibe | LDL −18%, ApoB −15% | CV |
| PCSK9i (evolocumab/alirocumab) | LDL −60%, ApoB −50%, Lp(a) −25% | CV |
| Bempedoic acid | LDL −18–21%, hs-CRP −16–22% | CV |
| Inclisiran | LDL ~−50% (sustained 6-month dose) | CV |
| Pelacarsen / olpasiran / lepodisiran | Lp(a) −80–95% (Phase 2/3) | CV |
| Metformin | A1c −0.7 to −1%; modest weight; B12 absorption ↓ | Metab/Liver, Nutrients |
| GLP-1 (semaglutide) | A1c −1.5%, weight −15%, uACR −32%, LDL −5%, hs-CRP −40%, MASH resolution | Metab/Liver, CV, Hema/Other |
| SGLT2i | A1c −0.7%, UA −0.5 mg/dL, uACR −30%, eGFR initial dip then preserved | Metab/Liver, Hema/Other |
| Pioglitazone | A1c −0.8%, MASLD ALT/liver-fat improvement | Metab/Liver |
| Resmetirom | Liver fat −34–39% by MRI-PDFF (MAESTRO-NASH 2024) | Metab/Liver |
| Allopurinol / febuxostat | UA −2 to −3 mg/dL | Metab/Liver |
| ACEi / ARB | uACR −30–40%, BP, eGFR initial dip | Hema/Other |
| Finerenone | uACR −30%, kidney + CV protection | Hema/Other |
| TRT (testosterone cypionate) | Total T → 600–900 ng/dL; Hct rise +3–5%; SHBG suppression; LH/FSH suppression | Endocrine, Hema/Other |
| Levothyroxine | TSH titration; modest symptom benefit only in overt hypoT (TRUST null in mild SCH) | Endocrine |
| Selenium 200 µg/d | TPO Ab −20–55%; no progression benefit | Endocrine |
| IV iron (FCM 1 g) | Ferritin +100–200 µg/L over 4–6 wk | Nutrients |
| High-dose oral B12 | MMA normalization; serum B12 normal in ~4 wk | Nutrients |
| Prescription EPA (icosapent ethyl 4 g/d) | TG −20–30%, Omega-3 Index +4–6% | Nutrients, CV |

---

## Cross-cutting caveats (apply across all five files)

**1. Floor effects.** Most effect sizes come from baseline-elevated populations (T2D, MetS, hyperlipidemia). At a lean 20yM with already-near-optimum markers, expect roughly **30–60% of the cited effect magnitude**. This is not a flaw of the references — it's the population the data is from. Where lean-young-male data exists, panel files flag it.

**2. Time-to-effect ≠ time-to-steady-state.** Many interventions have a fast initial response and a slow plateau. Examples: vit D supplementation reaches steady-state at 8–12 wk; A1c integrates over 90 days but stabilizes by 12 wk; Omega-3 Index turnover is 120-day t½ so 6 months for full equilibration; ferritin response to oral iron plateaus ~12 wk; PCSK9i full effect by 4 wk; statin LDL effect by 2–4 wk.

**3. Responder variation.** APOE genotype × LDL response to SFA reduction (3–5× spread). FADS1/2 × ALA→DHA conversion (5–10× spread). PNPLA3 × MASLD response to weight loss (slower in GG). MTHFR × folate response to folic acid (negligible vs methylfolate in TT carriers). These genetic modifiers are detailed in the panel files; cross-cut summary in §SNP Modifiers below.

**4. Compound effects don't fully add.** Stacking 6 lifestyle interventions doesn't yield 6× the single-intervention effect — there's diminishing return as you approach physiological optimum. Combined effect is typically 60–80% of the linear sum, more for elevated baselines, less for already-optimum.

**5. Pharmacotherapy comparisons are scale anchors, not recommendations.** The panel files include drugs to give you a numerical sense of how big a "big" effect is. Lifestyle-only interventions for a healthy 20yM with mostly-optimal markers will not reach drug-class magnitudes for ApoB, Lp(a), or A1c — and shouldn't need to.

---

## South Asian–specific cross-cutting

The five panel files each carry SA-specific notes per marker. The cross-cutting threads:

- **Vitamin D deficiency is near-universal** in SA populations (72–94% in UK studies). Larger oral doses needed (2000–4000 IU/d typical). Sun exposure ~3–5× less efficient due to pigment.
- **Lean MASLD / "TOFI" phenotype.** SA visceral fat at low BMI means MASLD, IR, and ALT/GGT/UA elevations occur at apparently-normal weight. Weight-loss interventions still leverage but the "you're not overweight" objection is invalid.
- **Lipid risk is undertreated by LDL-C alone.** ApoB is the more SA-faithful particle marker; SAs run small-dense LDL more often, so per unit LDL-C they carry more particles. Lp(a) baseline distribution is shifted higher; measure it once.
- **B12 deficiency very common in vegetarian SA diets** (up to 75% in some Indian cohorts). Oral 500–1000 µg/d cyanocobalamin is sufficient repletion; no IM needed unless absorption-impaired.
- **Iron-handling complications.** TMPRSS6 variants common in SA populations affect iron absorption regulation. HFE C282Y much rarer in SA than European (~0.3% vs 6% allele frequency).
- **FADS2 advantage for omega-3 conversion.** ~70% of SAs carry rs66698963 insertion enhancing ALA→EPA/DHA conversion. Still insufficient to reach Omega-3 Index ≥8% without direct marine/algal supplementation.
- **ALDH2 / ADH1B variants** in some Asian populations (more common in E Asians than SAs) — alcohol → larger increases in liver enzymes, BP, and cancer risk.
- **SHBG set-point lower** in SAs — total T may run lower but free T parity is maintained. Apparent "low T" can be SHBG-driven.
- **Higher T2D risk at lower A1c.** SAs develop T2D at lower BMI and lower A1c; intervention thresholds should be moved down accordingly.
- **Mercury exposure higher in Asian Americans** (Caldwell 2014 NHANES) — fish-source audit (especially tuna, kingfish, large predator fish) higher yield.

---

## 23andMe-relevant SNPs that modify multiple cross-cutting responses

Pull these from your existing 23andMe data; details and sources in the panel files. This list is the **cross-marker** subset — single-marker SNPs are in the respective panel file.

| SNP / variant | Modifies | Effect direction |
|---|---|---|
| **APOE genotype** (rs429358 + rs7412) | LDL/ApoB response to SFA, dietary cholesterol; AD risk; B12 cutoffs; omega-3 effect | E4 carriers respond more strongly to SFA in both directions |
| **FADS1/2 cluster** (rs174537, rs66698963) | ALA→EPA/DHA conversion; PUFA metabolism | SA insertion variant ↑ conversion (~2–3×) |
| **HFE C282Y / H63D** (rs1800562, rs1799945) | Ferritin, TSAT; iron loading; donation strategy | C282Y homozygote → screen / consider donation |
| **TMPRSS6** | Iron absorption regulation | Common in SA; affects oral iron response |
| **MTHFR C677T** (rs1801133) | Folate metabolism; folic acid vs methylfolate response; homocysteine | TT carriers respond less to folic acid; methylfolate restores |
| **ALDH2 / ADH1B** | Alcohol → liver enzymes, BP, cancer risk | Asian variants → larger alcohol effect |
| **SLCO1B1** (rs4149056) | Statin (esp. simvastatin) myopathy risk | C carriers → use rosuvastatin/atorvastatin |
| **PNPLA3 rs738409** | MASLD severity; liver fat response to weight loss | GG → 73% more liver fat at any BMI |
| **TM6SF2** (rs58542926) | MASLD; lipid handling | T carriers → liver fat ↑, lipids ↓ |
| **GC vit D-binding protein** (Wang 2010 NEJM) | Circulating vs free 25-OH; supplementation response | Affects circulating 25-OH interpretation |
| **CYP2R1, CYP24A1** | Vit D activation/inactivation | Modifies oral D dose-response |
| **DIO2 Thr92Ala** (rs225014) | T4→T3 conversion | Ala carriers may respond less to T4-only thyroid Rx |
| **SELENOP / SEPP1** | Selenium transport to thyroid | Affects selenium supplementation response in TPO+ |
| **CYP17A1, CYP3A4** | Cortisol/androgen synthesis & metabolism | Modifies DHEA-S response to topical/inhaled steroids |
| **SHBG SNPs** (rs6258, rs12150660) | SHBG set-point | Genetic baseline ≠ pathology |
| **GCKR** (rs780094) | TG, uric acid, GGT, glucose, uACR | Multi-marker pleiotropy |
| **FTO, MC4R** | Body weight, secondary effects on multiple markers | Modifies weight-loss response |
| **SLC2A9, ABCG2** | Uric acid handling | Modifies UA response to diet/drugs |
| **LPA isoform size + rs10455872, rs3798220** | Lp(a) concentration | Genetic baseline; not lifestyle-modifiable |
| **PCSK9 LoF variants** | Baseline LDL | Lifelong low LDL → reduced CVD with no apparent harm |
| **CYP1A2** (rs762551) | Caffeine metabolism + caffeine × MI risk | Slow metabolizers + heavy coffee → CV risk ↑ |
| **APOL1 (G1/G2)** | CKD risk | African ancestry — for parents/friends, not directly self |
| **ACKR1 / Duffy** (rs2814778) | Baseline ANC | Mostly African ancestry |
| **G6PD** | Hemolysis triggers | Some SA regional carriers |
| **HBB / α-thal** | Microcytosis without iron def | Mediterranean / SA regional carriers |

Most of these are single SNPs grep-able directly from raw 23andMe data. The remaining (PRS scores) need imputation + scoring code.

---

## How to construct a personal combined-intervention projection

Once you have a baseline draw, build a 6-month "everything in" projection by walking each flagged or sub-optimal marker through its panel-file effect-size table:

1. **Identify the marker baseline** (your value vs. age-band optimal).
2. **List the lifestyle levers** that move it (from the relevant `effect_sizes_*.md` table).
3. **Sum the realistic deltas** at the high end of compliance (e.g., SFA reduction + fiber +10g/d + plant sterols 2g/d for ApoB; vit D loading dose for 25-OH-D; EPA+DHA 2g/d for Omega-3 Index; sleep 7.5–8h + zinc/magnesium repletion for endocrine markers).
4. **Apply ceiling effects.** Some markers have a floor (HbA1c rarely drops below 4.5 in a non-diabetic; hs-CRP rarely drops below 0.3) and lifestyle has a ceiling on most lipid markers (~10–25% drop in ApoB/LDL with maximal diet) — beyond that you are looking at pharmacotherapy.
5. **Mark the unreachable-without-drugs gaps explicitly.** For most lipid panels, ApoB <60 (Attia target) and LDL <70 will require statin / bempedoic acid / PCSK9i. The decision to bridge that gap in your 20s–30s is driven by Lp(a) result + family history + APOE + LPA-PRS, not the lipid panel alone.

This projection becomes the explicit hypothesis tested by the next draw 6–12 months out. Predict before measuring; that is the only way to learn whether the effect-size literature transports to *you*.

---

## How to use these files going forward

1. **New draw arrives** → look up flagged markers in their panel file's effect-size section to plan response strategy with quantified expectations for the next draw.
2. **Considering an intervention** → grep this index for the intervention name to see all markers it moves, then go to the panel files for full detail.
3. **Trajectory tracking** → each marker's effect-size table includes time-to-peak, which is the minimum interval before retesting can show a real change. Don't retest faster than the marker biology allows.
4. **Sourcing claims** → every effect size is tagged with provenance and cited; chase the primary source if a number drives a real decision.
5. **Updating** → these files are reference, not personal. They get updated when a new high-quality study (large RCT, IPD meta) shifts a documented effect size, not when your draw values change.

---

## What's still missing (next research priorities)

In ranked order of leverage (per prior audit conversation):

1. **Within-person biological variability (CVI) / Reference Change Values (RCV) per marker** — to interpret semi-annual draw deltas. Westgard database has CVI for ~600 analytes; would let you separate signal from noise.
2. **South Asian + lean-male specific cutoffs** — every existing interpretation is calibrated to NW European reference populations. MASALA / INTERHEART / Bhopal data exists.
3. **23andMe linkage per marker** — formalize the cross-table above into per-marker callouts in each panel research file.
4. **Cross-panel pattern recognition library** — negative APR block, MetS signature, low-cellularity pattern, MASLD rule-out, iron-overload screen.
5. **Family history modifier framework** — explicit how-to-update-thresholds for premature ASCVD, T2D, AD, cancer.

These are listed for handoff to future writing sessions. The effect-size corpus closes the largest single gap (intervention quantification); the above close the second-tier gaps.
