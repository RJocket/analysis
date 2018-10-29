from pyecharts import Map
value = [155,10,66,78]
attr = ["福建","山东","北京","上海"]
map =Map("全国地图示例")
map.add("",attr,value,maptype = "china")
map.render("map01.html")

value = [20,100,253,77,65]
attr =['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map =Map("广东地图示例",width=1200,height =600)
map.add("",attr,value,maptype ="广东",is_visualmap=True,
	visual_text_color ="#000",is_label_show=True)
map.render("map02.html")