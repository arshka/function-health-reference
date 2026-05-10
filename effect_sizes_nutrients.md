# Intervention Effect Sizes — Nutrient Markers

**Scope:** Quantified effect sizes for interventions that move iron studies (ferritin, serum iron, TSAT, TIBC), vitamins (D, B12, MMA, folate, homocysteine), minerals (magnesium, zinc, calcium), and the omega-3 index. This file is a companion to `nutrients_vitamins_minerals.md` and `nutrients_omega_fatty_acids.md`, which cover biology and reference ranges. This file covers *what moves markers and by how much* — not what the markers mean.

**Evidence grading applied per claim:**
- **[Meta]** — systematic review / meta-analysis
- **[RCT]** — individual randomized controlled trial
- **[Cohort]** — prospective or retrospective observational
- **[Mechanism]** — in vitro, animal, or pharmacological reasoning
- **[MR]** — Mendelian randomization
- **[Consensus/GL]** — clinical guideline or expert consensus

**Serum vs. functional markers — global caveat:** Serum concentrations often poorly reflect tissue stores or functional sufficiency. This matters most for: magnesium (serum Mg is 99% extracellular and tightly buffered; RBC Mg is more informative), B12 (serum cobalamin vs MMA — serum is insensitive for functional deficiency), zinc (serum zinc is an acute-phase reactant — infected/inflamed individuals look falsely replete), vitamin D (circulating 25-OH is the accepted clinical proxy but tissue 1,25-OH₂D activity is separate). Ferritin is an acute-phase reactant and unreliable in inflammation (see ferritin section). Where intervention data are available for both serum and functional markers, both are reported.

**South Asian (SA) context — global note:** SA populations carry elevated baseline risk for deficiency across almost all markers in this file: near-universal vitamin D deficiency regardless of latitude (≥80% in some UK SA winter samples) **[Meta — BMC Public Health 2021]**, high B12 deficiency prevalence in vegetarian SA (up to 70% in some Indian cohorts) **[Cohort — Antony 2003, Grover 2011]**, lower phytate-adjusted zinc and iron bioavailability in high-phytate vegetarian diets **[Meta — Gibson AJCN 2018]**, and lower omega-3 index from lower fish consumption offset somewhat by a FADS2 insertion (rs66698963) present in ~70% of South Asians that upregulates ALA→EPA/DHA conversion **[Cohort — 1000 Genomes project analysis]**. These factors are noted inline under each marker.

**Responder variation:** Supplement responses for every nutrient here span a 2–5× range across individuals, driven by: baseline status (larger deficit → larger response per dose), genetics, body composition (D3 is fat-soluble — adipose dilutes it), gut absorption efficiency, competing dietary factors (phytate, calcium × iron, zinc × copper), and form/timing of supplement. Single mean effect sizes without uncertainty ranges should not be treated as expected individual responses.

---

## Ferritin

**Quick read:** Oral iron raises ferritin slowly — ~3–6 months for meaningful repletion from frank deficiency. Alternate-day dosing absorbs ~34% more than daily (hepcidin effect). IV iron (ferric carboxymaltose 1000 mg) achieves repletion in 4–6 weeks and is the scale reference. Ferritin can fall without supplementation in endurance athletes, vegetarians, and high-tea/coffee consumers.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral ferrous sulfate, daily | 60 mg elemental Fe/d | Ferritin +10–25 µg/L per 8 wk in depleted women; Hgb +1.0–1.4 g/dL over 8 wk | 4–12 wk for Hgb; 3–6 mo for ferritin repletion | [RCT, Meta] | Stoffel 2017 *Lancet Haematol*; pooled RCT meta (Cançado 2024 *Am J Med*) | GI side effects (nausea, constipation) in ~25% at 60 mg elemental; dose-response flattens above 40–60 mg/d on consecutive days due to hepcidin |
| Oral ferrous sulfate, alternate-day | 60 mg elemental Fe every other day | Fractional absorption ~21.8% vs 16.3% daily (34% relative increase); similar absolute ferritin change at 4 wk (no stat diff) | 8–16 wk | [RCT] | Stoffel 2017 *Lancet Haematol* (PMID 29032957) | Alternate-day works by allowing hepcidin to fall overnight between doses; cumulative dose lower but absorption per dose higher — better GI tolerance |
| Oral ferrous bisglycinate | 25–30 mg elemental Fe/d | Similar ferritin rise to ferrous sulfate at half the elemental dose; fewer GI side effects | 8–12 wk | [RCT, Meta] | Meta — Milman 2012 *Eur J Nutr*; Frykman 1994 comparison RCT | Bisglycinate chelate bypasses hepcidin inhibition more than inorganic salts; preferred for GI-sensitive patients |
| Oral ferric forms (ferric maltol, ferric citrate) | 30 mg elemental Fe/d (ferric maltol typical) | Hgb +1.0 g/dL over 12 wk; ferritin response similar to ferrous at equivalent elemental dose | 12–16 wk | [RCT] | Elli 2021 *Gut* (ferric maltol in IBD); AEGIS trials | Less GI intolerance than ferrous sulfate; newer formulations |
| IV iron — ferric carboxymaltose (FCM) | 1000 mg single infusion | Ferritin: baseline ~13 µg/L → ~112 µg/L at 6 wk; mean increase ~150 µg/L vs baseline; vs oral iron the advantage was +163 µg/L (95% CI 153–173) | Peak 4–6 wk, then declines as iron is incorporated | [RCT, Meta] | PREFER trial; meta (Anker 2020 *JACC*); clinical review (NCBIbooks NBK614950) | Ferritin transiently very high (>500 µg/L) at 1–2 wk post-infusion — not iron overload, it's acute-phase ferritin from the infusion; TSAT is more reliable immediately post-infusion |
| IV iron — iron sucrose | 200 mg × 3–5 doses | Ferritin +80–150 µg/L over 4–6 wk | 4–6 wk | [RCT] | Multiple nephrology RCTs; meta vs FCM (PMC12099480) | More infusions required for equivalent iron dose; comparable efficacy to FCM per dose-corrected analyses |
| Dietary heme iron (red meat, 3 oz/d) | ~2–3 mg heme Fe/d | Ferritin +5–15 µg/L over 3 mo in mildly depleted adults | 8–12 wk | [RCT, Cohort] | Hallberg 1991 *Am J Clin Nutr*; NHANES longitudinal data | Heme iron absorption is 15–35% and largely hepcidin-insensitive vs non-heme 2–20% |
| Non-heme iron with vitamin C co-administration | +75–100 mg vitamin C per iron dose | Absorption increase ~2–3× in isolated meal studies; but in real diets (multiple meal contexts) the increment was only +30–50% | Acute; meal-by-meal effect | [RCT] | Cook & Reddy 2001 *Am J Clin Nutr* (PMID 11157344) | The dogma of "double absorption" was derived from isolated test meals with phytate-free conditions. In real mixed diets with phytate and other inhibitors, the vitamin C benefit is meaningful but not multiplicative. |
| Tea or coffee with iron meal | 1 cup co-ingested | Non-heme iron absorption ↓ 50–80% (polyphenols/tannins) | Acute | [RCT] | Hallberg & Rossander 1982; Disler 1975 | Effect is on non-heme only; heme iron barely affected. Even 1 hour post-meal coffee reduces absorption ~40%. |
| Calcium co-ingestion with iron | 300–600 mg Ca with iron | Non-heme iron absorption ↓ 30–60%; heme iron also ↓ modestly (~25%) | Acute | [RCT] | Hallberg 1992 *Am J Clin Nutr* (PMID 1519451); Cook 1994 | The competition is for shared transporter DMT1 at enterocytes. Clinically, separate calcium and iron supplements by ≥2 hours. |
| High-phytate meal (whole grain bread, legumes) | Phytate:iron molar ratio >10 | Non-heme iron absorption ↓ 50–90% depending on ratio | Acute | [RCT] | Hallberg 1989; Gibson 2018 *AJCN* | Relevant for vegetarian SA diet: dal + roti without animal protein or vitamin C dramatically limits iron uptake |
| Endurance exercise (intense training) | >10 h/wk sustained | Ferritin ↓10–30 µg/L over 12 wk training block in initially replete athletes | 8–12 wk | [Cohort, RCT] | Burden 2015; McClung 2013 *Am J Clin Nutr* | Mechanisms: foot-strike hemolysis, sweat iron losses (~0.3 mg/sweat-L), post-exercise hepcidin elevation suppressing absorption for 3–6 h |
| Alcohol (chronic, >2 drinks/d) | — | Ferritin ↑ (spurious elevation) via hepatic ferritin release and dysmetabolic iron overload | Sustained | [Cohort] | Whitfield 2001 *Alcohol Clin Exp Res*; NHANES analysis | Ferritin in alcohol use disorder can be 2–5× elevated without true iron overload — always pair with TSAT |

**Synthesis:**

- **Highest-leverage interventions:** IV iron (FCM) is the reference; 1000 mg raises ferritin to repletion in 4–6 weeks, bypassing all absorption barriers. For oral repletion from frank deficiency (ferritin <15), expect 3–5 months with alternate-day dosing at 60 mg ferrous sulfate to reach ferritin 50–100.
- **Alternate-day dosing** (Stoffel 2017) is underutilized. The 34% relative absorption advantage is mechanistically robust (hepcidin suppression between doses) and the clinical data support it. For patients with GI side effects, every-other-day dosing at 60 mg elemental iron is strongly preferred over twice-daily.
- **Bisglycinate vs sulfate:** Bisglycinate achieves similar ferritin response at half the elemental iron dose with substantially fewer GI side effects. Premium is worthwhile for anyone with GI sensitivity. Absorption advantage is not as dramatic as often marketed — the key benefit is tolerability, enabling adherence.
- **Vitamin C:** Meaningful in high-phytate contexts (vegetarian SA diet), modest in typical Western mixed-diet contexts. The Cook 2001 real-diet data showed a much smaller benefit than isolated meal experiments. Still worth co-ingesting with iron-rich meals, but it is not a multiplier of ×2 in real-world practice.
- **Oversold:** "Ferric" forms marketed as superior — in systematic comparisons, elemental-iron-equivalent doses of ferric and ferrous forms achieve similar ferritin responses, though ferric has better GI profile.

**South Asian-specific:**
- Vegetarian SA diet combines high phytate (legumes, whole wheat), low heme iron, often low vitamin C with cooked meals, and low ascorbate-to-phytate ratio. This can reduce non-heme iron bioavailability to 2–5% vs 15–35% for heme iron. Practical strategy: vitamin C at every iron-rich meal, separate tea/coffee by ≥1 hour, consider soaking/fermenting legumes to hydrolyze phytate by 20–60%.
- TMPRSS6 (rs855791) — loss-of-function variants increase hepcidin, blunting oral iron response; found at higher allele frequency in SA populations than European. A poor oral iron responder should consider alternate-day dosing or IV iron earlier.

**23andMe-relevant SNPs:**
- HFE rs1800562 (C282Y) and rs1799945 (H63D): C282Y/C282Y homozygotes absorb excess iron; heterozygotes are generally unaffected in terms of clinical overload but can have higher-normal ferritin. Important: do not supplement iron without confirming you are not a C282Y compound heterozygote.
- TMPRSS6 rs855791: T allele associated with higher hepcidin → reduced oral iron absorption → harder to replete with daily oral iron → consider alternate-day or IV strategy.

