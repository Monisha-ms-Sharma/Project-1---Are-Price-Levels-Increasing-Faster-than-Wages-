"""
==============================================================
Executive Report

Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Author:
Monisha Sharma

Description:
Creates an executive summary from the engineered dataset and
business insights.
==============================================================
"""

import logging
import pandas as pd

logger = logging.getLogger("executive_report")


def create_executive_report(
    merged_df: pd.DataFrame,
    insights: list[str]
) -> str:
    """
    Build an executive report.

    Parameters
    ----------
    merged_df : DataFrame
        Final engineered dataset.

    insights : list
        Business insights.

    Returns
    -------
    str
        Executive report.
    """

    logger.info("Creating executive report...")

    latest = merged_df.iloc[-1]

    report = []

    report.append("=" * 70)
    report.append("EXECUTIVE SUMMARY")
    report.append("=" * 70)
    report.append("")

    report.append("Project")
    report.append(
        "U.S. Inflation, Wage Growth & Purchasing Power Analysis"
    )
    report.append("")

    report.append("Latest Economic Indicators")
    report.append("-" * 70)

    report.append(
        f"Latest Year                : {int(latest['Year'])}"
    )

    report.append(
        f"Average CPI               : {latest['Average CPI']:.2f}"
    )

    report.append(
        f"Inflation Rate            : "
        f"{latest['Annual Inflation Rate (%)']:.2f}%"
    )

    report.append(
        f"Average Hourly Wage       : "
        f"${latest['Average Hourly Wage']:.2f}"
    )

    report.append(
        f"Wage Growth               : "
        f"{latest['Annual Wage Growth (%)']:.2f}%"
    )

    report.append(
        f"Real Wage Growth          : "
        f"{latest['Real Wage Growth (%)']:.2f}%"
    )

    report.append("")
    report.append("Business Insights")
    report.append("-" * 70)

    for i, insight in enumerate(insights, start=1):
        report.append(f"{i}. {insight}")

    report.append("")
    report.append("Conclusion")
    report.append("-" * 70)

    if latest["Real Wage Growth (%)"] > 0:
        report.append(
            "Overall purchasing power has improved because wages "
            "grew faster than inflation."
        )
    else:
        report.append(
            "Overall purchasing power weakened because inflation "
            "grew faster than wages."
        )

    logger.info("Executive report created successfully.")

    return "\n".join(report)