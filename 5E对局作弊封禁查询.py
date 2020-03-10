import urllib.request
import re
import webbrowser

i = 0

#ban-type3-simplified-chinese 表示非法行为冻结
#ban-type4-simplified-chinese 表示作弊封禁

def get(userurl):
	response = urllib.request.urlopen(userurl) #获取网页代码
	data = response.read() ###次行内容不太清楚，后续查查
	if data != None:
		data = data.decode('utf-8')#转换编码
		reg = r'<a href="(.+?)" target="_blank">查看详情</a>'
		rereg = re.compile(reg)
		relist = re.findall(rereg,data)
		del relist[10:12] #还没有做如果战绩少于10场怎么办
		print(relist)
		return(relist)



def search(dataurl):#查找该战绩是否含有封禁玩家
	response = urllib.request.urlopen(dataurl)
	data = response.read()
	data = data.decode('utf-8')
	bantype3 = 'ban-type3'
	bantype4 = 'ban-type4'
	findban = data.find(bantype4)#括号内容的数字为查找的封禁类型,后续加可选择
	if findban != -1:
		return(dataurl)

url = "https://www.5ewin.com/data/player/4132633imxyu4"#玩家战绩网址

getwz = get(url)

for i in range(10):#不点刷新之前只显示最后10的战绩
	getbanwz = search(getwz[i])
	if getbanwz != None:
		print(getbanwz)
	i+1



#加上少于10场怎么办
#可选择玩家网址
#模拟点击刷新网址获取后续的战绩
