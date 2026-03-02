"""
Day 33 Activity Solution: Correlation Heatmaps
"""

import pandas as pd              # للتعامل مع البيانات
import seaborn as sns            # للرسم البياني
import matplotlib.pyplot as plt  # لعرض الرسومات والتحكم فيها

# مسار ملف البيانات
path = "data/day33_corr.csv"

# قراءة الملف وتحويله الى DataFrame
df = pd.read_csv(path)

# حساب مصفوفة الارتباط بين الاعمدة الرقمية
corr = df.corr()

# رسم خريطة حرارية توضح قوة الارتباط
# annot=True يعرض قيمة الارتباط داخل كل مربع
# cmap="coolwarm" يحدد الوان من ازرق (سالب) الى احمر (موجب)
# vmin و vmax يثبت المدى من -1 الى 1
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

# اضافة عنوان للرسم
plt.title("Correlation Heatmap")

# عرض الرسم
plt.show()