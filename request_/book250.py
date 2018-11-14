#-*- coding:utf-8 -*-
# 图书top250

import requests
from lxml import etree
import time   #这里导入时间模块，以免豆瓣封你IP

with open('C:/Users/tesla/Desktop/book.txt','w',encoding='utf-8') as file:

    url = 'https://book.douban.com/top250'
    data = requests.get(url).text
    books = etree.HTML(data)

    name = books.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')  # @title
    score = books.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

    for i in range(20):
        #print('{} 的评分是: {}'.format(name[i],score[i]))
        file.write('{} 的评分是: {}\n'.format(name[i],score[i]))

    time.sleep(1) #加个睡眠，防止IP被封


# //*[@id="content"]/div/div[1]/div/table[9]//tr/td[2]

# //*[@id="content"]/div/div[1]/div/table[1]//tr/td[1]/a/img 图片

# //*[@id="content"]/div/div[1]/div/table[22]/tr/td[2]/div[1]/a/@title
# //*[@id="content"]/div/div[1]/div/table[15]/tr/td[2]/div[1]/a

