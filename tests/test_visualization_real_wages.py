"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Test:
Real Wage Growth Visualization

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
)

from src.visualization import plot_real_wage_growth


# ----------------------------------------------------------
# Load datasets
# ----------------------------------------------------------

datasets = load_all_datasets()


# ----------------------------------------------------------
# CPI Pipeline
# ----------------------------------------------------------

cpi = parse_report(datasets["cpi"])
cpi = reshape_cpi(cpi)
cpi = calculate_annual_average_cpi(cpi)
cpi = calculate_annual_inflation_rate(cpi)


# ----------------------------------------------------------
# Wage Pipeline
# ----------------------------------------------------------

wage = parse_report(datasets["average_hourly_earnings"])
wage = reshape_wage_data(wage)
wage = calculate_annual_average_wages(wage)
wage = calculate_annual_wage_growth(wage)


# ----------------------------------------------------------
# Merge datasets
# ----------------------------------------------------------

merged = merge_cpi_wages(cpi, wage)
print("\nMERGED COLUMNS")
print("=" * 60)
print(merged.columns.tolist())

print("\nMERGED DATA")
print("=" * 60)
print(merged.head())

# ----------------------------------------------------------
# Calculate Real Wage Growth
# ----------------------------------------------------------

merged = calculate_real_wage_growth(merged)


# ----------------------------------------------------------
# Create visualization
# ----------------------------------------------------------

plot_real_wage_growth(merged)