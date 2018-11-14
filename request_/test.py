#-*- coding:utf-8 -*-
import requests
from lxml import etree
import time   #这里导入时间模块，以免豆瓣封你IP

url = 'https://movie.douban.com/subject/26942674/'
data = requests.get(url).text
movies = etree.HTML(data)

name = movies.xpath('//*[@id="content"]/h1/span[1]/text()')
score = movies.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
actor = movies.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')

actors = []
for i in actor:
    actors.append(i)

print('电影名称：',name)
print('评分：',score)
print('主演：',actors)

# //*[@id="interest_sectl"]/div[1]/div[2]/strong
# //*[@id="interest_sectl"]/div[1]/div[2]/strong

