"""
Day 13 Activity Solution: Large Dataset Cleaning
"""

import pandas as pd  # استيراد مكتبة بانداز للتعامل مع البيانات
import time  # استيراد مكتبة الوقت لحساب مدة التنفيذ


def clean_chunk(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()  # عمل نسخة لتجنب تعديل الأصلي
    out["age"] = pd.to_numeric(out["age"], errors="coerce")  # تحويل العمر لأرقام، أي خطأ يصبح NaN
    out["income"] = pd.to_numeric(out["income"], errors="coerce")  # تحويل الدخل لأرقام، أي خطأ يصبح NaN
    out["city"] = out["city"].astype("string").str.strip().str.lower()  # تنظيف عمود المدينة: نصوص، إزالة مسافات، تحويل لحروف صغيرة
    return out  # إعادة الداتا المعدلة


def process_large_file(path_in: str, path_out: str, chunksize: int = 50000) -> None:
    start = time.perf_counter()  # تسجيل وقت البداية
    reader = pd.read_csv(path_in, chunksize=chunksize)  # قراءة الملف على شكل أجزاء (chunks) لتجنب استهلاك الذاكرة
    for i, chunk in enumerate(reader):  # المرور على كل جزء من الملف
        cleaned = clean_chunk(chunk)  # تنظيف الجزء الحالي
        mode = "w" if i == 0 else "a"  # كتابة الجزء الأول "w"، والبقية "a" للإلحاق
        header = i == 0  # كتابة العناوين مرة واحدة فقط
        cleaned.to_csv(path_out, mode=mode, header=header, index=False)  # حفظ الجزء بعد التنظيف
    elapsed = time.perf_counter() - start  # حساب الوقت المستغرق
    print(f"Completed in {elapsed:.2f}s")  # طباعة مدة التنفيذ


# Example run
process_large_file("data/day13_large_users.csv", "data/day13_large_users_clean.csv", chunksize=1000)  
# تشغيل الدالة على ملف كبير مع تقسيمه لـ 1000 صف لكل جزء
