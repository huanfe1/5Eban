import urllib
import requests
import re
import webbrowser
import json
import os



def pages(uid,p):#变化网址页数
	url = "https://www.5ewin.com/api/data/match_list/" + uid + "?yyyy=2020&page=" + p
	return(url)


def get(url,i): #i表示第10场内的第几场
	response = urllib.request.urlopen(url)
	getdata = response.read().decode('utf-8')
	timename = json.loads(getdata)["data"][i]["match_code"]
	return(timename)


def findnumber(url): #检测该10场数据是否少于10场
	response = urllib.request.urlopen(url)
	getdata = response.read().decode('utf-8')
	sub = "match_code"
	num = getdata.count(sub)#number正常为10
	return(num)


def search(url):
	response = urllib.request.urlopen(url)
	#print("代码：",response.getcode())#代码如果是200表示获取成功
	getdata = response.read().decode('utf-8')
	#ban1 = "ban-type1" #违规行为封禁
	#ban3 = "ban-type3" #非法行为冻结
	#ban4 = "ban-type4" #作弊封禁
	ban = "ban-type4"
	searchresult = getdata.find(ban)
	#print(searchresult)
	if searchresult != -1:
		return(url)



userall = input("请输入5E玩家地址:")


reg = r'https://www.5ewin.com/data/player/(.*)'
imgre = re.compile(reg)
userid = ''.join(re.findall(imgre,userall))

page = 1
i = 0
for x in range(10):
	allpage = pages(userid,str(page))#获取到的总体战绩页
	page = page + 1
	number = findnumber(allpage)
	if number == 0: #检测剩余战绩是否为零
		break
	#print(allpage)
	for i in range(number):
		data = get(allpage,i)
		data = "https://www.5ewin.com/data/match/" + data
		#print(data)
		i + 1
		banwz = search(data)
		if banwz != None:
			print(banwz)
input("按任意键退出")
