"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data
np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})


# TODO: Implement iqr_bounds and detect_outliers_iqr
def iqr_bounds(s, k=1.5):
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


def detect_outliers_iqr(df, col, k=1.5):
    lower, upper = iqr_bounds(df[col], k)
    return (df[col] < lower) | (df[col] > upper)


# TODO: Implement detect_outliers_zscore
def detect_outliers_zscore(df, col, threshold=3):
    mean = df[col].mean()
    std = df[col].std()
    z = (df[col] - mean) / std
    return z.abs() > threshold


# TODO: Apply capping and log1p transformation
lower, upper = iqr_bounds(df["income"])

df_no_handling = df.copy()

df_iqr_capped = df.copy()
df_iqr_capped["income"] = df_iqr_capped["income"].clip(lower, upper)

df_log = df.copy()
df_log["income"] = np.log1p(df_log["income"])