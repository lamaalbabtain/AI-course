"""
Day 9 Activity: Data Types Practice
Tasks:
1) Identify numeric-like, currency-like, datetime-like columns
2) Convert to proper dtypes
3) Validate conversions by checking NaN counts
"""

import pandas as pd

raw = {
    "age": ["25", "30", "unknown"],
    "income": ["$50,000", "$60,000", None],
    "signup": ["2024-01-01", "01/05/2024", "not a date"],
}

df = pd.DataFrame(raw)

# TODO: Implement normalize_schema(df) to convert types safely
def normalize_schema(df):#رتّبي أنواع البيانات
    df = df.copy()

    df["age"] = pd.to_numeric(df["age"], errors="coerce") # اذا كان ايرورو خليه nan

    df["income"] = df["income"].str.replace(r"[^0-9.]", "", regex=True)# وبتعامل معها كـ strings" - بدّل جزء من النص بشي ثاني
    df["income"] = pd.to_numeric(df["income"], errors="coerce")

    df["signup"] = pd.to_datetime(df["signup"], errors="coerce")

    return df


df_clean = normalize_schema(df)

print(df_clean)
print("\nNaN counts:")
print(df_clean.isna().sum())