**Realistic 3–6 month trajectory from frank deficiency (ferritin <15):**
- Oral ferrous sulfate 60 mg alternate-day: ferritin 15 → ~60–80 µg/L at 16–20 weeks (rough estimate; high individual variability)
- Oral ferrous bisglycinate 25 mg daily: similar trajectory, better GI tolerance
- IV FCM 1000 mg: ferritin 15 → ~100–150 µg/L by week 6

---

## Serum Iron

**Quick read:** Serum iron is highly variable (30–50% within-person day-to-day variation, diurnal variation peaks late morning). It is most useful as the numerator for TSAT calculation, not as a standalone marker. Interventions that move ferritin move serum iron in parallel, but the relationship is loose. Always interpret serum iron in the context of TSAT and ferritin.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral iron supplement (ferrous sulfate) | 60 mg elemental Fe | Serum Fe transiently ↑ 50–100 µg/dL for 4–6 h post-dose; fasting TSAT rises 5–15% over 4–8 wk in deficient individuals | Hours (acute); weeks (sustained) | [RCT] | Hallberg 1958 absorption studies; diurnal data (Kim 2017 PMID 28947322) | Supplement taken within 24 h of draw falsely elevates serum iron by 30–80 µg/dL — always hold oral iron ≥24 h before iron studies draw |
| IV iron (any formulation) | Standard dose | Serum Fe ↑ markedly for 24–72 h post-infusion; returns toward baseline by 2 wk as iron is stored | 1–72 h | [Mechanism, RCT] | FCM pharmacokinetics | TSAT can transiently reach 60–80% immediately post-IV iron — not iron overload |
| Dietary meat increase | 3 oz red meat/d | Small sustained ↑ in fasting serum iron (~10–20 µg/dL over weeks) | 4–8 wk | [Cohort] | NHANES observational | Highly variable; dominated by TSAT changes |
| Inflammation / acute illness | Any systemic infection/inflammatory state | Serum Fe ↓ 20–60 µg/dL (hepcidin-driven macrophage iron trapping) | Hours to days | [Mechanism, Cohort] | Nemeth 2004 *Science* (hepcidin-ferroportin axis) | Iron "disappears" into macrophages; ferritin simultaneously rises — together this mimics iron deficiency when it isn't |

**Synthesis:** Serum iron does not have a clinically useful optimization target independent of TSAT. Its main role is TSAT computation. Key practical point: standardize timing of draws (fasting morning, supplements held ≥24 h) and always assess alongside ferritin and TSAT. Standalone serum iron values should not drive supplementation decisions.

---

## TSAT (Transferrin Saturation)

**Quick read:** TSAT responds to the same interventions as serum iron (same numerator, stable denominator) but is a better single-snapshot iron status indicator. The big levers are treating iron deficiency (raises TSAT from <20% toward 25–40%) or addressing iron overload via phlebotomy (lowers TSAT from >45%).

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral iron repletion (ferrous sulfate 60 mg/d) | 60 mg elemental Fe/d from TSAT <16% | TSAT ↑ from ~10–15% to ~25–35% over 8–12 wk | 6–10 wk | [RCT] | Cançado 2024 pooled RCT analysis | Responds faster than ferritin in first 4–6 wk; ferritin catches up after |
| IV ferric carboxymaltose 1000 mg | Single infusion | TSAT ↑ transiently to 60–80% at 24–48 h; settles to 30–45% by 4–6 wk | 24 h–6 wk | [RCT] | NCBIbooks NBK614950 | Transient very-high TSAT is expected and benign; schedule re-check at 4–8 wk, not 48 h |
| Therapeutic phlebotomy (hemochromatosis) | 450–500 mL / session, weekly | TSAT ↓ ~3–5% per session; ferritin ↓ ~30–50 µg/L per session | Per session | [Cohort, GL] | EASL 2022 hemochromatosis guidelines | Target TSAT <45% and ferritin 50–100; weekly phlebotomy for overloaded patients |
| Inflammation / infection | — | TSAT ↓ 5–20 percentage points acutely | Hours to days | [Mechanism] | Hepcidin axis — Nemeth 2004 | TSAT <20% in active inflammation does NOT necessarily mean iron deficiency; pair with ferritin (elevated in ACD vs low in IDA) |
| Tea/coffee with iron | 1 cup co-ingested | TSAT response to iron dose blunted (absorption blocked); no acute effect on TSAT | — | [RCT] | Absorption studies | Affects absorption, not steady-state TSAT directly |

**Synthesis:** TSAT is most clinically actionable in two scenarios: (1) diagnosing iron deficiency vs. anemia of chronic disease (pattern interpretation — see `nutrients_vitamins_minerals.md` Table), and (2) hemochromatosis screening (TSAT >45% fasting on repeat draw + ferritin >300 → HFE genotyping). Optimal TSAT for a healthy young man: 25–40%.

---

## TIBC (Total Iron-Binding Capacity)

**Quick read:** TIBC is a liver-synthesized protein (transferrin) and reflects the body's iron "demand signal." It is high when iron is scarce (deficiency) and low in inflammation, malnutrition, and overload. Interventions move it indirectly through iron status.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Iron repletion from deficiency | Oral or IV iron, standard doses | TIBC ↓ from ~400–450 µg/dL to ~300–350 µg/dL as iron stores replenish | 4–12 wk | [RCT] | Cançado 2024; multiple repletion trials | TIBC is a negative signal: as ferritin rises, TIBC should fall — useful verification of adequate repletion |
| Protein malnutrition (correction) | Protein supplementation in hypoalbuminemia | TIBC ↑ as liver resumes transferrin synthesis | 2–4 wk | [Cohort] | Nutritional rehabilitation data | Low TIBC with low albumin = low transferrin synthesis, not iron overload |
| Oral contraceptive pills / estrogen | OCP use | TIBC ↑ 25–30% via estrogen-driven hepatic transferrin synthesis | Weeks | [Cohort] | Multiple OCP studies | Higher TIBC can mask iron deficiency — TSAT falls even if iron status unchanged |
| Chronic inflammation treatment | Treating underlying inflammatory disease | TIBC ↑ as negative APR resolves | Variable | [Mechanism, Cohort] | — | TIBC normalizing + ferritin falling = resolving ACD pattern |

**Synthesis:** TIBC is rarely the direct target of optimization; it is a confirmatory pattern marker. The key diagnostic use is in distinguishing IDA (high TIBC) from ACD (low/normal TIBC) and overload (low TIBC). For healthy young men, TIBC 300–400 µg/dL in the context of normal ferritin and TSAT requires no action.

---

## Vitamin D (25-OH)

**Quick read:** 25-OH vitamin D responds predictably to supplementation but with marked individual variation (2–3× spread around mean responses). The rule-of-thumb is approximately +1 ng/mL per 100 IU/d at baseline deficiency, but this is non-linear and baseline-dependent — the increment is larger when starting very low. D3 is substantially superior to D2. Body fat reduces response. SA populations near-universally require supplementation regardless of sun exposure due to pigmentation, dress, and dietary factors.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Vitamin D3 (cholecalciferol) oral | 1000 IU/d | 25-OH ↑ ~8–11 ng/mL at steady state from baseline ~15 ng/mL | 8–12 wk | [Meta] | Heaney 2003 *Am J Clin Nutr*; Gallagher 2014 JCEM | Response is curvilinear: at baseline 10 ng/mL, +1000 IU/d → ~+11 ng/mL; at baseline 30 ng/mL → ~+8 ng/mL; response diminishes at higher baseline |
| Vitamin D3 oral | 2000 IU/d | 25-OH ↑ ~15–20 ng/mL at steady state | 10–14 wk | [RCT, Meta] | European meta (MDPI Nutrients 2023): +36 nmol/L = ~14.4 ng/mL overall across 49 trials | Obese individuals typically achieve 60–70% of lean-person response at the same dose |
| Vitamin D3 oral | 4000 IU/d | 25-OH ↑ ~25–35 ng/mL | 12–16 wk | [RCT] | Garland/Heaney dose-response; VITAL supplementation pharmacology | UL for most adults is 4000 IU/d (IOM), though the Endocrine Society uses 10,000 IU/d as upper tolerable for short-term therapeutic use |
| Loading dose — Endocrine Society protocol | 50,000 IU D2 or D3 weekly × 8 wk (or equivalent 6000 IU/d) | 25-OH ↑ ~30–40 ng/mL from deficient baseline; final mean ~47 ng/mL (one representative trial) | 8 wk | [GL, RCT] | Endocrine Society guideline *JCEM* 2011; PMC2683376 repletion trial | Achieves repletion faster; typically followed by maintenance 1500–2000 IU/d. The Endocrine Society 2024 update no longer endorses a specific 30 ng/mL target, but the loading dose protocol remains standard clinical practice. |
| Vitamin D2 (ergocalciferol) oral | Same IU dose as D3 | 25-OH ↑ approximately 25–30% less than D3 at equivalent IU | Same | [Meta] | Tripkovic 2012 *Am J Clin Nutr* meta (PMID 22552031): D3 was 87% more potent at raising 25-OH than D2 in one meta-analysis; the numerical advantage is ~1.5–2× for D3 | D2 is still effective; the gap is real but not disqualifying. Most prescription vitamin D in the US is D2 (50,000 IU ergocalciferol) |
| Sun exposure — midday, low UV | UV index 2–3 (winter, northern latitudes), full-arm exposure, 20–30 min | Synthesis negligible to zero | N/A | [Mechanism, Cohort] | Webb & Engelsen 2006; Holick rule | UV index <3 produces essentially no cutaneous vitamin D synthesis at any skin type |
| Sun exposure — midday, high UV | UV index 6–8 (summer, 40°N, noon), face + arms, skin type II (fair), 15–20 min | ~1000 IU vitamin D3/equivalent synthesized (~10 µg); 25-OH ↑ ~5–10 ng/mL over weeks of consistent exposure | 4–8 wk sustained | [RCT, Mechanism] | Holick 2007 reference; Miyauchi 2016 *Photochem Photobiol*; estimated from 1/4 MED = ~1000 IU rule | SA skin type (V–VI) requires ~3–5× more exposure time to synthesize equivalent D3 as skin type II. Covered dress, sunscreen (SPF 15 reduces synthesis ~93%), and indoor work nearly eliminate this route for SA individuals even in sunny climates. |
| Sun exposure — SA skin type (V), midday summer | UV index 6–8, face + arms, 45–60 min | ~800–1000 IU equivalent if exposure is adequate and uncovered | 4–8 wk | [Cohort, Mechanism] | Lowe & Bhojani 2017 *Ther Adv Musculoskelet Dis*; Bouillon 2019 review | In practice, traditional SA dress (shalwar kameez covering arms/legs) and predominantly indoor lifestyle mean this exposure is rarely achieved; supplementation is the reliable route |
| Body fat / obesity effect | BMI >30 vs normal | 25-OH response to the same supplement dose is ~40–60% lower in obese individuals | Same | [Meta] | Blum 2012 *Am J Clin Nutr*; multiple pharmacokinetic analyses | Mechanism: volumetric dilution in adipose; also possibly reduced 25-hydroxylation efficiency. Obese individuals need 2–3× higher maintenance dose for same 25-OH target |
| Magnesium co-supplementation | 250–400 mg Mg/d with vitamin D | May improve D3 → 25-OH conversion (CYP2R1 is Mg-dependent); some evidence that Mg deficiency blunts vitamin D response | Simultaneous | [RCT — modest quality] | Deng 2018 *Am J Clin Nutr* (PMID 29794773); Uwitonze 2018 review | Effect size not well-quantified; relevance is mainly if Mg is concurrently deficient (common in SA diets low in leafy greens/nuts) |
| Vitamin K2 (MK-7) co-administration | 100–200 µg/d MK-7 | Does not significantly affect 25-OH levels; theoretical role in directing calcium away from arteries toward bone | — | [Mechanism, RCT limited] | Rheaume-Bleue 2012; PMC4566462 review | K2 evidence for CVD/calcification is mechanistically plausible but RCT evidence for hard outcomes is limited; does not change the 25-OH dose-response |
| Worsener: dark pigmentation (endogenous) | — | Lower cutaneous D3 synthesis per UV dose; requires 3–5× more sun exposure for same synthesis | Ongoing | [Cohort] | Webb 2006; SA-specific data (Bouillon 2019) | This is the dominant driver of SA vitamin D deficiency |

