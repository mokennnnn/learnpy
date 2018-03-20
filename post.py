# -*- coding: utf-8 -*
import requests
import json
import time
import hashlib

#327584
#64145



# 评论

def send(s):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')

    url = 'https://mostprise.com'

    try:
        hl = hashlib.md5();
        hl.update(str(s).encode(encoding='utf-8'));
        req=print('建立网站链接 %s' %(s));
        data = {'md5':str(s),'key':hl.hexdigest()};
        req = requests.post(url,cookies=cookies,headers=headers,data=data)
        back=req.text;
    except:
        back = 'error'
    return back



glo='';
for i in range(1000, 3000):

    glo=send(str(glo));
    print(glo);
