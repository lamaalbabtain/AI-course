"""
Day 39 Activity Solution: Broadcasting
"""

import numpy as np  # استيراد مكتبة numpy للتعامل مع المصفوفات والعمليات الرياضية

# إنشاء مصفوفة 2D (كل صف يمثل متجه)
X = np.array([
    [3.0, 4.0],
    [1.0, 2.0],
    [0.0, 5.0],
])

# حساب طول كل صف (Norm) باستخدام المعادلة الجذر التربيعي لمجموع المربعات
# axis=1 يعني نحسب لكل صف
# keepdims=True حتى تبقى النتيجة كمصفوفة عمودية (3x1) لتعمل مع Broadcasting
row_norms = np.linalg.norm(X, axis=1, keepdims=True)

# تطبيع كل صف بقسمته على طوله
# هنا يحدث Broadcasting لأننا نقسم مصفوفة (3x2) على (3x1)
X_normalized = X / row_norms

# طباعة أطوال الصفوف قبل التطبيع
print("Row norms:", row_norms.ravel())  # ravel لتحويلها لشكل 1D عند الطباعة

# طباعة المصفوفة بعد التطبيع
print("Normalized X:\n", X_normalized)

# التأكد أن طول كل صف أصبح = 1 بعد التطبيع
print("Norms after:", np.linalg.norm(X_normalized, axis=1))