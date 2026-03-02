# Day 40 Activity Solution: Matrix Operations Exercise

import numpy as np  # استيراد مكتبة numpy

X = np.array([  # تعريف المصفوفة X (المدخلات)
    [1.0, 0.5],  # العينة الأولى
    [2.0, -1.0],  # العينة الثانية
    [0.0, 3.0],  # العينة الثالثة
])

W = np.array([  # تعريف مصفوفة الأوزان W
    [0.2, -0.1, 0.5],  # أوزان الميزة الأولى
    [0.7, 0.3, -0.2],  # أوزان الميزة الثانية
])

b = np.array([0.1, 0.0, -0.3])  # تعريف متجه الانحياز (bias)

Y = X @ W + b  # ضرب X في W ثم إضافة bias

print("X shape:", X.shape)  # طباعة أبعاد X
print("W shape:", W.shape)  # طباعة أبعاد W
print("b shape:", b.shape)  # طباعة أبعاد b
print("Y shape:", Y.shape)  # طباعة أبعاد Y
print("Y:\n", Y)  # طباعة القيم الناتجة