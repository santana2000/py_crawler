import urllib
import re
import requests
from bs4 import BeautifulSoup



res = requests.get('https://book.douban.com/top250')

soup = BeautifulSoup(res.text,'html.parser')

print(soup.select('img'))

f = open(file_name, 'wb')
f.write(res.content)
f.close()