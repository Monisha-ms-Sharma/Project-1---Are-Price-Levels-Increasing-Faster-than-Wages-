"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
fact_table.py

Author:
Monisha Sharma

Description:
Builds the master analytical fact table used
throughout the project.

This module serves as the single source of truth
for all downstream analytics, including:

• Statistical Analysis
• Business Insights
• Dashboard Metrics
• Power BI Export
• Executive Reports
• Visualizations

The module performs:

• Data Loading
• Report Parsing
• Feature Engineering
• Dataset Merging

and returns the completed analytical dataset.
============================================================
"""

import pandas as pd

from src.logger import logger

from src.data_loader import (
    load_all_datasets
)

from src.report_parser import (
    parse_report
)

from src.feature_engineering import (

    # CPI
    reshape_cpi,
    calculate_annual_average_cpi,
    calculate_annual_inflation_rate,

    # Wages
    reshape_wage_data,
    calculate_annual_average_wages,
    calculate_annual_wage_growth,

    # Merge
    merge_cpi_wages,
    calculate_real_wage_growth,

    # Employment
    reshape_employment_data,
    calculate_annual_average_employment,

    # Unemployment
    reshape_unemployment_data,
    calculate_annual_average_unemployment,
)


# ==========================================================
# BUILD FACT TABLE
# ==========================================================

def build_fact_economic_indicators():
    """
    Build the master analytical fact table.

    Returns
    -------
    tuple

        fact_table

        annual_employment

        annual_unemployment
    """

    logger.info("=" * 60)
    logger.info("Building Analytical Fact Table")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # LOAD DATASETS
    # ------------------------------------------------------

    datasets = load_all_datasets()

    # ------------------------------------------------------
    # CPI DATA
    # ------------------------------------------------------

    logger.info("Processing CPI dataset...")

    cpi = parse_report(
        datasets["cpi"]
    )

    cpi = reshape_cpi(
        cpi
    )

    annual_cpi = (
        calculate_annual_average_cpi(
            cpi
        )
    )

    annual_cpi = (
        calculate_annual_inflation_rate(
            annual_cpi
        )
    )

    # ------------------------------------------------------
    # WAGE DATA
    # ------------------------------------------------------

    logger.info("Processing Wage dataset...")

    wages = parse_report(
        datasets["average_hourly_earnings"]
    )

    wages = reshape_wage_data(
        wages
    )

    annual_wages = (
        calculate_annual_average_wages(
            wages
        )
    )

    annual_wages = (
        calculate_annual_wage_growth(
            annual_wages
        )
    )

    # ------------------------------------------------------
    # MERGE CPI & WAGES
    # ------------------------------------------------------

    logger.info(
        "Merging CPI and Wage datasets..."
    )

    fact_table = merge_cpi_wages(
        annual_cpi,
        annual_wages
    )

    # ------------------------------------------------------
    # REAL WAGE GROWTH
    # ------------------------------------------------------

    logger.info(
        "Calculating Real Wage Growth..."
    )

    fact_table = (
        calculate_real_wage_growth(
            fact_table
        )
    )

    # ------------------------------------------------------
    # EMPLOYMENT DATA
    # ------------------------------------------------------

    logger.info(
        "Processing Employment dataset..."
    )

    employment = parse_report(
        datasets["employment"]
    )

    employment = (
        reshape_employment_data(
            employment
        )
    )

    annual_employment = (
        calculate_annual_average_employment(
            employment
        )
    )

    # ------------------------------------------------------
    # UNEMPLOYMENT DATA
    # ------------------------------------------------------

    logger.info(
        "Processing Unemployment dataset..."
    )

    unemployment = parse_report(
        datasets["unemployment"]
    )

    unemployment = (
        reshape_unemployment_data(
            unemployment
        )
    )

    annual_unemployment = (
        calculate_annual_average_unemployment(
            unemployment
        )
    )

    # ------------------------------------------------------
    # MERGE EMPLOYMENT
    # ------------------------------------------------------

    logger.info(
        "Merging Employment dataset..."
    )

    fact_table = pd.merge(
        fact_table,
        annual_employment,
        on="Year",
        how="left"
    )

    # ------------------------------------------------------
    # MERGE UNEMPLOYMENT
    # ------------------------------------------------------

    logger.info(
        "Merging Unemployment dataset..."
    )

    fact_table = pd.merge(
        fact_table,
        annual_unemployment,
        on="Year",
        how="left"
    )

    # ------------------------------------------------------
    # SORT DATA
    # ------------------------------------------------------

    fact_table = (
        fact_table
        .sort_values("Year")
        .reset_index(drop=True)
    )

    # ------------------------------------------------------
    # REORDER COLUMNS
    # ------------------------------------------------------

    fact_table = fact_table[

        [

            "Year",

            "Average CPI",

            "Annual Inflation Rate (%)",

            "Average Hourly Wage",

            "Annual Wage Growth (%)",

            "Real Wage Growth (%)",

            "Average Employment",

            "Average Unemployment Rate",

        ]

    ]

    # ------------------------------------------------------
    # ROUND NUMERIC COLUMNS
    # ------------------------------------------------------

    numeric_columns = [

        "Average CPI",

        "Annual Inflation Rate (%)",

        "Average Hourly Wage",

        "Annual Wage Growth (%)",

        "Real Wage Growth (%)",

        "Average Employment",

        "Average Unemployment Rate",

    ]

    fact_table[numeric_columns] = (
        fact_table[numeric_columns]
        .round(2)
    )

    # ------------------------------------------------------
    # FINAL DATASET SUMMARY
    # ------------------------------------------------------

    logger.info("=" * 60)
    logger.info(
        f"Analytical Fact Table created ({len(fact_table)} rows × {len(fact_table.columns)} columns)."
    )
    logger.info("=" * 60)

    return (
        fact_table,
        annual_employment,
        annual_unemployment,
    )


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    fact_table, annual_employment, annual_unemployment = (
        build_fact_economic_indicators()
    )

    print()
    print("=" * 80)
    print("FACT ECONOMIC INDICATORS")
    print("=" * 80)

    print(fact_table)

    print()
    print("Columns")
    print("-" * 80)
    print(fact_table.columns.tolist())

    print()
    print("Shape")
    print("-" * 80)
    print(fact_table.shape)

    print()
    print("Employment Table")
    print("-" * 80)
    print(annual_employment.head())

    print()
    print("Unemployment Table")
    print("-" * 80)
    print(annual_unemployment.head())