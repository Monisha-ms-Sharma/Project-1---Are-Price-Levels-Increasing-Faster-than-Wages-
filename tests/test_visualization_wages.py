from src.data_loader import load_all_datasets
from src.report_parser import parse_report

from src.feature_engineering import (
    reshape_wage_data,
    calculate_annual_average_wages,
)

from src.visualization import plot_annual_wages


datasets = load_all_datasets()

raw = parse_report(
    datasets["average_hourly_earnings"]
)

monthly = reshape_wage_data(raw)

annual = calculate_annual_average_wages(monthly)

plot_annual_wages(annual)