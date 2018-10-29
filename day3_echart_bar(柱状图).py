
# 1. 柱状图
from pyecharts import Bar

bar = Bar("我的第一个图表","Bar")

# 将3个关键字参数打包成1个数据类型为字典的变量kwargs。
kwargs = dict(
	name ="柱状图",
	x_axis = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
	y_axis = [5,20,6,36,10,75]
	)

# kwargs作为参数传入Bar对象的add方法中时，
# 需要使用**kwargs，这样可以使其自动解包，字典中的键值对会对应函数需要的参数。
bar.add(**kwargs)

# Bar对象的render方法会产生一个html文件，可以用浏览器打开该文件进行查看。
bar.render("bar01.html")

# 2. 直方图
# 在pyecharts中，直方图也是使用Bar对象画出。
# 与柱形图的不同之处是实例化Bar对象时多了1个参数bar_category_gap，
# 含义是每个柱子之间的间隔，如果设置为0，则画直方图。
bar = Bar("我的第二个图表","Histogram")
kwargs = dict(
	name ="直方图",
	x_axis = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
	y_axis = [5,20,6,36,10,75],
	bar_category_gap = 0
	)
bar.add(**kwargs)
bar.render('Histogram.html')

# 3. 堆叠柱状图
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y1 = [5,20,36,10,75,90]
y2 = [10,25,8,60,20,80]
bar = Bar("柱状图数据堆叠示例")
title1 ="商家A"
title2 ="商家B"
bar.add(title1,x,y1,is_stack = True)
bar.add(title2,x,y2,is_stack =True)
bar.render("Stacked_histogram.html")

# 4. 标记线和标记点
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y1 = [5,20,36,10,75,90]
y2 = [10,25,8,60,20,80]
bar = Bar("标记线和标记点示例")
title1 ="商家A"
title2 ="商家B"
bar.add(title1,x,y1,mark_point=["average"])
bar.add(title2,x,y2,mark_line=["min","max"])
bar.render("bar02.html")

# 5. 条形图
x = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
y1 = [5,20,36,10,75,90]
y2 = [10,25,8,60,20,80]
bar = Bar("条形图","x轴与y轴交换")
title1 ="商家A"
title2 ="商家B"
bar.add(title1,x,y1)
bar.add(title2,x,y2,is_convert=True) #折叠
bar.render("bar03.html")
