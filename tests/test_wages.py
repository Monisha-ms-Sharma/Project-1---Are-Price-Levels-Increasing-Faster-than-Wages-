from src.data_loader import load_all_datasets
from src.report_parser import parse_report
from src.feature_engineering import (
    reshape_wage_data,
    calculate_monthly_wage_growth,
    calculate_annual_average_wages,
    calculate_annual_wage_growth,
)

datasets = load_all_datasets()

df = parse_report(
    datasets["average_hourly_earnings"]
)

wage = reshape_wage_data(df)

wage = calculate_monthly_wage_growth(wage)

annual_wages = calculate_annual_average_wages(wage)

annual_wages = calculate_annual_wage_growth(
    annual_wages
)

print()
print("=" * 80)
print("ANNUAL WAGE GROWTH")
print("=" * 80)

print(annual_wages)

print()
print(annual_wages.info())