**Synthesis:**

- **Highest-leverage intervention:** Oral vitamin D3, 2000–4000 IU/d for maintenance; 50,000 IU/wk × 8 wk for acute repletion from deficiency.
- **D3 vs D2:** D3 is meaningfully superior (~1.7–2× more potent per IU) for raising 25-OH. The Tripkovic 2012 meta is the definitive study here. When given the option between the two, always choose D3 (cholecalciferol).
- **Oversold:** Sun exposure as a practical source for SA individuals. The physics don't work: pigmentation, covered dress, latitude >35°N for >6 months/year, and indoor lifestyle combine to make cutaneous synthesis negligible. Supplementation is not a lifestyle recommendation; it is a physiological necessity for most SA individuals.
- **VITAL caveat:** VITAL (Manson 2019 *NEJM*, n=25,871) found that 2000 IU/d vitamin D3 did not reduce cancer incidence or CV events in a primary-prevention general population. Subgroup with low baseline D (<20 ng/mL) showed directionally favorable but non-significant signals. The lack of hard CV endpoint benefit does NOT mean supplementation is pointless — the target is sufficiency (>30 ng/mL), not pharmacological supraphysiological levels.
- **Kidney stones concern (VITAL data):** 2000 IU/d D3 in VITAL did not increase kidney stone risk. The stones concern came from calcium + vitamin D combined (WHI showed small increased risk with combined supplementation, not D alone). For D3 alone at ≤4000 IU/d without excessive calcium co-supplementation, the risk is not elevated.
- **D3 + K2 combination:** Mechanistically sensible (K2 activates matrix Gla protein to prevent soft-tissue calcification, and activates osteocalcin for bone Ca binding), but RCT evidence for hard outcomes (fracture, calcification) is limited. Does not change 25-OH response to D3.

**South Asian-specific:**
- UK Biobank analysis (n=6,433 SA adults): 72% had 25-OH <25 nmol/L (10 ng/mL) in winter; prevalence of deficiency <30 nmol/L was >80%. **[Cohort — PMC7844605]**
- SA individuals need approximately double the oral dose of D3 vs European descent individuals to achieve the same 25-OH target, based on pharmacokinetic modeling and cohort data, partly from higher body mass in older adults and partly from possible differences in GC (vitamin D binding protein) variants.
- GC gene SNPs (rs4588, rs7041, rs2282679) affect vitamin D binding protein and circulating 25-OH: the T allele of rs4588 associated with higher binding affinity → lower bioavailable 25-OH at same total 25-OH. Wang 2010 *NEJM* GWAS found GC variants explain a major portion of 25-OH variance.

**23andMe-relevant SNPs:**
- GC rs4588 and rs7041 — vitamin D-binding protein variants; T allele carriers have lower bioavailable vitamin D at a given 25-OH level — may need to target higher circulating 25-OH.
- CYP2R1 rs10741657 — hepatic vitamin D 25-hydroxylase; minor allele associated with lower 25-OH for a given D3 intake; more supplementation needed for target.
- VDR rs2228570, rs1544410 (BsmI), rs731236 (TaqI) — vitamin D receptor variants affecting downstream gene expression. Tissue-level D activity can differ even at same circulating 25-OH.

**Realistic 3-month trajectory:**
- Starting 25-OH ~12 ng/mL (deficient SA individual), 2000 IU D3/d: reaches ~25–30 ng/mL by 12 wk. Loading dose (50,000 IU/wk × 8 wk) followed by 2000 IU/d: likely achieves >40 ng/mL.

---

## Vitamin B12 (Serum Cobalamin)

**Quick read:** Oral high-dose B12 (≥500–1000 µg/d cyanocobalamin) is equivalent to intramuscular injection for normalizing serum B12 and MMA in most people — mass-action absorption bypasses intrinsic factor at high doses. Response is fast for serum B12 (weeks) but MMA normalization is the true functional endpoint. Cyanocobalamin and methylcobalamin are clinically equivalent for healthy individuals; renal disease is the exception. SA vegetarians have very high prevalence of B12 deficiency and require proactive supplementation.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral cyanocobalamin | 1000 µg/d | Serum B12 ↑ from deficient (<200 pg/mL) to >400 pg/mL within 4 wk; MMA ↓ by 33% at this dose (see MMA section) | 2–4 wk serum B12; 4–8 wk MMA | [RCT] | Kuzminski 1998 *Blood* (n=33, oral vs IM equivalent); dose-finding trial (PMID 15911731) | Mass-action absorption: ~1–2% of any oral B12 dose is absorbed by passive diffusion independent of IF. At 1000 µg/d, ~10–20 µg absorbed daily — adequate for repletion |
| Oral cyanocobalamin | 500 µg/d | MMA ↓ ~33% from deficient baseline; serum B12 normalizes | 8–16 wk | [RCT] | PMID 15911731 dose-finding trial (2.5, 100, 250, 500, 1000 µg doses in 120 older people) | The 33% MMA reduction was seen at ≥500 µg/d; lower doses (100–250 µg) achieved only 16–23% MMA reduction |
| Oral cyanocobalamin | 100 µg/d | MMA ↓ ~23%; serum B12 may not fully normalize from frank deficiency | 12–16 wk | [RCT] | PMID 15911731 | Standard "multivitamin" B12 doses (6–25 µg) are insufficient for repletion from deficiency; may maintain adequacy if stores are replete |
| IM cyanocobalamin (conventional) | 1000 µg IM | Serum B12 ↑ within hours to days; MMA normalizes within days to weeks | Days (serum); 1–2 wk (MMA) | [RCT, GL] | Kuzminski 1998; AAFP oral vs IM review 2022 | IM is still preferred for pernicious anemia (IF deficiency — passive absorption insufficient); neurological deficiency benefits from faster IM normalization |
| IM hydroxocobalamin | 1000 µg IM | Superior serum B12 retention vs cyanocobalamin (longer-acting depot); equivalent MMA normalization | Days | [RCT] | BMJ 1979 historical RCT; UK/EU preferred form for pernicious anemia | |
| Methylcobalamin oral | 1000–2000 µg/d | Serum B12 and MMA response equivalent to cyanocobalamin in healthy individuals | Same | [RCT, Systematic review] | PMC12681447 comprehensive review 2025; PMC11128391 network meta-analysis | No advantage of methyl vs cyano form in terms of B12 status markers in people without metabolic disorders. The methylcobalamin marketing ("more bioavailable/active") is not supported in healthy adults; both are dephosphorylated and re-synthesized intracellularly. |
| Dietary: animal products (meat, dairy, eggs) | 2.4–3 µg/d (RDA) from mixed animal diet | Serum B12 maintenance at adequate level (>200 pg/mL); MMA <0.20 µmol/L | Ongoing maintenance | [Cohort] | NHANES data; European EPIC-Oxford cohort | Strict vegetarians/vegans accumulating B12 deficiency over years; stores last 2–5 years before MMA rises |
| Dietary: eggs | 2 large eggs/d | ~1.5 µg B12 from yolk; one study found egg B12 absorbed less efficiently than meat B12 | — | [RCT] | Donaldson 2000; small absorption studies | Eggs are a poor B12 source for vegetarians due to lower bioavailability |
| PPI (proton pump inhibitor), chronic use | ≥30 mg/d for >6 months | OR 1.42 (95% CI 1.16–1.73) for B12 deficiency; serum B12 ↓ ~25 pmol/L in cohort data; 21% vs 15% prevalence of deficiency in high-dose users | Years of use | [Meta, Cohort] | Systematic review (PMID 37060552, 25 studies, n=30,922); cohort PMC9577826 | PPI suppresses gastric acid needed to cleave B12 from food protein; does NOT affect supplement B12 absorption (already free). Solution: take B12 supplement as free cyanocobalamin tablet, not food-source B12. |
| Metformin chronic use | Standard therapeutic doses | B12 ↓; OR for deficiency ~1.5–2.0 in diabetic populations; serum B12 ↓ ~50–90 pmol/L | Years of use | [Meta, Cohort] | Multiple metformin-B12 meta-analyses; mechanism: metformin blocks ileal IF-B12 complex uptake via calcium-dependent mechanism | High-dose oral B12 (1000 µg/d) partially overcomes metformin-induced deficiency via passive absorption |
| Worsener: nitrous oxide anesthesia | Single surgical exposure | Oxidizes cobalt in methylcobalamin → functional B12 inactivation acutely; MMA and Hcy can spike; neurological injury reported in deficient patients | Hours | [Case series, Mechanism] | Hadzic 1995 *Anesthesiology*; Doran 2004 | Not relevant for routine supplementation; relevant clinical note for anyone with low-normal B12 undergoing general anesthesia |

**Synthesis:**

- **Highest-leverage:** Any oral B12 ≥500 µg/d — this dose reliably repletes even severe deficiency through passive diffusion. The InjectionReflexive default ("B12 must be injected") is outdated for most cases. Exception: pernicious anemia (absent intrinsic factor) where passive absorption at 1–2% is the only route and IM remains preferred by many gastroenterologists.
- **Cyanocobalamin vs methylcobalamin in healthy individuals:** Equivalent. The methylcobalamin premium is not supported by clinical outcome data in adults without metabolic disorders. Both reach tissue as the same active cofactor forms (methylcobalamin for methionine synthase, adenosylcobalamin for MMA mutase).
- **Multivitamin doses:** 6–50 µg B12 in most multivitamins is maintenance-dose only. Will not replete deficiency. Anyone with deficiency needs stand-alone high-dose supplementation.
- **PPI users:** Switch B12 source from food to oral supplement — food-bound B12 absorption is acid-dependent, supplement absorption is not.

**South Asian-specific:**
- B12 deficiency in vegetarian Indians estimated at 47–70% in several cohort studies (Antony 2003; Grover 2011; Pasricha 2012). Even non-vegetarian SA: ~20–30% deficiency in Indian urban cohorts, attributed to low total meat consumption and processing effects (Yajnik 2014).
- Practical threshold: any SA male eating predominantly vegetarian diet should supplement B12 regardless of serum B12 — serum B12 misses functional deficiency (check MMA) and B12 has no known toxicity at supplemental doses.

