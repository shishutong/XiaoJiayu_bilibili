# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json

content = input("请输入要翻译的内容：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
'i': content,
'type': 'AUTO',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'ue' : 'UTF-8',
'typoResult' : 'true'}
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果：%s"%(target['translateResult'][0][0]['tgt']))
