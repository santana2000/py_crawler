import requests

url = 'http://www.ip138.com/ips138.asp?'
kv = {'ip':'58.218.185.64'}
r = requests.get(url,params=kv)
r.encoding = 'GBK'
print(r.status_code)
print(r.encoding)

print(r.text[7150:7500])