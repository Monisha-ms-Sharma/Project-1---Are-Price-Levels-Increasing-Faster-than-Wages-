"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
report_parser.py

Author:
Monisha Sharma

Description:
Parses raw BLS Excel report exports into clean,
analysis-ready DataFrames.
============================================================
"""

import pandas as pd

from src.logger import logger


def parse_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse a raw BLS Excel report into a clean DataFrame.
    """

    logger.info("Parsing BLS report...")

    header_row = None

    # Find the row whose first column is "Year"
    for i in range(len(df)):

        first_cell = str(df.iloc[i, 0]).strip()

        if first_cell == "Year":

            header_row = i
            break

    if header_row is None:
        raise ValueError("Could not locate the header row.")

    logger.info(f"Header row found at row {header_row}")

    # Set the header
    df.columns = df.iloc[header_row]

    # Keep only the data
    df = df.iloc[header_row + 1:].copy()

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Clean column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace("\n", " ", regex=False)
    )

    logger.info(
        f"Successfully parsed dataset "
        f"({df.shape[0]} rows × {df.shape[1]} columns)"
    )

    return df