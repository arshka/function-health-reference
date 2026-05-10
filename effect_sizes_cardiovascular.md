# Intervention Effect Sizes — Cardiovascular Markers

A quantitative reference for how interventions move ApoB, LDL-C, HDL-C, non-HDL-C, Total Cholesterol, Triglycerides, TC/HDL ratio, ApoB/ApoA1 ratio, Lp(a), and hs-CRP. Biology, clinical significance, and lab-range commentary are in `heart_lipids_basic.md` and `heart_lipids_advanced.md`. This file is exclusively effect sizes.

---

## Evidence-Grading Legend

| Tag | Meaning |
|---|---|
| **[Meta]** | Well-replicated meta-analysis of ≥5 RCTs with consistent direction |
| **[RCT]** | Single high-quality landmark RCT (≥1,000 participants or pivotal design) |
| **[Cohort]** | Prospective observational; can't establish direction of causality |
| **[MR]** | Mendelian randomization — genetic proxies used to estimate causal effects |
| **[Mechanism]** | Extrapolation from pharmacology or physiology; no direct human RCT for this specific effect |

---

## Cross-Cutting Caveats

1. **Population mismatch.** Most lipid-intervention RCTs enrolled predominantly White adults aged 50–70 with existing CVD or hypercholesterolemia. Effect sizes in a 20-year-old lean South Asian primary-prevention subject are often extrapolated, not directly measured. Where South Asian–specific data exist (MASALA, INTERHEART, START-India), they are flagged.

2. **Baseline effect modification.** Absolute reductions are larger when baseline values are higher. A statin that drops LDL-C by 40% gives −60 mg/dL if you start at 150 and only −30 mg/dL if you start at 75. Tables show percentages and representative absolute numbers; apply the percentage to your baseline.

3. **Floor effects.** Lifestyle changes plateau. After diet and exercise, further LDL-C reduction below ~90–100 mg/dL typically requires pharmacotherapy; further TG reduction below ~80 mg/dL requires meaningful carbohydrate restriction or pharmacotherapy.

4. **Lp(a) is almost entirely genetic.** Lifestyle and most drugs move it by ≤25%. Do not conflate "can be changed" with "meaningfully changed" for Lp(a).

5. **HDL-C is not a therapeutic target.** Every pharmacologic HDL-raising trial (torcetrapib, dalcetrapib, evacetrapib, niacin in AIM-HIGH and HPS2-THRIVE) failed to reduce events. HDL-C rows in these tables describe the *observed change*, not a rationale for chasing HDL-C upward.

---

## ApoB

**Quick read:** Statins are the highest-leverage drug class (−20–55% depending on intensity). Lifestyle changes are additive but individually modest (each −5–15%). Combination approaches — plant-based high-fiber diet + weight loss + exercise + statin — can achieve −40–60% from baseline. PCSK9 inhibitors add another −50–60% on top of maximally tolerated statins.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| High-intensity statin (rosuvastatin 20–40 mg) | 20–40 mg/d | ApoB −42–52% | 6–12 wk | **[Meta]** | STELLAR trial (Ballantyne et al., *Am J Cardiol* 2003); Elam et al. meta-analysis (*Circ Cardiovasc Qual Outcomes* 2020) | Larger % in higher baselines; −21 mg/dL (pooled weighted mean in one meta-analysis) |
| High-intensity statin (atorvastatin 40–80 mg) | 40–80 mg/d | ApoB −37–49% | 6–12 wk | **[Meta]** | STELLAR; Elam et al. 2020 | Less predictable than rosuvastatin at matched intensity |
| Moderate-intensity statin (atorvastatin 10–20 mg, rosuvastatin 5–10 mg, simvastatin 20–40 mg) | per label | ApoB −25–40% | 6 wk | **[Meta]** | STELLAR; Elam et al. 2020 | — |
| Ezetimibe (as monotherapy) | 10 mg/d | ApoB −17% | 4–6 wk | **[RCT]** | Ballantyne et al. *Am J Cardiol* 2003 | Added on statin: an additional −10–15% ApoB |
| Evolocumab (PCSK9i) | 140 mg q2wk or 420 mg monthly | ApoB −55–60% on top of statin | 12 wk | **[RCT]** | FOURIER (Sabatine et al., *NEJM* 2017); pooled phase 3 | Combined with statin: ApoB can reach −70% from untreated baseline |
| Alirocumab (PCSK9i) | 75–150 mg q2wk | ApoB −55–60% | 12 wk | **[RCT]** | ODYSSEY OUTCOMES (Schwartz et al., *NEJM* 2018) | Similar magnitude to evolocumab |
| Inclisiran (PCSK9 siRNA) | 284 mg SC q6 months after day-1 and day-90 loading | ApoB ~50% | 6 months | **[RCT]** | ORION-10, ORION-11 (Ray et al., *NEJM* 2020) | Twice-yearly dosing; ApoB data extrapolated from LDL-C response |
| Bempedoic acid | 180 mg/d | ApoB −9–12% | 12 wk | **[RCT]** | CLEAR Harmony (Ray et al., *NEJM* 2019); JAMA Cardiol 2020 pooled phase 3 | Modest standalone; adds to statin; also reduces hs-CRP −16–22% |
| Obicetrapib (CETP inhibitor) | 10 mg/d | ApoB −33–42%; LDL-C −36–42%; HDL-C +130–135% | 12–52 wk | **[RCT]** | BROOKLYN (Nicholls et al., *Nature Med* 2025); BROADWAY 2025 | Pending FDA approval; ApoB benefit appears independent of HDL-C rise; Lp(a) −45% in high-baseline patients |
| Portfolio diet (full) | Soy + fiber + sterols + nuts | ApoB ~−15–20% | 4–12 wk | **[Meta]** | Chiavaroli et al., *J Am Heart Assoc* 2018 (7 RCTs, n=439) | Adherence-dependent; approaches lovastatin 20 mg effect size in motivated individuals |
| Plant-based / vegan diet | Full elimination of animal products | ApoB −14% (~−13 mg/dL) | 8–12 wk | **[Meta]** | Wang et al., *J Am Heart Assoc* 2023 (ACC.org) | Heterogeneous diets; lower-fat plant-based > higher-fat |
| Weight loss (lifestyle) | per kg lost | ApoB ~−1.5 mg/dL per kg (extrapolated from LDL-C and TG coupled changes) | Ongoing with weight loss | **[Mechanism]** | Extrapolated from Liu et al., *J Clin Endocrinol Metab* 2020 (73 RCTs) | Direct ApoB-per-kg data sparse; tracks LDL-C + TG improvements |
| Aerobic exercise | ≥150 min/wk moderate intensity | ApoB −2–5 mg/dL | 12–26 wk | **[Meta]** | Holme et al., *J Intern Med* 2007 (Oslo DOSE); aerobic exercise meta-analysis PMC10036419 | Modest standalone; most effective when accompanied by weight loss |
| Saturated fat ↓ + PUFA ↑ | From ~15% → <7% kcal as SFA, replacing with n-6 PUFA | LDL-C and non-HDL-C −10–20%; ApoB proportionally | 8–12 wk | **[Meta]** | Mensink RPM, WHO 2016 systematic review; Hooper et al., *Cochrane* 2020 | Each 1% kcal SFA replaced by PUFA: LDL-C −2.1 mg/dL; proportional ApoB reduction ~0.6× that |
| Trans fat elimination | From ~2% kcal iTFA → <0.1% | LDL-C +3.4% reversed; HDL-C +6.8% reversal (LDL:HDL ratio improved); ApoB improved proportionally | 4–8 wk | **[RCT]** | Mensink & Katan, *NEJM* 1990; meta-analysis Mozaffarian, *PMC2830458* | iTFA now banned in US foods; legacy risk persists via imported/residual processed food |
| Red yeast rice (monacolin K) | 3–10 mg/d monacolin K (~600–2400 mg RYR) | LDL-C −15–25% at low-dose monacolin; up to −35 mg/dL at higher doses | 8–24 wk | **[Meta]** | PMC8802088 (15 RCTs); JACC Focus Seminar 2021 | Chemically identical to lovastatin; statin-intolerant patients may tolerate ≤10 mg/d; supplement quality variable |
| Berberine | 500 mg TID (1500 mg/d) | LDL-C −0.38–0.50 mmol/L (~15–19 mg/dL); TG −0.28–0.37 mmol/L | 8–12 wk | **[Meta]** | Kong et al. *J Clin Lipidol* 2013; Zamani et al. *Pharmacol Res* 2019 | ApoB data insufficient in trials; mechanism via LDLR upregulation; most RCTs in Chinese populations; GI side effects common |

