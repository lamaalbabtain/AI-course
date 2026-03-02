"""
Day 34 Activity Solution: Pattern Discovery
"""

import pandas as pd              # للتعامل مع البيانات
import seaborn as sns            # للرسم البياني
import matplotlib.pyplot as plt  # لعرض الرسومات

# مسار ملف البيانات
path = "data/day34_patterns.csv"

# قراءة ملف CSV وتحويله الى DataFrame
df = pd.read_csv(path)

# رسم scatter plot يوضح العلاقة بين الوقت والقيمة
# hue يلوّن النقاط حسب segment
# col يقسم الرسوم لاعمدة حسب season
g = sns.relplot(
    data=df,
    x="time",
    y="value",
    hue="segment",   # تلوين حسب الفئة
    col="season",    # تقسيم حسب الموسم
    kind="scatter"   # نوع الرسم نقاط
)

# عرض الرسم
plt.show()

# رسم lmplot
# هذا نفس السكتر تقريباً لكن يضيف خط انحدار يوضح الاتجاه العام
sns.lmplot(
    data=df,
    x="time",
    y="value",
    hue="segment",   # تلوين حسب الفئة
    col="season"     # تقسيم حسب الموسم
)

# عرض الرسم الثاني
plt.show()