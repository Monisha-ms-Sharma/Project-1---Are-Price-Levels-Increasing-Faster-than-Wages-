"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
logger.py

Author:
Monisha Sharma

Description:
Central logging configuration for the project.

This module creates a reusable logger that writes
messages to both:

1. The terminal (console)
2. The project log file

Every project module imports this logger instead of
creating its own.

============================================================
"""

import logging
from pathlib import Path

from src.config import LOG_FILE

# ==========================================================
# CREATE LOG DIRECTORY IF IT DOES NOT EXIST
# ==========================================================

Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

# ==========================================================
# CREATE LOGGER
# ==========================================================

logger = logging.getLogger("inflation_analysis")

# Prevent duplicate log messages
logger.propagate = False

# Set the minimum logging level
logger.setLevel(logging.INFO)

# ==========================================================
# CREATE FORMATTER
# ==========================================================

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(module)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ==========================================================
# FILE HANDLER
# ==========================================================

file_handler = logging.FileHandler(LOG_FILE)

file_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)

# ==========================================================
# CONSOLE HANDLER
# ==========================================================

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)

console_handler.setFormatter(formatter)

# ==========================================================
# AVOID DUPLICATE HANDLERS
# ==========================================================

if not logger.handlers:

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)