**23andMe-relevant SNPs:**
- FUT2 rs601338 (secretor status): non-secretors (AA genotype, ~20% of population) produce less intrinsic factor and have lower baseline serum B12 independent of diet. Non-secretors absorb food B12 less efficiently — more reliant on supplements.
- MTRR rs1801394 (methionine synthase reductase): affects B12 recycling in the methionine cycle; TT homozygotes may need higher functional B12 to maintain methylation capacity.
- MTR rs1805087 (methionine synthase): affects B12 utilization directly.

---

## MMA (Methylmalonic Acid — Functional B12)

**Quick read:** MMA is the most sensitive and specific functional marker of B12 adequacy. It normalizes within 1–2 weeks of parenteral B12 and within 4–8 weeks of high-dose oral B12 (≥500 µg/d). Renal function must be checked simultaneously — eGFR <60 independently raises MMA regardless of B12 status. Serum B12 in the "normal" range does not exclude functional B12 deficiency measurable by MMA.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| IM/IV B12 (cyano or hydroxo) | 1000 µg IM | MMA normalization (<0.40 µmol/L) within days; 50–70% reduction in plasma MMA within 1 wk | Days | [RCT, Mechanism] | Kuzminski 1998 *Blood*; AAFP 2022 review | Gold standard speed; useful diagnostically — if MMA fails to normalize with adequate B12 repletion, consider renal disease or methylmalonic acidemia |
| Oral cyanocobalamin | 1000 µg/d | MMA ↓ 33% from baseline (dose-finding trial); full normalization in most non-PA patients within 4–8 wk | 4–8 wk | [RCT] | PMID 15911731 (16-wk dose-finding, n=120) | MMA normalization with oral is somewhat slower than IM but achieves same endpoint |
| Oral cyanocobalamin | 100–250 µg/d | MMA ↓ 16–23% from baseline; often incomplete normalization from frank deficiency | 8–16 wk | [RCT] | PMID 15911731 | These doses are maintenance doses if baseline is replete, not adequate for repletion |
| High-dose oral cyanocobalamin (2000 µg/d) | 2000 µg/d | Network meta-analysis: clinically equivalent to IM for MMA normalization and serum B12 at >3 months | 8–16 wk | [Meta] | PMC11128391 network meta-analysis | At this dose, passive absorption (~20–40 µg/d absorbed) is adequate even in pernicious anemia |
| Renal function improvement | Treatment of underlying CKD or acute AKI | MMA ↓ proportionally as GFR improves; MMA-GFR relationship is linear | Variable | [Cohort] | Lifelines-MINUTHE 2020 (PMC7726887) | Always rule out renal disease before attributing elevated MMA to B12 deficiency. eGFR <45: MMA interpretation very uncertain. eGFR <60: partial MMA elevation expected. |

**Synthesis:** MMA is the functional target, not serum B12. The intervention is the same (high-dose oral or parenteral B12), but MMA normalization is the confirmatory endpoint. Response is faster with IM (days vs weeks for oral). Important: always check creatinine/eGFR before concluding that elevated MMA = B12 deficiency.

---

## Folate (Serum and RBC)

**Quick read:** Serum folate responds rapidly to folic acid supplementation (weeks); RBC folate is a longer-term pool (takes 36+ weeks to fully equilibrate). The MTHFR C677T TT genotype blunts serum folate accumulation by ~16% and may warrant L-methylfolate supplementation, though the clinical effect is modest in folate-replete individuals. Folic acid supplementation lowers homocysteine regardless of MTHFR status. High-dose folate without adequate B12 can mask megaloblastic anemia while allowing neurological damage — the "masking" concern.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Folic acid supplement | 400 µg/d (RDA for adults) | Serum folate ↑ ~11.6% per 100 µg/d added (linear at low doses); serum reaches ~20–25 nmol/L from typical Western baseline ~10–15 nmol/L | 2–4 wk | [Meta] | Bayesian dose-response meta (MDPI Nutrients 2019) | Serum folate responds rapidly and is sensitive to recent intake; RBC folate (4–6× lower response per dose) is the better long-term tissue marker |
| Folic acid supplement | 400 µg/d | RBC folate ↑ ~23% per doubling of folate intake; steady-state takes median 36 wk (95% CI 27–52 wk) | 36 wk for steady state | [Meta] | MDPI Nutrients 2019 systematic review | RBC folate is a 3-month rolling average; not a useful acute-change marker |
| Folic acid supplement | 800–1000 µg/d | Serum folate approximately doubles from typical Western baseline; sufficient to normalize folate-deficient homocysteine in most individuals | 4–8 wk | [Meta, RCT] | Homocysteine Lowering Trialists' Collaboration (PMID 9569395, n=1114) | At 400–5000 µg/d, the homocysteine-lowering effect of folic acid reaches a plateau — no additional Hcy lowering above ~800 µg/d for most people |
| L-methylfolate (5-MTHF) vs folic acid — MTHFR TT | 400 µg/d L-methylfolate | Slightly better serum homocysteine reduction in TT homozygotes vs folic acid (interaction p significant); but population-level difference in folate status is modest (~16% lower serum folate in TT vs CC) | 8–12 wk | [RCT] | Anderson 2013 (PMID 23456769) *Mol Nutr Food Res*; recent Greek RCT (PMID 38056998) | The MTHFR "crisis" is oversold in functional medicine. TT homozygotes have mildly lower folate and mildly higher Hcy, but both respond to folic acid. The use of L-methylfolate in MTHFR TT is reasonable but its advantage over standard folic acid is modest in healthy replete individuals. |
| Dietary folate from fortified foods | US folic acid fortification (since 1998) | Population NTD reduction ~28%; mean serum folate doubled in US women post-fortification | Ongoing | [Cohort] | CDC MMWR 1999; Honein 2001 *JAMA* | US diet is generally folate-sufficient with fortification; supplementation above RDA is relevant mainly for pregnancy (800 µg/d NTD prevention), MTHFR TT, or dietary restriction |
| Worsener: high-dose folate without B12 | ≥1000 µg/d folic acid in B12-deficient state | Can normalize megaloblastic anemia while B12 deficiency continues to damage the nervous system ("masking") | — | [Mechanism, Case reports] | Lindenbaum 1988 *NEJM* (PMID 3374550) | This is the main safety concern with high-dose folate. In practice, supplementing B12 alongside folate eliminates the risk. |
| Methotrexate (folate antagonist) | Therapeutic doses | Serum and RBC folate ↓ significantly; Hcy rises; NTD risk in pregnancy | Weeks | [Mechanism, RCT] | Standard pharmacology | Leucovorin (folinic acid) is rescue; not relevant for dietary folate supplementation context |

**Synthesis:**

- **MTHFR C677T clinical reality:** TT homozygotes (~10–15% European descent, lower in SA) have ~70% reduced MTHFR activity, modestly lower folate (~16%), and mildly higher Hcy (+2–3 µmol/L average). Both folic acid and L-methylfolate raise folate status and lower Hcy in TT homozygotes. L-methylfolate is reasonable but the "you must take methylfolate" framing overstates the evidence.
- **No benefit of B-vitamin supplementation for CV mortality in already-replete populations:** Clarke 2010 meta-analysis (8 RCTs, n=37,485 high-risk adults) showed that folic acid ± B12, despite lowering Hcy by 25%, produced no significant reduction in cardiovascular events or total mortality **[Meta — PMID 20937919]**. The homocysteine-causal-CVD hypothesis failed RCT confirmation.
- **Oversold:** High-dose methylfolate for MTHFR TT as a health intervention — the clinical data for hard outcomes do not support this beyond ensuring adequate folate status (which standard folic acid achieves).

---

## Homocysteine

**Quick read:** Homocysteine is highly modifiable by B vitamins — folic acid alone lowers it ~25%, folic acid + B12 by ~33%. However, RCT evidence shows that lowering Hcy with B vitamins does not reduce CV events in already-replete or high-risk populations. Hcy is best treated as a downstream marker of methylation B-vitamin status, not a direct CV target. The biggest lever is ensuring folate and B12 adequacy.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Folic acid | 0.5–5 mg/d | Hcy ↓ ~25% (3 µmol/L from baseline ~12 µmol/L in Western populations) | 4–8 wk | [Meta] | Homocysteine Lowering Trialists' Collaboration (PMID 9569395, n=1114, 12 RCTs) | Effect is near-plateau at 0.5 mg/d; higher doses do not produce meaningfully larger Hcy reductions beyond ~25% |
| Folic acid + vitamin B12 | 0.5–5 mg FA + 0.5 mg B12 | Hcy ↓ ~33% (from baseline ~12 µmol/L: down to ~8–9 µmol/L) | 4–8 wk | [Meta] | Homocysteine Lowering Trialists' Collaboration (PMID 9569395) | B12 alone contributes ~7% additional reduction on top of folic acid (3–10% CI) |
| Vitamin B6 | 16.5 mg/d | No significant additional Hcy reduction beyond FA ± B12 | — | [Meta] | Same meta-analysis | B6 is relevant mainly for CBS enzyme in transsulfuration; does not affect remethylation pathway Hcy |
| Betaine (trimethylglycine) | 3–6 g/d | Hcy ↓ ~10–20% via BHMT enzyme remethylation; effect is additive to folate | 4–8 wk | [RCT] | Olthof 2003 *Am J Clin Nutr*; Schwab 2002 | Effect is partly independent of folate/B12 status; useful adjunct in MTHFR TT or high Hcy refractory to folate + B12 |
| Riboflavin (B2) | 1.6 mg/d (for MTHFR TT specifically) | Hcy ↓ additional 2.2 µmol/L in MTHFR 677TT homozygotes who are B2-deficient | 12 wk | [RCT] | McNulty 2006 *Circulation*; McNulty 2017 | Riboflavin is a cofactor for MTHFR; deficiency in TT individuals specifically amplifies Hcy elevation. Not relevant if B2 replete. |
| Protein reduction (low-methionine diet) | Low-methionine diet | Hcy ↓ proportionally (less methionine → less SAH → less Hcy) | Weeks | [Mechanism, small RCT] | Theoretical; used in homocystinuria management | Not a practical intervention for mild Hcy elevation in healthy individuals |
| Alcohol cessation | Heavy drinking → abstinence | Hcy ↓ 2–4 µmol/L after cessation; alcohol depletes folate and B6 | 2–4 wk | [Cohort] | Halsted 2003 review | Heavy alcohol is a major driver of elevated Hcy; standard B vitamins partially compensate but cessation is the lever |
| Worsener: methotrexate | Therapeutic doses | Hcy ↑ substantially (folate antagonist) | Weeks | [Mechanism] | — | Leucovorin rescue; relevant for patients on MTX |
| Worsener: renal insufficiency | eGFR <60 | Hcy ↑ 1–3 µmol/L per 10 mL/min decline in GFR; CKD5: Hcy >20 µmol/L common | Sustained | [Cohort] | Suliman 2002 *Kidney Int* | B vitamin supplementation partially lowers Hcy in CKD but does not normalize it |
| Worsener: hypothyroidism | Untreated | Hcy ↑ ~2–3 µmol/L | Sustained | [Cohort] | Diekman 2001 review | TSH check when Hcy unexpectedly elevated in young person with adequate B vitamins |
| Worsener: smoking | Active smoking vs non-smoker | Hcy ↑ ~1–2 µmol/L | Ongoing | [Cohort] | Nygård 1995 *NEJM* (Hordaland Homocysteine Study) | Minor effect compared to B-vitamin status |

