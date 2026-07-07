"""
Test the Data Validation module.
"""

from src.data_loader import load_all_datasets
from src.data_validation import validate_dataset


def main():

    datasets = load_all_datasets()

    for name, df in datasets.items():

        validate_dataset(name, df)


if __name__ == "__main__":

    main()