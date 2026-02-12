"""
Day 14 Activity Solution: Full Cleaning Pipeline
"""

import pandas as pd  # استيراد مكتبة بانداز
import numpy as np  # استيراد مكتبة نمباي (للحسابات العددية)


def clean_types(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # عمل نسخة من الداتا
    out["age"] = pd.to_numeric(out["age"], errors="coerce")  # تحويل العمر لأرقام، أي خطأ يصبح NaN
    out["income"] = pd.to_numeric(out["income"], errors="coerce")  # تحويل الدخل لأرقام، أي خطأ يصبح NaN
    out["signup_time"] = pd.to_datetime(out["signup_time"], errors="coerce")  # تحويل وقت التسجيل لتاريخ/وقت
    return out  # إعادة الداتا بعد التحويلات


def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # نسخة جديدة
    out["age_missing"] = out["age"].isna().astype(int)  # علامة 1 إذا العمر مفقود، 0 إذا موجود
    out["age"] = out["age"].fillna(out["age"].median())  # ملء العمر المفقود بالوسيط
    out["income"] = out["income"].fillna(out["income"].median())  # ملء الدخل المفقود بالوسيط
    return out


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # نسخة جديدة
    upper = out["income"].quantile(0.99)  # تحديد الحد الأعلى للقيم الشاذة (99%)
    out["income"] = out["income"].clip(upper=upper)  # تقليم أي دخل أعلى من الحد الأعلى
    return out


def clean_strings_and_dates(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # نسخة جديدة
    out["city"] = out["city"].astype("string").str.strip().str.lower()  # تنظيف نص المدينة
    out["signup_time"] = out["signup_time"].dt.tz_localize("UTC", ambiguous="NaT", nonexistent="NaT")  
    # ضبط التوقيت ليكون UTC
    return out


def validate_cleaned(df: pd.DataFrame) -> None:
    assert df["age"].min() >= 0, "Negative ages found"  # التأكد أن العمر غير سلبي
    assert df["income"].notna().all(), "Income has NaN"  # التأكد أن الدخل لا يحتوي NaN


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    out = clean_types(df)  # تنظيف أنواع البيانات
    out = clean_missing(out)  # التعامل مع القيم المفقودة
    out = handle_outliers(out)  # التعامل مع القيم الشاذة
    out = clean_strings_and_dates(out)  # تنظيف النصوص والتواريخ
    validate_cleaned(out)  # التحقق من صحة البيانات النهائية
    return out  # إعادة الداتا النهائية


# Example run
raw = pd.read_csv("data/day14_users_raw.csv")  # قراءة الملف الأصلي
cleaned = clean_data(raw)  # تطبيق كل خطوات التنظيف
print(cleaned.head())  # عرض أول 5 صفوف بعد التنظيف
