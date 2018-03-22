# -*- coding: utf-8 -*
import requests
from urllib import parse
import time
# 327584
# 64145


# 评论

def send(s):
    headers = {
        "Accept": 'application/json, text/plain, */*',
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'
        ,"Content-Type": "application/x-www-form-urlencoded"
    }
    data = "phone="+str(s)
    url = 'http://112.74.179.199:3030/api/registercode'

    print('建立网站链接 %s' % (s));
    try :
        req = requests.post(url, headers=headers, data=data,timeout=0.2);
        print(req)
        back = req.text
        time.sleep(1)

    except:
        back='error';
    finally:
        return back


glo = '';
for i in range(13813813800, 15018759899):
    glo = send(str(i));
    print(glo);
