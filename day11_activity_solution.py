"""
Day 11 Activity Solution: Outlier Strategies
"""

import pandas as pd      # نستدعي مكتبة البانداز عشان نتعامل مع البيانات
import numpy as np       # نستدعي numpy (هنا احتياط لو احتجنا عمليات رقمية)

# Load data
path = "data/day11_income.csv"   # حددنا مسار ملف البيانات
df = pd.read_csv(path)           # قرينا الملف وخزناه في df


def winsorize_series(s: pd.Series, lower_q=0.01, upper_q=0.99) -> pd.Series:
    # دالة تقص القيم المتطرفة عند نسب مئوية معينة

    lower, upper = s.quantile(lower_q), s.quantile(upper_q)
    # نحسب الحد الأدنى (1%) والحد الأعلى (99%)

    return s.clip(lower=lower, upper=upper)
    # أي قيمة أقل من lower أو أعلى من upper تتعدل لهذي الحدود


def remove_upper_tail(s: pd.Series, upper_q=0.99) -> pd.Series:
    # دالة تحذف القيم العالية جدًا

    upper = s.quantile(upper_q)
    # نحسب حد 99%

    return s[s <= upper]
    # نرجع بس القيم اللي أقل أو تساوي الحد (يعني حذفنا الباقي)


raw = df["income"]  
# هذا العمود الأصلي بدون أي تعديل

cap = winsorize_series(raw, 0.01, 0.99)
# طبقنا القص (ما حذفنا صفوف، بس عدلنا القيم الكبيرة)

rem = remove_upper_tail(raw, 0.99)
# حذفنا القيم الأعلى من 99%


print("Raw mean:", raw.mean())
# طبعنا متوسط البيانات الأصلية

print("Capped mean:", cap.mean())
# طبعنا المتوسط بعد القص

print("Removed mean:", rem.mean())
# طبعنا المتوسط بعد الحذف

print("Raw max:", raw.max())
# أعلى قيمة قبل أي تعديل

print("Capped max:", cap.max())
# أعلى قيمة بعد القص (بتكون = حد 99%)

print("Removed max:", rem.max())
# أعلى قيمة بعد الحذف (أقل من الأصلية)
