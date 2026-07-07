"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
visualization.py

Author:
Monisha Sharma

Description:
Reusable visualization functions for Exploratory Data Analysis.

Visualizations
--------------
• Annual Average CPI
• Annual Inflation Rate
• Annual Average Wage
• Annual Wage Growth
• Inflation vs Wage Growth
• Real Wage Growth
• Employment Trend
• Unemployment Trend

============================================================
"""

import matplotlib.pyplot as plt
import pandas as pd

from src.config import IMAGES_DIR
from src.logger import logger


# ==========================================================
# SAVE FIGURE
# ==========================================================

def save_plot(
    filename: str
) -> None:
    """
    Save the current matplotlib figure.
    """

    output_file = IMAGES_DIR / filename

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    logger.info(
        f"Saved plot: {output_file}"
    )


# ==========================================================
# CPI TREND
# ==========================================================

def plot_cpi_trend(
    annual_cpi: pd.DataFrame
) -> None:
    """
    Plot Annual Average CPI.
    """

    logger.info(
        "Creating CPI Trend chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual_cpi["Year"],
        annual_cpi["Average CPI"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Average Annual CPI"
    )

    plt.xlabel("Year")

    plt.ylabel("Average CPI")

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_average_cpi.png"
    )

    plt.close()

    logger.info(
        "CPI Trend chart created."
    )


# ==========================================================
# ANNUAL INFLATION RATE
# ==========================================================

def plot_annual_inflation_rate(
    annual_cpi: pd.DataFrame
) -> None:
    """
    Plot Annual Inflation Rate.
    """

    logger.info(
        "Creating Annual Inflation Rate chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual_cpi["Year"],
        annual_cpi["Annual Inflation Rate (%)"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Annual Inflation Rate"
    )

    plt.xlabel("Year")

    plt.ylabel("Percent")

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_inflation_rate.png"
    )

    plt.close()

    logger.info(
        "Annual Inflation Rate chart created."
    )

# ==========================================================
# ANNUAL WAGE TREND
# ==========================================================

def plot_annual_wages(
    annual_wages: pd.DataFrame
) -> None:
    """
    Plot Annual Average Hourly Wage Trend.
    """

    logger.info(
        "Creating Annual Wage Trend chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual_wages["Year"],
        annual_wages["Average Hourly Wage"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Average Annual Hourly Wage"
    )

    plt.xlabel("Year")

    plt.ylabel(
        "Average Hourly Wage ($)"
    )

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_average_wage.png"
    )

    plt.close()

    logger.info(
        "Annual Wage Trend chart created."
    )


# ==========================================================
# ANNUAL WAGE GROWTH
# ==========================================================

def plot_annual_wage_growth(
    annual_wages: pd.DataFrame
) -> None:
    """
    Plot Annual Wage Growth.
    """

    logger.info(
        "Creating Annual Wage Growth chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual_wages["Year"],
        annual_wages["Annual Wage Growth (%)"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Annual Wage Growth"
    )

    plt.xlabel("Year")

    plt.ylabel(
        "Percent"
    )

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_wage_growth.png"
    )

    plt.close()

    logger.info(
        "Annual Wage Growth chart created."
    )


# ==========================================================
# INFLATION VS WAGE GROWTH
# ==========================================================

def plot_inflation_vs_wages(
    merged_df: pd.DataFrame
) -> None:
    """
    Plot Annual Wage Growth vs Inflation Rate.
    """

    logger.info(
        "Creating Inflation vs Wage Growth chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        merged_df["Year"],
        merged_df["Annual Wage Growth (%)"],
        marker="o",
        linewidth=2,
        label="Wage Growth",
    )

    plt.plot(
        merged_df["Year"],
        merged_df["Annual Inflation Rate (%)"],
        marker="s",
        linewidth=2,
        label="Inflation",
    )

    plt.title(
        "Annual Wage Growth vs Inflation"
    )

    plt.xlabel("Year")

    plt.ylabel("Percent")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "inflation_vs_wage_growth.png"
    )

    plt.close()

    logger.info(
        "Inflation vs Wage Growth chart created."
    )

# ==========================================================
# REAL WAGE GROWTH
# ==========================================================

def plot_real_wage_growth(
    merged_df: pd.DataFrame
) -> None:
    """
    Plot Real Wage Growth (Purchasing Power).
    """

    logger.info(
        "Creating Real Wage Growth chart..."
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        merged_df["Year"],
        merged_df["Real Wage Growth (%)"],
        marker="o",
        linewidth=2,
    )

    plt.axhline(
        y=0,
        linestyle="--",
        linewidth=1,
    )

    plt.title(
        "Real Wage Growth (Purchasing Power)"
    )

    plt.xlabel("Year")

    plt.ylabel(
        "Real Wage Growth (%)"
    )

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "real_wage_growth.png"
    )

    plt.close()

    logger.info(
        "Real Wage Growth chart created."
    )


# ==========================================================
# EMPLOYMENT TREND
# ==========================================================

def plot_employment_trend(
    employment_df: pd.DataFrame
) -> None:
    """
    Plot Annual Employment Trend.
    """

    logger.info(
        "Creating Employment Trend chart..."
    )

    employment = employment_df.copy()

    month_columns = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    employment = employment.melt(
        id_vars="Year",
        value_vars=month_columns,
        var_name="Month",
        value_name="Employment",
    )

    employment["Year"] = pd.to_numeric(
        employment["Year"],
        errors="coerce",
    )

    employment["Employment"] = pd.to_numeric(
        employment["Employment"],
        errors="coerce",
    )

    annual = (
        employment
        .groupby("Year", as_index=False)
        .agg({
            "Employment": "mean"
        })
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual["Year"],
        annual["Employment"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Annual Employment Trend"
    )

    plt.xlabel("Year")

    plt.ylabel(
        "Employment (Thousands)"
    )

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_employment.png"
    )

    plt.close()

    logger.info(
        "Employment Trend chart created."
    )


# ==========================================================
# UNEMPLOYMENT TREND
# ==========================================================

def plot_unemployment_trend(
    unemployment_df: pd.DataFrame
) -> None:
    """
    Plot Annual Unemployment Rate Trend.
    """

    logger.info(
        "Creating Unemployment Trend chart..."
    )

    unemployment = unemployment_df.copy()

    month_columns = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    unemployment = unemployment.melt(
        id_vars="Year",
        value_vars=month_columns,
        var_name="Month",
        value_name="Unemployment Rate",
    )

    unemployment["Year"] = pd.to_numeric(
        unemployment["Year"],
        errors="coerce",
    )

    unemployment["Unemployment Rate"] = pd.to_numeric(
        unemployment["Unemployment Rate"],
        errors="coerce",
    )

    annual = (
        unemployment
        .groupby("Year", as_index=False)
        .agg({
            "Unemployment Rate": "mean"
        })
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual["Year"],
        annual["Unemployment Rate"],
        marker="o",
        linewidth=2,
    )

    plt.title(
        "Annual Unemployment Rate"
    )

    plt.xlabel("Year")

    plt.ylabel(
        "Unemployment Rate (%)"
    )

    plt.grid(True)

    plt.tight_layout()

    save_plot(
        "annual_unemployment.png"
    )

    plt.close()

    logger.info(
        "Unemployment Trend chart created."
    )

# ==========================================================
# GENERATE ALL VISUALIZATIONS
# ==========================================================

def generate_all_visualizations(
    annual_cpi: pd.DataFrame,
    annual_wages: pd.DataFrame,
    merged_df: pd.DataFrame,
    employment_df: pd.DataFrame,
    unemployment_df: pd.DataFrame,
) -> None:
    """
    Generate all project visualizations.

    Parameters
    ----------
    annual_cpi : pd.DataFrame
        Annual CPI dataset with Inflation Rate.

    annual_wages : pd.DataFrame
        Annual Wage dataset with Wage Growth.

    merged_df : pd.DataFrame
        Combined CPI and Wage dataset including
        Real Wage Growth.

    employment_df : pd.DataFrame
        Monthly employment dataset.

    unemployment_df : pd.DataFrame
        Monthly unemployment dataset.
    """

    logger.info("=" * 60)
    logger.info("Generating all visualizations...")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # CPI
    # ------------------------------------------------------

    plot_cpi_trend(
        annual_cpi
    )

    plot_annual_inflation_rate(
        annual_cpi
    )

    # ------------------------------------------------------
    # Wages
    # ------------------------------------------------------

    plot_annual_wages(
        annual_wages
    )

    plot_annual_wage_growth(
        annual_wages
    )

    plot_inflation_vs_wages(
        merged_df
    )

    plot_real_wage_growth(
        merged_df
    )

    # ------------------------------------------------------
    # Employment
    # ------------------------------------------------------

    plot_employment_trend(
        employment_df
    )

    plot_unemployment_trend(
        unemployment_df
    )

    logger.info("=" * 60)
    logger.info(
        "All visualizations generated successfully."
    )
    logger.info("=" * 60)