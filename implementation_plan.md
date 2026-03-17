# Implementation Plan: Reviewer Comments on WP3 Hazard Prioritisation

Target notebook: `notebooks/WP3_07_Hazard_Prioritisation_Tool_RankingNorm.ipynb`

---

## Task A: Methodology & Classification Documentation
**Addresses:** C1, C6, C7, C31

Add a new section **"Data Sources and Hazard Classification"** after the PRESENCE_RULES cell:

| Sub-task | What | Comments |
|----------|------|----------|
| A1 | Render PRESENCE_RULES as a clean table: Hazard -> Datasets -> Indicators -> Threshold | C6 |
| A2 | Scoring pipeline walkthrough with concrete 1-country example | C1 |
| A3 | Explain thunderstorm vs flash flood classification (TH.TS_LEVEL vs TH.UF_LEVEL) | C7 |
| A4 | Note on EM-DAT event attribution ambiguity (wind/flood vs thunderstorm) | C31 |

---

## Task B: Dataset Reliability Section (online research required)
**Addresses:** C4, C5, C11

Add a new section **"Data Source Reliability and Limitations"**:

| Sub-task | What | Comments |
|----------|------|----------|
| B1 | ThinkHazard: methodology, disclaimers, cross-country reliability | C4 |
| B2 | EM-DAT: cross-country consistency, reporting bias, Africa coverage gaps | C4, C5 |
| B3 | INFORM Risk Index: methodology, update frequency, limitations | C4 |
| B4 | IDMC: displacement data methodology and limitations | C4 |
| B5 | Cross-dataset agreement summary (reference diagnostics notebook) | C4 |
| B6 | EM-DAT multi-country comparison limitations note | C5 |

---

## Task C: Uncertainty & Dataset Parity Analysis
**Addresses:** C8, C10, C12

Strengthen existing Q&A Diagnosis section:

| Sub-task | What | Comments |
|----------|------|----------|
| C1 | Count datasets per hazard, show coverage disparity table | C8 |
| C2 | Sensitivity: rank hazards using EM-DAT only vs full dataset | C8, C12 |
| C3 | Single-indicator dominance: % of score from top indicator, flag >60% | C10 |
| C4 | Interpretation markdown: where is confidence high vs low? | C8, C10 |

---

## Task D: Heatmap Readability Fix
**Addresses:** C9

- Fix text contrast on all heatmaps (white text on dark, black on light)
- Ensure `plot_coverage_heatmap` helper has same contrast logic as Cell 29

---

## Task E: Regional Ranking Tables & Focus Hazards
**Addresses:** C13, C14, C25, C28

| Sub-task | What | Comments |
|----------|------|----------|
| E1 | Full ranking table per region: all 9 hazards, pop-weighted + unweighted score, rank | C13 |
| E2 | Add 5 dimension sub-scores per region x hazard | C14 |
| E3 | Score gap column: absolute gap to next-ranked hazard + close/clear indicator | C25 |
| E4 | Label existing Top 3 as "Recommended Focus Hazards" + brief justification per region | C28 |

---

## Task F: Wind -> Tropical Cyclone Clarification
**Addresses:** C18, C19, C27

| Sub-task | What | Comments |
|----------|------|----------|
| F1 | Rename "Wind" -> "Tropical Cyclone (Wind)" in HAZARDS list + alias mapping | C18, C27 |
| F2 | Explanatory markdown: Wind uses TH.CY_LEVEL + INFORM.HAZEX.TROPICAL_CYCLONE | C18 |
| F3 | Update figure captions/titles | C19 |

---

## Task G: Dust/DR Congo Investigation
**Addresses:** C20

- Add diagnostic code cell investigating why DR Congo ranks higher for dust than Sahel
- Add markdown interpretation

---

## Task H: Cross-Cutting Issues & Intra-Regional Variation
**Addresses:** C29, C30

| Sub-task | What | Comments |
|----------|------|----------|
| H1 | Identify hazards ranking top-3 in multiple regions (coordination opportunities) | C29 |
| H2 | Coefficient of variation within regions (where does the average mask differences) | C30 |
| H3 | Note cross-reference with Jerome's deliverable | C30 |

---

## Caveat Text (woven into existing sections)

| Caveat | Location | Addresses |
|--------|----------|-----------|
| Population weighting limitations + double-counting risk | Section 7 intro | C2, C16, C17 |
| Physical/hydrometeorological hazards scope only | Notebook intro | C3 |
| Stakeholder awareness bias in datasets | Limitations section | C24 |
| Temporal lag in cascade impacts | Cascade impacts dimension | C26 |

---

## Deferred Items

| Item | Why Deferred | Next Step |
|------|-------------|-----------|
| C21, C23: Add Mauritania | Requires re-running all 6 extraction notebooks | Add MRT to scope CSV, then re-run WP3_01-06 |
| C32: Regional storylines | External — handled by designers | Coordinate with design team |
| C23: Transfer link to ECMWF | External infrastructure | Coordinate with ECMWF team |
