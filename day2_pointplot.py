'''
折线图 mtplotlib.pylot 里的plot命令;seaborn 中的potplot
一般表示数据变化的趋势 横轴一般是时间，或者数据规模的范围
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style(style="darkgrid")
df = pd.read_csv("HR.csv")

# 分组 聚合方法取均值
sub_df = df.groupby("time_spend_company").mean()
# 获得员工在该公司呆的时间的 离职率
f =plt.figure()
f.add_subplot(1,3,1)
sns.pointplot(x = sub_df.index,y=sub_df["left"])
f.add_subplot(1,3,2)
sns.pointplot(x="time_spend_company",y="left",data =df)

f.add_subplot(1,3,3)
plt.plot([1,2,3,4,5],[2,5,3,8,6]) #[1,2],[2,5],[3,3],[4,8],[5,6]

plt.show()