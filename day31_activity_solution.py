"""
Day 31 Activity Solution: Seaborn Visualizations
"""  

import pandas as pd  # استيراد مكتبة pandas للتعامل مع البيانات
import seaborn as sns  # استيراد مكتبة seaborn للرسم البياني
import matplotlib.pyplot as plt  # استيراد matplotlib للتحكم في الرسوم

path = "data/day31_seaborn.csv"  # تحديد مسار ملف البيانات
df = pd.read_csv(path)  # قراءة ملف CSV وتحويله إلى DataFrame

sns.histplot(df, x="income", bins=20)  # رسم Histogram لعمود income وتقسيمه إلى 20 فئة
plt.title("Income histplot")  # إضافة عنوان للرسم
plt.show()  # عرض الرسم على الشاشة

sns.kdeplot(df["age"], fill=True)  # رسم منحنى كثافة لتوزيع الأعمار مع تعبئة المساحة تحته
plt.title("Age KDE")  # إضافة عنوان للرسم
plt.show()  # عرض الرسم

sns.boxplot(x="segment", y="income", data=df)  # رسم Boxplot لمقارنة الدخل حسب كل فئة segment
plt.title("Income by Segment")  # إضافة عنوان للرسم
plt.show()  # عرض الرسم

sns.countplot(x="segment", data=df)  # رسم Countplot لعدّ عدد القيم في كل segment
plt.title("Segment counts")  # إضافة عنوان للرسم
plt.show()  # عرض الرسم