**Synthesis:**

- **Highly modifiable:** Hcy is one of the most modifiable biomarkers in this panel. Folic acid 0.8 mg + B12 1000 µg/d achieves the maximum nutritional Hcy lowering (~33%) within 8 weeks.
- **The Hcy-CVD paradox:** B vitamins lower Hcy but do NOT lower CV events (Clarke 2010, HOPE-2, VITATOPS). Mendelian randomization shows a small causal effect on stroke specifically (Yuan 2021 BMC Med: OR ~1.11 per SD for any stroke) but not on coronary disease. Best interpretation: treat Hcy elevation as a signal of methylation/B-vitamin inadequacy, not as a direct CV risk target. Get Hcy <8, not because it will reduce MI, but because it confirms adequate B12 and folate status.
- **Oversold:** High-dose B vitamins for CV prevention in people with high Hcy. The intervention works as a methylation-status restoration, not as CV risk reduction.

---

## Magnesium (Serum)

**Quick read:** Serum magnesium is buffered tightly (~0.7–1.0 mmol/L) and is a poor indicator of total body or intracellular magnesium status — only ~1% of body Mg is in serum. RBC magnesium is more informative. Despite the insensitivity of serum Mg, supplementation does produce small but significant serum increases. High responder variation is the rule. Dietary magnesium is substantially lower in SA diets than in traditional Mediterranean or Japanese diets.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral Mg — any soluble form (glycinate, citrate, malate, threonate) | 300–400 mg elemental Mg/d | Serum Mg ↑ 0.12–0.15 mg/dL (0.05 mmol/L) over 8–12 wk | 8–12 wk | [Meta] | Meta of 16 RCTs in T2DM (PMC9065397): MD +0.15 mg/dL; meta of 34 trials (Cheung 2016): +0.05 mmol/L = +0.12 mg/dL | High I² (heterogeneity 99.9%) — individual response varies from undetectable to +0.30 mg/dL; serum Mg is an insensitive marker |
| Oral Mg oxide | 400–500 mg elemental Mg/d | Serum Mg: similar or slightly less response vs organic salts at equivalent elemental dose | 8–12 wk | [RCT] | Bioavailability comparison studies (Coudray 2005 *Magnes Res*) | Mg oxide has only ~4–5% bioavailability (vs 30–60% for citrate/glycinate); laxative effect common; serves mainly as bulk stool softener, not Mg repletion |
| Oral Mg citrate | 300 mg elemental/d | Better absorption than oxide; serum Mg response moderate | 8–12 wk | [RCT] | Coudray 2005 magnesium bioavailability study | Better than oxide; lower GI side effects than sulfate |
| Oral Mg glycinate / bisglycinate | 200–400 mg elemental/d | Good GI tolerance; reported to have superior absorption (30–40%) vs oxide; serum Mg rises modestly but RBC Mg may show larger response | 8–12 wk | [RCT — limited data] | Small head-to-head studies; manufacturer-sponsored data; clinical literature for anxiety, sleep shows functional benefit not always captured by serum Mg | Most popular "premium" Mg form; well-tolerated; limited strong RCT evidence vs citrate for serum Mg |
| Oral Mg threonate | 144 mg elemental/d (marketed dose) | Crosses blood-brain barrier in animal models; brain Mg increases; serum Mg: minimal measurable effect at this dose | 8–12 wk | [Animal, small RCT] | Slutsky 2010 *Neuron* (animal); human data limited | Marketed primarily for cognitive effects, not serum Mg optimization; very low elemental dose relative to other forms |
| Dietary Mg (nuts, leafy greens, legumes, whole grains) | 100 mg/d incremental increase | Serum Mg ↑ ~0.02–0.05 mg/dL over months | Ongoing | [Cohort] | NHANES dietary analysis; Guerrero-Romero 2016 *Eur J Clin Nutr* | Most impactful on long-term RBC Mg status; difficult to achieve therapeutic doses through diet alone if starting significantly depleted |
| Alcohol cessation | Chronic heavy drinking → abstinence | Serum and RBC Mg can rise ~15–20% with cessation; alcohol causes urinary Mg wasting | 2–4 wk | [Cohort] | Alcoholism + Mg depletion literature | One of the strongest single-step Mg increases available for heavy drinkers |
| Worsener: PPIs, diuretics (loop, thiazide) | Chronic use | Serum Mg ↓ 0.1–0.2 mg/dL; symptomatic hypomagnesemia in ~5% of chronic PPI users | Months of use | [Cohort, GL] | FDA safety communication 2011 on PPI hypomagnesemia | PPIs reduce intestinal Mg absorption; thiazides increase renal Mg excretion |
| Worsener: excess zinc supplementation | Zn >25–40 mg/d elemental | Serum Mg ↓ (Zn competes with Mg intestinally); copper deficiency is better-documented risk at high Zn | Months | [Mechanism] | Spencer 1994 *Biol Trace Elem Res* | Keep zinc supplementation ≤15–25 mg elemental/d to avoid mineral competition |

**Synthesis:**

- **Serum Mg insensitivity:** The most important fact about this marker. Homeostatic mechanisms pull Mg from bone and soft tissue to maintain serum concentration — serum Mg can be "normal" while total body Mg is ~15% depleted. RBC Mg (intracellular) is not routinely ordered but is clinically superior. Optimal serum Mg ≥0.85 mmol/L (≥2.07 mg/dL) is a reasonable target, but a normal result does not exclude meaningful intracellular depletion.
- **High responder variation:** At 300–400 mg/d, some individuals have no measurable serum Mg change; others gain +0.3 mg/dL. This is partly explained by baseline status (more depleted → bigger response), GI absorption efficiency, and possibly SLC41A1/TRPM6 genetic variants.
- **Oxide is oversold and underperforms:** Widely found in cheap multivitamins. Only ~4–5% bioavailability — mostly laxative effect, minimal Mg repletion. Any organic chelate (glycinate, citrate, malate, threonate) is substantially more bioavailable.
- **Blood pressure effect:** Meta of 34 trials (Zhang 2016 *Hypertension*): supplemental Mg (median 368 mg/d) lowered SBP by –2.0 mmHg and DBP by –1.7 mmHg. Small but consistent signal, most pronounced in baseline Mg-deficient individuals.

**South Asian-specific:**
- SA diets often low in Mg: low nut/seed intake, lower leafy greens in processed SA diets, legume phytate reduces Mg bioavailability. Estimated SA dietary Mg intake is ~200–280 mg/d vs recommended 400 mg/d — a population-level gap.
- Type 2 diabetes (elevated in SA populations) independently depletes Mg via osmotic diuresis. SA individuals with T2DM or insulin resistance should treat Mg deficiency as likely and supplement proactively.

**23andMe-relevant SNPs:**
- TRPM6 rs3750425, TRPM7 — magnesium transport channels; loss-of-function variants linked to hypomagnesemia, though individually rare.
- SLC41A1 rs708727 — solute carrier for Mg; common variant associated with serum Mg concentration in GWAS.

---

## Zinc (Serum)

**Quick read:** Serum zinc is a mediocre marker of zinc status (acute-phase reactant — falls in infection and inflammation regardless of stores). Zinc supplementation raises serum zinc by approximately 9 µg/dL (~2.2 µmol/L) on average across trials, but with very high heterogeneity. The main practical bottleneck for SA individuals is phytate — high-phytate vegetarian diets can reduce zinc bioavailability by 30–55% relative to omnivore diets.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral zinc supplement (any form) | 10–40 mg elemental Zn/d | Serum/plasma Zn ↑ ~9 µg/dL (range 5–13 µg/dL) | 4–12 wk | [Meta] | Meta of multiple RCTs; MD 9.08 µg/dL (95% CI 5.46–12.70) from pooled analysis (Nutrition Reviews 2025, 4316 participants) | Very high heterogeneity (I² = 97.6% for RCTs); response depends heavily on baseline status and formulation |
| Zinc gluconate | 15–25 mg elemental/d | Serum Zn ↑ modestly; higher bioavailability than sulfate; preferred for GI tolerance | 4–8 wk | [RCT] | Gibson 2018 *AJCN*; Singh 1998 | Well-absorbed; standard supplement form |
| Zinc sulfate | 10–30 mg elemental/d | Serum Zn ↑; effective but higher GI side effects (nausea) than organic chelates | 4–8 wk | [RCT] | Standard comparison studies | Take with small amount of food to reduce GI effects; do not take with high-phytate meal |
| Zinc picolinate / zinc acetate | 15–25 mg elemental/d | Comparable absorption to gluconate | 4–8 wk | [RCT] | Barrie 1987 *Agents Actions* (picolinate) | Marginal absorption advantage vs other organic forms |
| Zinc oxide | 15–50 mg elemental | Lower bioavailability than organic forms (~50% relative); cheap, common in multivitamins | 4–12 wk | [RCT] | Sandström 1989 *J Nutr*; Wegmüller 2014 | Not the preferred form for therapeutic zinc supplementation |
| Dietary: oysters | 6 medium oysters/d (~50 mg Zn) | Major food source; heme zinc has high bioavailability even in phytate-rich context | — | [Food composition] | USDA FoodData | 1 medium oyster ≈ 7–10 mg Zn; most bioavailable food source |
| Dietary: red meat | 3 oz beef (~5 mg Zn) | Good bioavailability; heme context reduces phytate inhibition | — | [Food composition] | — | For vegetarians, equivalent intake requires substantially higher zinc intake from plant sources |
| Phytate-rich plant diet (high whole grain, legume) | High phytate:Zn molar ratio (>15) | Zinc absorption ↓ to ~15% (vs 50–55% in low-phytate diet) | Ongoing | [RCT, Meta] | Gibson 2018 *AJCN* (PMID 30010865); Sandström bioavailability data | Phytate:Zn molar ratio >15 = low-bioavailability diet; 5–15 = moderate; <5 = high bioavailability. Vegetarian SA diet can easily reach ratio >15. |
| Soaking/fermenting legumes | Before cooking | Phytate hydrolysis 20–60% → zinc absorption improves proportionally | Per preparation | [RCT] | Hemalatha 2007 *Br J Nutr*; Gibson 2018 | Practical SA food-prep strategy to improve zinc bioavailability |
| Zinc lozenges (acetate ≥75 mg/d) — cold treatment | ≥75 mg/d elemental Zn as lozenge | Cold duration ↓ 37% (relative); high-dose zinc acetate: 42% reduction; gluconate: 20% reduction | Treatment duration only | [Meta] | Hemilä 2017 (PMID 28515951); Hemilä 2024 response to Cochrane (PMC11521859) | Cochrane 2024 review found less generous effect sizes and highlighted methodological limitations; Hemilä argues Cochrane methodology (mean difference rather than relative scale) is inappropriate for cold duration data. Current evidence: modest-to-meaningful effect size, formulation-dependent, requires high dose. |
| Worsener: excess copper deficiency (from high Zn) | Zn >40–50 mg elemental/d chronically | Cu deficiency → neutropenia, anemia, neurological symptoms; serum Cu ↓ | Months | [Case reports, Mechanism] | Spencer 1994; clinical reports | Maintain Zn supplement ≤15–25 mg/d unless deficient. If higher doses needed (e.g., dermatologic use), add Cu 1–2 mg/d. |
| Worsener: iron co-supplementation | Iron >25 mg taken simultaneously | Zn absorption ↓ 30–40% at Fe:Zn ratio >2:1 (non-heme iron competes via DMT1) | Acute | [RCT] | Lönnerdal 2017 review | Separate iron and zinc supplements by ≥2 hours |

