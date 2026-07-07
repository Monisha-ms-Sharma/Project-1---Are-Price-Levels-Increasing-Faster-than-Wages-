"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
preprocessing.py

Author:
Monisha Sharma

Description:
Simple data preprocessing functions used to clean
parsed BLS datasets before feature engineering.
============================================================
"""

import pandas as pd


# ==========================================================
# REMOVE EMPTY ROWS
# ==========================================================

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows that are completely empty."""
    return df.dropna(how="all").reset_index(drop=True)


# ==========================================================
# REMOVE EMPTY COLUMNS
# ==========================================================

def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns that are completely empty."""
    return df.dropna(axis=1, how="all")


# ==========================================================
# CLEAN COLUMN NAMES
# ==========================================================

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Remove extra spaces and line breaks from column names."""

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace("\n", " ", regex=False)
    )

    return df


# ==========================================================
# CONVERT NUMERIC COLUMNS
# ==========================================================

def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to numeric where possible.

    If a column cannot be converted, leave it unchanged.
    """

    for column in df.columns:

        try:
            df[column] = pd.to_numeric(df[column])

        except (ValueError, TypeError):
            # Leave non-numeric columns unchanged
            pass

    return df


# ==========================================================
# PREPROCESS DATASET
# ==========================================================

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all preprocessing steps.
    """

    df = remove_empty_rows(df)

    df = remove_empty_columns(df)

    df = clean_column_names(df)

    df = convert_numeric_columns(df)

    df.reset_index(drop=True, inplace=True)

    return df