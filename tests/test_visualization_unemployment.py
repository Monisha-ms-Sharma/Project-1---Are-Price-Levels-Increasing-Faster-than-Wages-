from src.data_loader import load_all_datasets
from src.report_parser import parse_report
from src.visualization import plot_unemployment_trend

# ======================================================
# LOAD DATA
# ======================================================

datasets = load_all_datasets()

unemployment = parse_report(
    datasets["unemployment"]
)

plot_unemployment_trend(
    unemployment
)