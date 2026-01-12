# Data Directory

This directory contains all data files used in the analysis.

## Structure

- **raw/**: Raw data files (already downloaded, input data)
  - Place your original, unmodified data files here
  - This data should not be modified by the analysis

- **processed/**: Intermediate processed data
  - Transformed and aggregated data
  - Cleaned datasets ready for analysis

- **output/**: Final output files
  - CSV files with final results
  - Ready to share or upload to Teams

## Data Flow

```
raw/ → [Transform & Aggregate] → processed/ → [Analysis] → output/
```

## Note

Data files are not tracked in git (see .gitignore). Store large data files in Teams and document the source in the project README.
