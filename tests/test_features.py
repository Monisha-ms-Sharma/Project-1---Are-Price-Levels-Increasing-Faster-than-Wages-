"""
Test Feature Engineering
"""

from src.data_loader import load_all_datasets
from src.report_parser import parse_report
from src.preprocessing import preprocess

from src.feature_engineering import (
    reshape_cpi,
    calculate_monthly_inflation,
    calculate_annual_average_cpi,
    calculate_annual_inflation_rate
)

datasets = load_all_datasets()

cpi = datasets["cpi"]

cpi = parse_report(cpi)

cpi = preprocess(cpi)

cpi = reshape_cpi(cpi)

cpi = calculate_monthly_inflation(cpi)

annual_cpi = calculate_annual_average_cpi(cpi)

annual_cpi = calculate_annual_inflation_rate(annual_cpi)

print()

print("=" * 80)
print("ANNUAL INFLATION RATE")
print("=" * 80)

print(annual_cpi)

print()

print(annual_cpi.info())

from src.config import PROCESSED_DATA_DIR
from src.feature_engineering import save_feature_dataset

output_file = (
    PROCESSED_DATA_DIR /
    "features" /
    "annual_cpi.csv"
)

save_feature_dataset(
    annual_cpi,
    output_file
)