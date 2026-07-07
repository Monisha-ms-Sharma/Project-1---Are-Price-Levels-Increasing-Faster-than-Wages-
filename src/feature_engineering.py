"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
feature_engineering.py

Author:
Monisha Sharma

Description:
Creates analytical features used throughout the project.

Current Features
----------------
• Reshape CPI data
• Calculate Monthly Inflation Rate
• Calculate Annual Average CPI
• Calculate Annual Inflation Rate

Future Features
---------------
• Wage Growth
• Real Wage Growth
• Purchasing Power
============================================================
"""

import pandas as pd

from src.logger import logger

# ==========================================================
# MONTH ORDER
# ==========================================================

MONTH_ORDER = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# ==========================================================
# RESHAPE CPI DATA
# ==========================================================

def reshape_cpi(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert CPI data from wide format to long format.
    """

    logger.info("Reshaping CPI dataset...")

    cpi_long = df.melt(
        id_vars="Year",
        value_vars=MONTH_ORDER,
        var_name="Month",
        value_name="CPI"
    )

    cpi_long["Month"] = pd.Categorical(
        cpi_long["Month"],
        categories=MONTH_ORDER,
        ordered=True
    )

    cpi_long = (
        cpi_long
        .sort_values(["Year", "Month"])
        .reset_index(drop=True)
    )

    logger.info(f"CPI reshaped to {len(cpi_long)} rows.")

    return cpi_long


# ==========================================================
# MONTHLY INFLATION RATE
# ==========================================================

