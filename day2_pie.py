'''
饼图 -- 结构分析
seaborn中没有提供画饼图的方法；使用maplotlib.pyplot中的pie绘制
'''
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot  as plt

df = pd.read_csv("HR.csv")
df = df.dropna(axis=0,how= "any")
df = df[df["last_evaluation"]<=1][df["salary"]!="nme"][df["department"]!="sale"]

# 绘制饼图
lbs = df["department"].value_counts().index #标签
# 突出重点图 0.1为间隔
explodes = [0.1 if i=="sales" else 0 for i in lbs] #list
plt.pie(df["department"].value_counts(normalize =True),explode = explodes,labels =lbs, autopct="%1.1f%%",colors =sns.color_palette("Reds"))

plt.show()
