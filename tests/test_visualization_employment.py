from src.data_loader import load_all_datasets
from src.report_parser import parse_report
from src.visualization import plot_employment_trend

# ======================================================
# LOAD DATA
# ======================================================

datasets = load_all_datasets()

employment = parse_report(
    datasets["employment"]
)

plot_employment_trend(
    employment
)