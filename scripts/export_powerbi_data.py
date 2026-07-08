"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Script:
export_powerbi_data.py

Author:
Monisha Sharma

Description:
Exports curated datasets for Power BI.

This script:

• Builds the master analytical fact table
• Creates dashboard KPI metrics
• Exports CSV files for Power BI

Output

powerbi/
└── exported_data/
    ├── FactEconomicIndicators.csv
    └── DashboardKPIs.csv

============================================================
"""

from pathlib import Path

from src.logger import logger

from src.fact_table import (
    build_fact_economic_indicators,
)

from src.dashboard_metrics import (
    create_dashboard_metrics,
)

# ==========================================================
# EXPORT DIRECTORY
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXPORT_DIR = (
    PROJECT_ROOT
    / "powerbi"
    / "exported_data"
)

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

FACT_FILE = (
    EXPORT_DIR
    / "FactEconomicIndicators.csv"
)

KPI_FILE = (
    EXPORT_DIR
    / "DashboardKPIs.csv"
)

# ==========================================================
# EXPORT POWER BI DATA
# ==========================================================

def export_powerbi_data():
    """
    Build and export datasets for Power BI.
    """

    logger.info("=" * 60)
    logger.info("Exporting Power BI datasets...")
    logger.info("=" * 60)

    # ------------------------------------------------------
    # BUILD FACT TABLE
    # ------------------------------------------------------

    (
        fact_table,
        annual_employment,
        annual_unemployment,
    ) = build_fact_economic_indicators()

    # ------------------------------------------------------
    # CREATE DASHBOARD KPIs
    # ------------------------------------------------------

    dashboard_kpis = create_dashboard_metrics(
        fact_table,
        annual_employment,
        annual_unemployment,
    )

    logger.info(
        "Power BI datasets created successfully."
    )

    # ------------------------------------------------------
    # EXPORT FACT TABLE
    # ------------------------------------------------------

    logger.info(
        "Exporting FactEconomicIndicators.csv..."
    )

    fact_table.to_csv(
        FACT_FILE,
        index=False
    )

    logger.info(
        "Fact table exported successfully."
    )

    # ------------------------------------------------------
    # EXPORT DASHBOARD KPIs
    # ------------------------------------------------------

    logger.info(
        "Exporting DashboardKPIs.csv..."
    )

    dashboard_kpis.to_csv(
        KPI_FILE,
        index=False
    )

    logger.info(
        "Dashboard KPI table exported successfully."
    )

    # ------------------------------------------------------
    # EXPORT SUMMARY
    # ------------------------------------------------------

    logger.info("=" * 60)

    logger.info(
        f"Fact Table Shape: {fact_table.shape}"
    )

    logger.info(
        f"Dashboard KPI Shape: {dashboard_kpis.shape}"
    )

    logger.info(
        f"Fact Table Export: {FACT_FILE}"
    )

    logger.info(
        f"Dashboard KPI Export: {KPI_FILE}"
    )

    logger.info("=" * 60)

    logger.info(
        "Power BI export completed successfully."
    )

    return (
        fact_table,
        dashboard_kpis,
    )


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    fact_table, dashboard_kpis = (
        export_powerbi_data()
    )

    print()
    print("=" * 80)
    print("POWER BI EXPORT SUMMARY")
    print("=" * 80)

    print()

    print("FactEconomicIndicators")
    print("-" * 80)
    print(fact_table.head())

    print()
    print("Shape")
    print(fact_table.shape)

    print()
    print("Columns")
    print(fact_table.columns.tolist())

    print()

    print("DashboardKPIs")
    print("-" * 80)
    print(dashboard_kpis)

    print()
    print("Shape")
    print(dashboard_kpis.shape)

    print()

    print("CSV Files Created")
    print("-" * 80)
    print(FACT_FILE)
    print(KPI_FILE)

    print()
    print("=" * 80)
    print("Power BI Export Completed Successfully")
    print("=" * 80)