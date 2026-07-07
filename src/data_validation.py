"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
data_validation.py

Author:
Monisha Sharma

Description:
Validates and profiles datasets loaded into the project.

Responsibilities
----------------
• Dataset profiling
• Schema validation
• Data quality checks
• Summary statistics
• Logging

============================================================
"""

import pandas as pd

from src.logger import logger


# ==========================================================
# DATASET OVERVIEW
# ==========================================================

def dataset_overview(dataset_name: str,
                     df: pd.DataFrame) -> None:
    """
    Log basic dataset information.
    """

    memory = df.memory_usage(deep=True).sum() / 1024

    logger.info("=" * 60)
    logger.info(f"Dataset : {dataset_name}")
    logger.info("=" * 60)

    logger.info(f"Rows            : {df.shape[0]:,}")
    logger.info(f"Columns         : {df.shape[1]}")
    logger.info(f"Memory (KB)     : {memory:.2f}")

    logger.info("")


# ==========================================================
# COLUMN INFORMATION
# ==========================================================

def validate_schema(df: pd.DataFrame) -> None:
    """
    Log column names and data types.
    """

    logger.info("Schema")

    for column in df.columns:

        logger.info(
            f"{column:<40} {str(df[column].dtype)}"
        )

    logger.info("")


# ==========================================================
# MISSING VALUES
# ==========================================================

def check_missing_values(df: pd.DataFrame) -> None:
    """
    Log missing value counts.
    """

    logger.info("Missing Values")

    missing = df.isna().sum()

    for column, value in missing.items():

        if value > 0:

            pct = value / len(df) * 100

            logger.warning(
                f"{column:<35}"
                f"{value:>6} "
                f"({pct:.2f}%)"
            )

    if missing.sum() == 0:

        logger.info("No missing values detected.")

    logger.info("")


# ==========================================================
# DUPLICATE ROWS
# ==========================================================

def check_duplicates(df: pd.DataFrame) -> None:
    """
    Log duplicate row count.
    """

    duplicates = df.duplicated().sum()

    if duplicates == 0:

        logger.info("Duplicate Rows : 0")

    else:

        logger.warning(
            f"Duplicate Rows : {duplicates}"
        )

    logger.info("")


# ==========================================================
# CONSTANT COLUMNS
# ==========================================================

def check_constant_columns(df: pd.DataFrame) -> None:
    """
    Detect columns with only one unique value.
    """

    logger.info("Constant Columns")

    found = False

    for column in df.columns:

        if df[column].nunique(dropna=False) == 1:

            logger.warning(column)

            found = True

    if not found:

        logger.info("None")

    logger.info("")


# ==========================================================
# SUMMARY STATISTICS
# ==========================================================

def summary_statistics(df: pd.DataFrame) -> None:
    """
    Log summary statistics for numeric columns.
    """

    numeric = df.select_dtypes(include="number")

    if numeric.empty:

        logger.info("No numeric columns.")

        return

    logger.info("Summary Statistics")

    logger.info("\n" + str(numeric.describe()))

    logger.info("")


# ==========================================================
# COMPLETE VALIDATION
# ==========================================================

def validate_dataset(dataset_name: str,
                     df: pd.DataFrame) -> None:
    """
    Run all validation steps.
    """

    dataset_overview(dataset_name, df)

    validate_schema(df)

    check_missing_values(df)

    check_duplicates(df)

    check_constant_columns(df)

    summary_statistics(df)