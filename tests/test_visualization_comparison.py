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
)

from src.visualization import plot_inflation_vs_wages


# Load datasets
datasets = load_all_datasets()

# CPI
cpi = parse_report(datasets["cpi"])
cpi = reshape_cpi(cpi)
cpi = calculate_annual_average_cpi(cpi)
cpi = calculate_annual_inflation_rate(cpi)

# Wages
wages = parse_report(datasets["average_hourly_earnings"])
wages = reshape_wage_data(wages)
wages = calculate_annual_average_wages(wages)
wages = calculate_annual_wage_growth(wages)

# Merge
merged = merge_cpi_wages(cpi, wages)

# Plot
plot_inflation_vs_wages(merged)