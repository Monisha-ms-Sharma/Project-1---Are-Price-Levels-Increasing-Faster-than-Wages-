from src.data_loader import load_all_datasets
from src.report_parser import parse_report

from src.feature_engineering import (
    reshape_cpi,
    calculate_annual_average_cpi,
    reshape_wage_data,
    calculate_annual_average_wages,
    merge_cpi_wages
)

datasets = load_all_datasets()

# -----------------------------
# CPI
# -----------------------------

cpi = parse_report(datasets["cpi"])

cpi = reshape_cpi(cpi)

annual_cpi = calculate_annual_average_cpi(cpi)

# -----------------------------
# WAGES
# -----------------------------

wages = parse_report(
    datasets["average_hourly_earnings"]
)

wages = reshape_wage_data(wages)

annual_wages = calculate_annual_average_wages(
    wages
)

# -----------------------------
# MERGE
# -----------------------------

merged = merge_cpi_wages(
    annual_cpi,
    annual_wages
)

print()
print("=" * 80)
print("MERGED DATA")
print("=" * 80)

print(merged)

print()
print(merged.info())