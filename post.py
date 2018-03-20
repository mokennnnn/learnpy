# -*- coding: utf-8 -*
import requests
import json
import time

#327584
#64145



# 评论
def send(s):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')

    url = 'http://112.74.179.199:3030/api/registercode'

    try:
        req=print('建立网站链接 %s' %(s));
        data = {'phone': str(s)};
        req = requests.post(url,cookies=cookies,headers=headers,data=data)
        back=req.text;
        time.sleep(1);
    except:
        back = 'error'
    return back




for i in range(7440, 7450):
    print(i)

    ww=send(str(18819460000+i));
    print(ww);
