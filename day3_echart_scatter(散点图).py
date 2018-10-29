# 散点图1
from pyecharts import Scatter
v1 = [10,20,30,40,50,60]
v2 = [10,20,30,40,50,60]

scatter =Scatter("散点图示例")
scatter.add("A",v1,v2)
scatter.add("B",v1[::-1],v2) #v1[::-1] 倒序

scatter.render("scatter01.html")

# 散点图2
v1 = [10,20,30,40,50,60]
v2 = [10,20,30,40,50,60]

scatter =Scatter("散点图示例")
scatter.add("A",v1,v2)
scatter.add("B",v1[::-1],v2,
is_visualmap =True,visual_type ="size",
visual_range_size=[20,80])#散点可见

scatter.render("scatter02.html")