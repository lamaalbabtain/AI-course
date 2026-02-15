
# DAY 30 
 

import pandas as pd              # استيراد مكتبة pandas للتعامل مع الجداول والبيانات
import numpy as np               # استيراد numpy للحسابات العددية
import matplotlib.pyplot as plt  # مكتبة الرسم البياني الأساسية
import seaborn as sns            # مكتبة رسم متقدمة وجميلة مبنية على matplotlib
%matplotlib inline               # يخلي الرسوم تظهر داخل Jupyter Notebook

# تحميل البيانات
df = pd.read_csv("data/house_prices.csv")  # قراءة ملف CSV وتخزينه في DataFrame اسمه df

# عرض معلومات عامة
print(df.shape)        # يعرض عدد الصفوف والأعمدة (حجم البيانات)
print(df.describe())   # يعطي ملخص إحصائي للأعمدة الرقمية (mean, std, min, max...)

# -----------------------
# Univariate Analysis
# -----------------------

numeric_cols = ["SalePrice", "GrLivArea", "LotArea", "TotalBsmtSF", "YearBuilt"]  
# تحديد قائمة بالأعمدة الرقمية اللي نبي نحلل توزيعها

for col in numeric_cols:                  # نكرر العملية لكل عمود في القائمة
    plt.figure(figsize=(6,4))             # إنشاء شكل رسم بحجم 6x4
    sns.histplot(df[col], kde=True)       # رسم Histogram + منحنى كثافة (KDE)
    plt.title(f"Distribution of {col}")   # وضع عنوان للرسم باسم العمود
    plt.show()                            # عرض الرسم

# -----------------------
# Boxplots (Target vs Categories)
# -----------------------

plt.figure(figsize=(12,5))                               # إنشاء شكل بحجم أكبر
sns.boxplot(x="Neighborhood", y="SalePrice", data=df)    # رسم Boxplot لعرض توزيع السعر حسب الحي
plt.xticks(rotation=90)                                  # تدوير أسماء الأحياء 90 درجة عشان تكون مقروءة
plt.title("SalePrice by Neighborhood")                   # عنوان الرسم
plt.show()                                               # عرض الرسم

plt.figure(figsize=(8,5))                                # إنشاء شكل جديد
sns.boxplot(x="HouseStyle", y="SalePrice", data=df)      # مقارنة السعر حسب نمط المنزل
plt.title("SalePrice by HouseStyle")                     # عنوان الرسم
plt.show()                                               # عرض الرسم

# -----------------------
# GroupBy Aggregation
# -----------------------

grouped = df.groupby("Neighborhood")["SalePrice"].agg(["mean", "count"])  
# تجميع البيانات حسب الحي وحساب:
# mean → متوسط السعر
# count → عدد المنازل في كل حي

print(grouped.sort_values("mean", ascending=False).head())  
# ترتيب الأحياء من الأعلى سعرًا إلى الأقل وعرض أعلى 5

# -----------------------
# Correlation Heatmap
# -----------------------

numeric_df = df.select_dtypes(include=["int64", "float64"])  
# اختيار الأعمدة الرقمية فقط

corr = numeric_df.corr()  
# حساب مصفوفة الارتباط بين كل الأعمدة الرقمية

plt.figure(figsize=(12,8))  
# إنشاء شكل كبير لعرض الخريطة الحرارية

sns.heatmap(corr, cmap="coolwarm")  
# رسم خريطة الارتباط بالألوان (أحمر = ارتباط قوي موجب، أزرق = سالب)

plt.title("Correlation Heatmap")  
# وضع عنوان للرسم

plt.show()  
# عرض الخريطة

# -----------------------
# Insights & Answers
# -----------------------

print("\nINSIGHTS:")  
# طباعة عنوان قسم الاستنتاجات

print("1) GrLivArea strongly correlates with SalePrice.")  
# استنتاج: مساحة المعيشة مرتبطة بقوة مع السعر

print("2) Neighborhood shows major price differences.")  
# استنتاج: الأحياء تختلف بشكل واضح في الأسعار

print("3) LotArea is right-skewed → needs log transform.")  
# استنتاج: مساحة الأرض منحرفة لليمين → تحتاج تحويل لوغاريتمي

print("\nAssessment:")  
# طباعة قسم التقييم

print("Q1 → SalePrice, LotArea need transformation (skewed).")  
# الأعمدة المنحرفة تحتاج تحويل

print("Q2 → Neighborhood groups differ clearly.")  
# يوجد فرق واضح بين الأحياء

print("Q3 → GarageCars & GarageArea likely redundant.")  
# عدد السيارات ومساحة القراج غالبًا مترابطين (تكرار معلومات)

print("Q4 → Log target, remove multicollinearity, try tree models.")  
# اقتراحات: تحويل الهدف لوغاريتميًا، إزالة التعدد الخطي، تجربة نماذج الأشجار