**Synthesis:**

- **Serum zinc limitations:** Serum zinc is an acute-phase reactant — it falls with infection, inflammation, stress, and fasting, independently of total body zinc. It is less sensitive than RBC zinc for chronic deficiency. A normal serum zinc does not exclude mild-moderate zinc deficiency.
- **Phytate is the dominant lever for SA vegetarians:** Zinc bioavailability of 15% in a high-phytate diet vs 50% in a mixed/omnivore diet means that effective zinc intake from a vegetarian SA diet is 3× lower than calculated from food composition tables alone. Practical implications: soaking/fermenting legumes, adding vitamin C (minor effect on Zn — less than on iron), separating supplements from high-phytate meals.
- **Zinc lozenges for cold duration:** Hemilä's meta-analysis supports a ~37% relative reduction in cold duration with high-dose zinc acetate lozenges ≥75 mg/d elemental zinc. The Cochrane 2024 review is less generous and identified methodological issues. Current evidence summary: there is a real effect, it is formulation-dependent (acetate > gluconate, lozenges > tablets), and it is dose-dependent (>75 mg/d elemental Zn as lozenge). Note: these are therapeutic doses for acute illness — not daily supplement doses.

**South Asian-specific:**
- High-phytate vegetarian diets represent the dominant risk factor for inadequate zinc status in SA populations. FADS conversion advantage (more EPA/DHA) does not offset zinc limitations.

**23andMe-relevant SNPs:**
- SLC30A8 rs13266634 — zinc transporter 8 (ZnT8); primarily affects beta-cell zinc secretion; associated with T2DM risk. Not directly relevant for serum zinc supplementation response.
- ZIP4 (SLC39A4) — severe mutations cause acrodermatitis enteropathica (rare); common variants associated with zinc homeostasis.

---

## Calcium (Total Serum)

**Quick read:** Total serum calcium is tightly regulated by PTH and is rarely moved clinically by oral calcium supplementation alone (the body adjusts absorption and renal reabsorption to maintain the set point). Supplementation primarily benefits bone density and is relevant when dietary calcium is chronically low (common in SA diets). The CV risk signal from Bolland 2010 has been reassessed — long-term follow-up (WHI 22-year follow-up) shows no significant effect on all-cause mortality, and recent large cohort data do not confirm the MI signal.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to effect | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Oral calcium carbonate | 500–1200 mg elemental Ca/d | Total serum Ca ↑ transiently for 4–8 h post-dose (~0.1–0.2 mg/dL); fasting serum Ca unchanged in replete adults | Hours (transient) | [RCT] | Randomized crossover: Cambridge 2003 *Br J Nutr*; Carson 2020 review | Serum Ca is PTH-regulated — chronic supplementation does not persistently elevate serum Ca in people with normal PTH/parathyroid function |
| Oral calcium citrate | 500–1200 mg elemental Ca/d | Similar total serum Ca effect to carbonate; better absorbed without food (citrate does not require acid) | Hours (transient) | [RCT] | Cambridge 2003 RCT; Carson 2020 | Citrate preferred for patients with achlorhydria, PPI users, post-bariatric; carbonate is adequate with food in normal stomach acid |
| High dietary calcium (dairy, fortified foods, leafy greens) | +500 mg/d incremental diet Ca | Bone mineral density stabilization or modest increase; ionized Ca maintained; no persistent serum total Ca change | Months to years | [Meta, Cohort] | Bauer 2009 meta; dietary calcium-BMD literature | Dietary calcium has a better safety profile than supplements — no acute calcium spike — and may explain why dietary calcium does not carry the CV signal |
| Calcium supplementation + bone density (postmenopausal women) | 1000–1200 mg Ca + 400–800 IU D3 | BMD hip: +1–2% over 2 years; fracture reduction ~12% in compliant participants | 1–2 years | [Meta] | Chapuy 1992 *NEJM* original; combined Ca+D meta (PMC12506016) | Effect is modest and mostly seen in Ca-deficient/elderly; young replete individuals show less benefit |
| CV risk — Bolland 2010 and re-analyses | Calcium supplement alone (no D) | Original: MI risk RR 1.27 (95% CI 1.01–1.59); WHI 22-year follow-up (2024): no significant CV mortality increase; large cohort studies: OR not significantly elevated | — | [Meta, RCT reanalysis, Cohort] | Bolland 2010 *BMJ*; WHI long-term follow-up *Ann Intern Med* 2024; large population-based Canadian case-control study | **Evidence status as of 2025:** The Bolland signal was real in the 2010 meta, but has NOT been robustly replicated in subsequent prospective analyses. The WHI 22-year follow-up (2024, *Annals of Internal Medicine*) showed a 6% higher CV death risk with Ca+D vs placebo — borderline significant and driven by D co-administration. The mechanism proposed is arterial Ca deposition from acute serum Ca spikes with supplementation (vs. dietary Ca which is absorbed slowly). Practical implication: take supplements with food; split doses; add vitamin K2 if concerned; dietary Ca is preferred if achievable. |
| Vitamin K2 (MK-7) co-supplementation | 100–200 µg/d MK-7 with Ca | Matrix Gla protein (MGP) activation → reduced arterial calcification in some trials; Knapen 2015 *Thromb Haemost* (n=244, 3 yr): arterial stiffness ↓ 3.3% in MK-7 group | 2–3 years | [RCT — limited] | Knapen 2015 (PMID 25694037); review (PMC4566462) | MK-7 data are promising but limited in sample size and duration; the MGP mechanism is biologically robust; hard outcomes not proven in RCT. Does not change serum Ca levels. |
| Worsener: vitamin D toxicity (25-OH >100–150 ng/mL) | Very high dose vitamin D | Hypercalcemia → serum Ca ↑ above 10.5 mg/dL; symptoms: polyuria, nausea, kidney stones, confusion | Months | [Case reports] | Vitamin D toxicity literature | VITAL (2000 IU/d D3): no excess hypercalcemia. Risk begins at sustained very-high doses (>10,000 IU/d in many adults). |

**Synthesis:**

- **Serum total calcium is not the optimization target** for calcium supplementation; bone mineral density is. Serum Ca will remain in normal range even with significant Ca supplementation in individuals with normal parathyroid function.
- **Dietary calcium is preferred over supplement calcium** when achievable. Dairy, fortified plant milks, leafy greens (kale, bok choy, not spinach — high oxalate), and calcium-set tofu provide Ca without the acute serum Ca spikes associated with bolus supplementation.
- **Calcium carbonate requires food:** Gastric acid needed for absorption. Take with largest meal. Calcium citrate: independent of acid, can be taken any time — important for PPI users and post-bariatric patients.
- **K2 co-supplementation:** Mechanistically rational if supplementing Ca long-term; evidence for hard CV outcomes is limited but the safety profile of K2 at 100–200 µg/d MK-7 is excellent.

**South Asian-specific:**
- SA diets are generally low in dairy (lactose intolerance prevalence ~65–70% in South Asians), and leafy green calcium is variable. Mean dietary Ca intake in India ~400–500 mg/d vs recommended 1000 mg/d — a substantial chronic gap. This increases osteoporosis risk later in life; supplementation is more strongly justified than in Western omnivore diets.

---

## Omega-3 Index (RBC EPA+DHA %)

**Quick read:** The omega-3 index is highly responsive to supplementation — roughly +1–2 percentage points per 1000 mg/d of EPA+DHA added, from a typical Western baseline of 4–5%. Reaching the ≥8% target from baseline ~4–5% requires approximately 2000 mg/d EPA+DHA for 3–4 months. RBC equilibration takes ~120 days (erythrocyte lifespan). Algal oil is bioavailable-equivalent to fish oil for DHA. ALA→DHA conversion is too low in men to be meaningfully relied upon without direct EPA/DHA intake. SA populations with higher FADS2 insertion frequency may convert ALA more efficiently, but this advantage is insufficient without marine or algal supplementation.

### Effect size table

| Intervention | Dose | Direction & magnitude | Time to peak | Evidence | Source | Caveats |
|---|---|---|---|---|---|---|
| Fish oil (EPA+DHA, TG form) | 1000 mg EPA+DHA/d | Omega-3 index ↑ ~1–1.5 percentage points from baseline ~4–5% | 3–4 months | [RCT, Meta] | Harris & Von Schacky 2004; predictive model (AJCN 2022 n=1,422 supplemented) | Final model explained 62% of variance; includes dose, baseline O3I, and formulation |
| Fish oil (EPA+DHA, TG form) | 2000 mg EPA+DHA/d | Omega-3 index ↑ ~2–3 percentage points (mean ~4.5% → 7.0–7.5%) | 3–4 months | [RCT, Meta] | AJCN 2022 predictive meta-analysis; mean 1983 mg/d across trials: O3I 4.9% → 8.1% | Adequate to reach ≥8% for most individuals starting at 4–5% |
| Fish oil (EPA+DHA, TG form) | 4000 mg/d (REDUCE-IT dose) | Omega-3 index ↑ ~4–6 percentage points (pharmacological zone: 9–12% achievable) | 3–4 months | [RCT] | REDUCE-IT/STRENGTH pharmacodynamics; Browning 2012: 1.9 g/d × 12 months → O3I +5 percentage points | Above 4 g/d, AF risk signal emerges (see omega-3 file for detail) |
| Algal oil (DHA-dominant, with EPA) | 600–1000 mg DHA + 300 mg EPA/d | DHA bioavailability from algal oil is equivalent to fish oil (non-inferior); Omega-3 index ↑ similarly | 3–4 months | [RCT, Meta] | PMC12524788 (2025): microalgal vs fish oil non-inferior in plasma phospholipids; Walker 2019 comparative review; Algal-oil study PMC9684969 | Algal DHA accumulates at least as well as fish oil DHA in vegetarians; EPA from algae is smaller (less EPA in algal oil vs fish oil) — for EPA-specific effects (REDUCE-IT), fish or EPA concentrate preferred |
| ALA from flaxseed, chia, walnuts | 2–5 g ALA/d | Omega-3 index ↑ negligibly in men (~0 to +0.3 percentage points); ALA raises total omega-3 but EPA/DHA barely rises | 3–4 months | [RCT] | Brenna 2009 *PLEFA* (PMID 19053988): <1% ALA→EPA in men; multiple ALA supplementation trials | ALA conversion to EPA is <5% in men, and ALA→DHA is ~0–4% in men. Relying on ALA for omega-3 index improvement is not a viable strategy in males. |
| FADS2 rs66698963 insertion (SA "vegetarian allele") | Endogenous (genetic) | Carriers (~70% of SA individuals) have enhanced Δ6-desaturase activity → better ALA→EPA/DHA conversion vs non-carriers | — | [Cohort, MR] | 1000 Genomes project analysis; Mathias 2014 *Hum Mol Genet*; Frontiers 2022 FADS+ancestry review | Carries advantage vs European "A" haplotype but still produces substantially lower EPA/DHA than direct marine intake. Even with favorable FADS2 allele, plant-based-only diets produce O3I ~3–5%, below target. |
| Fatty fish (salmon, sardines, mackerel) | 2–3 servings/wk (~300 g cooked, ~2000 mg EPA+DHA/wk) | Omega-3 index ↑ ~1.5–2.5 percentage points over 3–4 months | 3–4 months | [Cohort, RCT] | Browning 2012; NHANES diet-biomarker correlations | Equivalent to ~300–400 mg EPA+DHA/d dietary; sufficient for borderline-deficient individuals; may not reach ≥8% in all individuals |
| Krill oil (phospholipid form) | 500–1000 mg EPA+DHA/d | O3I response per gram EPA+DHA may be modestly greater than triglyceride fish oil due to phospholipid carrier (better tissue incorporation) | 3–4 months | [RCT] | Ulven 2011 *Lipids*: krill vs fish oil at equivalent EPA+DHA dose — PL form had slightly higher plasma EPA at 7 wk; RBC difference less clear | The advantage of krill is modest and dose-for-dose comparisons are complicated by lower absolute EPA+DHA in krill products |
| Ethyl ester fish oil vs triglyceride form | Same EPA+DHA dose | Ethyl ester form may have ~20–30% lower bioavailability vs TG form when taken without fat; difference eliminated when taken with fatty meal | Same timing | [RCT, Mechanism] | Lawson 1988; Neubronner 2011 *Eur J Clin Nutr* | Practically: take any fish oil with the largest/fattiest meal of the day for optimal absorption, regardless of form |
| Triglycerides (serum) — with omega-3 supplementation | 2000–4000 mg EPA+DHA/d | TG ↓ ~20–30% at 4 g/d (pharmacological); ↓ ~5–15% at 2 g/d | 8–12 wk | [Meta, RCT] | Multiple meta-analyses (Skulas-Ray 2019 *Circulation*: 4 g/d → TG –1.8 mmol/L or ~30%); REDUCE-IT pharmacodynamics | TG-lowering is the most reproducible metabolic effect of omega-3 supplementation; dose-dependent; most useful if baseline TG is elevated |
| Worsener: smoking | Active smoking vs nonsmoker | Omega-3 index ↓ ~0.5–1.0 percentage points | Ongoing | [Cohort] | *Lipids Health Dis* 2012 (smoking case-control) | Oxidative stress from smoking increases EPA/DHA peroxidation and turnover |
| Worsener: obesity/high BMI | BMI >30 | Omega-3 index typically 0.5–1 percentage point lower for same intake, partly dilutional | Ongoing | [Cohort] | BMI-omega-3 index inverse relationship (multiple cohort data) | Need higher dose to achieve same index target |

