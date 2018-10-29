# 1.折线图
from pyecharts import Line
attr = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
v1 = [5,20,36,10,10,90]
v2 = [55,60,16,20,15,80]
line_1 =Line("折线图示例1")
line_1.add("商家A",attr,v1,mark_point=["average"])
line_1.add("商家B",attr,v2,is_smooth = True,mark_line =["max","average","min"])

line_1.render("line01.html")

# 2. 折线图2
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y1 = [5,20,36,10,10,90]
y2 = [55,60,16,20,15,80]
line_2 =Line("折线图示例2")
label1="商家A"
label2="商家B"
# diamond 钻石/菱形
kwargs =dict(
	mack_point =["average","min","max"],
	symbol ="diamond",
	showSymbol =True)

line_2.add(label1,x,y1,**kwargs)

# "arrow" 箭头
kwargs2 = dict(
	mack_point =["average","min","max"],
	symbol ="arrow",
	showSymbol =True
	)
line_2.add(label2,x,y2,**kwargs2)
line_2.render("line02.html")

# 3. 面积图
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y1 = [5,20,36,10,10,90]
y2 = [55,60,16,20,15,80]
line_3 = Line("面积图示例")
label1="商家A"
label2="商家B"
kwargs = dict(is_fill =True,
	line_opacity = 0.2,
    area_opacity = 0.4,
    symbol = None)
line_3.add(label1,x,y1,**kwargs)

kwargs2 = dict(
	is_fill= True,
    area_color= '#000',
    area_opacity= 0.3, 
    is_smooth= True)

line_3.add(label2,x,y2,**kwargs2)
line_3.render("line03.html")