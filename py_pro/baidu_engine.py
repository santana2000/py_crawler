import requests

kv = {'wd':'Python'}
url = 'https://www.baidu.com/s'
r = requests.get(url,params=kv)
print(r.request.url)
print(len(r.text))
