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

Current Visualizations
----------------------
• CPI Trend

Future Visualizations
---------------------
• Wage Trend
• Inflation vs Wage
• Real Wage Growth
• Correlation Heatmap
• Histograms
• Boxplots
============================================================
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.logger import logger


# ==========================================================
# OUTPUT DIRECTORY
# ==========================================================

IMAGE_DIR = Path("images")

IMAGE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================================
# SAVE FIGURE
# ==========================================================

def save_plot(
    filename: str
) -> None:
    """
    Save the current matplotlib figure.
    """

    output_file = IMAGE_DIR / filename

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
        linewidth=2
    )

    plt.title(
        "Average Annual CPI"
    )

    plt.xlabel("Year")

    plt.ylabel("Average CPI")

    plt.grid(True)

    save_plot(
        "annual_cpi_trend.png"
    )

    plt.show()

    logger.info(
        "CPI Trend chart created."
    )

def plot_annual_wages(df):
    """
    Plot Annual Average Hourly Wage Trend.
    """

    logger.info("Creating Annual Wage Trend chart...")

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Year"],
        df["Average Hourly Wage"],
        marker="o",
        linewidth=2,
    )

    plt.title("Average Hourly Wage (2016–2026)")
    plt.xlabel("Year")
    plt.ylabel("Average Hourly Wage ($/hour)")

    plt.grid(True)

    plt.tight_layout()

    output_path = "images/annual_wage_trend.png"

    plt.savefig(output_path)

    plt.close()

    logger.info(f"Saved plot: {output_path}")
    logger.info("Annual Wage Trend chart created.")

def plot_inflation_vs_wages(df):
    """
    Plot Annual Wage Growth vs Inflation Rate.
    """

    logger.info("Creating Inflation vs Wage Growth chart...")

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Year"],
        df["Annual Wage Growth (%)"],
        marker="o",
        linewidth=2,
        label="Wage Growth",
    )

    plt.plot(
        df["Year"],
        df["Annual Inflation Rate (%)"],
        marker="s",
        linewidth=2,
        label="Inflation",
    )

    plt.title("Annual Wage Growth vs Inflation")

    plt.xlabel("Year")
    plt.ylabel("Percent")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    output_path = "images/inflation_vs_wage_growth.png"

    plt.savefig(output_path)

    plt.close()

    logger.info(f"Saved plot: {output_path}")
    logger.info("Inflation vs Wage Growth chart created.")

def plot_real_wage_growth(df):
    """
    Plot Real Wage Growth (Purchasing Power).
    """

    logger.info("Creating Real Wage Growth chart...")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Year"],
        df["Real Wage Growth (%)"],
        marker="o",
        linewidth=2
    )

    plt.axhline(
        y=0,
        linestyle="--",
        linewidth=1
    )

    plt.title("Real Wage Growth (Purchasing Power)")
    plt.xlabel("Year")
    plt.ylabel("Real Wage Growth (%)")

    plt.grid(True)

    save_plot("real_wage_growth.png")

    plt.close()

    logger.info("Real Wage Growth chart created.")

# ==========================================================
# EMPLOYMENT TREND
# ==========================================================

def plot_employment_trend(
    employment_df
):
    """
    Plot Annual Employment Trend.
    """

    logger.info("Creating Employment Trend chart...")

    import matplotlib.pyplot as plt
    import pandas as pd

    # ---------------------------------------------
    # Prepare Data
    # ---------------------------------------------

    employment = employment_df.copy()

    month_columns = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    employment = employment.melt(
        id_vars="Year",
        value_vars=month_columns,
        var_name="Month",
        value_name="Employment"
    )

    employment["Employment"] = pd.to_numeric(
        employment["Employment"],
        errors="coerce"
    )

    employment["Year"] = pd.to_numeric(
        employment["Year"],
        errors="coerce"
    )

    annual = (
        employment
        .groupby("Year", as_index=False)
        .agg({
            "Employment": "mean"
        })
    )

    # ---------------------------------------------
    # Plot
    # ---------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual["Year"],
        annual["Employment"],
        marker="o",
        linewidth=2
    )

    plt.title(
        "Annual Employment Trend",
        fontsize=15,
        weight="bold"
    )

    plt.xlabel("Year")
    plt.ylabel("Employment (Thousands)")

    plt.grid(True)

    save_plot(
        "employment_trend.png"
    )

    logger.info("Employment Trend chart created.")

# ==========================================================
# UNEMPLOYMENT TREND
# ==========================================================

def plot_unemployment_trend(
    unemployment_df
):
    """
    Plot Annual Unemployment Rate Trend.
    """

    logger.info("Creating Unemployment Trend chart...")

    import matplotlib.pyplot as plt
    import pandas as pd

    # ---------------------------------------------
    # Prepare Data
    # ---------------------------------------------

    unemployment = unemployment_df.copy()

    month_columns = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    unemployment = unemployment.melt(
        id_vars="Year",
        value_vars=month_columns,
        var_name="Month",
        value_name="Unemployment Rate"
    )

    unemployment["Year"] = pd.to_numeric(
        unemployment["Year"],
        errors="coerce"
    )

    unemployment["Unemployment Rate"] = pd.to_numeric(
        unemployment["Unemployment Rate"],
        errors="coerce"
    )

    annual = (
        unemployment
        .groupby("Year", as_index=False)
        .agg({
            "Unemployment Rate": "mean"
        })
    )

    # ---------------------------------------------
    # Plot
    # ---------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        annual["Year"],
        annual["Unemployment Rate"],
        marker="o",
        linewidth=2
    )

    plt.title(
        "Annual Unemployment Rate",
        fontsize=15,
        weight="bold"
    )

    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")

    plt.grid(True)

    save_plot(
        "unemployment_trend.png"
    )

    logger.info("Unemployment Trend chart created.")