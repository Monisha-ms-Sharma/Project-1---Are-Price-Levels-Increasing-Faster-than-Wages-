"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
run_pipeline.py

Author:
Monisha Sharma

Description:
End-to-End Business Analytics Pipeline.

Pipeline Steps
--------------
1. Load BLS datasets
2. Parse Excel reports
3. Feature Engineering
4. Statistical Analysis
5. Correlation Analysis
6. Dashboard Metrics
7. Business Insights
8. Executive Report
9. Visualizations
10. PDF Report

============================================================
"""

from src.logger import logger

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

from src.visualization import (
    generate_all_visualizations,
)

from src.statistical_analysis import (
    descriptive_statistics,
)

from src.correlation_analysis import (
    calculate_correlation_matrix,
)

from src.heatmap import (
    plot_correlation_heatmap,
)


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():
    """
    Execute the complete analytics pipeline.
    """
    try:
        logger.info("=" * 60)
        logger.info("STARTING ANALYTICS PIPELINE")
        logger.info("=" * 60)

        # ======================================================
        # LOAD DATASETS
        # ======================================================

        logger.info("Loading datasets...")

        datasets = load_all_datasets()

        # ======================================================
        # PARSE REPORTS
        # ======================================================

        logger.info("Parsing BLS reports...")

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
        # CPI FEATURE ENGINEERING
        # ======================================================

        logger.info("Processing CPI...")

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
        # WAGE FEATURE ENGINEERING
        # ======================================================

        logger.info("Processing Wage data...")

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
        # MERGE DATASETS
        # ======================================================

        logger.info("Merging CPI and Wage datasets...")

        merged = merge_cpi_wages(
            annual_cpi,
            annual_wages,
        )

        merged = calculate_real_wage_growth(
            merged
        )

        # ======================================================
        # EMPLOYMENT
        # ======================================================

        logger.info("Processing Employment...")

        employment_monthly = reshape_employment_data(
            employment_raw
        )

        annual_employment = (
            calculate_annual_average_employment(
                employment_monthly
            )
        )

        # ======================================================
        # UNEMPLOYMENT
        # ======================================================

        logger.info("Processing Unemployment...")

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
        # ======================================================
        # DASHBOARD METRICS
        # ======================================================

        logger.info("Creating dashboard metrics...")

        metrics_df = create_dashboard_metrics(
            merged,
            annual_employment,
            annual_unemployment,
        )

        # ======================================================
        # STATISTICAL ANALYSIS
        # ======================================================

        logger.info("Running descriptive statistics...")

        descriptive_statistics(
            merged
        )

        logger.info(
            "Descriptive statistics completed."
        )

        # ======================================================
        # CORRELATION ANALYSIS
        # ======================================================

        logger.info("Running correlation analysis...")

        correlation_matrix = (
            calculate_correlation_matrix(
                merged
            )
        )

        logger.info(
            "Correlation analysis completed."
        )

        # ======================================================
        # BUSINESS INSIGHTS
        # ======================================================

        logger.info("Generating business insights...")

        business_insights = (
            generate_business_insights(
                merged
            )
        )

        # ======================================================
        # EXECUTIVE REPORT
        # ======================================================

        logger.info(
            "Creating executive report..."
        )

        business_insight_list = []

        latest = business_insights[
            "Latest Economic Conditions"
        ]

        business_insight_list.append(
            f"Latest available year ({latest['Year']}) "
            f"recorded an inflation rate of "
            f"{latest['Inflation Rate']:.2f}%."
        )

        highest = business_insights[
            "Highest Inflation"
        ]

        business_insight_list.append(
            f"Highest inflation occurred in "
            f"{highest['Year']} at "
            f"{highest['Inflation Rate']:.2f}%."
        )

        highest_wage = business_insights[
            "Highest Wage Growth"
        ]

        business_insight_list.append(
            f"Highest wage growth occurred in "
            f"{highest_wage['Year']} at "
            f"{highest_wage['Wage Growth']:.2f}%."
        )

        lowest = business_insights[
            "Lowest Real Wage Growth"
        ]

        business_insight_list.append(
            f"Weakest purchasing power "
            f"occurred in {lowest['Year']}, "
            f"when Real Wage Growth fell to "
            f"{lowest['Real Wage Growth']:.2f}%."
        )

        executive_summary = (
            create_executive_report(
                merged,
                business_insight_list,
            )
        )

        logger.info(
            "Executive report completed."
        )
        # ======================================================
        # VISUALIZATIONS
        # ======================================================

        logger.info(
            "Generating visualizations..."
        )

        generate_all_visualizations(
            annual_cpi,
            annual_wages,
            merged,
            employment_raw,
            unemployment_raw,
        )

        logger.info(
            "Visualizations completed."
        )

        # ======================================================
        # CORRELATION HEATMAP
        # ======================================================

        logger.info(
            "Generating correlation heatmap..."
        )

        plot_correlation_heatmap(
            correlation_matrix
        )

        logger.info(
            "Correlation heatmap created."
        )

        # ======================================================
        # GENERATE PDF REPORT
        # ======================================================

        logger.info(
            "Generating Executive PDF Report..."
        )

        pdf_path = generate_pdf_report(
            executive_summary=executive_summary,
            metrics_df=metrics_df,
            business_insights=business_insights,
        )

        logger.info(
            f"PDF report saved to {pdf_path}"
        )
        # ======================================================
        # PIPELINE COMPLETED
        # ======================================================

        logger.info("=" * 60)
        logger.info("ANALYTICS PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 60)

        print()
        print("=" * 70)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 70)

        print("\nOutputs Generated")

        print("- Dashboard Metrics")
        print("- Business Insights")
        print("- Executive Report")
        print("- Statistical Analysis")
        print("- Correlation Analysis")
        print("- Correlation Heatmap")
        print("- Visualizations")
        print("- Executive PDF Report")

        print("\nThank you for using the")
        print("U.S. Inflation, Wage Growth & Purchasing Power")
        print("Analysis Pipeline.")

    except Exception as error:

        logger.exception(
            "Pipeline execution failed."
        )

        print()
        print("=" * 70)
        print("PIPELINE FAILED")
        print("=" * 70)

        print(error)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    main()