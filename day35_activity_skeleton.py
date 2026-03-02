"""
Day 35 Activity Solution: EDA Mini-Project
"""

import pandas as pd              # للتعامل مع البيانات
import seaborn as sns            # للرسم البياني
import matplotlib.pyplot as plt  # لعرض الرسومات والتحكم فيها

path = "data/day35_project.csv"  # مسار ملف البيانات
df = pd.read_csv(path)           # قراءة الملف وتحويله الى DataFrame

sns.histplot(df, x="income", bins=15, kde=True)  # رسم توزيع الدخل مع منحنى الكثافة
plt.title("توزيع الدخل")                        # اضافة عنوان
plt.show()                                      # عرض الرسم

sns.boxplot(x="segment", y="income", data=df)  # رسم صندوقي لمقارنة الدخل حسب الفئة
plt.title("الدخل حسب الفئة")                   # اضافة عنوان
plt.show()                                      # عرض الرسم

sns.scatterplot(x="age", y="spend", hue="segment", data=df)  # العلاقة بين العمر والمصروف وتلوين حسب الفئة
plt.title("العمر مقابل المصروف")                                # اضافة عنوان
plt.show()                                                    # عرض الرسم

corr_matrix = df[["age", "income", "spend"]].corr()           # حساب مصفوفة الارتباط للمتغيرات الرقمية
sns.heatmap(corr_matrix, annot=True, cmap="viridis", vmin=-1, vmax=1)  # رسم خريطة حرارية لمصفوفة الارتباط
plt.title("مصفوفة الارتباط")                                  # اضافة عنوان
plt.show()                                                    # عرض الرسم