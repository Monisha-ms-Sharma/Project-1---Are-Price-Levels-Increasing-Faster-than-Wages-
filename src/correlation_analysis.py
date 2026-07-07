"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
correlation_analysis.py

Author:
Monisha Sharma

Description:
Performs statistical correlation analysis
between economic indicators.
============================================================
"""

import pandas as pd

from src.logger import logger


def calculate_correlation_matrix(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate correlation matrix for
    all numeric variables.
    """

    logger.info("Calculating correlation matrix...")

    numeric_columns = [
        "Average CPI",
        "Annual Inflation Rate (%)",
        "Average Hourly Wage",
        "Annual Wage Growth (%)",
        "Real Wage Growth (%)"
    ]

    correlation = (
        df[numeric_columns]
        .corr(numeric_only=True)
        .round(3)
    )

    logger.info("Correlation matrix created.")

    return correlation