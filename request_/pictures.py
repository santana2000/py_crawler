
# 通过requests+soup实现爬取图片

import time
import requests
from urllib import  request
from bs4 import BeautifulSoup

# https://book.douban.com/top250?start=0
# https://book.douban.com/top250?start=25

x = 1
for i in range(2):  #0~9
    url = 'https://book.douban.com/top250?start={}'.format(i * 25)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')

    # imgs = soup.select('img')
    imgs = soup.find_all('img',{'width':'90'})

    for img in imgs:
        print(img['src'])
        request.urlretrieve(img['src'], 'C:/Users/tesla/Desktop/top250\%s.jpg'%x)
        x += 1

# for k,v in xxx

    time.sleep(1)

