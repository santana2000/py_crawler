import requests

url = 'https://item.jd.com/100000287113.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    print(r.encoding)
    print(r.text)
except:
    print('爬取失败，哭哭惹')