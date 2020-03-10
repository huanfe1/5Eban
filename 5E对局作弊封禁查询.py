import urllib.request
import re
import webbrowser



#ban-type3-simplified-chinese 表示非法行为冻结
#ban-type4-simplified-chinese 表示作弊封禁
def get(url0):
	response0 = urllib.request.urlopen(url0)
	#print("代码：",response0.getcode()) 	#代码如果是200表示获取成功
	data0 = response0.read()	#获取网页代码
	if data0 != None:
		data0 = data0.decode('utf-8')	#转换编码
		reg0 = r'<a href="(.+?)" target="_blank">查看详情</a>'
		imreg0 = re.compile(reg0)
		imglist = re.findall(imreg0,data0)
		del imglist[10:12] #删除列表中11号到12行的内容
		#getwz = '\n'.join(imglist) #'\n' 输入换行   #可以直接用getwz[第几行]来代替
		return(imglist)



def search(url):
	response = urllib.request.urlopen(url)
	#print("代码：",response.getcode())	#代码如果是200表示获取成功
	data = response.read()
	data = data.decode('utf-8')
	regban4 = 'ban-type4'
	regban3 = 'ban-type3'
	findresult = data.find(regban4)
	if findresult != -1:
		return(url)

url0 = "https://www.5ewin.com/data/player/4132633imxyu4"
getwz = get(url0)

i = 0
for i in range(10):
	print(getwz[i])#打印10场战绩
	getbanwz =  search(getwz[i])
	if getbanwz != None:
		print(getbanwz)
	i+1