 """
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd

# Sample dataset
train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

# TODO: Implement fit_imputer
# def fit_imputer(train_df, num_cols, cat_cols):
def fit_imputer(train_df, num_cols, cat_cols):
    return {
        "num_median": {c: train_df[c].median() for c in num_cols},
        "cat_mode": {c: train_df[c].mode(dropna=True)[0] for c in cat_cols}
    }


# TODO: Implement transform_imputer
# def transform_imputer(df, params, add_indicators=True):
def transform_imputer(df, params, add_indicators=True):
    df = df.copy()

    for c, v in params["num_median"].items():
        if add_indicators:
            df[c + "_missing"] = df[c].isna().astype(int)
        df[c] = df[c].fillna(v)

    for c, v in params["cat_mode"].items():
        if add_indicators:
            df[c + "_missing"] = df[c].isna().astype(int)
        df[c] = df[c].fillna(v)

    return df


num_cols = ["age"]
cat_cols = ["city"]

params = fit_imputer(train, num_cols, cat_cols)

train_with_ind = transform_imputer(train, params, add_indicators=True)
test_with_ind = transform_imputer(test, params, add_indicators=True)

train_no_ind = transform_imputer(train, params, add_indicators=False)
test_no_ind = transform_imputer(test, params, add_indicators=False)

print(train_with_ind)
print(test_with_ind)