**Synthesis:**

- **Highest-leverage:** PCSK9 inhibitors (−55–60% ApoB on top of statin), then high-intensity statins (−40–52%), then ezetimibe (+additional −10–15%). Combination statin + ezetimibe + PCSK9i can theoretically reduce ApoB by ~75–80% from an untreated baseline.
- **Lifestyle ceiling:** Even the best diet + exercise + weight loss combination rarely achieves more than −20–25% ApoB without pharmacotherapy. The Portfolio diet is the highest-leverage single dietary pattern.
- **South Asian–specific:** The MASALA cohort (Kanaya et al., UCSF) shows SA individuals have a characteristic lipid phenotype: lower HDL-C, higher TG, and high ApoB/ApoA1 ratio with modest absolute LDL-C elevations — meaning standard LDL-C-based treatment algorithms systematically undertreate ApoB burden in this population. NLA 2021 statement on SA cardiovascular risk recommends using ApoB (not LDL-C alone) in South Asians. An Indian statin trial (START-India; open-label atorvastatin 20 mg) found similar percent LDL-C reduction in South Asians (~43%) as in White comparators (~41%) — statin pharmacodynamics appear preserved. The SA-specific phenotype warrants earlier ApoB testing and lower thresholds for intervention.
- **23andMe SNPs:** *PCSK9* loss-of-function variants (e.g., rs11591147, R46L) lower baseline LDL-C and ApoB ~15–20% lifelong, indicating individuals who may have lower baselines and higher residual risk from non-LDL factors [MR]. *APOE* ε4 carriers have greater LDL-C rise from saturated fat intake than ε3/ε3 or ε2/ε3 (Minihane, *Proc Nutr Soc* 2007) — APOE ε4 SA individuals likely benefit most from SFA reduction. *SLCO1B1* rs4149056 C allele: OR for myopathy 4.5 per copy with simvastatin 80 mg (NEJM 2008 GWAS); not significantly associated with atorvastatin or rosuvastatin myopathy — rosuvastatin preferred if SLCO1B1 risk allele present (CPIC 2022 guideline).
- **Realistic 3-month outcome (no drugs, optimal lifestyle):** From a starting ApoB of ~100–110 mg/dL (population-typical suboptimal), a high-adherence diet + exercise program achieves approximately ApoB −10–15 mg/dL (−10–14%) in 12 weeks.
- **Realistic 6-month outcome (no drugs):** −15–20 mg/dL (−13–20%) with sustained adherence; diminishing returns after 12–16 weeks on the same lifestyle program.

---

## LDL-C

**Quick read:** Statins remain the most evidence-dense drug class. High-intensity statins (rosuvastatin 20–40 mg, atorvastatin 40–80 mg) reduce LDL-C by 46–55% and 37–51% respectively. Diet + supplements can add another −10–25%. The floor of dietary intervention is roughly −25% from baseline; below that, pharmacotherapy is needed to reach low targets.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Rosuvastatin 40 mg | 40 mg/d | LDL-C −55% | 6 wk | **[RCT]** | STELLAR (Ballantyne, *Am J Cardiol* 2003) | Individual SD 12.8–17.9%; 5–53% are suboptimal responders depending on statin/dose |
| Rosuvastatin 20 mg | 20 mg/d | LDL-C −52% | 6 wk | **[RCT]** | STELLAR 2003 | Standard high-intensity statin starting point |
| Rosuvastatin 10 mg | 10 mg/d | LDL-C −46% | 6 wk | **[RCT]** | STELLAR 2003 | — |
| Atorvastatin 80 mg | 80 mg/d | LDL-C −51% | 6 wk | **[RCT]** | STELLAR 2003 | Rosuvastatin ~8% more potent mg-for-mg |
| Atorvastatin 40 mg | 40 mg/d | LDL-C −43% | 6 wk | **[RCT]** | STELLAR 2003 | — |
| Atorvastatin 10–20 mg | 10–20 mg/d | LDL-C −37–39% | 6 wk | **[RCT]** | STELLAR 2003 | Moderate-intensity threshold |
| Simvastatin 20–40 mg | 20–40 mg/d | LDL-C −28–39% | 6 wk | **[RCT]** | STELLAR 2003; MERCURY-I | FDA limits simvastatin to 40 mg due to myopathy risk at 80 mg |
| Pravastatin 40 mg | 40 mg/d | LDL-C −30% | 6 wk | **[RCT]** | STELLAR 2003 | Weakest standard statin; but fewest drug interactions (not CYP3A4) |
| Ezetimibe (alone) | 10 mg/d | LDL-C −17–18% (~−28 mg/dL at LDL-C 160) | 4–6 wk | **[Meta]** | Multiple RCTs; Catapano et al. meta-analysis 2021 | Added to statin: incremental −14–25% on top of statin; IMPROVE-IT: −16% further reduction on simvastatin 40 mg |
| Evolocumab / alirocumab (PCSK9i) | Std dosing on statin | LDL-C −55–65% on top of maximally tolerated statin | 12 wk | **[RCT]** | FOURIER (Sabatine, *NEJM* 2017); ODYSSEY OUTCOMES (Schwartz, *NEJM* 2018) | Median on-treatment LDL-C of ~30 mg/dL in FOURIER; no signal of harm at these levels |
| Inclisiran | 284 mg SC q6mo | LDL-C −50–53% on top of statin | 6 months | **[RCT]** | ORION-10, ORION-11 (Ray, *NEJM* 2020); ORION-8 extension (4-year) | Twice-yearly dosing; sustained durable effect |
| Bempedoic acid | 180 mg/d | LDL-C −18–21% | 12 wk | **[RCT]** | CLEAR Harmony, CLEAR Serenity (2019); CLEAR Outcomes (*NEJM* 2023) | Statin-intolerant option; does not cause myopathy (pro-drug not activated in skeletal muscle) |
| Obicetrapib (CETP inhibitor) | 10 mg/d | LDL-C −36% (HeFH on statin, BROOKLYN) to −41% (extension) | 12–52 wk | **[RCT]** | BROOKLYN (*Nature Med* 2025); BROADWAY 2025 | Pending regulatory approval; HDL-C +130% (not the mechanism of benefit) |
| Portfolio diet | Full pattern | LDL-C −17% (MD −0.73 mmol/L ~−28 mg/dL) | 4–12 wk | **[Meta]** | Chiavaroli et al. *J Am Heart Assoc* 2018 (7 RCTs, n=439) | Max adherence required; components: 45 g/d nuts, 25 g/d soy protein, 2 g/d plant sterols, ≥8 g/d soluble fiber |
| Mediterranean diet | Full pattern | LDL-C −10 mg/dL (~−0.25 mmol/L) | 12–24 wk | **[Meta]** | Liyanage et al. 2016; umbrella review PMC11795232 | Highly heterogeneous across studies; statistically significant but modest vs. Portfolio |
| Plant sterols/stanols | 2 g/d | LDL-C −10% (~−12 mg/dL at LDL-C 120) | 3–4 wk | **[Meta]** | Ras et al. *Eur J Nutr* 2014; Musa-Veloso et al. 2011 (meta-analysis 41 trials) | Dose-response: 1 g → −6%, 2 g → −10%, 3 g → −12%; diminishing returns above 3 g/d; does not stack linearly with statins (same mechanism — cholesterol absorption inhibition competes with ezetimibe) |
| Psyllium | 10–12 g/d | LDL-C −0.35 mmol/L (~−13 mg/dL) | 4–8 wk | **[Meta]** | Soluble fiber meta-analysis PMC12690803; Gibb et al. 2015 | Add-on to diet; combines well with statins (different mechanism) |
| Oat beta-glucan | ≥3 g/d | LDL-C −0.20 mmol/L (~−8 mg/dL) | 4–8 wk | **[Meta]** | Whitehead et al. *Am J Clin Nutr* 2014; Ho et al. 2016 (PMC5394769) | FDA health claim threshold is 3 g/d; approximately 60–70 g oats dry weight |
| Nuts (mixed, 45 g/d) | ~45–60 g/d | LDL-C −0.12 mmol/L (~−4.6 mg/dL) | 4–8 wk | **[Meta]** | Guasch-Ferré et al. *Nutr Metab Cardiovasc Dis* 2024 (113 trials, 8,060 adults) | Walnuts and almonds have strongest evidence; no significant dose-response above 60 g/d |
| Saturated fat ↓ (replace with PUFA) | 1% kcal SFA → PUFA | LDL-C −2.1 mg/dL per 1% kcal swap | 8–12 wk | **[Meta]** | Mensink WHO 2016 systematic review; Hooper *Cochrane* 2020 | From 15% → 7% SFA (−8% kcal) = ~−16 mg/dL LDL-C. MUFA replacement: −1.6 mg/dL per 1% kcal |
| Trans fat elimination | Removal of iTFA from diet | LDL-C −3.4% reversed + HDL-C +6.8% reversed | 4–8 wk | **[RCT]** | Mensink & Katan *NEJM* 1990; Mozaffarian review *PMC2830458* | Industrial trans fat now <0.5 g/serving in US foods since 2018; residual risk from imported/restaurant sources |
| Red yeast rice (standardized) | 3 mg monacolin K (~ low dose) | LDL-C −15% at 3 mg; −25–35% at 10 mg (lovastatin-equivalent) | 8–24 wk | **[Meta]** | PMC8802088; JACC Focus Seminar 2021 | Participants in trials take ~5–6 mg/d monacolin K equivalent with LDL-C results similar to lovastatin 20–40 mg |
| Berberine | 500 mg TID | LDL-C ~−15–19 mg/dL (−0.38–0.50 mmol/L) | 8–12 wk | **[Meta]** | Kong *J Clin Lipidol* 2013 (16 trials, 2,147 participants) | Most RCTs in Chinese populations; poor GI tolerability in some; mechanism: LDLR upregulation + reduced hepatic VLDL secretion |
| Aerobic exercise | ≥150 min/wk moderate | LDL-C −7 mg/dL | 12–26 wk | **[Meta]** | Kelley et al. *Sports Med* 2024 (148 RCTs, 8,673 participants) | Modest standalone; greatest effect when paired with dietary fat reduction |
| Weight loss (lifestyle) | Per 1 kg lost | LDL-C −1.28 mg/dL (95% CI −2.19 to −0.37) | Ongoing | **[Meta]** | Liu et al. *J Clin Endocrinol Metab* 2020 (73 RCTs) | 10 kg loss → ~−13 mg/dL LDL-C; TG changes larger (−4 mg/dL per kg) |
| Low-carb / ketogenic diet | <50 g carb/d | LDL-C **+** 4.8–5.1 mg/dL (mean increase); variable; TG ↓ −15 mg/dL; HDL-C +2.9 mg/dL | 12–24 wk | **[Meta]** | PLOS One 2020; AJCN 2024 meta-analysis | **LDL-C increases in lean individuals** — the "lean mass hyperresponder" phenotype (KETO trial, *JACC Adv* 2024). TG and HDL-C improve. Check ApoB directly, as LDL-C may be especially unreliable on keto. |
| Fructose / added sugar ↑ (hypercaloric) | >50–100 g/d fructose, hypercaloric | LDL-C +0.29 mmol/L (~+11 mg/dL), ApoB ↑; TG ↑ | 8–10 wk | **[RCT]** | Stanhope et al. *J Clin Endocrinol Metab* 2011 | Isocaloric fructose substitution: minimal LDL-C effect; effect requires positive energy balance |
| Smoking cessation | — | LDL-C not significantly changed (−0.064 mmol/L, CI not significant) | 6–12 wk | **[Meta]** | Eliasson et al. *Prev Med* 2003 (meta-analysis) | Main lipid benefit of quitting is on HDL-C, not LDL-C |

