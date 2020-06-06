'''
@Author: your name
@Date: 2020-02-14 20:10:40
@LastEditTime: 2020-06-06 17:59:54
@LastEditors: Please set LastEditors
@Description: 这是最初版本的播放量增长爬虫,能够在单一用户模式下实现多个视频的播放量增长.效率很低,但是非常稳定.
@FilePath: /bilibili_PV_spider/simple_spider.py
'''

import requests
import time
import json
from settings import *


headers = {
    'Host':'api.bilibili.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.bilibili.com',
    'Content-type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bilibili.com/video/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    '$Cookie':cookie
}

count = 0

with open('info.json','r') as f:
    infos = json.load(f)

while True:
    # data_list = [data_generator(aid_list[index],cid_list[index]) for index in range(len(aid_list))]
    for data in infos:
        stime = str(int(time.time()))
        data['stime'] = stime
        headers['Referer'] = 'https://www.bilibili.com/video/{}'.format(data['bvid'])
        print(data)
        req = requests.post('https://api.bilibili.com/x/click-interface/click/web/h5',data=data,headers=headers)
        print(count,data['aid'],req.text)
        time.sleep(5)
    
    count += 1
    print("now in loop {}".format(count))
    # print(req.text)
    time.sleep(300)


print('over')