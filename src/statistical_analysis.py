"""
============================================================
Project:
U.S. Inflation, Wage Growth &
Purchasing Power Analysis

Module:
statistical_analysis.py

Author:
Monisha Sharma

Description:
Performs descriptive statistical analysis on the
annual economic indicators.
============================================================
"""

import pandas as pd

from src.logger import logger


def descriptive_statistics(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate descriptive statistics for all
    numeric columns.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
        Summary statistics.
    """

    logger.info(
        "Generating descriptive statistics..."
    )

    numeric_df = df.select_dtypes(include="number")

    summary = (
        numeric_df
        .describe()
        .transpose()
    )

    summary = summary.round(2)

    logger.info(
        "Descriptive statistics created."
    )

    return summary


def save_statistics(
    df: pd.DataFrame,
    file_path: str
) -> None:
    """
    Save statistics to CSV.
    """

    df.to_csv(
        file_path,
        index=True
    )

    logger.info(
        f"Saved statistics: {file_path}"
    )