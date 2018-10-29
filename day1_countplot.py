'''
柱状图
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# seaborn 可以设置样式
sns.set_style(style="whitegrid")
sns.set_context(context="poster",font_scale=0.6)
# sns.set_palette("Reds")
sns.set_palette(sns.color_palette("RdBu",n_colors=7))


df =pd.read_csv("HR.csv")
df =df[df["salary"]!="nme"]#去掉异常值
# seaborn 也可以直接绘制柱状图
sns.countplot(x="salary", hue="department",data= df)

# pd.set_option('display.width',130)
# pd.set_option('display.max_columns',130)
# pd.set_option('display.max_colwidth',130)
# print(df["salary"].value_counts())#统计次数
# plt.title("SALARY")#标题
# plt.xlabel("salary")#x标签
# plt.ylabel("Number")#y标签
# plt.xticks(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts().index)#设置横轴的标注;图像右移0.5
# plt.axis([0,4,0,10000])#设置显示范围，横轴[0.4];纵轴[0,10000]
# plt.bar(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts(), width=0.5)#图像右移0.5;宽度也为0.5
#
# # 把数值标注在图表上
# for x,y in zip(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts()):
#     plt.text(x,y,y,ha="center",va="bottom")
#
plt.show()