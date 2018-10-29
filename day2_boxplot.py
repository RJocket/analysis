'''
异常值分析——箱线图
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

sns.set_style(style="darkgrid")
sns.set_palette(sns.color_palette("RdBu",n_colors=7))

df = pd.read_csv("HR.csv")
#  处理异常值
df = df.dropna(axis=0,how ="any")
df = df[df["last_evaluation"]<=1][df["salary"]!="nme"][df["department"]!="sale"]

f =plt.figure()
f.add_subplot(1,2,1)
sns.boxplot(y=df["time_spend_company"]) #竖着

f.add_subplot(1,2,2)
#横着 whis =3，即k=3，默认为1.5；saturation=0.75 即四分位
sns.boxplot(x=df["time_spend_company"], saturation =0.75,whis = 3) 

plt.show()
