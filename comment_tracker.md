# Reviewer Comment Tracker

This file maps every reviewer comment (C1–C33) to its classification, assigned task group, and implementation status.

## Legend
- **REPO**: Actionable within this repository (notebook changes)
- **NON-REPO**: Requires discussion, external action, or is deferred
- **CAVEAT**: Addressed by adding explanatory/caveat text (no code changes)
- **DEFERRED**: Tracked but not implemented in this round
- **POSITIVE**: Positive feedback, no action needed

---

## Comment Tracking Table

| ID | Reviewer | Comment Summary | Classification | Task Group | Status |
|----|----------|----------------|----------------|------------|--------|
| C1 | Katherine Egan | How are these actually scored from the datasets? | REPO | A — Methodology | DONE — Scoring pipeline walkthrough added |
| C2 | Katherine Egan | Population weighting debate: not just number of people, also how protected | CAVEAT | Caveat 1 | DONE — Caveat in Section 7 + Limitations |
| C3 | Katherine Egan | Use weather/climate examples, not covid/earthquakes/dam failure | CAVEAT | Caveat 2 | DONE — Scope section added to intro |
| C4 | Katherine Egan | Need critical analysis of dataset reliability (ThinkHazard disclaimers, etc.) | REPO | B — Reliability | DONE — Full reliability section with online research |
| C5 | Katherine Egan | Is EM-DAT supporting standardized multi-country comparison? | REPO | B — Reliability | DONE — Addressed in EM-DAT reliability section |
| C6 | Katherine Egan | Which datasets used for what? Clear mapping table needed. Flooding classification unclear | REPO | A — Methodology | DONE — Dataset-to-hazard mapping table added |
| C7 | Katherine Egan | How distinguished thunderstorm impacts from flash flood impacts? | REPO | A — Methodology | DONE — Hazard definitions + classification note |
| C8 | Katherine Egan | Can we compare hazards with different dataset coverage (dust=1 vs river flooding=6)? | REPO | C — Uncertainty | DONE — Dataset parity analysis + EM-DAT sensitivity |
| C9 | Katherine Egan | Numbers hard to read on dark heatmap colours | REPO | D — Visual fix | DONE — Text contrast logic added |
| C10 | Katherine Egan | Strengthen uncertainty analysis: gaps, single-indicator dominance | REPO | C — Uncertainty | DONE — Single-indicator dominance analysis |
| C11 | Katherine Egan | Are datasets better in some countries than others? | NON-REPO | Absorbed into B | DONE — Covered in reliability section |
| C12 | Katherine Egan | How much does different dataset usage per hazard affect ranking? | REPO | C — Uncertainty | DONE — EM-DAT-only vs full-dataset sensitivity |
| C13 | Katherine Egan | Need a table showing rankings in each region | REPO | E — Tables | DONE — Full 9-hazard ranking table per region |
| C14 | Karolin Eichler | Show different dimensions and how scoring differs | REPO | E — Tables | DONE — Dimension sub-scores in ranking table |
| C15 | Katherine Egan | River flooding also has the most data available (observation) | NON-REPO | Absorbed into C8 | DONE — Addressed in dataset parity analysis |
| C16 | Katherine Egan | Population weighting: mountain example, location matters not just numbers | CAVEAT | Caveat 1 | DONE — Caveat in Section 7 |
| C17 | Katherine Egan | Underlying data already does population weighting — double counting? | CAVEAT | Caveat 1 | DONE — Caveat in Section 7 |
| C18 | Katherine Egan | Explain why "Wind" — not in hazard list. Is it only TCs? | REPO | F — Wind/TC | DONE — Renamed to "Tropical Cyclone (Wind)" + explanation |
| C19 | Karolin Eichler | Make Wind/TC clear in figure captions too | REPO | F — Wind/TC | DONE — Rename cascades through all outputs |
| C20 | Katherine Egan | Dust storms ranking higher in DR Congo than Sahel — why? | REPO | G — Investigation | DONE — Diagnostic code + interpretation added |
| C21 | Katherine Egan | Include Mauritania | DEFERRED | — | Requires re-running all extraction notebooks |
| C22 | Katherine Egan | Maps are really good — thank you | POSITIVE | — | No action needed |
| C23 | Karolin Eichler | Transfer link to ECMWF; include Mauritania in West Africa | DEFERRED | — | ECMWF = external; Mauritania = deferred |
| C24 | Katherine Egan | Lorraine's point: stakeholder awareness gaps (dust-meningitis link) | CAVEAT | Caveat 3 | DONE — Limitations section point 1 |
| C25 | Katherine Egan | Table + indication of how close the ranking is | REPO | E — Tables | DONE — Score gap + confidence columns |
| C26 | Katherine Egan | Cascading hazards may have time lag (rain then landslide later) | CAVEAT | Caveat 4 | DONE — Limitations section point 2 |
| C27 | Katherine Egan | Wind isn't in hazards list — it's TCs specifically | REPO | F — Wind/TC | DONE — Renamed throughout |
| C28 | Katherine Egan | Deliverable needs to propose up to 3 focus hazards per region | REPO | E — Tables | DONE — "Recommended Focus Hazards" label + existing Top 3 |
| C29 | Katherine Egan | Cross-cutting issues and coordination opportunities across regions | REPO | H — Cross-cutting | DONE — Section 11 added |
| C30 | Katherine Egan | Note strong variation within regions; cross-ref Jerome's deliverable | REPO | H — Cross-cutting | DONE — CV analysis + Jerome reference |
| C31 | Katherine Egan | Impact attribution: could wind/flood categories steal from thunderstorms? | REPO | A — Methodology | DONE — Note in hazard definitions + limitations |
| C32 | Karolin Eichler | Impactful storyline per region grounded in WP2 stakeholder input | NON-REPO | — | External: handled by designers |
| C33 | — | (Empty) | — | — | — |

---

## Summary

| Classification | Count | Completed |
|---------------|-------|-----------|
| REPO-ACTIONABLE | 21 | 21 |
| CAVEAT (text only) | 6 | 6 |
| NON-REPO / Absorbed | 3 | 3 |
| DEFERRED | 2 | 0 |
| POSITIVE | 1 | 1 |
| EXTERNAL | 1 | 0 |
| Empty | 1 | — |

**Remaining items:**
- **C21/C23 (Mauritania):** Requires adding MRT to scope CSV and re-running all 6 extraction notebooks
- **C23 (ECMWF transfer):** External infrastructure task
- **C32 (Storylines):** Handled by designers externally
