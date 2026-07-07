from src.data_loader import (
    load_all_datasets,
    dataset_summary,
)

datasets = load_all_datasets()

dataset_summary(datasets)