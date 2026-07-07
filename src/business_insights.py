"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
business_insights.py

Author:
Monisha Sharma

Description:
Generates business insights from the engineered
economic datasets.

This module converts analytical metrics into
business-friendly findings that can be used in:

• Executive Reports
• Dashboards
• Power BI
• Portfolio Presentations
============================================================
"""

import pandas as pd

from src.logger import logger


# ==========================================================
# LATEST ECONOMIC CONDITIONS
# ==========================================================

def latest_economic_conditions(
    df: pd.DataFrame
) -> dict:
    """
    Return the latest available economic indicators.
    """

    logger.info(
        "Generating latest economic conditions..."
    )

    latest = df.iloc[-1]

    return {
        "Latest Year": int(latest["Year"]),
        "Average CPI": round(
            latest["Average CPI"], 2
        ),
        "Inflation Rate": round(
            latest["Annual Inflation Rate (%)"], 2
        ),
        "Average Hourly Wage": round(
            latest["Average Hourly Wage"], 2
        ),
        "Wage Growth": round(
            latest["Annual Wage Growth (%)"], 2
        ),
        "Real Wage Growth": round(
            latest["Real Wage Growth (%)"], 2
        ),
    }


# ==========================================================
# HIGHEST INFLATION
# ==========================================================

def highest_inflation(
    df: pd.DataFrame
) -> dict:
    """
    Identify the year with the highest inflation.
    """

    logger.info(
        "Finding highest inflation year..."
    )

    row = df.loc[
        df["Annual Inflation Rate (%)"].idxmax()
    ]

    return {
        "Year": int(row["Year"]),
        "Inflation": round(
            row["Annual Inflation Rate (%)"], 2
        )
    }


# ==========================================================
# HIGHEST WAGE GROWTH
# ==========================================================

def highest_wage_growth(
    df: pd.DataFrame
) -> dict:
    """
    Identify the year with the highest wage growth.
    """

    logger.info(
        "Finding highest wage growth year..."
    )

    row = df.loc[
        df["Annual Wage Growth (%)"].idxmax()
    ]

    return {
        "Year": int(row["Year"]),
        "Wage Growth": round(
            row["Annual Wage Growth (%)"], 2
        )
    }

    """
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
business_insights.py

Author:
Monisha Sharma

Description:
Generates business insights from the engineered
economic datasets.

This module converts analytical metrics into
business-friendly findings that can be used in:

