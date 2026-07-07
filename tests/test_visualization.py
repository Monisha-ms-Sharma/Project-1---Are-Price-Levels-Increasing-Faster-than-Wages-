from src.data_loader import load_all_datasets
from src.report_parser import parse_report

from src.feature_engineering import (
    reshape_cpi,
    calculate_annual_average_cpi,
)

from src.visualization import plot_cpi_trend


# Load all datasets
datasets = load_all_datasets()

# Parse CPI report
cpi = parse_report(
    datasets["cpi"]
)

# Reshape CPI
cpi = reshape_cpi(cpi)

# Calculate annual average CPI
annual_cpi = calculate_annual_average_cpi(cpi)

# Plot CPI trend
plot_cpi_trend(annual_cpi)