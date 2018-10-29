'''
柱状图和直方图 虽然看上去形状差不多，但是意义不同。
柱状图 的横轴，可以是类别，也可以是表示类别或者范围的数字。有意义的是其纵轴的高低。
直方图 的横轴，是一个范围或者区间，有意义的是其面积。所以，理论中，是可以画出粗细不同的直方图，而直方图的粗细也是有含义的。
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style="darkgrid")
sns.set_palette(sns.color_palette("RdBu",n_colors=7))

df = pd.read_csv("HR.csv")
# 处理异常值
df = df.dropna(axis=0,how ="any")
df = df[df["last_evaluation"]<=1][df["salary"]!="nme"][df["department"]!="sale"]


f = plt.figure()
f.add_subplot(1,3,1)
# 绘制直方图 kde=False,则不显示直方图的折线；hist =Flase,则不显示直方图的柱
sns.distplot(df["satisfaction_level"],bins =10)

f.add_subplot(1,3,2)
sns.distplot(df["last_evaluation"],bins=10)

f.add_subplot(1,3,3)
sns.distplot(df["average_monthly_hours"],bins=10)
print(df["satisfaction_level"].value_counts())
plt.show()

