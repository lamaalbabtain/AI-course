"""
Day 19 Activity: Transformation Practice
Tasks:
1) Load skewed feature
2) Apply log1p, sqrt, and Yeo-Johnson
3) Compare before/after
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import PowerTransformer

# TODO: Load data from data/day19_transform.csv
df = pd.read_csv("data/day19_transform.csv")


# TODO: Apply transforms and compare summary stats
df["log1p"] = np.log1p(df["value"])

df["sqrt"] = np.sqrt(df["value"])

pt = PowerTransformer(method="yeo-johnson")
df["yeo_johnson"] = pt.fit_transform(df[["value"]])

print(df[["value", "log1p", "sqrt", "yeo_johnson"]].describe())