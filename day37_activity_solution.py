"""
Day 37 Activity Solution: Dot Product
"""

import numpy as np  # للتعامل مع المصفوفات والعمليات الرياضية

a = np.array([1.0, 2.0, 3.0])     # المصفوفة الأولى
b = np.array([0.5, 1.0, 1.5])     # المصفوفة الثانية

dot = a @ b                        # حاصل الضرب النقطي بين a و b
cos = dot / (np.linalg.norm(a) * np.linalg.norm(b))  # التشابه الكوني بين المصفوفات

print("a:", a)                     # عرض المصفوفة a
print("b:", b)                     # عرض المصفوفة b
print("dot:", dot)                 # عرض ناتج الضرب النقطي
print("cosine similarity:", cos)   # عرض التشابه الكوني