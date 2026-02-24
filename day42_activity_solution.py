"""
Day 42 Activity Solution: Distributions
"""
import numpy as np           # استدعاء مكتبة numpy للتعامل مع الأرقام والمصفوفات
import seaborn as sns        # استدعاء مكتبة seaborn لرسم الرسومات البيانية
import matplotlib.pyplot as plt  # استدعاء مكتبة matplotlib لعرض الرسومات

np.random.seed(42)          # تثبيت "بذرة" الأرقام العشوائية لتظهر نفس الأرقام في كل مرة

# توليد 5000 رقم عشوائي من توزيع متساوي بين 0 و 1
uniform = np.random.uniform(0, 1, size=5000)

# توليد 5000 رقم عشوائي من توزيع طبيعي بمتوسط 0 وانحراف معياري 1
normal = np.random.normal(0, 1, size=5000)

# رسم الرسم البياني للتوزيع المتساوي مع رسم الخط التقديري للكثافة
sns.histplot(uniform, bins=30, stat="density", kde=True)
plt.title("Uniform Distribution (0,1)")   # Plot title
plt.show()                                # Show the plot

# رسم الرسم البياني للتوزيع الطبيعي مع رسم الخط التقديري للكثافة
sns.histplot(normal, bins=30, stat="density", kde=True)
plt.title("Normal Distribution (mean=0, std=1)")  # Plot title
plt.show()                                        # Show the plot

# حساب وعرض المتوسط والانحراف المعياري للتوزيع المتساوي
print("Uniform mean/std:", uniform.mean(), uniform.std())

# حساب وعرض المتوسط والانحراف المعياري للتوزيع الطبيعي
print("Normal mean/std:", normal.mean(), normal.std())
