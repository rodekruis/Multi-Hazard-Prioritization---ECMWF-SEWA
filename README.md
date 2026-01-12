# Multi-Hazard Prioritization - ECMWF SEWA

## Introduction
This repository contains data analysis notebooks for multi-hazard prioritization analysis using ECMWF SEWA data.

- **Project**: Multi-Hazard Prioritization Analysis
- **Contact**: [rodekruis](https://github.com/rodekruis)
- **Workflow**: Extract → Transform → Load (ETL) using Jupyter notebooks

## Project Structure

```
.
├── data/
│   ├── raw/          # Raw input data (already downloaded)
│   ├── processed/    # Transformed and aggregated data
│   └── output/       # Final CSV outputs
├── notebooks/        # Jupyter notebooks for analysis
├── src/             # Reusable utility functions (optional)
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Input and Output

### Input
- **Directory**: `data/raw/`
- **Source**: Raw data should be downloaded and placed in the `data/raw/` directory
- **Link to data**: [Add link to data in Teams]

### Output
- **Directory**: `data/output/`
- **Format**: CSV files
- **Link to outputs**: [Add link to outputs in Teams]

## Setup

### Requirements
- Python 3.8 or higher
- Jupyter Notebook
- See `requirements.txt` for complete list of dependencies

### Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Starting Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your browser. Navigate to the `notebooks/` directory.

### Workflow

1. **Place raw data** in `data/raw/` directory
2. **Open notebooks** in order (e.g., `01_*.ipynb`, `02_*.ipynb`, etc.)
3. **Run each notebook** sequentially to:
   - Load and explore raw data
   - Transform and aggregate data
   - Generate final outputs
4. **Find results** in `data/output/` as CSV files

### Notebook Organization

Notebooks should follow a numbered naming convention:
- `01_data_exploration.ipynb` - Initial data exploration
- `02_data_transformation.ipynb` - Data transformation and aggregation
- `03_analysis.ipynb` - Main analysis and calculations
- `04_visualization.ipynb` - Visualization and reporting

Each notebook follows the ETL pattern:
1. **Extract**: Load data from `data/raw/`
2. **Transform**: Clean, process, and aggregate data
3. **Load**: Save results to `data/processed/` or `data/output/`

## Notes

- Data files are not tracked in version control (see `.gitignore`)
- Store large data files in Teams and document the source
- Intermediate results can be saved in `data/processed/`
- Final outputs should be CSV files in `data/output/`
- Use `src/` for any reusable functions needed across notebooks

See example structure [here](https://github.com/rodekruis/GloFAS-river-depth-analysis).