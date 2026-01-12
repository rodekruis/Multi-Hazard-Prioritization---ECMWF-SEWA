# Source Code Directory

This directory contains reusable utility functions and helper scripts.

## Purpose

While the main analysis is done in notebooks, you can create Python modules here for:
- Reusable data processing functions
- Custom visualization functions
- Helper utilities used across multiple notebooks
- Configuration management

## Usage

Import utilities in your notebooks:

```python
import sys
sys.path.append('../src')
from utils import load_data, clean_data
```

## Note

This directory is optional. For simple analyses, all code can remain in notebooks.
