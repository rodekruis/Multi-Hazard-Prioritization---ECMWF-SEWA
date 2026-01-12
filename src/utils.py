"""
Utility functions for data processing.

This module contains reusable helper functions that can be imported
and used across multiple notebooks.
"""

import pandas as pd
from pathlib import Path


def load_csv_data(filename, data_dir='../data/raw'):
    """
    Load CSV data from the specified directory.
    
    Parameters:
    -----------
    filename : str
        Name of the CSV file to load
    data_dir : str, default '../data/raw'
        Directory containing the data file
        
    Returns:
    --------
    pd.DataFrame
        Loaded data as a pandas DataFrame
    """
    filepath = Path(data_dir) / filename
    return pd.read_csv(filepath)


def save_csv_data(df, filename, data_dir='../data/output'):
    """
    Save DataFrame to CSV in the specified directory.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to save
    filename : str
        Name of the output CSV file
    data_dir : str, default '../data/output'
        Directory to save the file
    """
    filepath = Path(data_dir) / filename
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")


def clean_missing_values(df, strategy='drop', fill_value=None):
    """
    Handle missing values in a DataFrame.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input DataFrame
    strategy : str, default 'drop'
        Strategy for handling missing values: 'drop' or 'fill'
    fill_value : any, optional
        Value to use when strategy is 'fill'
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with missing values handled
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(fill_value)
    else:
        raise ValueError("strategy must be 'drop' or 'fill'")


def summarize_dataframe(df):
    """
    Print a comprehensive summary of a DataFrame.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to summarize
    """
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nFirst few rows:\n{df.head()}")
