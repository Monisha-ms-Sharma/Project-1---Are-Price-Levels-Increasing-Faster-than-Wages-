# U.S. Inflation, Wage Growth & Purchasing Power Analysis

## An End-to-End Business Analytics Case Study Using Python, SQL, APIs, Data Engineering, Data Visualization, and Statistical Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQL](https://img.shields.io/badge/SQL-Analytics-green)
![REST API](https://img.shields.io/badge/REST-API-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-success)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-purple)
![Status](https://img.shields.io/badge/Project-In%20Progress-yellow)

---

# Table of Contents

- Project Overview
- Business Problem
- Business Objectives
- Business Questions
- Project Architecture
- Project Workflow
- Project Roadmap
- Technologies Used
- Repository Structure
- Data Sources
- Methodology
- Key Features
- Project Deliverables
- Expected Outcomes
- Future Enhancements
- About the Author

---

# Project Overview

Inflation and wage growth are two of the most important economic indicators because they directly influence purchasing power, consumer spending, business strategy, and economic policy.

Although wages generally increase over time, rising prices can reduce the purchasing power of those earnings. Measuring **real wage growth** rather than **nominal wage growth** provides a more accurate picture of changes in living standards.

This project analyzes official U.S. Bureau of Labor Statistics (BLS) data to determine whether wage growth has kept pace with inflation and how purchasing power has changed over time.

Unlike a traditional analytics project, this repository demonstrates an end-to-end Business Analytics workflow by combining:

- Data Acquisition
- ETL Pipeline Development
- REST API Integration
- Data Validation
- Data Profiling
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization
- Business Storytelling
- Executive Reporting

The project is designed using modular, production-style software engineering principles so that new economic datasets can be added with minimal code changes.

---

# Business Problem

A fundamental economic question asked by businesses, policymakers, economists, and consumers is:

> **Have wages increased fast enough to keep up with inflation, or has purchasing power declined over time?**

Answering this question requires integrating multiple official economic datasets, calculating inflation-adjusted wages, and analyzing long-term trends to generate meaningful business insights.

---

# Business Objectives

The primary objectives of this project are to:

- Measure inflation using the Consumer Price Index (CPI).
- Measure wage growth using Average Hourly Earnings data.
- Calculate inflation-adjusted (real) wage growth.
- Analyze purchasing power over time.
- Compare wage growth with inflation.
- Identify periods where inflation exceeded wage growth.
- Visualize long-term economic trends.
- Generate business insights supported by statistical analysis.
- Present findings through professional reports and visualizations.

---

# Business Questions

This project seeks to answer the following questions:

1. Has inflation increased faster than wages?
2. How has purchasing power changed over time?
3. Which years experienced the largest gains or losses in purchasing power?
4. Does wage growth consistently keep pace with inflation?
5. What relationship exists between inflation and wage growth?
6. What business and policy recommendations can be derived from the analysis?

---

# Project Architecture

```
                 U.S. Bureau of Labor Statistics (BLS)
                               │
                               ▼
                    Data Acquisition Layer
                     (Excel Files / REST API)
                               │
                               ▼
                     download_data.py (ETL)
                               │
                               ▼
                          Raw Data (CSV)
                               │
                               ▼
                       Data Validation Layer
                               │
                               ▼
                        Processed Data
                               │
                               ▼
                     Feature Engineering
                               │
                               ▼
                 Exploratory Data Analysis
                               │
                               ▼
                    Statistical Analysis
                               │
                               ▼
                      Business Insights
                               │
                               ▼
                     Executive Reporting
```

The architecture separates **data acquisition** from **data analysis**, making the project reusable, maintainable, and easy to extend.

---

# Project Workflow

```
Business Problem
        │
        ▼
Data Acquisition
        │
        ▼
Data Profiling
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
Data Visualization
        │
        ▼
Business Insights
        │
        ▼
Executive Report
```

---

# Project Roadmap

The project is developed in incremental phases.

## Phase A — Data Acquisition

- Configure project structure
- Download official BLS datasets
- Store raw datasets
- Validate downloaded data

## Phase B — Data Profiling

- Inspect dataset structure
- Identify missing values
- Detect duplicates
- Validate schema

## Phase C — Data Cleaning

- Convert data types
- Standardize formats
- Handle missing values
- Prepare analysis-ready datasets

## Phase D — Feature Engineering

- Calculate Inflation Rate
- Calculate Wage Growth
- Calculate Real Wage Growth
- Calculate Purchasing Power Index

## Phase E — Exploratory Data Analysis

- Time-series analysis
- Trend visualization
- Correlation analysis
- Distribution analysis

## Phase F — Business Insights

- Executive Summary
- Key Findings
- Recommendations
- Business Conclusions

---

# Technologies Used

## Programming Languages

- Python
- SQL

## Python Libraries

- Pandas
- NumPy
- Requests
- Matplotlib
- Plotly
- SciPy
- Scikit-learn
- Logging
- JSON

## Data Sources

- U.S. Bureau of Labor Statistics (BLS)

## Development Tools

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

# Repository Structure

```
US-Inflation-Wage-Growth-Analysis/

│
├── README.md
├── requirements.txt
├── LICENSE
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── docs/
│   ├── Methodology.md
│   └── Data_Dictionary.md
│
├── notebooks/
│   ├── 01_Data_Profiling.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_EDA.ipynb
│   └── 05_Business_Insights.ipynb
│
├── src/
│   ├── config.py
│   ├── download_data.py
│   ├── data_loader.py
│   ├── data_validation.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── statistical_analysis.py
│   └── utils.py
│
├── reports/
│   ├── Executive_Summary.pdf
│   └── Technical_Report.pdf
│
├── images/
│
└── presentation/
    └── Business_Presentation.pptx
```

---

# Data Sources

This project uses publicly available datasets from the U.S. Bureau of Labor Statistics (BLS).

## Phase 1

- Consumer Price Index (CPI-U)
- Average Hourly Earnings

## Phase 2

- Unemployment Rate
- Employment Level

Initially, the project reads official BLS Excel files to establish a stable analytics workflow. A later enhancement replaces the manual data acquisition process with an automated REST API pipeline without requiring changes to the downstream analysis.

---

# Methodology

This project follows an end-to-end Business Analytics lifecycle.

1. Acquire official economic datasets
2. Validate incoming data
3. Profile dataset quality
4. Clean and preprocess data
5. Engineer analytical features
6. Perform exploratory data analysis
7. Conduct statistical analysis
8. Generate business insights
9. Develop executive recommendations

---

# Key Features

- Modular project architecture
- Reusable ETL pipeline
- REST API integration
- Data validation
- Logging and error handling
- Feature engineering
- Statistical analysis
- Interactive visualizations
- Executive reporting
- Reproducible workflow

---

# Project Deliverables

- Automated ETL Pipeline
- Clean Analytical Dataset
- Data Quality Report
- Exploratory Data Analysis
- Statistical Analysis
- Executive Summary
- Technical Report
- Business Presentation

---

# Expected Outcomes

The project will provide insights into:

- Inflation trends
- Wage growth trends
- Purchasing power changes
- Real wage growth
- Long-term economic patterns
- Business implications of inflation

---

# Future Enhancements

Future versions of the project will include:

- Automated BLS API integration
- Scheduled ETL pipeline
- Time-series forecasting
- Machine Learning models
- Interactive Power BI dashboard
- Tableau dashboard
- Streamlit web application
- Docker deployment
- CI/CD with GitHub Actions

---

# About the Author

## Monisha Sharma

**Business Intelligence | Business Analytics | Data Engineering | Data Governance | Master Data Management (MDM)**

### Technical Skills

- Python
- SQL
- REST APIs
- Power BI
- Tableau
- Data Engineering
- ETL Pipelines
- Data Governance
- Business Intelligence
- Statistical Analysis

---

⭐ If you found this project helpful, please consider giving it a star!
