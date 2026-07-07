"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
test_visualization.py

Author:
Monisha Sharma

Description:
Integration test for generating all project visualizations.
============================================================
"""

from pathlib import Path

from src.config import IMAGES_DIR
from src.data_loader import load_all_datasets
from src.report_parser import parse_report

from src.feature_engineering import (
    reshape_cpi,
    calculate_annual_average_cpi,
    calculate_annual_inflation_rate,
    reshape_wage_data,
    calculate_annual_average_wages,
    calculate_annual_wage_growth,
    merge_cpi_wages,
    calculate_real_wage_growth,
)

from src.visualization import (
    generate_all_visualizations,
)


def main():
    """
    Generate all project visualizations.
    """

    # ======================================================
    # LOAD DATASETS
    # ======================================================

    datasets = load_all_datasets()

    cpi_raw = parse_report(
        datasets["cpi"]
    )

    wage_raw = parse_report(
        datasets["average_hourly_earnings"]
    )

    employment_raw = parse_report(
        datasets["employment"]
    )

    unemployment_raw = parse_report(
        datasets["unemployment"]
    )

    # ======================================================
    # CPI
    # ======================================================

    cpi_monthly = reshape_cpi(
        cpi_raw
    )

    annual_cpi = calculate_annual_average_cpi(
        cpi_monthly
    )

    annual_cpi = calculate_annual_inflation_rate(
        annual_cpi
    )

    # ======================================================
    # WAGES
    # ======================================================

    wage_monthly = reshape_wage_data(
        wage_raw
    )

    annual_wages = calculate_annual_average_wages(
        wage_monthly
    )

    annual_wages = calculate_annual_wage_growth(
        annual_wages
    )

    # ======================================================
    # MERGE
    # ======================================================

    merged = merge_cpi_wages(
        annual_cpi,
        annual_wages,
    )

    merged = calculate_real_wage_growth(
        merged
    )

    # ======================================================
    # GENERATE ALL CHARTS
    # ======================================================

    generate_all_visualizations(
        annual_cpi,
        annual_wages,
        merged,
        employment_raw,
        unemployment_raw,
    )

    # ======================================================
    # VERIFY OUTPUTS
    # ======================================================

    expected_files = [

        "annual_average_cpi.png",

        "annual_inflation_rate.png",

        "annual_average_wage.png",

        "annual_wage_growth.png",

        "inflation_vs_wage_growth.png",

        "real_wage_growth.png",

        "annual_employment.png",

        "annual_unemployment.png",

    ]

    print()
    print("=" * 70)
    print("VISUALIZATION TEST RESULTS")
    print("=" * 70)

    for filename in expected_files:

        image = IMAGES_DIR / filename

        assert image.exists(), (
            f"{filename} was not created."
        )

        print(f"✓ {filename}")

    print()
    print("=" * 70)
    print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
    print("=" * 70)


# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    main()