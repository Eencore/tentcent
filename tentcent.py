import requests
import json
import time

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get(url)
print(res.content)
res = json.loads(res.text)
data_all = json.loads(res['data'])
history = {}  # 历史数据
for i in data_all['chinaDayList']:
    ds = "2020." + i['date']
    tup = time.strptime(ds, "%Y.%m.%d")
    ds = time.strftime("%y-%m-%d", tup)  # 改变时间格式，不然插入数据库会报错，数据库是datetime类型
    confirm = i['confirm']
    suspect = i['suspect']
    heal = i['heal']
    dead = i['dead']
    history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
#滴滴滴