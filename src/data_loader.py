"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
data_loader.py

Author:
Monisha Sharma

Description:
Loads official U.S. Bureau of Labor Statistics (BLS)
datasets into pandas DataFrames.

Responsibilities
----------------
• Validate dataset paths
• Inspect Excel workbooks
• Load Excel worksheets
• Log processing details
• Return datasets as pandas DataFrames

Future Enhancement
------------------
Replace Excel loading with BLS REST API downloads
without changing downstream modules.
============================================================
"""

from pathlib import Path

import pandas as pd

from src.config import (
    CPI_FILE,
    AVERAGE_HOURLY_EARNINGS_FILE,
    TOTAL_NONFARM_EMPLOYMENT_FILE,
    UNEMPLOYMENT_RATE_FILE,
    ECI_PRIVATE_WAGES_FILE,
    ECI_TOTAL_COMPENSATION_FILE,
)

from src.logger import logger

# ==========================================================
# DATASET CONFIGURATION
# ==========================================================

DATASETS = {
    "cpi": CPI_FILE,
    "average_hourly_earnings": AVERAGE_HOURLY_EARNINGS_FILE,
    "employment": TOTAL_NONFARM_EMPLOYMENT_FILE,
    "unemployment": UNEMPLOYMENT_RATE_FILE,
    "eci_private_wages": ECI_PRIVATE_WAGES_FILE,
    "eci_total_compensation": ECI_TOTAL_COMPENSATION_FILE,
}


# ==========================================================
# VALIDATE FILE
# ==========================================================

def validate_file(file_path: Path) -> bool:
    """
    Verify that a dataset exists.
    """

    if file_path.exists():

        logger.info(f"✓ Found: {file_path.name}")

        return True

    logger.error(f"✗ Missing dataset: {file_path}")

    return False


# ==========================================================
# INSPECT EXCEL WORKBOOK
# ==========================================================

def inspect_workbook(file_path: Path) -> list[str]:
    """
    Return the worksheet names contained
    within an Excel workbook.
    """

    workbook = pd.ExcelFile(file_path)

    logger.info(
        f"Workbook contains worksheets: {workbook.sheet_names}"
    )

    return workbook.sheet_names


# ==========================================================
# LOAD SINGLE DATASET
# ==========================================================

def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load a single Excel workbook.
    """

    logger.info(f"Loading dataset: {file_path.name}")

    workbook = pd.ExcelFile(file_path)

    sheet_name = workbook.sheet_names[0]

    logger.info(f"Using worksheet: {sheet_name}")

    df = pd.read_excel(
        workbook,
        sheet_name=sheet_name,
    )

    memory = df.memory_usage(deep=True).sum() / 1024

    logger.info(
        f"Rows={df.shape[0]:,} | "
        f"Columns={df.shape[1]} | "
        f"Memory={memory:.1f} KB"
    )

    return df


# ==========================================================
# LOAD ALL DATASETS
# ==========================================================

def load_all_datasets() -> dict[str, pd.DataFrame]:
    """
    Load every project dataset.
    """

    datasets = {}

    logger.info("=" * 60)
    logger.info("Starting Data Acquisition")
    logger.info("=" * 60)

    for dataset_name, file_path in DATASETS.items():

        if not validate_file(file_path):
            continue

        try:

            inspect_workbook(file_path)

            datasets[dataset_name] = load_dataset(file_path)

        except Exception:

            logger.exception(
                f"Unable to load {file_path.name}"
            )

            raise

    logger.info("=" * 60)
    logger.info(
        f"Successfully loaded {len(datasets)} datasets."
    )
    logger.info("=" * 60)

    return datasets


# ==========================================================
# DATASET SUMMARY
# ==========================================================

def dataset_summary(
    datasets: dict[str, pd.DataFrame],
) -> None:
    """
    Log a summary of every loaded dataset.
    """

    logger.info("")

    logger.info("=" * 60)
    logger.info("Dataset Summary")
    logger.info("=" * 60)

    for name, df in datasets.items():

        memory = df.memory_usage(deep=True).sum() / 1024

        logger.info(
            f"{name:<30}"
            f"{df.shape[0]:>6,} rows"
            f"{df.shape[1]:>5} cols"
            f"{memory:>10.1f} KB"
        )

    logger.info("=" * 60)