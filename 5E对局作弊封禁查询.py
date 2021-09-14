# -*- coding:utf-8 -*-

"""
时间:2021年09月14日
作者:幻非
"""

import os
import requests
import json

url = 'https://arena.5eplay.com/data/player/7132912j9dckv'
uid = os.path.basename(url)


games_list = []
i = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36 '
}


# 输入用户ID,输出比赛地址列表
def pages(self):
    global i
    page_url = "https://arena.5eplay.com/api/data/match_list/" + self + "?page=" + str(i)
    response = json.loads(requests.get(url=page_url, headers=headers).text)
    page_bool = response["success"]
    # print(page_url)
    if page_bool:
        for page in response['data']:
            games_list.append('https://arena.5eplay.com/data/match/' + page['match_code'])
        i = i + 1
        pages(self)
    else:
        print("战绩查询完毕,开始检测封禁玩家")
    return games_list


# 检测战绩页面是否含有封禁玩家
def check(self):
    for game_url in self:
        ban = requests.get(url=game_url, headers=headers).text
        if ban.find('ban-type') != -1:
            print(game_url)


check(pages(uid))

