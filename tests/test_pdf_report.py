"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
test_pdf_report.py

Author:
Monisha Sharma

Description:
Integration test for generating the Executive PDF Report.
============================================================
"""

from pathlib import Path

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
    reshape_employment_data,
    calculate_annual_average_employment,
    reshape_unemployment_data,
    calculate_annual_average_unemployment,
)

from src.dashboard_metrics import (
    create_dashboard_metrics,
)

from src.business_insights import (
    generate_business_insights,
)

from src.executive_report import (
    create_executive_report,
)

from src.pdf_report import (
    generate_pdf_report,
)

def main():
    """
    End-to-end integration test for generating
    the Executive PDF Report.
    """

    # ==========================================================
    # LOAD DATASETS
    # ==========================================================

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

    # ==========================================================
    # FEATURE ENGINEERING
    # ==========================================================

    cpi_monthly = reshape_cpi(cpi_raw)

    annual_cpi = calculate_annual_average_cpi(
        cpi_monthly
    )

    annual_cpi = calculate_annual_inflation_rate(
        annual_cpi
    )

    wage_monthly = reshape_wage_data(
        wage_raw
    )

    annual_wages = calculate_annual_average_wages(
        wage_monthly
    )

    annual_wages = calculate_annual_wage_growth(
        annual_wages
    )

    merged = merge_cpi_wages(
        annual_cpi,
        annual_wages
    )

    merged = calculate_real_wage_growth(
        merged
    )

    # ==========================================================
    # EMPLOYMENT
    # ==========================================================

    employment_monthly = reshape_employment_data(
        employment_raw
    )

    annual_employment = (
        calculate_annual_average_employment(
            employment_monthly
        )
    )

    # ==========================================================
    # UNEMPLOYMENT
    # ==========================================================

    unemployment_monthly = (
        reshape_unemployment_data(
            unemployment_raw
        )
    )

    annual_unemployment = (
        calculate_annual_average_unemployment(
            unemployment_monthly
        )
    )

     # ==========================================================
    # DASHBOARD METRICS
    # ==========================================================

    metrics_df = create_dashboard_metrics(
        merged,
        annual_employment,
        annual_unemployment,
    )

    # ==========================================================
    # BUSINESS INSIGHTS
    # ==========================================================

    business_insights = generate_business_insights(
        merged
    )

    print("\n============================")
    print("BUSINESS INSIGHTS DICTIONARY")
    print("============================")

    from pprint import pprint

    pprint(business_insights)

        # ==========================================================
    # EXECUTIVE REPORT
    # ==========================================================

    business_insight_list = []

    # Latest Economic Conditions
    latest = business_insights["Latest Economic Conditions"]

    business_insight_list.append(
        f"Latest available year ({latest['Latest Year']}) "
        f"recorded an inflation rate of "
        f"{latest['Inflation Rate']:.2f}%."
    )

    business_insight_list.append(
        f"Average hourly wages reached "
        f"${latest['Average Hourly Wage']:.2f} "
        f"in {latest['Latest Year']}."
    )

    # Highest Inflation
    highest = business_insights["Highest Inflation"]

    business_insight_list.append(
        f"Highest inflation occurred in "
        f"{highest['Year']} "
        f"at {highest['Inflation']:.2f}%."
    )

    # Highest Wage Growth
    highest_wage = business_insights["Highest Wage Growth"]

    business_insight_list.append(
        f"Highest wage growth occurred in "
        f"{highest_wage['Year']} "
        f"at {highest_wage['Wage Growth']:.2f}%."
    )

    # Lowest Real Wage Growth
    lowest = business_insights["Lowest Real Wage Growth"]

    business_insight_list.append(
        f"Weakest purchasing power occurred in "
        f"{lowest['Year']}, "
        f"when Real Wage Growth fell to "
        f"{lowest['Real Wage Growth']:.2f}%."
    )

    # Purchasing Power Trend
    business_insight_list.append(
        business_insights["Purchasing Power Trend"]
    )

    # Executive Report
    executive_summary = create_executive_report(
        merged,
        business_insight_list,
    )

    # ==========================================================
    # GENERATE PDF REPORT
    # ==========================================================

    pdf_path = generate_pdf_report(
        executive_summary=executive_summary,
        metrics_df=metrics_df,
        business_insights=business_insights,
    )

    # ==========================================================
    # VERIFY PDF CREATED
    # ==========================================================

    pdf_path = Path(pdf_path)

    assert pdf_path.exists(), (
        "PDF report was not created."
    )

    assert pdf_path.stat().st_size > 0, (
        "PDF report is empty."
    )

    print()

    print("=" * 70)
    print("PDF REPORT GENERATED SUCCESSFULLY")
    print("=" * 70)

    print(f"\nLocation:\n{pdf_path}")

    print(
        f"\nFile Size: "
        f"{pdf_path.stat().st_size:,} bytes"
    )

# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    main()      