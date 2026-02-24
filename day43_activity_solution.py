"""
Day 43 Activity Solution: Probability Computation with SciPy
"""

import numpy as np           # استدعاء مكتبة numpy للتعامل مع الأرقام والمصفوفات
from scipy import stats      # استدعاء مكتبة scipy لإجراء العمليات الإحصائية

np.random.seed(43)           # تثبيت "بذرة" الأرقام العشوائية لتظهر نفس النتائج في كل مرة

# تعريف التوزيع الطبيعي بمتوسط 0 وانحراف معياري 1
dist = stats.norm(loc=0.0, scale=1.0)

# تحديد النطاق بين -1 و 1
a, b = -1.0, 1.0

# حساب احتمال أن يكون المتغير في النطاق [a, b] باستخدام الدالة التراكمية
prob = dist.cdf(b) - dist.cdf(a)
print("CDF range prob:", prob)  # عرض الاحتمال المحسوب باستخدام CDF

# حساب percentile 90 (القيمة التي 90% من البيانات أقل منها)
q90 = dist.ppf(0.9)
print("90th percentile:", q90)  # عرض percentile 90

# توليد 100000 عينة عشوائية من التوزيع الطبيعي
samples = dist.rvs(size=100000)

# حساب الاحتمال تجريبيًا (عدد العينات بين a و b مقسوم على العدد الكلي)
empirical = np.mean((samples >= a) & (samples <= b))
print("Empirical prob:", empirical)  # عرض الاحتمال التجريبي