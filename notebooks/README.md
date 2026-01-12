# Notebooks Directory

This directory contains Jupyter notebooks for data analysis.

## Naming Convention

Use descriptive names with numbering to indicate the order of execution:

- `01_data_exploration.ipynb` - Initial data exploration
- `02_data_transformation.ipynb` - Data transformation and aggregation
- `03_analysis.ipynb` - Main analysis
- `04_visualization.ipynb` - Creating visualizations and reports

## Workflow

Each notebook should follow the ETL pattern:
1. **Extract**: Load data from `data/raw/`
2. **Transform**: Clean, transform, and aggregate data
3. **Load**: Save results to `data/processed/` or `data/output/`

## Best Practices

- Keep notebooks focused on specific tasks
- Document your code with markdown cells
- Include data sources and assumptions
- Save intermediate results to `data/processed/`
- Save final outputs as CSV files to `data/output/`