**Synthesis:**

- **Highest-leverage:** High-intensity statin remains the single most effective LDL-C intervention. PCSK9i on top of statin reaches levels otherwise unobtainable by any lifestyle approach.
- **Dietary ceiling:** Aggressive combined dietary intervention (Portfolio diet + saturated fat reduction + plant sterols + oat fiber) can yield approximately −25–35 mg/dL from a starting LDL-C of ~120 mg/dL. The ceiling is real and well-established.
- **What doesn't work as expected:** (a) Dietary cholesterol has a weak and highly heterogeneous effect on LDL-C in most people — ~⅔ of the population are "hypo-responders" to dietary cholesterol via LXR-mediated suppression of endogenous synthesis. (b) Low-carb diets frequently *raise* LDL-C in lean individuals despite reducing TG — always check ApoB alongside LDL-C on keto. (c) Saturated fat reduction produces much smaller absolute LDL-C reductions at lower baselines (e.g., someone already at LDL-C 90 will gain ~5–10 mg/dL, not 25 mg/dL, from SFA reduction).
- **South Asian note:** The MASALA cohort data show SA individuals' mean LDL-C was 112 ± 32 mg/dL — within "desirable" range by NCEP criteria — yet coronary calcium scores and event rates are disproportionately elevated. This argues against using LDL-C alone for risk stratification in SA individuals; ApoB or non-HDL-C better reflects their actual atherogenic particle burden. There is no SA-specific evidence that statin pharmacodynamics differ; a small open-label study (START-India equivalent) and the MASALA sub-analysis showed atorvastatin 20 mg producing −43% LDL-C in SA subjects, nearly identical to non-SA comparators.
- **23andMe SNPs:** *APOE* ε4 carriers benefit most from SFA reduction (LDL-C response ~2× that of ε3/ε3 homozygotes per Minihane 2007 and Corella et al. 2001). *LDLR* loss-of-function variants (FH diagnosis) blunt statin effect at low doses but respond to high-dose statin + ezetimibe + PCSK9i combinations. *PCSK9* gain-of-function variants (rare) may require PCSK9i to reach any guideline target.
- **Realistic 3-month outcome (no drugs):** From a starting LDL-C of ~120 mg/dL, optimal lifestyle achieves approximately −10–20 mg/dL in 12 weeks.
- **Realistic 6-month outcome (no drugs):** −15–25 mg/dL with sustained adherence.

---

## HDL-C