**Synthesis:**

- **Highest-leverage interventions:** Fish oil TG form or algal oil, 2000 mg EPA+DHA/d for 3–4 months. This achieves the ≥8% target in most individuals starting at 4–5%.
- **ALA is not a viable route in men:** ALA conversion to EPA/DHA is <5% in males; FADS2 SA advantage is real but insufficient. Vegetarian SA males must supplement algal oil or, if omnivore, eat fatty fish ≥2×/week.
- **Algal oil equivalence:** Multiple studies confirm algal DHA bioavailability is non-inferior to fish oil DHA. For DHA-specific goals (brain, omega-3 index), algal oil is a complete substitute. For EPA-specific pharmacological goals (REDUCE-IT dose range), direct EPA supplementation is needed.
- **REDUCE-IT / STRENGTH divergence:** High-dose EPA (pure icosapent ethyl, REDUCE-IT): 25% CV event reduction in statin-treated high-TG patients. High-dose EPA+DHA (STRENGTH): null. Mineral oil placebo controversy unresolved. For a healthy 20-year-old, neither trial directly applies — the intervention target is sufficiency (O3I ≥8%), not pharmacological doses. See `nutrients_omega_fatty_acids.md` §11 for full analysis.
- **Oversold:** ALA supplements (flax/chia) for omega-3 status in men; high-dose omega-3 for primary CV prevention in low-risk individuals (VITAL null result).

**South Asian-specific:**
- FADS2 rs66698963 insertion ("vegetarian gene") in ~70% of SA individuals does provide a conversion advantage. However, even with this advantage, plant-based-only diets still produce O3I ~3–5% in most studies. Direct EPA/DHA is necessary.
- Lower fish consumption in many SA communities (especially north Indian) compounds the deficiency. Urban SA vegetarians in the UK have among the lowest omega-3 indices measured.

**23andMe-relevant SNPs:**
- FADS1 rs174537 and FADS2 rs174575 — the "A" haplotype (inefficient conversion) is common in European ancestry; the FADS2 rs66698963 insertion is common in SA ancestry (~70%) and confers advantage. Check your haplotype to understand how much you can compensate through ALA intake.
- PPARA rs4253778 — PPAR-α variant affecting EPA/DHA-driven gene expression; affects lipid-lowering response to fish oil.

**Realistic 3–6 month trajectory from baseline O3I ~4–5%:**
- 2000 mg EPA+DHA/d (fish or algal oil): O3I 4.5% → ~7.5–8.5% by month 4
- 1000 mg EPA+DHA/d: O3I 4.5% → ~6–7% by month 4 (may not reach ≥8%)
- 3×/wk fatty fish + 1000 mg supplement: O3I 4.5% → ~8–9% by month 4

---

## Cross-Marker Patterns

### Iron cascade (ferritin + TSAT + Hgb)

Iron supplementation moves markers in a predictable sequence with characteristic lags:
1. **First to respond (week 2–4):** Reticulocyte count rises as marrow iron repletion allows erythropoiesis. Serum iron and TSAT begin to rise.
2. **Second (week 4–8):** Hemoglobin rises — classic benchmark is +1–2 g/dL over 4 weeks from frank IDA baseline.
3. **Last (week 8–20):** Ferritin rises as iron fills stores after functional Hgb/TSAT normalization. If ferritin is being used as an endpoint, expect 3–5 months of sustained oral iron therapy.
4. **Disordering the sequence:** IV iron bypasses all three steps simultaneously — ferritin rises within days (acute-phase; not useful), TSAT normalizes within weeks, Hgb rises by week 4–6.

### Vitamin D + calcium + PTH triad

Vitamin D supplementation has secondary effects beyond 25-OH:
- 25-OH ↑ → intestinal calcium absorption ↑ → ionized Ca ↑ slightly → PTH ↓ (parathyroid gland reduces secretion to maintain set point)
- In vitamin D deficiency: PTH is chronically elevated (secondary hyperparathyroidism); correcting 25-OH to >30 ng/mL suppresses PTH by 20–30% in deficient adults **[Meta, Holick 2007]**
- The net result: improved calcium-phosphate balance without raising fasting serum total calcium in replete individuals.

### Vegetarian diet — coupled deficits

A consistent vegetarian (and especially vegan) diet in a SA male produces predictable coupled deficiencies:
- **B12:** Essentially zero dietary intake → deficiency within 2–5 years without supplementation; MMA rises before serum B12 falls below "normal."
- **Iron:** Non-heme only, phytate-inhibited → serum ferritin trending low; TSAT <20% common; IDA not uncommon in vegetarian males.
- **Zinc:** Phytate inhibition → effective zinc intake 30–55% lower than food composition tables suggest.
- **Omega-3 index:** No EPA/DHA from diet → O3I typically <4% unless algal supplement used.
- **Vitamin D:** No contribution from diet beyond small amount in dairy/fortified foods.

These five deficits occur together and reinforce each other (e.g., B12 deficiency raises homocysteine; zinc deficiency impairs B12-dependent enzymes; low omega-3 may impair cell membrane function). A single semi-annual panel that catches all five simultaneously is high-yield.

### Alcohol — coupled B-vitamin/Mg/folate deficit

Chronic alcohol consumption (>2 drinks/d) depletes:
- **Folate:** direct mucosal impairment of folate absorption + altered hepatic folate metabolism
- **B12:** altered enterohepatic recycling
- **B6:** accelerated degradation of PLP
- **Magnesium:** urinary wasting (alcohol blocks tubular Mg reabsorption)
- **Zinc:** urinary excretion increased

The clinical presentation is elevated homocysteine (folate/B12/B6 depletion) + low serum Mg + moderately elevated ferritin (hepatic ALD release) with low TSAT (functional depletion from alcohol-related liver dysfunction). Cessation is the primary intervention; supplementation of folate + B12 + B6 + Mg in active drinkers partially mitigates but does not reverse the depletion.

### Homocysteine as a "methylation status composite"

Homocysteine sits at the intersection of folate (5-MTHF), B12 (methylcobalamin), and B6 (transsulfuration). A Hcy above 9 µmol/L in a 20-year-old male is a signal to check:
1. Serum B12 + MMA (functional B12 status)
2. Serum/RBC folate
3. TSH (hypothyroidism raises Hcy)
4. Creatinine/eGFR (renal disease raises Hcy and MMA)
5. MTHFR C677T on 23andMe

---

## Drug/Rx Reference Table (for scale)

| Intervention | Route/Dose | Effect size | Time to effect | Source/Context |
|---|---|---|---|---|
| IV ferric carboxymaltose (FCM) | 1000 mg IV single infusion | Ferritin: baseline ~15 → ~110–150 µg/L at 6 wk; TSAT ↑ transiently to 60–80% at 24–48 h | 4–6 wk (ferritin); 24–48 h (TSAT) | PREFER trial; NCBIbooks NBK614950; meta (Anker 2020 JACC) |
| IV iron sucrose | 200 mg × 5 infusions = 1000 mg total | Ferritin ↑ 80–150 µg/L; slightly lower peak than FCM per dose; requires more infusions | 4–6 wk | Multiple nephrology RCTs |
| IM/IV cyanocobalamin | 1000 µg IM | MMA normalization within days; serum B12 ↑ to >1000 pg/mL within 48 h | Days | Kuzminski 1998 *Blood*; pharmacokinetic data |
| IM hydroxocobalamin | 1000 µg IM q month | Longer-acting depot; serum B12 maintained >300 pg/mL throughout cycle | Days (peak); weeks (sustained) | UK/EU pernicious anemia guideline |
| Ergocalciferol 50,000 IU weekly × 8 wk (Endocrine Soc. protocol) | Oral D2 (or D3) | 25-OH ↑ ~30–40 ng/mL from deficient baseline; final ~47 ng/mL in one trial | 8 wk | Endo Soc 2011 *JCEM* guideline; PMC2683376 |
| Icosapent ethyl (Vascepa) 4 g/d | Oral prescription EPA-only ethyl ester | Omega-3 index ↑ 4–6 percentage points; TG ↓ 20–30%; significant CV event reduction (25% relative, HR 0.75) in REDUCE-IT population (statin-treated, high-TG, CV risk/diabetes) | 3–4 months (O3I); 8–12 wk (TG) | Bhatt 2019 *NEJM* (REDUCE-IT) — mineral oil placebo controversy unresolved |
| Omega-3 carboxylic acids (Epanova) 4 g/d | Oral prescription EPA+DHA free fatty acid | O3I ↑ ~3–5 percentage points; TG ↓ similar to icosapent ethyl; CV event reduction: NULL (STRENGTH trial) | 3–4 months | Nicholls 2020 *JAMA* (STRENGTH) |

---

## Sources

### Iron studies

