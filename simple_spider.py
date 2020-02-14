'''
@Author: your name
@Date: 2020-02-14 20:10:40
@LastEditTime : 2020-02-14 20:20:03
@LastEditors  : Please set LastEditors
@Description: 这是一个简单的播放量增长爬虫,实现了单进程单用户的播放量增长
@FilePath: /bilibili_PV_spider/simple_spider.py
'''

import requests
import time
from settings import *


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

stime = str(int(time.time()))

def data_generator(aid,cid):
    data ={
        'aid':aid,
        'cid':cid,
        'part':'1',
        'mid':mid,
        'lv':'5',
        # 'ftime':'1581244587',
        'stime':stime,
        'jsonp':'jsonp',
        'type':'3',
        'sub_type':'0'
    }
    return data

count = 0
while True:
    data_list = [data_generator(aid_list[index],cid_list[index]) for index in range(len(aid_list))]
    for data in data_list:
        req = requests.post('https://api.bilibili.com/x/click-interface/click/web/h5',data=data,headers=headers)    
    
    count += 1
    print("now in loop {}".format(count))
    print(req.text)
    time.sleep(400)


print('over')