• Executive Reports
• Dashboards
• Power BI
• Portfolio Presentations
============================================================
"""

import pandas as pd

from src.logger import logger


# ==========================================================
# LATEST ECONOMIC CONDITIONS
# ==========================================================

def latest_economic_conditions(
    df: pd.DataFrame
) -> dict:
    """
    Return the latest available economic indicators.
    """

    logger.info(
        "Generating latest economic conditions..."
    )

    latest = df.iloc[-1]

    return {
        "Latest Year": int(latest["Year"]),
        "Average CPI": round(
            latest["Average CPI"], 2
        ),
        "Inflation Rate": round(
            latest["Annual Inflation Rate (%)"], 2
        ),
        "Average Hourly Wage": round(
            latest["Average Hourly Wage"], 2
        ),
        "Wage Growth": round(
            latest["Annual Wage Growth (%)"], 2
        ),
        "Real Wage Growth": round(
            latest["Real Wage Growth (%)"], 2
        ),
    }


# ==========================================================
# HIGHEST INFLATION
# ==========================================================

def highest_inflation(
    df: pd.DataFrame
) -> dict:
    """
    Identify the year with the highest inflation.
    """

    logger.info(
        "Finding highest inflation year..."
    )

    row = df.loc[
        df["Annual Inflation Rate (%)"].idxmax()
    ]

    return {
        "Year": int(row["Year"]),
        "Inflation": round(
            row["Annual Inflation Rate (%)"], 2
        )
    }

# ==========================================================
# LOWEST REAL WAGE GROWTH
# ==========================================================

def lowest_real_wage_growth(
    df: pd.DataFrame
) -> dict:
    """
    Identify the year with the weakest purchasing power.
    """

    logger.info(
        "Finding lowest Real Wage Growth..."
    )

    valid = df.dropna(
        subset=["Real Wage Growth (%)"]
    )

    row = valid.loc[
        valid["Real Wage Growth (%)"].idxmin()
    ]

    return {
        "Year": int(row["Year"]),
        "Real Wage Growth": round(
            row["Real Wage Growth (%)"], 2
        )
    }


# ==========================================================
# AVERAGE INFLATION
# ==========================================================

def average_inflation(
    df: pd.DataFrame
) -> float:
    """
    Calculate the average inflation rate across
    the study period.
    """

    logger.info(
        "Calculating average inflation..."
    )

    return round(
        df["Annual Inflation Rate (%)"]
        .mean(),
        2
    )


# ==========================================================
# AVERAGE WAGE GROWTH
# ==========================================================

def average_wage_growth(
    df: pd.DataFrame
) -> float:
    """
    Calculate the average wage growth across
    the study period.
    """

    logger.info(
        "Calculating average wage growth..."
    )

    return round(
        df["Annual Wage Growth (%)"]
        .mean(),
        2
    )


# ==========================================================
# PURCHASING POWER TREND
# ==========================================================

def purchasing_power_trend(
    df: pd.DataFrame
) -> str:
    """
    Determine whether purchasing power generally
    improved or deteriorated over the study period.
    """

    logger.info(
        "Evaluating purchasing power trend..."
    )

    mean_growth = (
        df["Real Wage Growth (%)"]
        .mean()
    )

    if mean_growth >= 0:
        return (
            "Overall purchasing power improved "
            "because wage growth generally exceeded "
            "inflation."
        )

    return (
        "Overall purchasing power declined because "
        "inflation generally outpaced wage growth."
    )


# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

def executive_recommendations(
    df: pd.DataFrame
) -> list[str]:
    """
    Generate high-level executive recommendations.
    """

    logger.info(
        "Generating executive recommendations..."
    )

    recommendations = []

    avg_real = (
        df["Real Wage Growth (%)"]
        .mean()
    )

    avg_inflation = (
        df["Annual Inflation Rate (%)"]
        .mean()
    )

    if avg_real < 0:
        recommendations.append(
            "Monitor wage policies to reduce the "
            "erosion of purchasing power."
        )
    else:
        recommendations.append(
            "Maintain sustainable wage growth above "
            "the inflation rate."
        )

    if avg_inflation > 3:
        recommendations.append(
            "Continue monitoring inflationary "
            "pressures and consumer prices."
        )

    recommendations.append(
        "Use annual wage and inflation trends to "
        "support workforce planning and budgeting."
    )

    recommendations.append(
        "Track Real Wage Growth as a primary KPI for "
        "measuring purchasing power."
    )

    return recommendations

# ==========================================================
# HIGHEST WAGE GROWTH
# ==========================================================

def highest_wage_growth(
    df: pd.DataFrame
) -> dict:
    """
    Identify the year with the highest wage growth.
    """

    logger.info(
        "Finding highest wage growth year..."
    )

    row = df.loc[
        df["Annual Wage Growth (%)"].idxmax()
    ]

    return {
        "Year": int(row["Year"]),
        "Wage Growth": round(
            row["Annual Wage Growth (%)"], 2
        )
    }

# ==========================================================
# GENERATE BUSINESS INSIGHTS
# ==========================================================

def generate_business_insights(
    df: pd.DataFrame
) -> dict:
    """
    Generate a complete set of business insights
    from the engineered economic dataset.

    Returns
    -------
    dict
        Dictionary containing:
        • Latest Economic Conditions
        • Highest Inflation
        • Highest Wage Growth
        • Lowest Real Wage Growth
        • Average Inflation
        • Average Wage Growth
        • Purchasing Power Trend
        • Executive Recommendations
    """

    logger.info(
        "Generating business insights..."
    )

    insights = {

        "Latest Economic Conditions":
            latest_economic_conditions(df),

        "Highest Inflation":
            highest_inflation(df),

        "Highest Wage Growth":
            highest_wage_growth(df),

        "Lowest Real Wage Growth":
            lowest_real_wage_growth(df),

        "Average Inflation":
            average_inflation(df),

        "Average Wage Growth":
            average_wage_growth(df),

        "Purchasing Power Trend":
            purchasing_power_trend(df),

        "Executive Recommendations":
            executive_recommendations(df)

    }

    logger.info(
        "Business insights generated successfully."
    )

    return insights


# ==========================================================
# PRINT BUSINESS INSIGHTS
# ==========================================================

def print_business_insights(
    insights: dict
) -> None:
    """
    Print business insights in a readable format.
    """

    print()

    print("=" * 70)
    print("BUSINESS INSIGHTS")
    print("=" * 70)

    latest = insights["Latest Economic Conditions"]

    print("\nLatest Economic Conditions")
    print("-" * 70)

    print(
        f"Latest Year               : {latest['Latest Year']}"
    )
    print(
        f"Average CPI               : {latest['Average CPI']:.2f}"
    )
    print(
        f"Inflation Rate            : "
        f"{latest['Inflation Rate']:.2f}%"
    )
    print(
        f"Average Hourly Wage       : "
        f"${latest['Average Hourly Wage']:.2f}"
    )
    print(
        f"Wage Growth               : "
        f"{latest['Wage Growth']:.2f}%"
    )
    print(
        f"Real Wage Growth          : "
        f"{latest['Real Wage Growth']:.2f}%"
    )

    print("\nKey Findings")
    print("-" * 70)

    highest_inf = insights["Highest Inflation"]

    print(
        f"Highest Inflation         : "
        f"{highest_inf['Inflation']:.2f}% "
        f"({highest_inf['Year']})"
    )

    highest_wage = insights["Highest Wage Growth"]

    print(
        f"Highest Wage Growth       : "
        f"{highest_wage['Wage Growth']:.2f}% "
        f"({highest_wage['Year']})"
    )

    weakest = insights["Lowest Real Wage Growth"]

    print(
        f"Weakest Purchasing Power  : "
        f"{weakest['Real Wage Growth']:.2f}% "
        f"({weakest['Year']})"
    )

    print(
        f"Average Inflation         : "
        f"{insights['Average Inflation']:.2f}%"
    )

    print(
        f"Average Wage Growth       : "
        f"{insights['Average Wage Growth']:.2f}%"
    )

    print("\nOverall Trend")
    print("-" * 70)

    print(
        insights["Purchasing Power Trend"]
    )

    print("\nExecutive Recommendations")
    print("-" * 70)

    for i, recommendation in enumerate(
        insights["Executive Recommendations"],
        start=1
    ):
        print(f"{i}. {recommendation}")

    print()