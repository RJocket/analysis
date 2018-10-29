from pyecharts import Pie
# 1. 饼图
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y = [5,20,36,10,75,90]

pie =Pie("饼图示例")
pie.add("",x,y,is_label_show=True)

pie.render("pie.html")

# 2. 饼图2
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y = [5,20,36,10,75,90]

pie =Pie("饼图-圆环图示例",title_pos ="center")
#radius(rmin, _rmax)最大半径，最小半径
kwargs = dict(
	radius =(40,75), 
	label_text_color =None,
	is_label_show =True,
	legend_orient ="vertical",
	legend_pos = "left"
	)
pie.add("",x,y,**kwargs)
pie.render("pie02.html")