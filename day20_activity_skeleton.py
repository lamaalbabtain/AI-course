"""
Day 20 Activity: Integrated Feature Engineering
Tasks:
1) Load dataset
2) Encode categoricals, scale numerics
3) Add interaction and transformed feature
4) Compare baseline vs engineered features
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# TODO: Load data from data/day20_integration.csv
df = pd.read_csv("data/day20_integration.csv")


# TODO: Build engineered features

# تحديد الأعمدة
num_cols = ["age", "income"]
cat_cols = ["city"]

# نسخة baseline
df_baseline = df.copy()

# Scaling للمتغيرات الرقمية
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Encoding للمتغيرات الفئوية
encoder = OneHotEncoder(sparse=False, drop="first")
encoded = encoder.fit_transform(df[cat_cols])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(cat_cols),
    index=df.index
)

df = pd.concat([df.drop(columns=cat_cols), encoded_df], axis=1)

# Interaction feature
df["age_income_interaction"] = df["age"] * df["income"]

# Transformed feature
df["log_income"] = np.log1p(df["income"])


# TODO: Compare baseline vs engineered (summary stats or model)
print("Baseline summary:")
print(df_baseline.describe())

print("\nEngineered summary:")
print(df.describe())