**Quick read:** Exercise is the most reliable lifestyle modifier (+3–10%). Alcohol raises HDL-C meaningfully but via a non-causal mechanism for CV risk. Weight loss produces modest gains. No pharmacologic HDL-raising strategy has been shown to reduce CV events in RCTs — do not treat HDL-C as a therapeutic target.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Aerobic exercise (sustained) | ≥150 min/wk | HDL-C +2–4 mg/dL (+3–10%) | 12–26 wk | **[Meta]** | Kelley et al. *Sports Med* 2024; PMC10003711 | Each additional weekly session: +2.11 mg/dL per additional session-minute (meta-regression). Dose-response confirmed. |
| Weight loss (lifestyle) | Per 1 kg lost | HDL-C +0.46 mg/dL (95% CI 0.20–0.71) at stable weight | Ongoing | **[Meta]** | Liu et al. *J Clin Endocrinol Metab* 2020 | During active weight loss HDL-C may not rise or may temporarily dip; the gain occurs at stable reduced weight. 10 kg loss → ~+4.6 mg/dL. |
| Smoking cessation | — | HDL-C +0.100 mmol/L (~+3.9 mg/dL) | Peak 3–6 months | **[Meta]** | Forey et al. *Biomarker Res* 2013 (27 studies) | Rapid within first 3 months; plateaus by ~6 months |
| Alcohol (moderate) | ~30–40 g/d (~2–3 standard drinks/d) | HDL-C +5 mg/dL (mean, 40.9 g/d for 4.1 wk) | 4–6 wk | **[Meta]** | Rimm et al. *NEJM* 1993; Gaziano et al. *Circulation* 2000; men: +0.134 mg/dL per g/d | Mechanism: accelerated ApoA-I/ApoA-II transport rate, not enhanced function. **Not a reason to drink more.** CV benefits of moderate alcohol are debated post-Mendelian-randomization era. |
| Mediterranean diet | Full pattern | HDL-C: marginal or no significant effect | 12–24 wk | **[Meta]** | Umbrella review PMC11795232 | HDL-C not a robust target of Mediterranean diet; some studies show no change |
| Low-carb / ketogenic diet | <50 g carb/d | HDL-C +2.9 mg/dL | 12–24 wk | **[Meta]** | PLOS One 2020; meta-analysis AJCN 2024 | Consistent finding; absolute effect modest |
| Fibrates | Fenofibrate 145 mg/d or gemfibrozil 600 mg BID | HDL-C +2–20% (+2–10 mg/dL range) | 8–12 wk | **[Meta]** | EMA assessment report; ACCORD Lipid | Highly variable; greatest response in low-HDL/high-TG phenotype |
| Niacin (extended-release) | 1.5–2 g/d ER | HDL-C +20–25% | 12–16 wk | **[RCT]** | AIM-HIGH (Boden et al., *NEJM* 2011); HPS2-THRIVE (*NEJM* 2014) | **Despite HDL-C rise, no CV event reduction.** Both trials neutral or harmful. Niacin not recommended as HDL-C therapy. |
| CETP inhibitors (torcetrapib, dalcetrapib, evacetrapib) | Varied | HDL-C +30–130% | 12–24 wk | **[RCT]** | ILLUMINATE (2007); dal-OUTCOMES (2012); ACCELERATE (2017) | **All three failed to reduce events.** Torcetrapib increased mortality. HDL-C raising per se does not reduce CV risk. |
| Obicetrapib (CETP inhibitor) | 10 mg/d | HDL-C +130–135% | 12 wk | **[RCT]** | BROOKLYN 2025 | CV outcomes data pending; benefit attributed to LDL-C and Lp(a) reduction, not HDL-C rise |
| Anabolic steroids (oral 17α-alkylated) | Any therapeutic or non-therapeutic dose | HDL-C −30–60% (crash) | 4–8 wk | **[Cohort]** | Multiple case series; NAMS review | Most potent HDL-C suppressor known; depot testosterone also suppresses but less dramatically |
| Plant-based diet (low-fat) | Full elimination animal products | HDL-C slight decrease or no change | 12–16 wk | **[Meta]** | Wang 2023 meta-analysis | Very low-fat plant diets can modestly lower HDL-C; high-fat versions maintain it |

**Synthesis:**

- **What actually works:** Aerobic exercise and smoking cessation are the only lifestyle interventions with reliable, mechanistically coherent HDL-C improvements and where the mechanism (better HDL particle function, not just mass) is plausible. Weight loss at stable weight adds small gains.
- **What doesn't work despite appearing to:** Pharmacologic HDL-raising (niacin, CETP inhibitors) has universally failed in outcomes trials. Obicetrapib is promising but its benefit is from LDL-C and Lp(a) reduction.
- **The key insight (from MR, Voight et al., *Lancet* 2012):** Genetic variants raising HDL-C do **not** lower CHD risk. HDL-C is a marker of metabolic health, not a causal protector. The efflux capacity of HDL (Rohatgi *NEJM* 2014; Khera *NEJM* 2011/2017 JUPITER) predicts events better than HDL-C mass — and efflux capacity improves with exercise and weight loss even when HDL-C change is modest.
- **South Asian note:** SA individuals have characteristically lower HDL-C (median ~48 mg/dL in MASALA vs. ~55 mg/dL in White comparators), driven by insulin resistance and high TG — not a primary HDL defect. Addressing TG and insulin resistance (exercise, carbohydrate reduction, weight normalization) indirectly raises HDL-C more than targeting HDL-C directly.
- **Realistic 3-month outcome:** From HDL-C 45 mg/dL, sustained aerobic exercise + smoking cessation: +3–6 mg/dL at 12 weeks.

---

## Triglycerides

**Quick read:** The three highest-leverage interventions are (1) carbohydrate reduction (especially refined carbs and fructose), (2) alcohol elimination, and (3) weight loss — all of which can reduce TG by 20–50% in individuals with baseline TG >150. Pharmacotherapy (fibrates, high-dose omega-3) is needed for TG >500, or for individuals who cannot achieve target via lifestyle.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Carbohydrate restriction (low-carb/keto) | <50–100 g/d carb from high baseline | TG −15–30 mg/dL (modest baseline) to −50–100 mg/dL (TG >200 baseline) | 4–12 wk | **[Meta]** | PLOS One 2020; multiple RCTs; Boden et al. | Largest TG response in insulin-resistant phenotype with high baseline TG. Effect is rapid (2–4 weeks). |
| Fructose / added sugar ↓ | Removing HFCS / SSB from diet | TG −20–40 mg/dL at high baselines | 8–12 wk | **[RCT]** | Stanhope *J Clin Endocrinol Metab* 2011; Mayes *Biochem J* 1993 | Fructose is the primary de novo lipogenesis substrate; hypercaloric fructose raises TG more than glucose |
| Alcohol elimination | From moderate-to-heavy drinking | TG −30–50 mg/dL | 4–6 wk | **[Cohort]** | Van de Wiel *Int J Vasc Med* 2012 | Alcohol acutely inhibits LPL, chronically elevates VLDL secretion; one drink raises TG 20–50 mg/dL acutely in susceptible individuals |
| Weight loss (lifestyle) | Per 1 kg lost | TG −4.0 mg/dL (95% CI −5.24 to −2.77) | Ongoing | **[Meta]** | Liu et al. *J Clin Endocrinol Metab* 2020 | 10 kg loss → ~−40 mg/dL TG; strongest per-kg lipid effect of weight loss |
| Aerobic exercise | ≥150 min/wk | TG −8 mg/dL average | 12–26 wk | **[Meta]** | Kelley *Sports Med* 2024 | Effect most pronounced 24–48h post-exercise (acute) and with sustained training. Greater reduction at higher TG baselines. |
| High-dose omega-3 (EPA+DHA) | 3–4 g/d prescription | TG −42 to −69 mg/dL at 2–3 g/d; up to −45% from very high baseline | 8–12 wk | **[Meta]** | AHA Science Advisory (*Circulation* 2019); JAHA dose-response meta-analysis 2023 | 2 g/d: −43 mg/dL; 3 g/d: −69 mg/dL. EPA alone (icosapent ethyl, VASCEPA) reduces CV events in high-TG patients on statin (REDUCE-IT: −25% MACE, 4 g/d EPA). Note: mineral oil placebo controversy. DHA more TG-lowering per gram but raises LDL-C slightly; EPA does not raise LDL-C. |
| Fibrates (fenofibrate, gemfibrozil) | Fenofibrate 145 mg/d; gemfibrozil 600 mg BID | TG −30–50% | 8–12 wk | **[Meta]** | EMA assessment; ACCORD Lipid trial | Largest response in TG >400. Pemafibrate (selective PPARα, Japan-approved) reduced TG ~50% but failed to reduce CV events (PROMINENT, *NEJM* 2022) despite TG lowering — the pemafibrate finding **directly challenges** the causal hypothesis for TG-driven CV risk via LDL-C-neutral TG reduction. |
| Mediterranean diet | Full pattern | TG −16 to −30 mg/dL | 12–24 wk | **[Meta]** | Liyanage et al. 2016; PREDIMED sub-analyses | Driven by olive oil + fish + reduced refined carbs |
| Plant sterols/stanols | 2 g/d | No significant TG effect | — | **[Meta]** | Ras et al. 2014 | Sterols primarily reduce intestinal cholesterol absorption, not TG |
| Berberine | 1500 mg/d | TG −0.28–0.37 mmol/L (~−25–33 mg/dL) | 8–12 wk | **[Meta]** | Kong 2013; Zamani 2019 | One of berberine's stronger lipid effects |
| Low-fat diet | <25% kcal fat | TG ↑ (increases TG if refined carbs replace fat) | 8–12 wk | **[RCT]** | Multiple RCTs; Mensink WHO 2016 | Fat reduction replaced by refined carbs raises TG; replaced by fiber/vegetables does not |

