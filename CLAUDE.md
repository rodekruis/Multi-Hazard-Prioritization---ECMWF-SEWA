# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Multi-hazard risk prioritization analysis for Sub-Saharan Africa using ECMWF SEWA data. Analyzes 138 indicators across ~47 countries for 9 hazard types (Drought, Dust, Flash Flooding, Heatwave, River Flooding, Tropical Cyclone, Wildfire, Wind, Wind+River Flooding). Final decisions are documented in [FINAL_DECISIONS_SUMMARY.md](FINAL_DECISIONS_SUMMARY.md).

## Setup

```bash
pip install -r requirements.txt
jupyter notebook
```

External data access requires `.cdsapirc` with valid ECMWF CDS API credentials.

## Notebook Execution Order

Notebooks follow a numbered ETL pattern — run in sequence:

1. `WP3_01_WorldRiskIndex_extraction.ipynb` — World Risk Index
2. `WP3_02_INFORM_Risk_extraction.ipynb` — INFORM Risk Index
3. `WP3_03_INFORM_CC_pessimistic_2050_extraction.ipynb` — INFORM CC projections
4. `WP3_04_ThinkHazard_extraction.ipynb` — ThinkHazard exposure
5. `WP3_05_IDMC_displacement_extraction_final.ipynb` — IDMC displacement data
6. `WP3_06_EMDAT_DesInventar_exploration_extraction.ipynb` — EM-DAT / DesInventar
7. `WP3_07_diagnostics.ipynb` — Redundancy, stability, zero-inflation diagnostics
8. `WP3_07_Hazard_Prioritisation_Tool_RankingNorm.ipynb` — Final prioritization scoring

`Storylines/` notebooks are standalone climate story analyses (e.g., West Africa heatwave via ERA5).

## Data Flow

```
data/raw/  →  notebooks (extract/transform)  →  data/intermediate/  →  data/output/ (CSV)
```

Data files are not tracked in git (all `data/raw/`, `data/intermediate/`, `data/output/` are gitignored). Store large files in Teams/external storage. Directory structure is preserved via `.gitkeep` files.

## Shared Utilities

[src/utils.py](src/utils.py) provides:
- `load_csv_data()` / `save_csv_data()` — path-aware CSV I/O relative to `data/`
- `clean_missing_values()` — drop or fill strategies
- `summarize_dataframe()` — prints shape, dtypes, null counts, basic stats

Import with `from src.utils import load_csv_data` or add `src/` to `sys.path`.

## Analysis Methodology

- Normalization: percentile ranking
- Correlation: Spearman rank
- Quality thresholds: coverage, skewness, redundancy, zero-inflation
- Final recommendation: reduce 138 → ~75 indicators (46% reduction)
- 5 analysis dimensions: Impact, Prevalence, Scale, Cascade impacts, Future relevance
- Time period: 2000–2024

## New Notebooks

Use [notebooks/00_template.ipynb](notebooks/00_template.ipynb) as the starting point for new analysis notebooks.
