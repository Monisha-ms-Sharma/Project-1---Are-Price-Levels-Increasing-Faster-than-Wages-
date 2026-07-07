"""
Project: U.S. Inflation, Wage Growth & Purchasing Power Analysis
Module: business_insights.py
"""

import pandas as pd
from src.logger import logger

def latest_economic_conditions(df: pd.DataFrame)->dict:
    latest=df.sort_values("Year").iloc[-1]
    return {"Year":int(latest["Year"]),"Average CPI":round(latest["Average CPI"],2),
            "Inflation Rate":round(latest["Annual Inflation Rate (%)"],2),
            "Average Hourly Wage":round(latest["Average Hourly Wage"],2),
            "Wage Growth":round(latest["Annual Wage Growth (%)"],2),
            "Real Wage Growth":round(latest["Real Wage Growth (%)"],2)}

def highest_inflation(df):
    r=df.loc[df["Annual Inflation Rate (%)"].idxmax()]
    return {"Year":int(r["Year"]),"Inflation Rate":round(r["Annual Inflation Rate (%)"],2)}

def highest_wage_growth(df):
    r=df.loc[df["Annual Wage Growth (%)"].idxmax()]
    return {"Year":int(r["Year"]),"Wage Growth":round(r["Annual Wage Growth (%)"],2)}

def lowest_real_wage_growth(df):
    r=df.loc[df["Real Wage Growth (%)"].idxmin()]
    return {"Year":int(r["Year"]),"Real Wage Growth":round(r["Real Wage Growth (%)"],2)}

def average_inflation(df):
    return {"Average Inflation":round(df["Annual Inflation Rate (%)"].mean(),2)}

def average_wage_growth(df):
    return {"Average Wage Growth":round(df["Annual Wage Growth (%)"].mean(),2)}

def purchasing_power_trend(df):
    avg=round(df["Real Wage Growth (%)"].mean(),2)
    trend="Purchasing power remained relatively stable."
    if avg>0: trend="Purchasing power generally improved because wages grew faster than inflation."
    elif avg<0: trend="Purchasing power generally weakened because inflation outpaced wage growth."
    return {"Average Real Wage Growth":avg,"Trend":trend}

def executive_recommendations(df):
    rec=[]
    rec.append("Maintain wage growth above inflation to preserve purchasing power." if df["Real Wage Growth (%)"].mean()>0 else "Prioritize policies that reduce inflation or accelerate wage growth.")
    rec.append("Monitor inflationary pressures closely." if df["Annual Inflation Rate (%)"].mean()>3 else "Continue monitoring inflation for long-term stability.")
    rec.append("Track employment, wages, and inflation together when evaluating the economy.")
    return rec

def generate_business_insights(df):
    return {
        "Latest Economic Conditions":latest_economic_conditions(df),
        "Highest Inflation":highest_inflation(df),
        "Highest Wage Growth":highest_wage_growth(df),
        "Lowest Real Wage Growth":lowest_real_wage_growth(df),
        "Average Inflation":average_inflation(df),
        "Average Wage Growth":average_wage_growth(df),
        "Purchasing Power Trend":purchasing_power_trend(df),
        "Executive Recommendations":executive_recommendations(df),
    }

def print_business_insights(insights):
    print("="*70)
    print("BUSINESS INSIGHTS")
    print("="*70)
    for sec,val in insights.items():
        print(f"\n{sec}")
        print("-"*70)
        if isinstance(val,dict):
            for k,v in val.items():
                print(f"{k}: {v}")
        elif isinstance(val,list):
            for i,x in enumerate(val,1):
                print(f"{i}. {x}")
