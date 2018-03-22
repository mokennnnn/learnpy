from urllib3 import *
import re
import json
disable_warnings()
http = PoolManager()


def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    headers = re.split('\n',headersText)
    # 将每一行http请求拆分成key和value
    for header in headers:
        result = re.split(':',header,maxsplit = 1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict
headers = str2Headers('header.txt')



def getList(itemID, currentPage):
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId=37457670144&spuId=212312312&sellerId=47035594&order=1&currentPage=%s" % (
        currentPage)
    res = http.request('GET', url, headers=headers);
    c ='{' +res.data.decode('GB18030')+'}'
    tmalljson = json.loads(c)
    return (tmalljson)


def post():
    headers = {
        "Accept": 'application/json, text/plain, */*',
        "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.5 NetType/WIFI Language/zh_CN'
        , "Content-Type": "application/json; charset=utf-8"
    }
    data = {"data": {"teamname": "hello,My Name Is Alien.", "slogan": "I will Send more than 200W ddos to you.",
                     "leadername": "go luck.", "leaderwechat": "still not user random.", "leaderemail": "concat me at ",
                     "leadernum": "123", "leadercode": "123", "leadermsg": "123",
                     "mem1": {"mem1name": "空", "mem1wechat": "空", "mem1code": "空", "mem1msg": "空"},
                     "mem2": {"mem2name": "空", "mem2wechat": "空", "mem2code": "空", "mem2msg": "空"},
                     "mem3": {"mem3name": "空", "mem3wechat": "空", "mem3code": "空", "mem3msg": "空"},
                     "mem4": {"mem4name": "空", "mem4wechat": "空", "mem4code": "空", "mem4msg": "空"},
                     "mem5": {"mem5name": "空", "mem5wechat": "空", "mem5code": "空", "mem5msg": "空"}}}

    url = 'http://112.74.179.199:3030/gongneng/submit'
    res = http.request('POST', url, headers=headers,body=data);
    return res


back=post();
print(back)