def calculate_monthly_inflation(
    cpi_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Month-over-Month Inflation Rate.
    """

    logger.info("Calculating Monthly Inflation Rate...")

    cpi_df = cpi_df.copy()

    cpi_df["Monthly Inflation Rate (%)"] = (
        cpi_df["CPI"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    logger.info("Monthly Inflation Rate calculated.")

    return cpi_df


# ==========================================================
# ANNUAL AVERAGE CPI
# ==========================================================

def calculate_annual_average_cpi(
    cpi_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Annual Average CPI.
    """

    logger.info("Calculating Annual Average CPI...")

    annual_cpi = (
        cpi_df
        .groupby("Year", as_index=False)
        .agg({"CPI": "mean"})
    )

    annual_cpi.rename(
        columns={"CPI": "Average CPI"},
        inplace=True
    )

    annual_cpi["Average CPI"] = (
        annual_cpi["Average CPI"]
        .round(3)
    )

    logger.info(
        f"Created Annual CPI table ({len(annual_cpi)} rows)."
    )

    return annual_cpi


# ==========================================================
# ANNUAL INFLATION RATE
# ==========================================================

def calculate_annual_inflation_rate(
    annual_cpi: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Year-over-Year Inflation Rate.
    """

    logger.info("Calculating Annual Inflation Rate...")

    annual_cpi = annual_cpi.copy()

    annual_cpi["Annual Inflation Rate (%)"] = (
        annual_cpi["Average CPI"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    logger.info("Annual Inflation Rate calculated.")

    return annual_cpi

from pathlib import Path

def save_feature_dataset(
    df: pd.DataFrame,
    output_path: Path
) -> None:
    """
    Save a feature-engineered dataset as CSV.
    """

    logger.info(f"Saving dataset to {output_path}")

    df.to_csv(output_path, index=False)

    logger.info("Dataset saved successfully.")

# ==========================================================
# RESHAPE WAGE DATA
# ==========================================================

def reshape_wage_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the Average Hourly Earnings dataset
    from wide format to long format.
    """

    logger.info("Reshaping Wage dataset...")

    month_columns = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    wage = df.melt(
        id_vars="Year",
        value_vars=month_columns,
        var_name="Month",
        value_name="Average Hourly Earnings"
    )

    # Convert columns to numeric
    wage["Year"] = pd.to_numeric(
        wage["Year"],
        errors="coerce"
    )

    wage["Average Hourly Earnings"] = pd.to_numeric(
        wage["Average Hourly Earnings"],
        errors="coerce"
    )

    wage["Month"] = pd.Categorical(
        wage["Month"],
        categories=month_columns,
        ordered=True
    )

    wage = (
        wage
        .sort_values(["Year", "Month"])
        .reset_index(drop=True)
    )

    logger.info(
        f"Wage reshaped to {len(wage)} rows."
    )

    return wage

# ==========================================================
# MONTHLY WAGE GROWTH
# ==========================================================

def calculate_monthly_wage_growth(
    wage_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Month-over-Month Wage Growth.
    """

    logger.info("Calculating Monthly Wage Growth...")

    wage_df = wage_df.copy()

    wage_df["Monthly Wage Growth (%)"] = (
        wage_df["Average Hourly Earnings"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    logger.info("Monthly Wage Growth calculated.")

    return wage_df

# ==========================================================
# ANNUAL AVERAGE WAGES
# ==========================================================

def calculate_annual_average_wages(
    wage_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Annual Average Hourly Earnings.
    """

    logger.info("Calculating Annual Average Wages...")

    annual_wages = (
        wage_df
        .groupby("Year", as_index=False)
        .agg({
            "Average Hourly Earnings": "mean"
        })
    )

    annual_wages.rename(
        columns={
            "Average Hourly Earnings": "Average Hourly Wage"
        },
        inplace=True
    )

    annual_wages["Average Hourly Wage"] = (
        annual_wages["Average Hourly Wage"]
        .round(2)
    )

    logger.info(
        f"Created Annual Wage table ({len(annual_wages)} rows)."
    )

    return annual_wages

# ==========================================================
# ANNUAL WAGE GROWTH
# ==========================================================

def calculate_annual_wage_growth(
    annual_wages: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Year-over-Year Wage Growth.
    """

    logger.info("Calculating Annual Wage Growth...")

    annual_wages = annual_wages.copy()

    annual_wages["Annual Wage Growth (%)"] = (
        annual_wages["Average Hourly Wage"]
        .pct_change()
        .mul(100)
        .round(2)
    )

    logger.info("Annual Wage Growth calculated.")

    return annual_wages

# ==========================================================
# MERGE CPI & WAGES
# ==========================================================

def merge_cpi_wages(
    annual_cpi: pd.DataFrame,
    annual_wages: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge annual CPI and annual wage datasets.
    """

    logger.info("Merging CPI and Wage datasets...")

    merged = pd.merge(
        annual_cpi,
        annual_wages,
        on="Year",
        how="inner"
    )

    # Ensure numeric data types
    merged["Average CPI"] = pd.to_numeric(
        merged["Average CPI"],
        errors="coerce"
    )

    merged["Average Hourly Wage"] = pd.to_numeric(
        merged["Average Hourly Wage"],
        errors="coerce"
    )

    logger.info(
        f"Merged dataset contains {len(merged)} years."
    )

    return merged

# ==========================================================
# REAL WAGE GROWTH
# ==========================================================

def calculate_real_wage_growth(
    merged_df: pd.DataFrame,
    annual_wage_growth: pd.DataFrame,
    annual_inflation: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate Real Wage Growth after adjusting
    for inflation.

    Formula:

        ((1 + Wage Growth / 100)
         /
         (1 + Inflation / 100)
         - 1) * 100
    """

    logger.info("Calculating Real Wage Growth...")

    df = merged_df.copy()

    # ------------------------------------------------------
    # Merge Wage Growth
    # ------------------------------------------------------

    df = df.merge(
        annual_wage_growth[
            ["Year", "Annual Wage Growth (%)"]
        ],
        on="Year",
        how="left"
    )

    # ------------------------------------------------------
    # Merge Inflation
    # ------------------------------------------------------

    df = df.merge(
        annual_inflation[
            ["Year", "Annual Inflation Rate (%)"]
        ],
        on="Year",
        how="left"
    )

    # ------------------------------------------------------
    # Ensure numeric columns
    # ------------------------------------------------------

    numeric_columns = [
        "Average CPI",
        "Average Hourly Wage",
        "Annual Wage Growth (%)",
        "Annual Inflation Rate (%)"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # ------------------------------------------------------
    # Real Wage Growth
    # ------------------------------------------------------

    df["Real Wage Growth (%)"] = (
        (
            (1 + df["Annual Wage Growth (%)"] / 100)
            /
            (1 + df["Annual Inflation Rate (%)"] / 100)
            - 1
        ) * 100
    ).round(2)

    logger.info("Real Wage Growth calculated.")

    return df