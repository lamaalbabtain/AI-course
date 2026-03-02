"""
Day 36 Activity Solution: Vectors
"""

import numpy as np  # للتعامل مع المصفوفات والعمليات الرياضية

feature = np.array([30.0, 50.0, 10.0])  # مصفوفة السمات
weights = np.array([0.05, 0.8, -0.1])   # مصفوفة الأوزان

sum_vec = feature + weights  # جمع المصفوفات
scaled = 0.1 * weights       # ضرب الأوزان في عامل مقياس

print("feature:", feature, "shape:", feature.shape)   # عرض السمات وشكلها
print("weights:", weights, "shape:", weights.shape)   # عرض الأوزان وشكلها
print("sum:", sum_vec)                                # عرض ناتج الجمع
print("scaled:", scaled)                               # عرض ناتج الضرب بالمقياس
print("||feature||:", np.linalg.norm(feature))        # طول أو معيار مصفوفة السمات
print("||weights||:", np.linalg.norm(weights))       # طول أو معيار مصفوفة الأوزان