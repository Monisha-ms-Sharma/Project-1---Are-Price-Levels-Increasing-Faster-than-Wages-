"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
dashboard_metrics.py

Author:
Monisha Sharma

Description:
Creates dashboard-ready KPI metrics for reporting,
Power BI dashboards, and executive summaries.
============================================================
"""

import pandas as pd

from src.logger import logger


def create_dashboard_metrics(
    merged_df: pd.DataFrame,
    employment_df: pd.DataFrame,
    unemployment_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create a one-row dashboard KPI table.

    Parameters
    ----------
    merged_df : pd.DataFrame
        Annual CPI, Inflation, Wage Growth,
        and Real Wage Growth.

    employment_df : pd.DataFrame
        Annual Employment dataset.

    unemployment_df : pd.DataFrame
        Annual Unemployment dataset.

    Returns
    -------
    pd.DataFrame
        One-row dashboard metrics.
    """

    logger.info("Creating dashboard KPI metrics...")

    latest = (
        merged_df
        .sort_values("Year")
        .iloc[-1]
    )

    latest_employment = (
        employment_df
        .sort_values("Year")
        .iloc[-1]
    )

    latest_unemployment = (
        unemployment_df
        .sort_values("Year")
        .iloc[-1]
    )

    dashboard = pd.DataFrame({

        "Latest Year": [
            latest["Year"]
        ],

        "Average CPI": [
            latest["Average CPI"]
        ],

        "Inflation Rate (%)": [
            latest["Annual Inflation Rate (%)"]
        ],

        "Average Hourly Wage": [
            latest["Average Hourly Wage"]
        ],

        "Wage Growth (%)": [
            latest["Annual Wage Growth (%)"]
        ],

        "Real Wage Growth (%)": [
            latest["Real Wage Growth (%)"]
        ],

        "Employment": [
            latest_employment["Average Employment"]
        ],

        "Unemployment Rate (%)": [
            latest_unemployment[
                "Average Unemployment Rate"
            ]
        ]

    })

    logger.info(
        "Dashboard metrics created successfully."
    )

    return dashboard