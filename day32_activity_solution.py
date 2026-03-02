"""
Day 32 Activity Solution: Relationship Plots
"""  
# هذا تعليق متعدد الأسطر يوضح أن الملف يحتوي على حل نشاط اليوم 32
# الموضوع عن الرسوم التي تُظهر العلاقات بين المتغيرات

import pandas as pd  
# استيراد مكتبة pandas واختصار اسمها إلى pd للتعامل مع البيانات

import seaborn as sns  
# استيراد مكتبة seaborn واختصارها إلى sns للرسم البياني الإحصائي

import matplotlib.pyplot as plt  
# استيراد matplotlib واختصارها إلى plt لاستخدامها في عرض الرسوم

path = "data/day32_relationships.csv"  
# تخزين مسار ملف البيانات داخل متغير اسمه path

df = pd.read_csv(path)  
# قراءة ملف CSV من المسار المحدد وتحويله إلى DataFrame اسمه df

sns.scatterplot(data=df, x="feature1", y="outcome", hue="segment", style="priority")  
# رسم Scatter Plot
# data=df يعني استخدام البيانات من df
# x="feature1" تحديد المتغير الذي سيكون على المحور الأفقي
# y="outcome" تحديد المتغير الذي سيكون على المحور الرأسي
# hue="segment" تلوين النقاط حسب قيمة segment
# style="priority" تغيير شكل النقاط حسب قيمة priority

plt.title("Outcome vs feature1")  
# إضافة عنوان للرسم البياني

plt.show()  
# عرض الرسم على الشاشة

g = sns.relplot(
# إنشاء رسم علاقات متقدم وتخزينه في متغير g

    data=df,
    # تحديد مصدر البيانات

    x="feature1",
    # تحديد المتغير للمحور الأفقي

    y="outcome",
    # تحديد المتغير للمحور الرأسي

    hue="segment",
    # تلوين النقاط حسب segment

    col="priority",
    # تقسيم الرسم إلى أعمدة متعددة حسب قيمة priority

    kind="scatter",
    # تحديد نوع الرسم ليكون Scatter Plot

)
# إغلاق دالة relplot

plt.show()  
# عرض جميع الرسوم التي أنشأها relplot