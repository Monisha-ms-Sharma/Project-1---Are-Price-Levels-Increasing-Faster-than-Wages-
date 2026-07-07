"""
============================================================
Project:
U.S. Inflation, Wage Growth &
Purchasing Power Analysis

Test:
Dashboard Metrics

Author:
Monisha Sharma
============================================================
"""

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


datasets = load_all_datasets()


# ==========================================================
# CPI
# ==========================================================

cpi = parse_report(
    datasets["cpi"]
)

cpi = reshape_cpi(cpi)

cpi = calculate_annual_average_cpi(cpi)

cpi = calculate_annual_inflation_rate(cpi)


# ==========================================================
# WAGES
# ==========================================================

wages = parse_report(
    datasets["average_hourly_earnings"]
)

wages = reshape_wage_data(wages)

wages = calculate_annual_average_wages(
    wages
)

wages = calculate_annual_wage_growth(
    wages
)


# ==========================================================
# MERGE
# ==========================================================

merged = merge_cpi_wages(
    cpi,
    wages
)

merged = calculate_real_wage_growth(
    merged
)


# ==========================================================
# EMPLOYMENT
# ==========================================================

employment = parse_report(
    datasets["employment"]
)

employment = reshape_employment_data(
    employment
)

employment = calculate_annual_average_employment(
    employment
)


# ==========================================================
# UNEMPLOYMENT
# ==========================================================

unemployment = parse_report(
    datasets["unemployment"]
)

unemployment = reshape_unemployment_data(
    unemployment
)

unemployment = (
    calculate_annual_average_unemployment(
        unemployment
    )
)


# ==========================================================
# DASHBOARD
# ==========================================================

dashboard = create_dashboard_metrics(
    merged,
    employment,
    unemployment
)


print()

print("=" * 60)
print("DASHBOARD METRICS")
print("=" * 60)

print(dashboard)

print()

print("Columns")

print("-" * 60)

print(dashboard.columns.tolist())

print()

print("Shape")

print("-" * 60)

print(dashboard.shape)