**Synthesis:**

- **Highest-leverage lifestyle:** Remove alcohol, reduce fructose/refined carbs, lose weight. A motivated individual with TG 200 mg/dL can reach <100 mg/dL within 12 weeks purely from dietary changes.
- **The PROMINENT puzzle:** Pemafibrate (selective PPARα agonist, *NEJM* 2022) reduced TG by ~26%, reduced remnant cholesterol, but did not reduce CV events in 10,497 patients with TG 200–499 on statin. This directly challenges whether TG *per se* (vs. the particle context in which they travel) is the causally relevant variable. Remnant cholesterol MR data support causality for the particles, not TG mass per se. Verdict: don't treat TG as an isolated target — treat the underlying metabolic state (insulin resistance, dietary composition, weight) that drives it.
- **South Asian note:** SA individuals have a high prevalence of hypertriglyceridemia driven by insulin resistance even at normal BMI (MASALA). The TG response to carbohydrate restriction in SA individuals has not been directly studied in a large RCT, but the mechanism (suppression of hepatic de novo lipogenesis via reduced insulin-driven substrate) is not ethnicity-specific.
- **23andMe SNPs:** *APOC3* loss-of-function variants lower TG substantially lifelong (protective; consistent with the failed volanesorsen/APOC3-inhibitor hypothesis suggesting the causal direction is real). *LPL* variants (loss-of-function) elevate TG; *APOA5* variants modify TG response to fasting and carbohydrate intake.
- **Realistic 3-month outcome:** From TG 180 mg/dL, low-carb diet + alcohol removal: −40–70 mg/dL. From TG 120 mg/dL, less dramatic: −10–25 mg/dL.

---

## Non-HDL-C

**Quick read:** Non-HDL-C = TC − HDL-C. It responds to every intervention that moves LDL-C or TG, and is more sensitive than LDL-C in insulin-resistant phenotypes. Effect sizes are approximately LDL-C × 1.1–1.2 (since it also captures VLDL changes).

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| High-intensity statin | Rosuvastatin 20–40 mg or Atorvastatin 40–80 mg | Non-HDL-C −45–52% | 6–12 wk | **[RCT/Meta]** | STELLAR 2003; bempedoic acid pooled data (−13% incremental non-HDL-C) | Slightly larger % than LDL-C reduction due to VLDL contribution |
| Bempedoic acid | 180 mg/d | Non-HDL-C −10–13% | 12 wk | **[RCT]** | CLEAR Harmony (Ray, *NEJM* 2019) | Standalone or add-on |
| Portfolio diet | Full pattern | Non-HDL-C −17% (parallel to LDL-C) | 4–12 wk | **[Meta]** | Chiavaroli 2018 | No specific non-HDL-C sub-analysis published; inferred from LDL-C + TG components |
| Omega-3 (EPA+DHA 3–4 g/d) | 3–4 g/d | Non-HDL-C may rise slightly (DHA can raise LDL-C +1–3%); EPA neutral to LDL-C | 8–12 wk | **[Meta]** | EPA vs DHA differential effects meta-analysis, *Front Nutr* 2024 | Net non-HDL-C effect depends on EPA:DHA ratio; prescription EPA (icosapent ethyl) preferred if LDL-C already at target |
| Weight loss + exercise | 5–10% body weight reduction | Non-HDL-C −8–12% (captured from LDL-C + TG improvements) | 12–26 wk | **[Meta]** | Liu 2020 | Strongest effect in insulin-resistant / high-TG phenotype |

**Synthesis:**
Non-HDL-C is a superior metric to LDL-C in patients with TG >150 mg/dL (Boekholdt et al., *JAMA* 2012). For a lean individual with normal TG, non-HDL-C and LDL-C move in near-lockstep — in that case, LDL-C effect sizes can be applied directly. For the typical South Asian phenotype (TG 150–200, modestly elevated), non-HDL-C captures the additional remnant-cholesterol burden that LDL-C misses; drug effects on non-HDL-C are therefore more informative than LDL-C effects alone in this population.

---

## Total Cholesterol

Total cholesterol tracks non-HDL-C and LDL-C in parallel. Effect sizes for interventions are approximately LDL-C reduction + HDL-C change net. TC is the least informative single number for intervention monitoring; ApoB or non-HDL-C is preferred. TC tables are omitted here to avoid redundancy — apply LDL-C % reductions to TC while noting that HDL-C changes offset them (e.g., fibrates lower TG but raise HDL-C → TC change smaller than the ApoB change).

---

## TC/HDL Ratio and ApoB/ApoA1 Ratio

Both ratios improve when atherogenic particles decrease and/or HDL-C rises. There are no intervention trials specifically powered on the ratio as an outcome; ratio changes are derivable from LDL-C and HDL-C effect sizes above. Key points:

- **Statins:** TC/HDL ratio typically improves −25–40% (LDL-C driven numerator reduction; HDL-C minimally affected).
- **Fibrates:** TC/HDL ratio improved via TG reduction (numerator) + HDL-C increase (denominator) — one of fibrates' stronger points, particularly in atherogenic dyslipidemia.
- **Weight loss:** Improves TC/HDL through both channels (non-HDL-C down, HDL-C up at stable weight).
- **ApoB/ApoA1 ratio** (better than TC/HDL): improves proportionally to ApoB reduction (numerator). ApoA1 is modestly raised by exercise (+0.29 mg/dL per g/d alcohol via transport rate, but ApoA1 itself responds minimally to dietary change). The ratio is best thought of as a summary of ApoB trajectory plus HDL metabolic health.

---

## Lp(a)

