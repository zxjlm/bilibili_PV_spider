'''
@Author: your name
@Date: 2020-06-06 17:21:21
@LastEditTime: 2020-06-06 17:46:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /bilibili_PV_spider/info_getter.py
'''
import requests
from settings import *
import json


headers = {
    'Host':'api.bilibili.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bilibili.com/video/av88350865',
    'Cookie':cookie
}

author_url = 'https://api.bilibili.com/x/space/arc/search?mid=167679424&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
req = requests.get(author_url,headers=headers)
infos = [{'aid':foo['aid'],'cid':'','bvid':foo['bvid'],'part':'1','lv':'5','mid':str(foo['mid']),'ftime':'1581244587','stime':'','jsonp':'jsonp','type':'3','sub_type':'0'} for foo in req.json()['data']['list']['vlist']]
for ind,info in enumerate(infos[:2]):
    infos[ind]['cid'] = str(requests.get('https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(info['bvid'])).json()['data'][0]['cid'])

with open('info.json','w') as f:
    json.dump(infos,f)