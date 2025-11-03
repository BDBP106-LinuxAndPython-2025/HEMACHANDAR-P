# CSVProcessor.py
import pandas as pd
import numpy as np

def load_csv(filepath):
    """Load CSV data into a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

def total_columns(df):
    """Return total number of columns."""
    return df.shape[1]

def total_rows(df):
    """Return total number of rows."""
    return df.shape[0]

def fill_missing_with_zero(df):
    """Fill missing values in any column with zero."""
    return df.fillna(0)
