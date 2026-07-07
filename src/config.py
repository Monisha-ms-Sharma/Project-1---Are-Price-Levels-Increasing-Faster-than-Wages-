"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
config.py

Author:
Monisha Sharma

Description:
Central configuration file for the project.

This module defines:

• Project directories
• Dataset locations
• Report folders
• Image folders
• Logging paths
• API configuration
• Global project settings

By centralizing configuration, the project avoids
hard-coded paths and improves maintainability.

============================================================
"""

from pathlib import Path

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = (
    "U.S. Inflation, Wage Growth & Purchasing Power Analysis"
)

PROJECT_VERSION = "1.0.0"

AUTHOR = "Monisha Sharma"

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA DIRECTORIES
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
RAW_EXCEL_DIR = RAW_DATA_DIR / "excel"
RAW_API_DIR = RAW_DATA_DIR / "api"
RAW_CSV_DIR = RAW_DATA_DIR / "csv"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

# ==========================================================
# DOCUMENTATION
# ==========================================================

DOCS_DIR = PROJECT_ROOT / "docs"

# ==========================================================
# NOTEBOOKS
# ==========================================================

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# ==========================================================
# REPORTS
# ==========================================================

REPORTS_DIR = PROJECT_ROOT / "reports"

DATA_PROFILE_DIR = REPORTS_DIR / "data_profile"

FIGURES_DIR = REPORTS_DIR / "figures"

TABLES_DIR = REPORTS_DIR / "tables"

EXECUTIVE_REPORT_DIR = REPORTS_DIR / "executive_report"

# ==========================================================
# IMAGES
# ==========================================================

IMAGES_DIR = PROJECT_ROOT / "images"

ARCHITECTURE_IMAGES_DIR = IMAGES_DIR / "architecture"

CHART_IMAGES_DIR = IMAGES_DIR / "charts"

DASHBOARD_IMAGES_DIR = IMAGES_DIR / "dashboards"

# ==========================================================
# SQL
# ==========================================================

SQL_DIR = PROJECT_ROOT / "sql"

# ==========================================================
# LOGS
# ==========================================================

LOGS_DIR = PROJECT_ROOT / "logs"

LOG_FILE = LOGS_DIR / "project.log"

# ==========================================================
# SOURCE CODE
# ==========================================================

SRC_DIR = PROJECT_ROOT / "src"

# ==========================================================
# TESTS
# ==========================================================

TESTS_DIR = PROJECT_ROOT / "tests"

# ==========================================================
# SCRIPTS
# ==========================================================

SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# ==========================================================
# CREATE PROJECT DIRECTORIES
# ==========================================================

PROJECT_DIRECTORIES = [

    DATA_DIR,

    RAW_DATA_DIR,
    RAW_EXCEL_DIR,
    RAW_API_DIR,
    RAW_CSV_DIR,

    INTERIM_DATA_DIR,

    PROCESSED_DATA_DIR,

    EXTERNAL_DATA_DIR,

    DOCS_DIR,

    NOTEBOOKS_DIR,

    REPORTS_DIR,
    DATA_PROFILE_DIR,
    FIGURES_DIR,
    TABLES_DIR,
    EXECUTIVE_REPORT_DIR,

    IMAGES_DIR,
    ARCHITECTURE_IMAGES_DIR,
    CHART_IMAGES_DIR,
    DASHBOARD_IMAGES_DIR,

    SQL_DIR,

    LOGS_DIR,

    SRC_DIR,

    TESTS_DIR,

    SCRIPTS_DIR,
]

for directory in PROJECT_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# ==========================================================
# PROJECT DATASETS
# ==========================================================

CPI_FILE = (
    RAW_EXCEL_DIR /
    "CPI-U All Items - CUUR0000SA0 - Inflation.xlsx"
)

AVERAGE_HOURLY_EARNINGS_FILE = (
    RAW_EXCEL_DIR /
    "Average Hourly Earnings - CES0500000003 - Wage Growth.xlsx"
)

TOTAL_NONFARM_EMPLOYMENT_FILE = (
    RAW_EXCEL_DIR /
    "Total Nonfarm Employment - CES0000000001 - Labor Market.xlsx"
)

UNEMPLOYMENT_RATE_FILE = (
    RAW_EXCEL_DIR /
    "Unemployment Rate - LNS14000000 - Labor Market.xlsx"
)

ECI_PRIVATE_WAGES_FILE = (
    RAW_EXCEL_DIR /
    "ECI Private Wage & Salaries - CIU2020000000000A - Compensation Analysis.xlsx"
)

ECI_TOTAL_COMPENSATION_FILE = (
    RAW_EXCEL_DIR /
    "ECI Total Compensation Private - CIU2010000000000A - Benefits & Total Compensation.xlsx"
)

# ==========================================================
# DATASET DICTIONARY
# ==========================================================

PROJECT_DATASETS = {

    "cpi": CPI_FILE,

    "average_hourly_earnings": AVERAGE_HOURLY_EARNINGS_FILE,

    "employment": TOTAL_NONFARM_EMPLOYMENT_FILE,

    "unemployment": UNEMPLOYMENT_RATE_FILE,

    "eci_private_wages": ECI_PRIVATE_WAGES_FILE,

    "eci_total_compensation": ECI_TOTAL_COMPENSATION_FILE,
}

# ==========================================================
# PROJECT SETTINGS
# ==========================================================

# Phase 1
# Read locally downloaded BLS Excel files

USE_LOCAL_EXCEL = True

# Phase 2
# Read directly from the BLS API

USE_BLS_API = False

# ==========================================================
# BLS API CONFIGURATION
# ==========================================================

BLS_API_URL = (
    "https://api.bls.gov/publicAPI/v2/timeseries/data/"
)

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

# ==========================================================
# LOGGING CONFIGURATION
# ==========================================================

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | "
    "%(name)s | %(message)s"
)