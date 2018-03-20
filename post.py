# -*- coding: utf-8 -*
import requests
import json
import time

#327584
#64145



# 评论
def send(t):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')

    url = 'http://112.74.179.199:3030/api/registercod'
    data={'phone':str(t)};
    try:
        req = requests.get(url,cookies=cookies,headers=headers,data=data)
        back=req.text
    except:
        back = 'error'
    return back




for i in range(13813813800, 13813813801):
    print(i)

    ww=send(i);
    print(ww);