**Quick read:** Lp(a) is ~80–90% genetically determined and largely non-modifiable by lifestyle or standard lipid therapy. PCSK9 inhibitors lower it ~25–30% — meaningful if starting very high but insufficient as standalone therapy for Lp(a) >125 nmol/L. Targeted RNA-based therapies in Phase 2/3 achieve 80–94% reduction and represent a generational change in Lp(a) management pending outcomes data.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| PCSK9 inhibitors (evolocumab + alirocumab pooled) | Standard dosing | Lp(a) −27% (95% CI −29.8% to −24.1%); evolocumab −29%; alirocumab −25% | 12 wk | **[Meta]** | JACC Advances meta-analysis (2024); FOURIER, ODYSSEY analyses | At baseline Lp(a) 75 nmol/L, 27% reduction → −20 nmol/L; still above guideline threshold of <75 nmol/L. Insufficient as standalone Lp(a) therapy. |
| Inclisiran | 284 mg q6mo | Lp(a) ~−20–25% | 6 months | **[RCT]** | ORION trials sub-analyses | Similar profile to monoclonal PCSK9i; mechanism same |
| Niacin (extended-release) | 1.5–2 g/d | Lp(a) −19–25% | 12–16 wk | **[Meta]** | AIM-HIGH sub-analyses; niacin meta-analysis; HPS2-THRIVE | AIM-HIGH: −19% reduction in Lp(a) despite which no CV event benefit. Niacin no longer recommended. |
| Pelacarsen (ASO) | 80 mg SC monthly | Lp(a) −80% (Phase 2, median reduction) | 6 months | **[RCT]** | Tsimikas et al., *NEJM* 2020 (Phase 2); Phase 3 Lp(a)HORIZON results pending 2025/2026 | 98% of patients reduced Lp(a) below 50 mg/dL threshold in Phase 2. Phase 3 outcomes data pending. |
| Olpasiran (siRNA) | 75–225 mg SC q12wk | Lp(a) −90–95% | 3–6 months | **[RCT]** | Nissen et al., *NEJM* 2022 (OCEAN(a)-DOSE); Phase 3 OCEAN(a) ongoing (results ~2027) | 95% reduction sustained >6 months after single dosing cycle; most potent Lp(a) reduction of any agent tested. |
| Lepodisiran (siRNA) | 400 mg SC (single dose) | Lp(a) −93.9% at day 180; >90% at day 360 | 6 months | **[RCT]** | ALPACA Phase 2 (ACC.25, 2025); Phase 3 ACCLAIM-Lp(a) enrolling | Single injection with ~12-month effect duration; most convenient dosing profile of the siRNA class. |
| Obicetrapib (CETP inhibitor) | 10 mg/d | Lp(a) −45% in patients with baseline Lp(a) 50–150 nmol/L; pooled Phase 3 BROADWAY+BROOKLYN+TANDEM | 12 wk | **[RCT]** | NewAmsterdam Pharma EAS 2025 data | Most efficacious approved-pathway Lp(a) reducer if outcomes data support approval; mechanism unclear but plausible via CETP-mediated Lp(a) clearance |
| Estrogen (oral) | Standard doses | Lp(a) ↓ ~20–30% | 8–12 wk | **[Cohort/RCT]** | Multiple HRT studies | Mechanism unclear; not indicated for Lp(a) management; postmenopausal Lp(a) typically rises without estrogen |
| Statins | Any dose | Lp(a) **unchanged or slightly increased** (+5–15% in some studies) | 6–12 wk | **[Meta]** | Multiple statin RCT sub-analyses | Do not use statins expecting Lp(a) reduction; the slight Lp(a) rise is mechanistically attributed to upregulation of LDL receptor reducing the VLDL shunting that provides some Lp(a) clearance — not clinically meaningful |
| Lipoprotein apheresis | Weekly or biweekly | Lp(a) −60–70% per session (rebounds between sessions) | Immediate | **[Cohort]** | FDA approval for Lp(a) >60 mg/dL with ASCVD | Last resort; no RCT of outcomes; mean reduction over time ~25–35% at trough |
| Diet / exercise / weight loss | Any standard approach | Lp(a) essentially unchanged | Any duration | **[Cohort/MR]** | Multiple cohort studies; NLA 2024 statement | ~80–90% heritability means lifestyle effects are ≤5%; do not expect lifestyle to meaningfully change Lp(a) |

**Synthesis:**

- **The hard truth:** If you have elevated Lp(a) (>125 nmol/L), currently available pharmacotherapy (statins, ezetimibe, niacin) does not meaningfully lower it. PCSK9 inhibitors reduce it ~25–30%, which may be sufficient for borderline elevations (e.g., 150 → 110 nmol/L). For markedly elevated Lp(a) (>200 nmol/L), only the RNA-targeted therapies in Phase 2/3 achieve clinically meaningful absolute reductions. The rational response for a young person with high Lp(a) today is: (1) maximize control of all other CV risk factors (especially ApoB), and (2) monitor the siRNA trial landscape for approval.
- **The MR requirement:** Burgess et al. (*JAMA Cardiol* 2018) MR analysis estimates that 65–100 mg/dL **absolute** Lp(a) reduction is needed for a clinically meaningful (~22%) CV risk reduction — this is why only the siRNA/ASO agents are likely to show outcomes benefit in Phase 3 trials, and why Lp(a)HORIZON and OCEAN(a) are so consequential.
- **South Asian note:** SA individuals have substantially higher median Lp(a) than White or East Asian populations. Patel et al. (*Circulation* 2021, multi-ethnic analysis) reports SA median Lp(a) ~31 nmol/L (vs. ~19 nmol/L in Whites, ~16 nmol/L in East Asians, ~75 nmol/L in Black individuals). The proportion of SA individuals above the 125 nmol/L threshold is higher than in Europeans, meaning Lp(a)-targeted therapy, when it becomes available, will be particularly impactful in this population. This is not SA-specific guideline advice as of 2025 — but a reasonable prior given the distributional data.
- **23andMe SNPs:** *LPA* isoform size (KIV-2 repeat number) is the primary determinant of Lp(a) concentration — shorter isoforms (fewer KIV-2 repeats, ≤22) correspond to higher Lp(a) and independently higher risk per unit Lp(a) (Erqou et al., *JAMA* 2009). The SNPs rs10455872 and rs3798220 (tagging short isoforms) each carry ~1.7–1.9× CHD risk per allele (Clarke et al., *NEJM* 2009). If 23andMe reports these risk alleles, they confirm elevated Lp(a) is genetically driven and should prompt serum Lp(a) measurement if not already done.
- **Realistic outcome on any current non-targeted therapy:** A 20-year-old with Lp(a) 200 nmol/L on optimal lifestyle + PCSK9i → best achievable ~150 nmol/L. With RNA-targeted therapy (pending approval): ~10–20 nmol/L.

---

## hs-CRP

**Quick read:** Weight loss and exercise are the most reliable lifestyle reducers. Statins have a pleiotropic anti-inflammatory effect (independent of LDL-C lowering) — the JUPITER trial was built on this. Ultra-processed food removal, Mediterranean diet, and sleep optimization have documented but smaller effects. Most lifestyle interventions reduce hs-CRP by 20–40% from a modestly elevated baseline.

