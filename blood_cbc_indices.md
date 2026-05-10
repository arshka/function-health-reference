# Blood / CBC RBC-Index Markers — Comprehensive Reference

A deep-dive reference for interpreting the 10 blood-typing and CBC red-cell / platelet-index markers on a Function Health panel, written for a healthy 20-year-old male. All quantitative claims are cited inline; sex-specific reference ranges are noted.

---

## Table of Contents

1. [How these markers are measured (assay primer)](#1-how-these-markers-are-measured-assay-primer)
2. [ABO Group and Rhesus (Rh) Factor](#2-abo-group-and-rhesus-rh-factor)
3. [Hemoglobin (Hgb)](#3-hemoglobin-hgb)
4. [Hematocrit (Hct)](#4-hematocrit-hct)
5. [Red Blood Cell Count (RBC)](#5-red-blood-cell-count-rbc)
6. [Mean Corpuscular Volume (MCV)](#6-mean-corpuscular-volume-mcv)
7. [Mean Corpuscular Hemoglobin (MCH)](#7-mean-corpuscular-hemoglobin-mch)
8. [Mean Corpuscular Hemoglobin Concentration (MCHC)](#8-mean-corpuscular-hemoglobin-concentration-mchc)
9. [Red Cell Distribution Width (RDW)](#9-red-cell-distribution-width-rdw)
10. [Platelet Count](#10-platelet-count)
11. [Mean Platelet Volume (MPV)](#11-mean-platelet-volume-mpv)
12. [Cross-cutting clinical patterns](#12-cross-cutting-clinical-patterns)
13. [Confounders summary table](#13-confounders-summary-table)
14. [References](#14-references)

---

## 1. How these markers are measured (assay primer)

CBC parameters are measured by automated hematology analyzers (Sysmex, Beckman Coulter, Abbott, Siemens) using two complementary physical principles:

- **Coulter principle / electrical impedance.** Cells suspended in an isotonic conductive fluid pass single-file through a small aperture across which a current is maintained. Each cell, being a poor conductor, displaces conductive fluid and generates a voltage pulse. Pulse height is proportional to cell volume; pulse count is the cell number. RBC count, platelet count, MCV, and MPV are derived directly from impedance. ([Bioscience Pakistan — Working principles of automated hematology analyzers](https://www.bioscience.com.pk/en/topics/hematology/principles-of-working-of-automated-hemotology-analyzer); [Wikipedia — Hematology analyzer](https://en.wikipedia.org/wiki/Hematology_analyzer))
- **Light scatter / VCS technology.** A laser hits each cell in a flow cell; forward scatter encodes size, side scatter (90°) encodes internal complexity / granularity. Modern Beckman analyzers add radiofrequency conductivity (VCS = Volume, Conductivity, Scatter); Sysmex uses fluorescence flow cytometry on reticulocytes and abnormal cells. ([JLPM — Daves: Modern hematology analyzers](https://jlpm.amegroups.org/article/view/8320/html))
- **Hemoglobin** is measured by spectrophotometry of the lysed sample, classically as cyanmethemoglobin at 540 nm; modern analyzers use sodium-lauryl-sulfate or other cyanide-free chemistries. **Hematocrit** is calculated (MCV × RBC), not directly spun, on automated panels (the manual spun-microhematocrit gives a slightly higher number due to trapped plasma).
- **MCH** = Hgb / RBC. **MCHC** = Hgb / Hct. **RDW-CV** = (SD of RBC volume / MCV) × 100.
- **ABO and Rh** are determined by **serology — agglutination**. Forward typing tests the patient's RBCs against commercial anti-A, anti-B, and anti-D antisera. Reverse typing tests the patient's serum/plasma against known A and B reagent cells. Concordance between forward and reverse is required to call ABO. Rh(D) typing uses anti-D; weak D variants may need indirect antiglobulin testing. ([NCBI Bookshelf — The ABO blood group](https://www.ncbi.nlm.nih.gov/books/NBK2267/))

Practical implications: tube type matters. CBC requires EDTA (lavender top); EDTA-induced platelet clumping causes pseudothrombocytopenia (see §10). Cold agglutinins falsely raise MCHC (see §8). Diurnal variation, posture, and recent exercise meaningfully shift Hgb/Hct (see §13).

---

## 2. ABO Group and Rhesus (Rh) Factor

### 2.1 Biology

The **ABO** locus on chromosome 9q34 encodes a glycosyltransferase that adds either N-acetylgalactosamine (A allele) or galactose (B allele) to a precursor H-antigen on RBC surfaces and many endothelial / epithelial cells. The O allele is a loss-of-function frameshift; type O individuals express only the unmodified H antigen. Anti-A and anti-B antibodies form naturally in the first months of life (probably in response to gut bacterial antigens) against whichever antigen is *absent* from one's own cells. ([NCBI — ABO blood group](https://www.ncbi.nlm.nih.gov/books/NBK2267/); [ASH — Blood: The relationship between ABO blood group and von Willebrand factor levels](https://ashpublications.org/blood/article/136/25/2864/461790/))

The **Rh** system is far more complex (>50 antigens), but the clinically dominant one is **D**. RhD+ means the D antigen is expressed; RhD− lacks it. Unlike ABO, anti-D is *not* naturally occurring — it requires sensitization (transfusion or pregnancy). ([NCBI — Hemolytic disease of the newborn](https://www.ncbi.nlm.nih.gov/books/NBK2266/))

### 2.2 Population frequency (US)

Distribution is stable over decades (genetic, slow drift via immigration). Approximate US frequencies:

| Type | US frequency |
|---|---|
| O+ | ~37% |
| A+ | ~36% |
| B+ | ~9% |
| AB+ | ~3% |
| O− | ~7% |
| A− | ~6% |
| B− | ~2% |
| AB− | ~1% |

About **85% of Americans are RhD+**, **15% RhD−**. ([Stanford Blood Center — Blood Types](https://stanfordbloodcenter.org/donate-blood/blood-donation-facts/blood-types/); [Statista — US blood type distribution 2023](https://www.statista.com/statistics/1112664/blood-type-distribution-us/))

### 2.3 Donor compatibility (brief)

- **O− is the universal RBC donor**; **AB+ is the universal RBC recipient** (and the universal *plasma* donor — opposite logic, because plasma carries antibodies).
- ABO incompatibility in transfusion causes acute intravascular hemolysis — most lethal transfusion reaction.
- RhD− women of childbearing age must receive RhD− blood when possible to prevent anti-D sensitization. ([NCBI — HDN](https://www.ncbi.nlm.nih.gov/books/NBK2266/))

### 2.4 Disease associations

This is where ABO becomes biomarker-relevant rather than just transfusion-relevant. The mechanism for many findings is that the ABO glycosyltransferase modifies **von Willebrand factor (VWF)** glycans, altering its plasma half-life.

**Thrombosis / cardiovascular (non-O > O):**
- VWF:Ag is **~25% higher** in non-O vs. group O individuals; ABO genotype explains roughly **30% of the heritable variance in VWF**. Factor VIII (which circulates bound to VWF) tracks VWF levels. ([Franchini & Lippi 2007 — Thrombosis Journal review on ABO and VWF](https://link.springer.com/article/10.1186/1477-9560-5-14); [Franchini 2012 review summarized in PMC3626462 — Non-O blood group as VTE risk factor](https://pmc.ncbi.nlm.nih.gov/articles/PMC3626462/))
- **Pooled OR for VTE in non-O vs O ≈ 2.09**. Non-O is the most common inherited thrombophilia. ([PMC3626462](https://pmc.ncbi.nlm.nih.gov/articles/PMC3626462/))
- **Coronary artery disease / MI:** the [Reilly et al. 2011 *Lancet* GWAS (PubMed 21239051)](https://pubmed.ncbi.nlm.nih.gov/21239051/) identified the ABO locus as significantly associated with MI *given* underlying coronary atherosclerosis — non-O confers excess MI risk on top of equivalent atherosclerotic burden. The protective allele is the O (glycosyltransferase-deficient) allele.
- The 2008 systematic review by [Wu et al., *J Thromb Haemost*](https://pubmed.ncbi.nlm.nih.gov/17897103/) (often miscited as Vox Sang) confirmed elevated risk of both venous and arterial vascular disease in non-O.

**Type O — slightly elevated risks:**
- **GI ulcers / H. pylori binding.** Type O individuals are more frequently colonized with H. pylori; the bacterial adhesin BabA binds the Le^b antigen carried on the H structure. Meta-analysis confirms higher H. pylori infection in O. ([Nature Sci Rep 2018 — ABO and H. pylori meta-analysis](https://www.nature.com/articles/s41598-018-36006-x))
- **Norovirus susceptibility** is markedly higher in type O (the H/Le^b structure is the viral receptor). Meta-analysis OR ≈ 1.9 for O vs non-O. ([Sharma 2020 — ABO and norovirus susceptibility meta-analysis](https://pubmed.ncbi.nlm.nih.gov/32092482/))
- Bleeding risk in trauma/surgery slightly higher in O (lower VWF). Mechanism is the mirror image of the thrombosis finding.

**Type A — modest cancer risk increases:**
- **Gastric cancer**: OR ≈ 1.11–1.18 vs non-A. ([Wang et al. 2012 PMC3497328 — Meta-analysis ABO and gastric cancer](https://pmc.ncbi.nlm.nih.gov/articles/PMC3497328/))
- **Pancreatic cancer**: OR ≈ 1.23 vs non-A; type O shows ~25% reduction (OR ≈ 0.75). ([Risch et al. 2013 PMC3732019 — Pancreatic cancer ABO meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3732019/))

**COVID-19:**
- [Zietz et al. 2020 *Nature Communications*](https://www.nature.com/articles/s41467-020-19623-x) reported modestly higher SARS-CoV-2 infection odds in type A and lower in type O among RhD+ individuals; effects attenuated as cohorts grew.
- No reproducible association with intubation or death once cohorts were sufficiently large.

**Bottom line for a 20M:** ABO/Rh tells you (a) your transfusion compatibility, (b) a small lifelong shift in VTE/CV vs GI-cancer / hemorrhage / norovirus risk. Effect sizes are modest (OR ~1.1–2 range). Not actionable in isolation, but worth knowing — type A men with strong family history of pancreatic cancer should be more proactive about smoking cessation and abdominal symptoms; type O men should pay attention to bleeding tendency before surgery.

---

## 3. Hemoglobin (Hgb)

### 3.1 What it is

Hemoglobin is the iron-containing tetrameric protein (2 α + 2 β globin chains in adults; HbA = α₂β₂) that fills RBCs and reversibly binds O₂ via four heme groups. Each gram of Hgb carries ~1.34 mL O₂. Reported in g/dL (US) or g/L (WHO; multiply by 10).

### 3.2 Reference range

- **Conventional adult male reference: ~13.5–17.5 g/dL.**
- **WHO 2024** retains the **anemia threshold of 130 g/L (13.0 g/dL) for adult men**; the guideline panel acknowledged data suggesting 13.5 g/dL might be more appropriate but kept 13.0 to avoid driving over-supplementation. ([WHO 2024 — Guideline on haemoglobin cutoffs to define anaemia](https://iris.who.int/bitstream/handle/10665/376196/9789240088542-eng.pdf); [WHO 2024 page](https://www.who.int/publications/i/item/9789240088542))
- Female cutoff: **120 g/L (12.0 g/dL)**. Men run 1–2 g/dL higher than women due to androgen-driven erythropoiesis and absence of menstrual loss.
- **Polycythemia vera diagnostic threshold (WHO 2022): Hgb >16.5 g/dL in men, >16.0 g/dL in women** (one of the major criteria; the others are JAK2 mutation and hypercellular marrow). ([Tefferi & Barbui 2024 — Polycythemia vera 2024 update, Am J Hematol](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27002))

### 3.3 Optimal range for a healthy 20M

**14.0–16.0 g/dL is a reasonable optimal band.** Within the normal range, higher values are not "better" — viscosity rises non-linearly above ~17 g/dL, and population-mortality data show a soft U-shape with worse outcomes at both extremes. The CYTO-PV trial in PV patients showed maintaining Hct <45% (corresponds to Hgb roughly <15 g/dL) cut MACE 4-fold vs Hct 45–50%. ([NEJM 2013 — Cardiovascular Events and Intensity of Treatment in Polycythemia Vera](https://www.nejm.org/doi/full/10.1056/NEJMoa1208500)) That study is in disease context, but it anchors the upper-end reasoning.

### 3.4 What HIGH means

- **Absolute (true) erythrocytosis:**
  - **Primary — polycythemia vera (JAK2 V617F in 95–96% of cases).** Diagnose with EPO (low/suppressed), JAK2 testing, marrow biopsy. ([Tefferi & Barbui 2024](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27002))
  - **Secondary — hypoxia-driven EPO rise:** chronic OSA, COPD, right-to-left cardiac shunts, high altitude (~+1 g/dL Hgb sustained at ~8,000 ft after weeks; [PMC2599997 — Heights and haematology](https://pmc.ncbi.nlm.nih.gov/articles/PMC2599997/)), heavy smoking (CO competes for Hgb → tissue hypoxia → EPO ↑; [PMC5511531 — Smoking and hematological parameters](https://pmc.ncbi.nlm.nih.gov/articles/PMC5511531/)).
  - **Androgens:** physiologic (post-puberty males) and supraphysiologic (TRT, anabolic steroids, SARMs). Testosterone raises EPO and suppresses hepcidin; supraphysiologic doses commonly push Hct >54%, the threshold for thromboembolic concern. ([Bachman et al. 2014 — Testosterone induces erythrocytosis via EPO and suppressed hepcidin](https://pmc.ncbi.nlm.nih.gov/articles/PMC4022090/); [Mullen et al. 2014 — Hematopoietic profile in AAS users](https://onlinelibrary.wiley.com/doi/10.1155/2014/510257))
  - **EPO doping** (ESAs).
  - **Renal cell carcinoma, hepatoma, cerebellar hemangioblastoma** — paraneoplastic EPO.
- **Relative erythrocytosis (Gaisböck syndrome / "stress polycythemia"):** plasma volume contraction from dehydration, diuretics, hypertension, obesity, smoking. Hgb/Hct elevated, RBC mass normal. ([Orphanet — Gaisböck syndrome](https://www.orpha.net/en/disease/detail/90041); [Patient Care Online — workup of elevated Hgb](https://www.patientcareonline.com/view/what-include-workup-elevated-hemoglobin-concentration-and-hematocrit))

### 3.5 What LOW means (anemia)

Classify by MCV (see §6) and reticulocyte response.

- **Microcytic** (MCV <80): iron deficiency (most common in young people — chronic GI loss; in young men consider H. pylori, IBD, occult bleeding), thalassemia trait, anemia of chronic disease (sometimes), lead poisoning, sideroblastic anemia. Mnemonic **TAILS**. ([NCBI — Microcytic Hypochromic Anemia](https://www.ncbi.nlm.nih.gov/books/NBK470252/))
- **Macrocytic** (MCV >100): B12 / folate deficiency (megaloblastic, hypersegmented neutrophils), alcohol (most common real-world cause), hypothyroidism, liver disease, MDS, drug effect (hydroxyurea, methotrexate, AZT, 5-FU), reticulocytosis from recent bleed/hemolysis. ([Cleveland Clinic — Macrocytic Anemia](https://my.clevelandclinic.org/health/diseases/23017-macrocytic-anemia); [Nagao & Hirokawa 2017 — Diagnosis and treatment of macrocytic anemias in adults](https://onlinelibrary.wiley.com/doi/full/10.1002/jgf2.31))
- **Normocytic** (MCV 80–100): blood loss, hemolysis (hereditary spherocytosis, G6PD, sickle cell, AIHA, microangiopathic), anemia of chronic disease, CKD (low EPO), early iron deficiency, marrow infiltration / aplasia. ([Brill 2000 AAFP — Normocytic anemia](https://www.aafp.org/pubs/afp/issues/2000/1115/p2255.html))

In a healthy 20M, Hgb <13.5 with no obvious cause warrants iron studies (ferritin, TSAT) plus reticulocyte count first.

### 3.6 Direction of "better"

Clearly **U-shaped**. Optimal is in the middle of the reference range; both ends are pathological.

---

## 4. Hematocrit (Hct)

### 4.1 What it is

Hct is the volumetric fraction of whole blood occupied by RBCs, expressed as a percent or decimal fraction. On automated CBCs it is *calculated* (Hct = MCV × RBC × 10⁻¹), not spun.

### 4.2 Reference range

- **Adult male: 40–52%.** Female: 36–46%. ([NCBI — Normal and Abnormal CBC](https://www.ncbi.nlm.nih.gov/books/NBK604207/))
- **WHO 2022 PV criteria: Hct >49% (men) or >48% (women).** ([Tefferi & Barbui 2024](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27002))
- **Hct >54% — phlebotomy-considered threshold for absolute erythrocytosis** (testosterone-induced and otherwise), per Endocrine Society and PV management practice.
- In PV, **target Hct <45% in men** based on the [CYTO-PV trial (NEJM 2013)](https://www.nejm.org/doi/full/10.1056/NEJMoa1208500): 4-fold reduction in CV death + major thrombosis vs Hct 45–50%.

### 4.3 Optimal for a healthy 20M

**42–48%.** Tracks Hgb. The same U-shape applies; viscosity rises sharply above ~50%, and shear-stress / endothelial concerns above 52–54%.

### 4.4 High / Low / Direction of "better"

Same differentials as Hgb (§3). Hct and Hgb almost always move in lockstep; *discordance* is the diagnostically useful signal:
- High Hct with normal Hgb → may be lab artifact, very microcytic cells (thalassemia), or in vivo hemolysis with cell debris.
- Hct/Hgb ratio normally ~3:1.

U-shaped overall.

---

## 5. Red Blood Cell Count (RBC)

### 5.1 What it is

The absolute number of RBCs per µL (or × 10¹²/L). Counted by Coulter aperture or flow cytometry.

### 5.2 Reference range

- **Adult male: 4.5–5.9 × 10⁶/µL** (some labs 4.6–6.2). ([NCBI — Normal/Abnormal CBC](https://www.ncbi.nlm.nih.gov/books/NBK604207/); [Onedaytests — RBC reference ranges](https://onedaytests.com/pages/red-blood-cell-count-rbc-description-and-reference-ranges))
- Female: 4.0–5.2 × 10⁶/µL.

### 5.3 Optimal for a healthy 20M

**4.7–5.4 × 10⁶/µL.** RBC count by itself is rarely the headline finding — it's the *combination* with MCV and Hgb that flags pathology.

### 5.4 Key discordance pattern: thalassemia trait

In **β-thalassemia minor / α-thal trait**: RBC count is **HIGH** (often >5.5 × 10⁶/µL) while Hgb is normal-low and MCV is markedly low (often <75). The marrow makes lots of small, hemoglobin-poor cells.

In **iron-deficiency anemia**: RBC count is usually low or low-normal, MCV is low, Hgb is low. Marrow is iron-starved, can't crank out cells.

This drives the **Mentzer index** = MCV / RBC:
- **<13 → suggests thalassemia trait.**
- **>13 → suggests iron deficiency.**
- Sensitivity ~98.7%, specificity ~82.3% for β-thal trait detection. ([Wikipedia — Mentzer index](https://en.wikipedia.org/wiki/Mentzer_index); [Vehapoglu 2014 — Indices for differentiating BTT and IDA](https://onlinelibrary.wiley.com/doi/10.1155/2014/576738); [Frontiers Med 2024 — Mentzer index in Saudi children](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1361805/full))

### 5.5 High / Low

- **High RBC:** PV, secondary erythrocytosis (hypoxia, EPO, androgens), thalassemia trait (with low MCV), dehydration.
- **Low RBC:** all causes of anemia (see §3); also overhydration and (rarely) marrow failure.

### 5.6 Direction of "better"

U-shaped within the population; for an individual, isolated RBC is not actionable — interpret with MCV, Hgb, RDW.

---

## 6. Mean Corpuscular Volume (MCV)

### 6.1 What it is

The average volume of a single RBC, in **femtoliters (fL = 10⁻¹⁵ L)**. Directly measured on impedance / VCS analyzers (the height of each pulse encodes the volume of that single cell).

### 6.2 Reference range

- **Adult: 80–100 fL** (no meaningful sex difference in adults). ([NCBI — Mean Corpuscular Volume StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK545275/); [Medscape — MCV reference range](https://emedicine.medscape.com/article/2085770-overview))

### 6.3 Optimal for a healthy 20M

**87–92 fL.** A 2015 study of patients undergoing coronary angiography ([PubMed 26630695 — MCV and all-cause/liver cancer mortality](https://pubmed.ncbi.nlm.nih.gov/26630695/)) found mortality lowest near MCV ~86–87 fL and rising toward both ends. Population studies show all-cause mortality U-curves for MCV with the upper-quartile (>~94 fL in men) carrying clearly elevated mortality. ([PMC9189337 — Age-related MCV changes](https://pmc.ncbi.nlm.nih.gov/articles/PMC9189337/)) MCV climbs ~1–3 fL per decade with age even in non-anemic adults; a 20M who is at 95 fL is genuinely high for his age.

### 6.4 LOW (microcytic, MCV <80)

- **Iron deficiency** — most common; check ferritin (specific if <30 µg/L), TSAT.
- **Thalassemia trait** (use Mentzer index; confirm with Hgb electrophoresis).
- **Anemia of chronic disease** (microcytic in only ~25% of cases — usually normocytic).
- **Lead poisoning** — adds basophilic stippling on smear; lead inhibits ferrochelatase. ([NCBI — Lead Poisoning PMC5528905](https://pmc.ncbi.nlm.nih.gov/articles/PMC5528905/))
- **Sideroblastic anemia** — congenital (X-linked ALAS2) or acquired (MDS, alcohol, isoniazid, copper deficiency, lead). Marrow shows ring sideroblasts. ([NCBI — Sideroblastic Anemia](https://www.ncbi.nlm.nih.gov/books/NBK538287/))

### 6.5 HIGH (macrocytic, MCV >100)

Subclassified into megaloblastic vs nonmegaloblastic:

**Megaloblastic (impaired DNA synthesis → hypersegmented neutrophils, oval macrocytes):**
- **B12 deficiency** — pernicious anemia, dietary (strict vegan), terminal ileal disease, metformin (mild), PPIs (mild).
- **Folate deficiency** — alcohol, methotrexate, trimethoprim, phenytoin.

**Nonmegaloblastic:**
- **Alcohol** — most common real-world cause of mild macrocytosis in adults; direct toxicity to erythroid precursors, plus folate deficiency, plus liver disease compound.
- **Hypothyroidism.** ([Nagao & Hirokawa 2017](https://onlinelibrary.wiley.com/doi/full/10.1002/jgf2.31))
- **Liver disease** (membrane lipid abnormalities → target cells, mild macrocytosis).
- **Reticulocytosis** — recent acute bleed or hemolysis; reticulocytes are ~20% larger than mature RBCs.
- **Myelodysplastic syndrome** — typically older patients but can occur in young people.
- **Drugs:** hydroxyurea (predictable, marker of compliance in sickle cell), methotrexate, zidovudine (AZT), 5-fluorouracil, capecitabine, azathioprine.

### 6.6 Direction of "better"

Clear **U-shape**. Don't chase MCV outside reference range in either direction.

---

## 7. Mean Corpuscular Hemoglobin (MCH)

### 7.1 What it is

Average mass of hemoglobin per RBC, in **picograms (pg)**. Calculated: MCH = (Hgb × 10) / RBC.

### 7.2 Reference range

- **27–33 pg** (no meaningful sex difference). ([Cleveland Clinic — MCH](https://my.clevelandclinic.org/health/diagnostics/mch-blood-test); [Medscape — MCH/MCHC reference](https://emedicine.medscape.com/article/2054497-overview))

### 7.3 Optimal for a healthy 20M

**28–32 pg**, in tandem with MCV in the 87–92 range.

### 7.4 High / Low

MCH **tracks MCV very closely** because larger cells hold more Hgb in absolute terms. So:
- **Low MCH (hypochromic)** ≈ same differential as low MCV: iron deficiency, thalassemia, lead, sideroblastic, ACD.
- **High MCH** ≈ macrocytic causes: B12/folate deficiency, alcohol, liver disease, hypothyroidism, MDS.

MCH adds little independent information when MCV is interpreted; it occasionally flags subtle hypochromia before MCV drops below 80 in early iron deficiency.

### 7.5 Direction of "better"

U-shaped; track MCV.

---

## 8. Mean Corpuscular Hemoglobin Concentration (MCHC)

### 8.1 What it is

Hemoglobin concentration **per volume of packed cells**: MCHC = Hgb / Hct (g/dL). Unlike MCH which is mass per cell, MCHC is concentration density. It is bounded — Hgb cannot dissolve indefinitely in cytoplasm — so MCHC is the most "rigid" of the indices.

### 8.2 Reference range

- **33–36 g/dL** (some labs 32–36). ([Medscape — MCH/MCHC](https://emedicine.medscape.com/article/2054497-overview))

### 8.3 Optimal for a healthy 20M

**33–35 g/dL**.

### 8.4 What HIGH means (>36)

- **Hereditary spherocytosis** — RBC membrane defect (ankyrin, spectrin, band 3, protein 4.2 mutations); cells lose surface area without losing Hgb → mildly dehydrated, dense, spherical cells with high MCHC (often 36–38). ([NCBI — Hereditary Spherocytosis StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK539797/); [Wu et al. 2021 — Diagnostic protocol for HS](https://onlinelibrary.wiley.com/doi/full/10.1002/jcla.24034))
- **Cold agglutinins / autoimmune hemolytic anemia (cold type)** — RBCs clump in the analyzer's cooler aliquot, get counted as fewer-but-larger cells → **artifactually elevated MCHC** (often >40, a giveaway). Repeat the sample warmed to 37 °C.
- **Severe burns** — RBC fragmentation produces dense schistocytes.
- **Lipemia, hemolysis in tube** — interfere with the spectrophotometric Hgb measurement and inflate MCHC.

A **MCHC reproducibly >36** in a young person without obvious confound deserves a peripheral smear and EMA-binding test for HS.

### 8.5 What LOW means (<32)

- **Iron deficiency anemia** (advanced) — hypochromia.
- Thalassemias.
- Sideroblastic anemia.

### 8.6 Direction of "better"

U-shaped but the curve is narrow — most healthy people sit 33–35.

---

## 9. Red Cell Distribution Width (RDW)

### 9.1 What it is

The **coefficient of variation of RBC volume** — a measure of anisocytosis (cell-size variability). RDW-CV = (SD / MCV) × 100, expressed as a percent. Some analyzers also report RDW-SD in fL. ([Wikipedia — RDW](https://en.wikipedia.org/wiki/Red_blood_cell_distribution_width))

### 9.2 Reference range

- **11.5–14.5%** (RDW-CV) is the classic conventional range. ([Cleveland Clinic — RDW](https://my.clevelandclinic.org/health/diagnostics/22980-rdw-blood-test); [MedlinePlus — RDW](https://medlineplus.gov/lab-tests/rdw-red-cell-distribution-width/))
- Some modern analyzers and modern reference cohorts cite 11.5–15.4%.

### 9.3 Optimal for a healthy 20M

**<13%** is associated with the lowest mortality risk in cohort studies — and is what most healthy young people sit at. Patel 2009 [PMC2765040](https://pmc.ncbi.nlm.nih.gov/articles/PMC2765040/) found a stepwise mortality gradient with each percentage-point rise.

### 9.4 What HIGH means

RDW rises any time the marrow is producing RBCs of *mixed* sizes — so it's a sensitive non-specific flag.

- **Early or evolving iron deficiency** — small new cells alongside older normocytes; RDW rises before MCV falls below 80.
- **Mixed deficiency** (iron + B12, iron + folate) — small cells + large cells in the same sample.
- **Recent transfusion** — donor cells added to host cells of different size.
- **Hemolysis with brisk reticulocytosis** — reticulocytes are larger; in a marrow that is also pumping out younger cells, anisocytosis ↑.
- **Myelodysplastic syndromes.**
- **Thalassemia trait** — usually has *normal* RDW (uniformly small cells), distinguishing it from iron deficiency. Combined with the Mentzer index, this is a useful piece of evidence.

### 9.5 RDW as a mortality predictor — surprisingly strong

Three landmark studies established RDW as an independent predictor of all-cause mortality in apparently disparate populations:

- **[Felker et al. 2007, *J Am Coll Cardiol*](https://www.jacc.org/doi/10.1016/j.jacc.2007.02.067)** — CHARM heart-failure cohort + Duke databank; RDW was the strongest CBC-derived predictor of mortality and hospitalization, even after adjusting for hemoglobin.
- **[Patel et al. 2009, *Arch Intern Med*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2765040/)** — NHANES III middle-aged + older adults; **each 1% rise in RDW conferred a 22% increase in all-cause mortality** in adjusted models.
- **[Tonelli et al. 2008, *Circulation*](https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.107.727545)** — coronary disease cohort; higher RDW predicted death and CV events independent of hemoglobin and other RBC indices.

RDW also predicts mortality in pneumonia, sepsis, acute coronary syndrome, stroke, and CKD. The mechanism is not fully understood — current best hypothesis is that **inflammation, oxidative stress, and ineffective erythropoiesis** all enlarge size variability, and RDW is essentially a sensor for these chronic stresses. ([CFR Journal — RDW as biomarker of red cell dysfunction](https://www.cfrjournal.com/articles/red-blood-cell-distribution-width-biomarker-red-cell-dysfunction-associated-inflammation); [PMC6861793 — Role of RDW in CV risk](https://pmc.ncbi.nlm.nih.gov/articles/PMC6861793/))

For a healthy 20M, **a normal RDW is reassuring; an isolated RDW slightly above range with otherwise normal CBC is most often early iron deficiency** — recheck with ferritin.

### 9.6 What LOW means

Generally not clinically meaningful. ([Cleveland Clinic — RDW](https://my.clevelandclinic.org/health/diagnostics/22980-rdw-blood-test))

### 9.7 Direction of "better"

**Monotonic — lower is better** (within the normal range). Unlike most CBC indices, low RDW carries no demonstrated downside.

---

## 10. Platelet Count

### 10.1 What it is

The number of platelets per µL (or × 10⁹/L). Platelets are anucleate cytoplasmic fragments of megakaryocytes; they live ~7–10 days, primarily mediate primary hemostasis (adhesion via GPIb-VWF, aggregation via GPIIb/IIIa-fibrinogen) and contribute to thrombin generation, inflammation, and tissue repair.

### 10.2 Reference range

- **150,000–400,000 / µL** (150–400 × 10⁹/L) is the classic range. ([Cleveland Clinic — Platelet count](https://my.clevelandclinic.org/health/diagnostics/21782-platelet-count))
- Sex difference: women run ~10% higher than men after age 14. ([Haematologica — Platelet count and aging](https://haematologica.org/article/view/7058))
- Personalized intervals for men 15–64: ~120–369 × 10⁹/L. ([PMC4800691 — Personalized platelet reference intervals](https://pmc.ncbi.nlm.nih.gov/articles/PMC4800691/))

### 10.3 Optimal for a healthy 20M

**200,000–300,000 / µL.** Both ends of the population reference range carry marginal risk.

### 10.4 HIGH (thrombocytosis, >450,000)

**Reactive (≈85% of cases):**
- **Iron deficiency** (very common — frequently missed; resolves with iron repletion).
- Acute infection / inflammation (post-viral, post-surgical, post-trauma).
- Tissue injury, burns.
- Post-splenectomy or hyposplenism (e.g., sickle cell).
- Malignancy (lung, GI, breast, ovary, lymphoma, Hodgkin).
- Rebound after marrow recovery.

**Primary (myeloproliferative neoplasm):**
- **Essential thrombocythemia (ET):** WHO criterion ≥450 × 10⁹/L plus driver mutation. JAK2 V617F in ~62%, CALR in ~27%, MPL in ~3%; ~8% are "triple-negative." Median survival ~18 years; >35 years in younger patients. ([Tefferi & Barbui 2024 — ET update, Am J Hematol](https://onlinelibrary.wiley.com/doi/10.1002/ajh.27216))
- Polycythemia vera, primary myelofibrosis (early), CML — also drive thrombocytosis.

A persistent platelet count >450k in an otherwise healthy 20M warrants ferritin first (rule out iron deficiency), then JAK2 V617F testing if reactive cause not found.

### 10.5 LOW (thrombocytopenia, <150,000)

Differential is dense; group by mechanism:

**Decreased production:**
- Marrow failure / aplastic anemia, MDS, leukemia, marrow infiltration (lymphoma, mets).
- Chemotherapy, radiation.
- Severe B12 / folate deficiency.
- Viral suppression (CMV, EBV, hepatitis C, HIV, parvovirus B19, dengue).
- Alcohol.

**Increased destruction / consumption:**
- **Immune thrombocytopenia (ITP)** — autoantibodies to GPIIb/IIIa.
- **Drug-induced (DITP)** — quinine, vancomycin, heparin, sulfonamides, GPIIb/IIIa inhibitors. Onset 5–10 days post-exposure. ([Aster & Bougie 2007 — Drug-induced ITP](https://pmc.ncbi.nlm.nih.gov/articles/PMC4413903/))
- **HIT (heparin-induced thrombocytopenia)** — IgG vs PF4-heparin complexes; paradoxically prothrombotic.
- **TTP** — ADAMTS13 deficiency; pentad of MAHA + thrombocytopenia + neuro + renal + fever (rarely complete).
- **DIC.**
- **APS, SLE, antiphospholipid syndrome.**

**Sequestration:**
- Splenomegaly (cirrhosis, lymphoma, infiltrative).

**Pseudothrombocytopenia (artifact):**
- **EDTA-dependent agglutinin** causes platelet clumping in vitro → analyzer counts clumps as single big "platelets" or excludes them entirely → falsely low count. **Repeat in citrate or heparin tube.** ([NCBI — Thrombocytopenia](https://www.ncbi.nlm.nih.gov/books/NBK542208/)) Always rule out before any workup of an isolated low platelet count in an asymptomatic patient.

### 10.6 Bleeding-risk thresholds

- **<50,000 / µL:** bleeding risk on injury or invasive procedure rises; many procedures defer until ≥50k.
- **<20,000 / µL:** spontaneous mucocutaneous bleeding may occur.
- **<10,000 / µL:** **spontaneous bleeding emergency** — prophylactic platelet transfusion threshold in stable hem-onc patients. ([PMC9988645 — Platelet thresholds before invasive procedures](https://pmc.ncbi.nlm.nih.gov/articles/PMC9988645/); [ASH Education Program 2020 — How well do platelets prevent bleeding?](https://ashpublications.org/hematology/article/2020/1/518/474298/))

### 10.7 Direction of "better"

**U-shaped.** The mid-200s/300s range minimizes both bleeding risk (low end) and thrombosis/CV risk (high end, including the often-overlooked finding that high-normal platelets associate with cardiovascular events).

---

## 11. Mean Platelet Volume (MPV)

### 11.1 What it is

Average volume of a platelet, in fL. Younger platelets are larger; MPV is essentially a "platelet age" / turnover marker analogous to reticulocyte index for RBCs.

### 11.2 Reference range

- **Typically 7.5–11.5 fL**, sometimes 7–12 fL depending on the analyzer. ([Cleveland Clinic — MPV blood test](https://my.clevelandclinic.org/health/diagnostics/23572-mpv-blood-test))
- **MPV is not standardized between manufacturers** — a Sysmex MPV cannot be directly compared with a Beckman MPV. ([PMC6517618 — Sex-divided MPV reference intervals on Sysmex XN-10](https://pmc.ncbi.nlm.nih.gov/articles/PMC6517618/))
- EDTA causes progressive MPV swelling over hours; results are most accurate when the sample is run within 30–120 min.

### 11.3 Optimal for a healthy 20M

Mid-range, **~8–10 fL** depending on analyzer. Optimal value is less established than for other indices.

### 11.4 What HIGH means

- **Rapid platelet turnover** with peripheral destruction — ITP, TTP, DIC, hypersplenism. Platelet count is low or low-normal; MPV ↑ because the marrow is releasing larger young platelets.
- **MPN (ET, PV).**
- **Inflammation, sepsis** — relationship is complex; can go either way.
- **Cardiovascular risk:** [Chu et al. 2010 *J Thromb Haemost*](https://pubmed.ncbi.nlm.nih.gov/19691485/) meta-analysis of 16 cross-sectional studies (n=2,809) found MPV is **0.92 fL higher** in patients with AMI than controls; high MPV also predicts post-MI mortality and post-PCI restenosis. [Bath et al. 2004 *Stroke*](https://www.ahajournals.org/doi/10.1161/01.str.0000116105.26237.ec) found MPV was an independent predictor of recurrent stroke in patients with prior cerebrovascular disease. The mechanism: larger platelets are denser in granules and prothrombotic enzymes (more thromboxane, more GPIIb/IIIa), so they are more reactive.
- High MPV with normal platelet count is a soft cardiometabolic risk signal — worth noting, not a stand-alone diagnostic.

### 11.5 What LOW means

- Marrow suppression / failure (chemotherapy, aplastic anemia) — uniform or smaller-than-normal platelets, reflecting suppressed thrombopoiesis.
- Wiskott-Aldrich syndrome (congenitally small platelets, X-linked, presents in childhood).
- Some cases of chronic ITP late in disease (paradoxical).
- Reactive thrombocytosis (iron deficiency-driven) often shows low MPV with high count — a useful pattern.

### 11.6 Direction of "better"

**Mildly U-shaped**, but with caveats: MPV is informative mostly *in combination* with the platelet count and the clinical context. Isolated MPV is rarely actionable.

---

## 12. Cross-cutting clinical patterns

### 12.1 Anemia workup framework (MCV-based)

For any Hgb below the reference cutoff:

1. **Classify by MCV** (microcytic / normocytic / macrocytic).
2. **Reticulocyte count** (corrected for Hct): >2% = hyperproliferative (hemolysis or recent bleed); <2% = hypoproliferative (deficiency, marrow problem, ACD/CKD).
3. **Microcytic** → ferritin (most specific iron deficiency marker; <30 µg/L diagnostic), TSAT, hemoglobin electrophoresis if Mentzer <13, lead level if exposure history.
4. **Normocytic** → reticulocyte count splits the workup; if low retic and chronic disease present, often ACD; if high retic, look for hemolysis (LDH ↑, haptoglobin ↓, indirect bili ↑, smear, DAT) or bleed.
5. **Macrocytic** → B12 + folate first, TSH, LFTs/alcohol history; smear for hypersegmented neutrophils (megaloblastic) vs round macrocytes (liver/alcohol) vs oval macrocytes (MDS).

([Merck Manual — Evaluation of Anemia](https://www.merckmanuals.com/professional/hematology-and-oncology/approach-to-the-patient-with-anemia/evaluation-of-anemia))

### 12.2 Thalassemia vs iron deficiency

Both microcytic. Distinguishing features:

| Feature | Iron deficiency | β-thalassemia trait |
|---|---|---|
| RBC count | low/normal | **HIGH** (>5.5) |
| MCV | low | low |
| **Mentzer (MCV/RBC)** | **>13** | **<13** |
| RDW | high | normal |
| Ferritin | low (<30) | normal/high |
| Hgb electrophoresis | normal | HbA₂ ↑ (>3.5%) |

Mentzer index sensitivity ~98.7%, specificity ~82.3% for detecting β-TT. ([Vehapoglu 2014](https://onlinelibrary.wiley.com/doi/10.1155/2014/576738))

### 12.3 Athlete's pseudoanemia

Endurance training expands plasma volume by 9–25% (300–700 mL) within days, lowering Hgb/Hct by **dilution** even though absolute RBC mass and oxygen-carrying capacity are normal or *increased*. Hemoglobin in trained endurance athletes can run 0.5–1.0 g/dL below a sedentary reference, and this is **adaptive, not pathological**. ([PMC8472039 — Anemia in sports narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8472039/); [PubMed 1798375 — Blood volume adaptation to endurance training](https://pubmed.ncbi.nlm.nih.gov/1798375/)) For a 20M who runs significant volume, Hgb 13.5–14 g/dL is normal — *do not* interpret as iron deficiency without ferritin.

### 12.4 Smoking effect

Heavy smoking (>10 cig/day) elevates Hgb, Hct, and RBC by 0.5–1 g/dL via two compounding mechanisms: (a) chronic CO binding to Hgb (carboxyhemoglobin) impairs O₂ delivery, EPO rises; (b) plasma volume contraction. Cessation normalizes values within ~3 months. ([PMC5511531 — Smoking effects on hematological parameters](https://pmc.ncbi.nlm.nih.gov/articles/PMC5511531/); [PMC12048899 — Smoking cessation and hematological parameters](https://pmc.ncbi.nlm.nih.gov/articles/PMC12048899/))

### 12.5 Altitude

Above ~5,000 ft, Hgb rises — first via plasma-volume contraction within days, then via genuine erythropoiesis (EPO ↑) within weeks. **Roughly +1 g/dL Hgb sustained at 8,000 ft after several weeks.** ([PMC2599997 — Heights and haematology](https://pmc.ncbi.nlm.nih.gov/articles/PMC2599997/); [AltitudeOmics PLOS One — Hemoglobin mass at 5260 m](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0108788))

### 12.6 Anabolic / androgenic steroids

In a 20M, **unexplained Hgb >17 g/dL or Hct >50%** in a fit-looking individual should raise suspicion of exogenous androgen use; supraphysiological testosterone reliably drives erythrocytosis via EPO ↑ and hepcidin suppression. Erythrocytosis ≥54% Hct is the prescribing-society threshold for therapeutic dose-reduction or phlebotomy on TRT. ([Bachman et al. 2014 — Testosterone induces erythrocytosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC4022090/); [Heiland et al. 2023 — Supraphysiological AAS doses on EPO](https://pubmed.ncbi.nlm.nih.gov/36730044/))

---

## 13. Confounders summary table

| Marker | Hydration ↓ | Recent exercise | Time of day (AM higher) | Altitude (high) | Smoking | Endurance training | AAS / TRT |
|---|---|---|---|---|---|---|---|
| Hgb | ↑ (hemoconcentration) | ↑ briefly (~+0.5 g/dL, normalizes ≤2 h) | Higher in AM (~+0.5) | ↑ chronically (~+1 g/dL at 8k ft) | ↑ | ↓ (dilutional pseudo) | ↑↑ |
| Hct | ↑ | ↑ briefly | Higher in AM | ↑ | ↑ | ↓ | ↑↑ |
| RBC | ↑ | ↑ briefly | Higher in AM | ↑ | ↑ | ↔ or ↓ | ↑ |
| MCV | ↔ | ↔ | ↔ | ↔ | minor ↑ | ↔ | ↔ |
| MCH | ↔ | ↔ | ↔ | ↔ | ↔ | ↔ | ↔ |
| MCHC | ↔ | ↔ | ↔ | ↔ | ↔ | ↔ | ↔ |
| RDW | ↔ | ↔ | ↔ | ↔ | ↔ | ↔ | possible ↑ early |
| Platelets | ↔ | ↑ briefly (splenic release) | minor variation | ↔ | minor ↑ | ↔ | ↔ |
| MPV | ↔ | ↑ briefly | ↑ during day with EDTA storage time (artifact) | ↔ | ↔ | ↔ | ↔ |

(Diurnal variation of Hgb/Hct from [Sennels et al. 2011 PubMed 21988588](https://pubmed.ncbi.nlm.nih.gov/21988588/) and [Feriel et al. 2021 — IJLH circadian variation in hematology](https://onlinelibrary.wiley.com/doi/full/10.1111/ijlh.13590); exercise effects from [PMC9803156 — Hemoconcentration in canoeists](https://pmc.ncbi.nlm.nih.gov/articles/PMC9803156/).)

**Practical takeaway for interpreting a draw:**
- Standardize draw conditions (morning, fasted, no exercise <12 h, hydrated).
- A single borderline result is rarely a diagnosis — re-test before chasing.
- Discordances between markers (e.g., high RBC with normal Hgb; high MCHC alone; low platelets with normal MPV in a healthy person) are often artifactual — repeat first.

---

## 14. References

### Primary / landmark studies

1. Felker GM, Allen LA, Pocock SJ, et al. Red cell distribution width as a novel prognostic marker in heart failure. *J Am Coll Cardiol*. 2007. https://www.jacc.org/doi/10.1016/j.jacc.2007.02.067
2. Patel KV, Ferrucci L, Ershler WB, Longo DL, Guralnik JM. Red blood cell distribution width and the risk of death in middle-aged and older adults. *Arch Intern Med*. 2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC2765040/
3. Tonelli M, Sacks F, Arnold M, Moye L, Davis B, Pfeffer M. Relation between red blood cell distribution width and cardiovascular event rate in people with coronary disease. *Circulation*. 2008. https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.107.727545
4. Reilly MP, Li M, He J, et al. Identification of ADAMTS7 as a novel locus for coronary atherosclerosis and association of ABO with myocardial infarction in the presence of coronary atherosclerosis: two GWASs. *Lancet*. 2011. https://pubmed.ncbi.nlm.nih.gov/21239051/
5. Wu O, Bayoumi N, Vickers MA, Clark P. ABO(H) blood groups and vascular disease: a systematic review and meta-analysis. *J Thromb Haemost*. 2008. https://pubmed.ncbi.nlm.nih.gov/17897103/
6. Franchini M, Lippi G. The intriguing relationship between the ABO blood group, cardiovascular disease, and cancer. *BMC Med*. 2015. https://link.springer.com/article/10.1186/1477-9560-5-14 (and Franchini 2012 *Crit Rev Clin Lab Sci*)
7. Zietz M, Zucker J, Tatonetti NP. Associations between blood type and COVID-19 infection, intubation, and death. *Nat Commun*. 2020. https://www.nature.com/articles/s41467-020-19623-x
8. Marchioli R, Finazzi G, Specchia G, et al. Cardiovascular events and intensity of treatment in polycythemia vera (CYTO-PV). *N Engl J Med*. 2013. https://www.nejm.org/doi/full/10.1056/NEJMoa1208500
9. Tefferi A, Barbui T. Polycythemia vera: 2024 update on diagnosis, risk-stratification, and management. *Am J Hematol*. 2024. https://onlinelibrary.wiley.com/doi/10.1002/ajh.27002
10. Tefferi A, Vannucchi AM, Barbui T. Essential thrombocythemia: 2024 update on diagnosis, risk stratification, and management. *Am J Hematol*. 2024. https://onlinelibrary.wiley.com/doi/10.1002/ajh.27216
11. Chu SG, Becker RC, Berger PB, et al. Mean platelet volume as a predictor of cardiovascular risk: a systematic review and meta-analysis. *J Thromb Haemost*. 2010. https://pubmed.ncbi.nlm.nih.gov/19691485/
12. Bath P, Algert C, Chapman N, Neal B. Association of mean platelet volume with risk of stroke. *Stroke*. 2004. https://www.ahajournals.org/doi/10.1161/01.str.0000116105.26237.ec
13. Bachman E, Travison TG, Basaria S, et al. Testosterone induces erythrocytosis via increased erythropoietin and suppressed hepcidin. *J Clin Endocrinol Metab*. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4022090/

### Guidelines / consensus

14. World Health Organization. Guideline on haemoglobin cutoffs to define anaemia in individuals and populations. WHO 2024. https://www.who.int/publications/i/item/9789240088542 (PDF: https://iris.who.int/bitstream/handle/10665/376196/9789240088542-eng.pdf)
15. NCBI Bookshelf. The ABO blood group. https://www.ncbi.nlm.nih.gov/books/NBK2267/
16. NCBI Bookshelf. Hemolytic disease of the newborn (Rh disease). https://www.ncbi.nlm.nih.gov/books/NBK2266/

### Reviews / textbook chapters

17. Wikipedia — Mentzer index. https://en.wikipedia.org/wiki/Mentzer_index
18. Vehapoglu A, Ozgurhan G, Demir AD, et al. Hematological indices for differential diagnosis of beta thalassemia trait and iron deficiency anemia. *Anemia*. 2014. https://onlinelibrary.wiley.com/doi/10.1155/2014/576738
19. Frontiers in Medicine 2024 — Diagnostic test performance of the Mentzer index in evaluating Saudi children with microcytosis. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1361805/full
20. Nagao T, Hirokawa M. Diagnosis and treatment of macrocytic anemias in adults. *J Gen Fam Med*. 2017. https://onlinelibrary.wiley.com/doi/full/10.1002/jgf2.31
21. Wu Y, Liao Y, Xu G. Diagnostic protocol for hereditary spherocytosis — 2021 update. *J Clin Lab Anal*. 2021. https://onlinelibrary.wiley.com/doi/full/10.1002/jcla.24034
22. Brill JR, Baumgardner DJ. Normocytic anemia. *Am Fam Physician*. 2000. https://www.aafp.org/pubs/afp/issues/2000/1115/p2255.html
23. Merck Manual — Evaluation of Anemia. https://www.merckmanuals.com/professional/hematology-and-oncology/approach-to-the-patient-with-anemia/evaluation-of-anemia
24. Mullen JE, Thörngren JO, Schulze JJ, et al. Perturbation of the hematopoietic profile by anabolic androgenic steroids. *J Hormones*. 2014. https://onlinelibrary.wiley.com/doi/10.1155/2014/510257
25. Mairbäurl H. Heights and haematology: the story of haemoglobin at altitude. *Br J Haematol*. 2008. https://pmc.ncbi.nlm.nih.gov/articles/PMC2599997/
26. Anemia in sports — narrative review. *J Clin Med* 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8472039/
27. Smoking and hematological parameters. *J Clin Diagn Res* 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5511531/
28. Feriel J, Tchipeva D, Depasse F. Effects of circadian variation, lifestyle and environment on hematological parameters: a narrative review. *Int J Lab Hematol*. 2021. https://onlinelibrary.wiley.com/doi/full/10.1111/ijlh.13590
29. Wang Z, Liu L, Ji J, et al. ABO blood group system and gastric cancer: a case-control study and meta-analysis. *Int J Mol Sci*. 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3497328/
30. Risch HA, Lu L, Wang J, et al. ABO blood group and risk of pancreatic cancer: a study in Shanghai and meta-analysis. *Am J Epidemiol*. 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3732019/
31. Sharma V, Chaudhry D, Kaushik S. ABO blood group-associated susceptibility to norovirus infection: a systematic review and meta-analysis. *Infect Genet Evol*. 2020. https://pubmed.ncbi.nlm.nih.gov/32092482/
32. Reid R, et al. Association between ABO blood groups and *H. pylori* infection: a meta-analysis. *Sci Rep*. 2018. https://www.nature.com/articles/s41598-018-36006-x
33. Aster RH, Bougie DW. Drug-induced immune thrombocytopenia. *N Engl J Med* / review. https://pmc.ncbi.nlm.nih.gov/articles/PMC4413903/

### Reference range / lab sources

34. NCBI StatPearls — Normal and Abnormal Complete Blood Count. https://www.ncbi.nlm.nih.gov/books/NBK604207/
35. NCBI StatPearls — Mean Corpuscular Volume. https://www.ncbi.nlm.nih.gov/books/NBK545275/
36. NCBI StatPearls — Microcytic Hypochromic Anemia. https://www.ncbi.nlm.nih.gov/books/NBK470252/
37. NCBI StatPearls — Sideroblastic Anemia. https://www.ncbi.nlm.nih.gov/books/NBK538287/
38. NCBI StatPearls — Hereditary Spherocytosis. https://www.ncbi.nlm.nih.gov/books/NBK539797/
39. NCBI StatPearls — Thrombocytopenia. https://www.ncbi.nlm.nih.gov/books/NBK542208/
40. NCBI StatPearls — Essential Thrombocytosis. https://www.ncbi.nlm.nih.gov/books/NBK539709/
41. Cleveland Clinic — Platelet Count. https://my.clevelandclinic.org/health/diagnostics/21782-platelet-count
42. Cleveland Clinic — RDW Blood Test. https://my.clevelandclinic.org/health/diagnostics/22980-rdw-blood-test
43. Cleveland Clinic — MPV Blood Test. https://my.clevelandclinic.org/health/diagnostics/23572-mpv-blood-test
44. Cleveland Clinic — MCH. https://my.clevelandclinic.org/health/diagnostics/mch-blood-test
45. Cleveland Clinic — Macrocytic Anemia. https://my.clevelandclinic.org/health/diseases/23017-macrocytic-anemia
46. Stanford Blood Center — Blood Types. https://stanfordbloodcenter.org/donate-blood/blood-donation-facts/blood-types/
47. Statista — US blood type distribution. https://www.statista.com/statistics/1112664/blood-type-distribution-us/
48. Medscape — MCV reference range. https://emedicine.medscape.com/article/2085770-overview
49. Medscape — MCH/MCHC reference range. https://emedicine.medscape.com/article/2054497-overview
50. Wikipedia — RDW. https://en.wikipedia.org/wiki/Red_blood_cell_distribution_width
51. Bioscience Pakistan — Principles of automated hematology analyzer (Coulter principle). https://www.bioscience.com.pk/en/topics/hematology/principles-of-working-of-automated-hemotology-analyzer
52. Wikipedia — Hematology analyzer. https://en.wikipedia.org/wiki/Hematology_analyzer
53. PMC4800691 — Personalized reference intervals for platelet count. https://pmc.ncbi.nlm.nih.gov/articles/PMC4800691/
54. PMC9988645 — Minimum platelet count threshold before invasive procedures. https://pmc.ncbi.nlm.nih.gov/articles/PMC9988645/
55. ASH Education 2020 — How well do platelets prevent bleeding? https://ashpublications.org/hematology/article/2020/1/518/474298/
56. PMC6517618 — Sex-divided MPV reference intervals (Sysmex XN-10). https://pmc.ncbi.nlm.nih.gov/articles/PMC6517618/
57. ASH *Blood* 2020 — The relationship between ABO blood group, von Willebrand factor, and primary hemostasis. https://ashpublications.org/blood/article/136/25/2864/461790/
58. PMC3626462 — Non-O blood group as VTE risk factor. https://pmc.ncbi.nlm.nih.gov/articles/PMC3626462/
59. Orphanet — Gaisböck syndrome. https://www.orpha.net/en/disease/detail/90041
60. AltitudeOmics — Rapid hemoglobin mass alterations with acclimatization to 5260 m. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0108788
61. Heiland CE, et al. Supraphysiological AAS doses impact EPO and blood parameters. *Drug Test Anal*. 2023. https://pubmed.ncbi.nlm.nih.gov/36730044/
62. PMC9803156 — Exercise-related hemoconcentration in athletes. https://pmc.ncbi.nlm.nih.gov/articles/PMC9803156/
63. PMC8472039 — Anemia in sports narrative review. https://pmc.ncbi.nlm.nih.gov/articles/PMC8472039/
64. PMC12048899 — Smoking cessation and hematological parameters in polycythemic patients. https://pmc.ncbi.nlm.nih.gov/articles/PMC12048899/
65. Lu Y, Chen B, et al. Mean corpuscular volume levels and all-cause and liver cancer mortality. *Clin Chem Lab Med*. 2016. https://pubmed.ncbi.nlm.nih.gov/26630695/
66. PMC9189337 — Age-related changes in mean corpuscular volumes. https://pmc.ncbi.nlm.nih.gov/articles/PMC9189337/
67. JLPM — Daves: Modern hematology analyzers (focus on RBCs). https://jlpm.amegroups.org/article/view/8320/html
68. PMC6861793 — Role of RDW in cardiovascular risk assessment. https://pmc.ncbi.nlm.nih.gov/articles/PMC6861793/
69. CFR Journal — RDW as biomarker of red cell dysfunction associated with inflammation. https://www.cfrjournal.com/articles/red-blood-cell-distribution-width-biomarker-red-cell-dysfunction-associated-inflammation
70. Sennels HP, et al. Diurnal variation of hematology parameters in healthy young males. *Scand J Clin Lab Invest*. 2011. https://pubmed.ncbi.nlm.nih.gov/21988588/

---

*Document last reviewed: 2026-05-09. Built from external peer-reviewed and guideline sources (WHO 2024, ASH, NEJM, JACC, Circulation, Lancet, Am J Hematol 2024 updates). All quantitative claims cited inline; reference ranges assume an automated CBC analyzer (Coulter / impedance + light scatter) and serologic ABO/Rh typing.*
