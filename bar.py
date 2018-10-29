import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn 设置样式
sns.set_style(style="darkgrid")
# 设置字体，放大倍数
sns.set_context(context="poster",font_scale=0.8)
#设置颜色
sns.set_palette("Reds")

df = pd.read_csv("HR.csv")
# plt.title("SALARY")
# plt.xlabel("salary")
# plt.ylabel("Number")
# plt.xticks(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts().index)
# plt.bar(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts())
# for x,y in zip(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts()):
# 	plt.text(x,y,y,ha="center",va="bottom")
# plt.axis([0,5,0,10000])

# seaborn 是matplotlib 的封装
sns.countplot(x="salary",data=df,hue="department")
plt.show()
