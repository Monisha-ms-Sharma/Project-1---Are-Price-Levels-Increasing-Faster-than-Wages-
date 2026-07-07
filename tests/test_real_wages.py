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
    calculate_real_wage_growth
)

datasets = load_all_datasets()

# --------------------------------------------------
# CPI
# --------------------------------------------------

cpi = parse_report(datasets["cpi"])

cpi = reshape_cpi(cpi)

annual_cpi = calculate_annual_average_cpi(cpi)

annual_inflation = calculate_annual_inflation_rate(
    annual_cpi
)

# --------------------------------------------------
# WAGES
# --------------------------------------------------

wages = parse_report(
    datasets["average_hourly_earnings"]
)

wages = reshape_wage_data(wages)

annual_wages = calculate_annual_average_wages(
    wages
)

annual_wage_growth = calculate_annual_wage_growth(
    annual_wages
)

# --------------------------------------------------
# MERGE
# --------------------------------------------------

merged = merge_cpi_wages(
    annual_cpi,
    annual_wages
)

# --------------------------------------------------
# REAL WAGE GROWTH
# --------------------------------------------------

real = calculate_real_wage_growth(
    merged,
    annual_wage_growth,
    annual_inflation
)

print()
print("=" * 80)
print("REAL WAGE GROWTH")
print("=" * 80)

print(real)

print()
print(real.info())