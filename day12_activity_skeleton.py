"""
Day 12 Activity Solution: String & Date Cleaning
"""

import pandas as pd  # استيراد مكتبة بانداز للتعامل مع البيانات

path = "data/day12_users.csv"  # مسار ملف البيانات
df = pd.read_csv(path)  # قراءة الملف وتحويله ل DataFrame


def standardize_city(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # عمل نسخة من الداتا لتجنب تعديل الأصلي
    out["city_clean"] = (
        out["city"]
        .astype("string")  # تحويل العمود لنصوص
        .str.strip()  #
