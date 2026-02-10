"""
Day 18 Activity: Binning Practice
Tasks:
1) Load age dataset
2) Apply equal-width bins, equal-frequency bins, and domain bins
3) One-hot encode bins and compare
"""

import pandas as pd

# TODO: Load data from data/day18_binning.csv
df = pd.read_csv("data/day18_binning.csv")


# TODO: Apply pd.cut and pd.qcut
df["age_equal_width"] = pd.cut(
    df["age"],
    bins=4
)

df["age_equal_freq"] = pd.qcut(
    df["age"],
    q=4,
    duplicates="drop"
)


# TODO: Create domain bins
bins = [0, 18, 30, 45, 60, 100]
labels = ["child", "young", "adult", "mid_age", "senior"]

df["age_domain"] = pd.cut(
    df["age"],
    bins=bins,
    labels=labels
)


# TODO: Compare value counts
print(df["age_equal_width"].value_counts())
print(df["age_equal_freq"].value_counts())
print(df["age_domain"].value_counts())


# One-hot encoding for comparison
df_encoded = pd.get_dummies(
    df[["age_equal_width", "age_equal_freq", "age_domain"]],
    prefix=["ew", "ef", "domain"]
)

print(df_encoded.head())