**Effect size table:**

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| High-intensity statin (rosuvastatin 20 mg) | 20 mg/d | hs-CRP −37–43% (mean −0.97 mg/L, WMD) | 12 wk | **[Meta]** | Statin hs-CRP meta-analysis PMC8816584; JUPITER (Ridker *NEJM* 2008) | JUPITER: rosuvastatin 20 mg reduced hs-CRP from ~4.2 → ~2.2 mg/L at 12 months. Effect independent of LDL-C lowering. |
| Atorvastatin 80 mg | 80 mg/d | hs-CRP −4.3 mg/L (mean, starting from high CRP patients) | 12–24 wk | **[RCT]** | REVERSAL trial data; meta-analysis PMC8816584 | Context-dependent: larger reduction at higher baseline CRP |
| Bempedoic acid | 180 mg/d | hs-CRP −16–22% | 12 wk | **[RCT]** | CLEAR Harmony; CLEAR Serenity; Laufs et al. *JAMA Cardiol* 2021 | Anti-inflammatory mechanism independent of LDL-C lowering (inhibits ATP-citrate lyase in immune cells); CLEAR Outcomes trial confirmed hs-CRP as mediator |
| Canakinumab (anti-IL-1β) | 150 mg SC q3mo | hs-CRP −36% (from median ~3.6 mg/L); IL-6 −40% | 3–6 months | **[RCT]** | CANTOS (Ridker *NEJM* 2017; 10,061 patients) | **Proof of inflammation hypothesis:** reduced MACE by 15% **without** changing LDL-C. Not clinically available for CV indication; referenced as mechanistic anchor. |
| Weight loss (lifestyle) | Per 1 kg | hs-CRP −0.13 mg/L per kg; −0.25 mg/L per 6.4 kg | Ongoing | **[Meta]** | POUNDS LOST trial; multiple meta-analyses | 10 kg loss → ~−1.3 mg/L hs-CRP. Adipose tissue is the dominant source of IL-6 in lean-to-overweight individuals. |
| Mediterranean diet | Full pattern | hs-CRP −0.98 to −1.0 mg/L | 12–24 wk | **[Meta]** | Casas et al. *Nutrients* 2025; multiple meta-analyses | PREDIMED: Mediterranean + olive oil reduced hs-CRP vs. low-fat control. Heterogeneous across studies. |
| Aerobic exercise | ≥150 min/wk | hs-CRP −0.26 mg/L (mean) | 12–26 wk | **[Meta]** | Goldhammer review; Kelley 2024 | Modest standalone; effect larger in overweight or obese individuals (who also lose weight with exercise). |
| Low-carb / Mediterranean-style diet (reducing ultra-processed food) | Full pattern shift | hs-CRP −0.5–1.5 mg/L | 8–16 wk | **[Meta]** | Multiple dietary RCTs | The dominant driver is reduction in adiposity and processed food, not the macronutrient split per se |
| Sleep optimization | 7–9 h/night from <6 h baseline | hs-CRP: modest reduction; persistent sleep restriction (<5 h/night for >8 nights) raises CRP by d=0.76 (Cohen's d) | Chronic effect | **[Meta]** | Irwin et al. *Biol Psychiatry* 2016 (72 studies, n>50,000); Ballesio et al. *J Sleep Res* 2026 | Long sleep (>9 h) also associated with higher CRP — U-shaped; optimal appears to be 7–8 h. Single-night sleep deprivation: no CRP change; chronic restriction: significant. |
| Smoking cessation | — | hs-CRP progressively normalizes; OR 0.73 for elevated hs-CRP at ≥17 months post-cessation vs. current smokers | 12–24 months | **[Cohort]** | Korean NHIS data (Toxics 2022, n>100,000) | Time-course is slow — months to years; not captured in short-term RCTs |
| Omega-3 (EPA+DHA) | 3–4 g/d | hs-CRP direction variable (not a primary anti-inflammatory target for CRP specifically) | 8–12 wk | **[Meta]** | Mixed results; meta-analyses show no consistent hs-CRP reduction from omega-3 | Omega-3 reduces IL-6 and some inflammatory eicosanoids but hs-CRP response is heterogeneous |
| Periodontitis treatment | Professional dental cleaning + antibiotics | hs-CRP −0.50 mg/L (estimated from periodontal-CRP literature) | 4–8 wk | **[RCT]** | Caula et al. 2014; AHA statement | Periodontal disease is an underappreciated driver of hs-CRP in otherwise healthy young adults |
| Alcohol cessation (from heavy drinking) | Full elimination | hs-CRP: variable; heavy drinking raises hs-CRP; cessation normalizes over months | 3–6 months | **[Cohort]** | Multiple alcohol + inflammation cohorts | Moderate drinking has ambiguous hs-CRP effect; heavy drinking clearly pro-inflammatory |

**Synthesis:**

- **Highest-leverage:** Weight loss (if overweight), high-intensity statin (if using statins anyway — independent of LDL-C benefit), and sustained Mediterranean / whole-food dietary pattern.
- **What doesn't work as expected:** Omega-3 supplementation has inconsistent hs-CRP effects despite anti-inflammatory reputation — the mechanism is via resolvin/protectin pathways (resolution of inflammation), not acute CRP suppression. Short-term sleep deprivation in healthy people produces little acute hs-CRP change; the CRP risk from sleep is mediated by chronic restriction patterns over weeks.
- **Interpretation caution unique to hs-CRP:** Single measurements are highly variable (intra-individual CV ~30–50%). AHA recommends averaging two measurements 2 weeks apart obtained outside any acute illness, injury, vaccination, or intense exercise within 72 h. A single elevated hs-CRP in a healthy young male is frequently confounded — re-test before drawing conclusions.
- **South Asian note:** There is no SA-specific RCT on hs-CRP-lowering interventions. The MASALA cohort shows higher prevalence of metabolic syndrome and insulin resistance in SA individuals, which are the dominant non-infectious drivers of chronic low-grade inflammation. Weight management and carbohydrate restriction are therefore particularly high-yield in SA individuals with borderline hs-CRP.
- **23andMe SNPs:** No established pharmacogenomic SNPs modifying statin hs-CRP response. CRP-raising SNPs (*CRP* locus polymorphisms, e.g., rs1130864) influence baseline hs-CRP ~15–25% but do not modify intervention response. Not actionable from 23andMe data in terms of intervention effect-size modification.
- **Realistic 3-month outcome (no drugs):** From hs-CRP 2.5 mg/L with no acute illness, optimal dietary pattern + exercise + sleep: −0.8 to −1.5 mg/L.
- **Realistic 6-month outcome with weight loss of 5 kg:** −1.0 to −2.0 mg/L.

---

## Cross-Marker Patterns

Interventions rarely move a single marker in isolation. The following coupled effects are well-documented in RCTs and should be used when estimating total panel changes from a single intervention:

| Intervention | ApoB | LDL-C | HDL-C | TG | Non-HDL-C | hs-CRP |
|---|---|---|---|---|---|---|
| High-intensity statin | −40–52% | −46–55% | ±2% | −10–20% | −40–52% | −37–43% |
| Ezetimibe (add-on) | −10–15% | −14–18% | ±0% | ±0% | −12–16% | ±minimal |
| PCSK9i (evolocumab) | −55–60% | −58–65% | +5–9% | −12–19% | −50–55% | No primary effect |
| Portfolio diet | −15–20% | −17–28 mg/dL | ±minimal | −10–15% | ~−17% | −0.5 to −1.0 mg/L |
| Weight loss (10 kg) | ~−15 mg/dL | −13 mg/dL | +4.6 mg/dL | −40 mg/dL | ~−17 mg/dL | −1.3 mg/L |
| Aerobic exercise | −2–5 mg/dL | −7 mg/dL | +2–4 mg/dL | −8 mg/dL | −5–8 mg/dL | −0.26 mg/L |
| Mediterranean diet | ~−10% | ~−10 mg/dL | minimal | −16–30 mg/dL | ~−10% | −0.98 mg/L |
| Low-carb diet | variable (↑ in lean) | ↑+5 mg/dL (mean lean) | +2.9 mg/dL | −15 mg/dL | Net: variable | Limited data |
| Omega-3 (4 g/d EPA) | No primary effect | No change (EPA) | Minimal | −30–50% | Neutral to modest ↓ | Inconsistent |
| Fibrates | −10–15% | −15 mg/dL | +5–15% | −30–50% | −15–25% | Modest |
| Smoking cessation | Modest | Minimal | +3.9 mg/dL | Minimal | Minimal | Normalizes over 12–24 months |
| Bempedoic acid | −9–12% | −18–21% | Minimal | Minimal | −10–13% | −16–22% |

**Key insight:** Weight loss moves the most markers simultaneously and in the right direction. A 10 kg weight loss produces measurable improvements in ApoB, LDL-C, TG, non-HDL-C, HDL-C (at stable weight), and hs-CRP — no single non-pharmacologic intervention matches this breadth. This is particularly relevant for a lean individual: even a 3–5 kg reduction in visceral fat (measurable as waist circumference reduction) produces disproportionate metabolic improvements relative to total mass lost.

---

## Drug Class Reference Table

For context only. These are effect sizes from trials in mixed or high-risk adult populations; they do not represent recommendations.

| Drug class | Example agents | LDL-C | ApoB | TG | HDL-C | Lp(a) | hs-CRP | Primary source |
|---|---|---|---|---|---|---|---|---|
| **High-intensity statin** | Rosuvastatin 20–40 mg, Atorvastatin 40–80 mg | −46–55% | −40–52% | −10–20% | ±2% | +5–15% (slight ↑) | −37–43% | STELLAR 2003; JUPITER |
| **Moderate-intensity statin** | Atorvastatin 10 mg, Simvastatin 20–40 mg, Pravastatin 40 mg | −30–39% | −25–35% | −8–15% | ±2% | Slight ↑ | −25–35% | STELLAR 2003 |
| **Ezetimibe** | Ezetimibe 10 mg | −17–18% (mono); −14–25% (add-on statin) | −10–17% | No sig. effect | No sig. effect | Modest effect | Minimal | IMPROVE-IT; multiple meta-analyses |
| **PCSK9 monoclonal antibody** | Evolocumab 140 mg q2wk; Alirocumab 75–150 mg q2wk | −55–65% (on statin) | −55–60% | −15–20% | +5–9% | −25–30% | No primary effect | FOURIER (*NEJM* 2017); ODYSSEY OUTCOMES (*NEJM* 2018) |
| **PCSK9 siRNA** | Inclisiran 284 mg q6mo | −50–53% (on statin) | ~−50% | No primary | Minimal | No primary | No primary | ORION-10/11 (*NEJM* 2020); ORION-8 (4-yr extension) |
| **Bempedoic acid** | Bempedoic acid 180 mg/d | −18–21% | −9–12% | No sig. effect | No sig. effect | No effect | −16–22% | CLEAR trials (2019–2023) |
| **Fibrate** | Fenofibrate 145 mg/d; Gemfibrozil 600 mg BID | −5–15% | −10–15% | −30–50% | +5–20% | No effect | Modest | EMA assessment; ACCORD Lipid; PROMINENT (*NEJM* 2022) |
| **CETP inhibitor (obicetrapib)** | Obicetrapib 10 mg/d | −36–42% | −33–42% | Modest ↓ | +130–135% | No ↑ (neutral) | −45% Lp(a) in high-baseline patients | BROOKLYN (*Nature Med* 2025); BROADWAY 2025 |
| **Niacin (ER)** | 1.5–2 g/d | −15–20% | −15–20% | −25–35% | +20–25% | −19–25% | No benefit (trials negative) | AIM-HIGH (*NEJM* 2011); HPS2-THRIVE (*NEJM* 2014) |
| **Omega-3 (prescription EPA only)** | Icosapent ethyl (Vascepa) 4 g/d | No change | No primary | −25–45% at high TG | Minimal | No change | −25% MACE at 5 yr (REDUCE-IT) | REDUCE-IT (*NEJM* 2019) |
| **Omega-3 (EPA+DHA, prescription)** | Lovaza 4 g/d | LDL-C neutral to slight ↑ (DHA) | No primary | −30–45% | Modest ↑ | No primary change | No benefit in STRENGTH (*JAMA* 2020) | AHA Science Advisory 2019; STRENGTH 2020 |
| **Lp(a) antisense oligonucleotide** | Pelacarsen 80 mg SC/monthly | No primary | No primary | No primary | No primary | Lp(a) −80% (Phase 2) | Phase 3 Lp(a)HORIZON results pending | Tsimikas *NEJM* 2020 |
| **Lp(a) siRNA** | Olpasiran q12wk; Lepodisiran (single dose annually) | No primary | No primary | No primary | No primary | Lp(a) −90–94% | Outcomes pending | OCEAN(a) Phase 3; ALPACA ACC.25 2025 |

---

## Sources

### Primary trials cited

- Ballantyne CM et al. (STELLAR). *Am J Cardiol* 2003;92(2):152-60.
- Ray KK et al. (CLEAR Harmony). *NEJM* 2019;380(11):1022-1032.
- Nissen SE et al. (CLEAR Serenity). *JAMA* 2019;323(14):1345-1355.
- Ray KK et al. (ORION-10, ORION-11). *NEJM* 2020;382(16):1507-1519.
- Nissen SE et al. (OCEAN(a)-DOSE, olpasiran). *NEJM* 2022;387(20):1855-1864.
- Tsimikas S et al. (pelacarsen, APOLLO Phase 2). *NEJM* 2020;382(3):244-255.
- Sabatine MS et al. (FOURIER, evolocumab). *NEJM* 2017;376(18):1713-1722.
- Schwartz GG et al. (ODYSSEY OUTCOMES, alirocumab). *NEJM* 2018;379(22):2097-2107.
- Ridker PM et al. (JUPITER, rosuvastatin). *NEJM* 2008;359(21):2195-2207.
- Ridker PM et al. (CANTOS, canakinumab). *NEJM* 2017;377(12):1119-1131.
- Cannon CP et al. (IMPROVE-IT, ezetimibe). *NEJM* 2015;372(25):2387-2397.
- Bhatt DL et al. (REDUCE-IT, icosapent ethyl). *NEJM* 2019;380(1):11-22.
- Nissen SE et al. (STRENGTH, omega-3 carboxylic acids). *JAMA* 2020;324(22):2268-2280.
- Boden WE et al. (AIM-HIGH, niacin). *NEJM* 2011;365(24):2255-2267.
- HPS2-THRIVE Collaborative Group. *NEJM* 2014;371(3):203-212.
- Nicholls SJ et al. (BROOKLYN, obicetrapib). *Nature Med* 2025.
- Ballantyne CM et al. Statin-induced myopathy and SLCO1B1. *NEJM* 2008;359(8):789-799 (GWAS).
- Barter PJ et al. (ILLUMINATE, torcetrapib). *NEJM* 2007;357(21):2109-2122.
- Nissen SE et al. (PROMETHEUS — CLEAR Outcomes). *NEJM* 2023;388(15):1353-1364.
- Lincoff AM et al. (ACCELERATE, evacetrapib). *NEJM* 2017;376(18):1933-1942.
- Das Pradhan A et al. (PROMINENT, pemafibrate). *NEJM* 2022;387(21):1923-1934.

### Meta-analyses and systematic reviews

- Elam MB et al. ApoB lowering therapies meta-analysis. *Circ Cardiovasc Qual Outcomes* 2020.
- Liu Z et al. Weight loss and serum lipids. *J Clin Endocrinol Metab* 2020;105(12):3695-3708.
- Chiavaroli L et al. Portfolio diet pattern and CVD. *J Am Heart Assoc* 2018;7(23):e009862.
- Kelley GA et al. Exercise training and blood lipids. *Sports Med* 2024 (PMC update).
- Ras RT et al. Plant sterols/stanols dose-response. *Eur J Nutr* 2014;53:1149-1160.
- Mensink RPM. WHO systematic review of dietary fatty acids and serum lipids. WHO 2016.
- Hooper L et al. Reduction in saturated fat intake for CVD. *Cochrane* 2020.
- Kong W et al. Berberine and blood lipids. *J Clin Lipidol* 2013;7:68-82.
- Forey BA et al. Quitting smoking and HDL-C. *Biomarker Res* 2013;1:26.
- Eliasson M et al. Smoking cessation and lipid profiles. *Prev Med* 2003;37:219-224.
- Irwin MR et al. Sleep disturbance and inflammation. *Biol Psychiatry* 2016;80(1):40-52.
- Statin hs-CRP meta-analysis. PMC8816584.
- PCSK9i and Lp(a) meta-analysis. *JACC Advances* 2024;3(2):101549.
- Whitehead A et al. Oat beta-glucan and LDL-C. *Am J Clin Nutr* 2014;100(6):1413-21.
- Mozaffarian D et al. Industrial and ruminant trans fatty acids and CHD risk. *Eur J Clin Nutr* 2009;63:S5-21 (PMC2830458).

### Guidelines

- 2019 ESC/EAS Dyslipidaemia Guidelines. Mach F et al. *Eur Heart J* 2020;41(1):111-188.
- 2026 ACC/AHA/Multisociety Guideline on Dyslipidemia. *Circulation* 2026.
- NLA 2021 Scientific Statement on South Asians and ASCVD. *J Clin Lipidol* 2021.
- NLA 2024 Focused Update on Lp(a). Wilson DP et al. *J Clin Lipidol* 2024.
- CPIC Guideline for SLCO1B1 and Simvastatin. *Clin Pharmacol Ther* 2022.
- AHA Science Advisory on Omega-3 and Hypertriglyceridemia. *Circulation* 2019;140(12):e673-e691.

### South Asian–specific sources

- Kanaya AM et al. MASALA cohort design and lipid results. *BMC Public Health* 2013; *J Am Heart Assoc* multiple years.
- Patel AP et al. Multiethnic Lp(a) distribution. *Circulation* 2021;144:1671-1681.
- NLA Scientific Statement on Prevention of ASCVD in South Asians in the US. *J Clin Lipidol* 2021;15(1):46-73.
- Ranganath LR et al. START-India statin response. *Pilot open-label study* 2007 (PubMed 17315607).

### Pharmacogenomics

- SEARCH Collaborative Group. SLCO1B1 GWAS and simvastatin myopathy. *NEJM* 2008;359(8):789-799.
- Minihane AM. ApoE genotype and dietary fat responsiveness. *Proc Nutr Soc* 2007;66(2):183-188.
- Clarke R et al. LPA SNPs and CHD risk. *NEJM* 2009;361(26):2518-2528.
- Erqou S et al. Lipoprotein(a) concentration and risk of CHD, stroke, and nonvascular mortality. *JAMA* 2009;302(4):412-423.