- Stoffel NU et al. Iron absorption from oral iron supplements given on consecutive versus alternate days in iron-depleted women. *Lancet Haematol* 2017;4:e524–e533. PMID 29032957
- Cook JD, Reddy MB. Effect of ascorbic acid intake on nonheme-iron absorption from a complete diet. *Am J Clin Nutr* 2001;73:93–98. PMID 11157344
- Hallberg L et al. Calcium: effect of different amounts on nonheme- and heme-iron absorption in humans. *Am J Clin Nutr* 1992;53:112–119. PMID 1519451
- Hallberg L, Rossander L. Effect of different drinks on the absorption of non-haem iron from composite meals. *Hum Nutr Appl Nutr* 1982;36:116–123.
- Gibson RS et al. Implications of phytate in plant-based foods for iron and zinc bioavailability, setting dietary requirements, and formulating programs and policies. *Nutr Rev* 2018;76:793–804. PMID 30010865
- Anker SD et al. Ferric carboxymaltose in patients with heart failure and iron deficiency. *N Engl J Med* 2020;382:1419–1429. (AFFIRM-AHF)
- NCBI Bookshelf: Ferric Carboxymaltose (Ferinject) Clinical Review. NBK614950.
- Nemeth E et al. Hepcidin regulates cellular iron efflux by binding to ferroportin and inducing its internalization. *Science* 2004;306:2090–2093.
- EASL Clinical Practice Guidelines 2022: Haemochromatosis. *J Hepatol* 2022;77:479–502. PMID 35662478

### Vitamin D

- Heaney RP et al. Human serum 25-hydroxycholecalciferol response to extended oral dosing with cholecalciferol. *Am J Clin Nutr* 2003;77:204–210.
- Gallagher JC. Vitamin D and aging. *Endocrinol Metab Clin North Am* 2013;42:319–332.
- Tripkovic L et al. Comparison of vitamin D2 and vitamin D3 supplementation in raising serum 25-hydroxyvitamin D status: a systematic review and meta-analysis. *Am J Clin Nutr* 2012;95:1357–1364. PMID 22552031
- Manson JE et al. Vitamin D supplements and prevention of cancer and cardiovascular disease (VITAL). *N Engl J Med* 2019;380:33–44.
- Endocrine Society. Evaluation, Treatment, and Prevention of Vitamin D Deficiency: Clinical Practice Guideline. *JCEM* 2011;96:1911–1930.
- Holick MF. Vitamin D deficiency. *N Engl J Med* 2007;357:266–281.
- Webb AR, Engelsen O. Calculated ultraviolet exposure levels for a healthy vitamin D status. *Photochem Photobiol* 2006;82:1697–1703.
- Lowe NM, Bhojani I. Special considerations for vitamin D in the south Asian population in the UK. *Ther Adv Musculoskelet Dis* 2017;9:137–144. PMC5466148
- Palacios C et al. Very high prevalence of 25-hydroxyvitamin D deficiency in 6433 UK South Asian adults (UK Biobank). PMC7844605
- Wang TJ et al. Common genetic determinants of vitamin D insufficiency: a genome-wide association study. *Lancet* 2010;376:180–188. (GC, CYP2R1, DHCR7 SNPs)
- Deng X et al. Magnesium, vitamin D status and mortality. *Am J Clin Nutr* 2018;108:1233–1239. PMID 29794773
- Miyauchi M et al. Determining an effective UV radiation exposure time for vitamin D synthesis. *Photochem Photobiol* 2016;92:863–869. PMID 27754554
- Blum M et al. Vitamin D3 in fat tissue. *Endocrine* 2008;33:90–94. (adipose dilution)

### Vitamin B12 and MMA

- Kuzminski AM et al. Effective treatment of cobalamin deficiency with oral cobalamin. *Blood* 1998;92:1191–1198.
- Vidal-Alaball J et al. Oral vitamin B12 versus intramuscular vitamin B12 for vitamin B12 deficiency. *Cochrane Database Syst Rev* 2005. (Cochrane review)
- Eussen SM et al. Oral cyanocobalamin supplementation in older people with vitamin B12 deficiency: a dose-finding trial. *Arch Intern Med* 2005;165:1167–1172. PMID 15911731
- Lindenbaum J et al. Neuropsychiatric disorders caused by cobalamin deficiency in the absence of anemia or macrocytosis. *N Engl J Med* 1988;318:1720–1728. PMID 3374550
- Antony AC. Vegetarianism and vitamin B-12 (cobalamin) deficiency. *Am J Clin Nutr* 2003;78:3–6. PMID 12816768
- PMC12681447: Vitamin B12: A Comprehensive Review of Natural vs Synthetic Forms. 2025.
- PMC11128391: Efficacy of different routes of vitamin B12 supplementation: network meta-analysis. 2024.
- Sangle P et al. Vitamin B12 supplementation: preventing onset and improving prognosis of depression. *Cureus* 2020 (PPI-B12 meta).
- PMC9577826: Association of Vitamin B12 deficiency with long-term PPIs use: A cohort study.
- PMID 37060552: Vitamin B12 deficiency and use of proton pump inhibitors: systematic review and meta-analysis (25 studies, OR 1.42).

### Folate and Homocysteine

- Homocysteine Lowering Trialists' Collaboration. Lowering blood homocysteine with folic acid-based supplements: meta-analysis of randomised trials. *BMJ* 1998;316:894–898. PMID 9569395
- Clarke R et al. Effects of lowering homocysteine levels with B vitamins on cardiovascular disease, cancer, and cause-specific mortality: meta-analysis of 8 randomized trials involving 37,485 individuals. *Arch Intern Med* 2010;170:1622–1631. PMID 20937919
- HOPE-2 Investigators. Homocysteine lowering with folic acid and B vitamins in vascular disease. *N Engl J Med* 2006;354:1567–1577.
- Yuan S et al. Homocysteine and the risk of stroke: a Mendelian randomization. *BMC Med* 2021;19:87.
- Anderson OS et al. Response of serum and red blood cell folate concentrations to folic acid supplementation depends on MTHFR C677T genotype. *Mol Nutr Food Res* 2013;57:637–644. PMID 23456769
- Systematic review (MDPI Nutrients 2019): Dose-response of folic acid supplementation on blood folate concentrations. 108 articles reviewed.
- McNulty H et al. Riboflavin lowers homocysteine in individuals homozygous for the MTHFR 677C→T polymorphism. *Circulation* 2006;113:74–80.
- Olthof MR et al. Betaine supplementation lowers plasma homocysteine. *J Nutr* 2003;133:4135–4138.

### Magnesium

- Cheung MM et al. Effects of magnesium supplementation on blood pressure: a meta-analysis of randomized double-blind placebo-controlled trials. *Hypertension* 2016;68:324–333. PMID 27402922
- PMC9065397: The effects of magnesium supplementation on serum magnesium and calcium in T2DM: systematic review and meta-analysis (16 RCTs): MD +0.15 mg/dL.
- Coudray C et al. Study of magnesium bioavailability from ten organic and inorganic Mg salts in Mg-depleted rats using a stable isotope approach. *Magnes Res* 2005;18:215–223.

### Zinc

- Nutrition Reviews meta (Oxford, 2025; PMID 38917458 update): Methods of assessment of zinc status in humans.
- Gibson RS et al. Bioavailability of iron, zinc, and other trace minerals from vegetarian diets. *Am J Clin Nutr* 2003;78:633S–639S.
- Hemilä H. Zinc lozenges and the common cold: a meta-analysis comparing zinc acetate and zinc gluconate, and the role of zinc dosage. *JRSM Open* 2017;8:2054270417694291. PMID 28515951
- Hemilä H. Shortcomings in the Cochrane review on zinc for the common cold (2024). *Front Med* 2024;11:1470004. PMC11521859
- Spencer H et al. Effect of zinc supplements on the intestinal absorption of calcium, copper, and zinc in humans. *J Am Coll Nutr* 1994;13:584–589.

### Calcium

- Bolland MJ et al. Effect of calcium supplements on risk of myocardial infarction and cardiovascular events: meta-analysis. *BMJ* 2010;341:c3691. PMID 20671013
- WHI long-term follow-up (calcium + vitamin D, 22-year cumulative follow-up). *Ann Intern Med* 2024;177:497–508.
- Knapen MH et al. Three-year low-dose menaquinone-7 supplementation helps decrease bone loss in healthy postmenopausal women. *Osteoporos Int* 2013;24:2499–2507. (bone); Knapen 2015 *Thromb Haemost* (arterial stiffness). PMID 25694037
- PMC4566462: Proper calcium use: vitamin K2 as a promoter of bone and cardiovascular health.

### Omega-3

- Harris WS et al. Predicting the effects of supplemental EPA and DHA on the omega-3 index. *Am J Clin Nutr* 2022;116:1334–1342.
- Browning LM et al. Compared with usual eating, a diet containing oily fish improves the omega-3 index. *Br J Nutr* 2012;107:1076–1084. (1.9 g/d EPA+DHA × 12 months → O3I +5%)
- Bhatt DL et al. Cardiovascular risk reduction with icosapent ethyl (REDUCE-IT). *N Engl J Med* 2019;380:11–22.
- Nicholls SJ et al. Effect of high-dose omega-3 fatty acids vs corn oil on major adverse cardiovascular events (STRENGTH). *JAMA* 2020;324:2268–2280.
- Manson JE et al. Marine n-3 fatty acids and prevention of cardiovascular disease and cancer (VITAL). *N Engl J Med* 2019;380:23–32.
- Brenna JT et al. α-Linolenic acid supplementation and conversion to n-3 long-chain polyunsaturated fatty acids in humans. *Prostaglandins Leukot Essent Fatty Acids* 2009;80:85–91. PMID 19053988
- PMC12524788 (2025): Comparative bioavailability of DHA and EPA from microalgal and fish oil in adults.
- Stark KD et al. Red blood cell fatty acid patterns from 7 countries. *Prostaglandins Leukot Essent Fatty Acids* 2022. (population O3I data)
- Frontiers in Nutrition 2022: Interpreting clinical trials with omega-3 supplements in context of ancestry and FADS genetic variation. PMC8861490

### South Asian–specific sources

- BMC Public Health 2021 (PMC8501935): High prevalence of vitamin D deficiency among South Asian adults: systematic review and meta-analysis.
- PMC7844605: Very high prevalence of 25-OH vitamin D deficiency in 6,433 UK South Asian adults (UK Biobank).
- Bouillon R. Vitamin D: from photosynthesis, metabolism, and action to clinical applications. *Endocrinology* 2019.
- Mithal A et al. Global vitamin D status and determinants of hypovitaminosis D. *Osteoporos Int* 2009;20:1807–1820. (IOF report; SA data)
- Antony AC. Vegetarianism and vitamin B-12 deficiency. *Am J Clin Nutr* 2003.
- Pasricha S-R et al. Control of iron deficiency anaemia in low- and middle-income countries. *Blood* 2013;121:2607–2617.
- Mathias RA et al. FADS genetic variants and omega-6 polyunsaturated fatty acid metabolism in a heterogeneous ancestry population. *J Lipid Res* 2014; + Frontiers 2022 FADS ancestry review.
- 1000 Genomes project analysis of FADS2 rs66698963 ("vegetarian allele") frequency by ancestry.

---

*Companion files: `nutrients_vitamins_minerals.md` (biology, reference ranges, clinical interpretation), `nutrients_omega_fatty_acids.md` (omega panel biology and evidence), `biomarker_confounds_reference.md` (pre-analytical confounders).*
