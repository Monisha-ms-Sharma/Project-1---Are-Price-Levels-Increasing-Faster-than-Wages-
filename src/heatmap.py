"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
heatmap.py

Author:
Monisha Sharma

Description:
Creates a correlation heatmap for the
economic indicators.
============================================================
"""

import matplotlib.pyplot as plt

from src.logger import logger
from src.config import IMAGES_DIR


def plot_correlation_heatmap(correlation_matrix):
    """
    Create a correlation heatmap using matplotlib.
    """

    logger.info("Creating Correlation Heatmap...")

    fig, ax = plt.subplots(figsize=(8, 6))

    image = ax.imshow(
        correlation_matrix,
        interpolation="nearest",
        aspect="auto",
    )

    plt.colorbar(image)

    labels = correlation_matrix.columns

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(
        labels,
        rotation=45,
        ha="right"
    )

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)

    # Display correlation coefficients
    for row in range(len(labels)):
        for col in range(len(labels)):
            value = correlation_matrix.iloc[row, col]

            ax.text(
                col,
                row,
                f"{value:.2f}",
                ha="center",
                va="center",
                fontsize=9
            )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    output_file = IMAGES_DIR / "correlation_heatmap.png"

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logger.info(f"Saved plot: {output_file}")

    logger.info("Correlation Heatmap created.")