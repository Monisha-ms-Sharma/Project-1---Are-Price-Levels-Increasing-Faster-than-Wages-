"""
============================================================
Project:
U.S. Inflation, Wage Growth & Purchasing Power Analysis

Module:
pdf_report.py

Author:
Monisha Sharma

Description:
Generates a professional Executive PDF Report containing:

• Project Title
• Executive Summary
• Dashboard KPIs
• Business Insights
• Statistical Highlights
• Charts
• Final Conclusions

Uses ReportLab.
============================================================
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from src.config import (
    REPORTS_DIR,
    IMAGES_DIR,
)

from src.logger import logger


# ============================================================
# Report Location
# ============================================================

PDF_NAME = "Executive_Report.pdf"

PDF_PATH = REPORTS_DIR / PDF_NAME


# ============================================================
# Styles
# ============================================================

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading_style = styles["Heading2"]

normal_style = styles["BodyText"]


# ============================================================
# Helper Functions
# ============================================================

def add_heading(story, text):
    """
    Add section heading.
    """

    story.append(Paragraph(text, heading_style))
    story.append(Spacer(1, 0.20 * inch))


def add_paragraph(story, text):
    """
    Add paragraph.
    """

    story.append(Paragraph(text, normal_style))
    story.append(Spacer(1, 0.15 * inch))


def add_image(story, image_path, width=6.5 * inch):
    """
    Add chart if it exists.
    """

    image_path = Path(image_path)

    if image_path.exists():

        img = Image(str(image_path))

        img.drawWidth = width

        img.drawHeight = width * 0.60

        story.append(img)

        story.append(Spacer(1, 0.25 * inch))

    else:

        logger.warning(f"Image not found: {image_path}")

# ============================================================
# Dashboard Table
# ============================================================

def create_dashboard_table(metrics_df):
    """
    Create KPI table for the Executive Report.
    """

    latest = metrics_df.iloc[0]

    data = [

        ["Metric", "Value"],

        ["Latest Year", f"{int(latest['Latest Year'])}"],

        ["Average CPI", f"{latest['Average CPI']:.2f}"],

        ["Inflation Rate (%)", f"{latest['Inflation Rate (%)']:.2f}%"],

        ["Average Hourly Wage", f"${latest['Average Hourly Wage']:.2f}"],

        ["Wage Growth (%)", f"{latest['Wage Growth (%)']:.2f}%"],

        ["Real Wage Growth (%)", f"{latest['Real Wage Growth (%)']:.2f}%"],

        ["Employment", f"{latest['Employment']:,.0f}"],

        [
            "Unemployment Rate (%)",
            f"{latest['Unemployment Rate (%)']:.2f}%"
        ],
    ]

    table = Table(data, colWidths=[3.5 * inch, 2.5 * inch])

    table.setStyle(
        TableStyle(
            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("GRID", (0, 0), (-1, -1), 1, colors.black),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ]
        )
    )

    return table


# ============================================================
# Executive Report
# ============================================================

def generate_pdf_report(
    executive_summary,
    metrics_df,
    business_insights,
):
    """
    Generate Executive PDF Report.
    """

    logger.info("Generating Executive PDF Report...")

    doc = SimpleDocTemplate(str(PDF_PATH))

    story = []


    # ========================================================
    # Title
    # ========================================================

    story.append(

        Paragraph(

            "U.S. Inflation, Wage Growth & Purchasing Power Analysis",

            title_style,

        )

    )

    story.append(Spacer(1, 0.30 * inch))

    add_paragraph(

        story,

        "<b>Author:</b> Monisha Sharma"

    )

    add_paragraph(

        story,

        "<b>Project Type:</b> End-to-End Business Analytics Case Study"

    )

    add_paragraph(

        story,

        "<b>Data Source:</b> U.S. Bureau of Labor Statistics (BLS)"

    )

    story.append(Spacer(1, 0.25 * inch))


    # ========================================================
    # Executive Summary
    # ========================================================

    add_heading(

        story,

        "Executive Summary"

    )

    add_paragraph(

        story,

        executive_summary

    )


    # ========================================================
    # Dashboard KPIs
    # ========================================================

    add_heading(

        story,

        "Dashboard KPIs"

    )

    story.append(

        create_dashboard_table(metrics_df)

    )

    story.append(

        Spacer(1, 0.35 * inch)

    )

    # ========================================================
    # Business Insights
    # ========================================================

    add_heading(
        story,
        "Business Insights"
    )

    if isinstance(business_insights, list):

        for insight in business_insights:

            add_paragraph(
                story,
                f"• {insight}"
            )

    else:

        add_paragraph(
            story,
            str(business_insights)
        )

    story.append(
        Spacer(1, 0.25 * inch)
    )


    # ========================================================
    # Inflation Trend
    # ========================================================

    add_heading(
        story,
        "Annual Inflation Trend"
    )

    add_image(
        story,
        IMAGES_DIR / "annual_inflation_rate.png"
    )


    # ========================================================
    # Wage Growth Trend
    # ========================================================

    add_heading(
        story,
        "Annual Wage Growth"
    )

    add_image(
        story,
        IMAGES_DIR / "annual_wage_growth.png"
    )


    # ========================================================
    # Real Wage Growth
    # ========================================================

    add_heading(
        story,
        "Real Wage Growth"
    )

    add_image(
        story,
        IMAGES_DIR / "real_wage_growth.png"
    )


    # ========================================================
    # Employment Trend
    # ========================================================

    add_heading(
        story,
        "Employment Trend"
    )

    add_image(
        story,
        IMAGES_DIR / "employment_trend.png"
    )


    # ========================================================
    # Unemployment Trend
    # ========================================================

    add_heading(
        story,
        "Unemployment Trend"
    )

    add_image(
        story,
        IMAGES_DIR / "unemployment_trend.png"
    )


    # ========================================================
    # Correlation Heatmap
    # ========================================================

    add_heading(
        story,
        "Correlation Heatmap"
    )

    add_image(
        story,
        IMAGES_DIR / "correlation_heatmap.png"
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )

    # ========================================================
    # Statistical Highlights
    # ========================================================

    add_heading(
        story,
        "Statistical Highlights"
    )

    add_paragraph(
        story,
        """
        • Inflation and Wage Growth were positively correlated during the
        study period.

        • Real Wage Growth became negative during periods of exceptionally
        high inflation.

        • Wage growth generally outpaced inflation over the eleven-year
        analysis, resulting in gradual improvements in purchasing power.

        • Employment continued to trend upward following the COVID-19
        recovery while unemployment returned to historically lower levels.
        """
    )


    # ========================================================
    # Final Conclusions
    # ========================================================

    add_heading(
        story,
        "Final Conclusions"
    )

    add_paragraph(
        story,
        """
        This project demonstrates a complete Business Analytics workflow
        using official U.S. Bureau of Labor Statistics (BLS) data.

        The analysis integrates ETL, data engineering, feature engineering,
        statistical analysis, visualization, KPI development and executive
        reporting into a reproducible analytics pipeline.

        The results indicate that although inflation surged during 2022,
        wage growth eventually recovered, allowing purchasing power to
        improve in subsequent years. Employment continued to strengthen
        while unemployment stabilized near historically normal levels.

        This project showcases practical data analytics skills including
        Python, Pandas, data cleaning, business intelligence reporting,
        visualization, statistical analysis and executive communication.
        """
    )


    # ========================================================
    # Build PDF
    # ========================================================

    doc.build(story)

    logger.info(
        f"Executive PDF saved to: {PDF_PATH}"
    )

    return PDF_PATH


# ============================================================
# Standalone Execution
# ============================================================

if __name__ == "__main__":

    logger.info(
        "pdf_report.py is a utility module."
    )