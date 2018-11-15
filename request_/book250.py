#-*- coding:utf-8 -*-

# 爬取豆瓣图书top250---文字

import requests
from lxml import etree
import time   #这里导入时间模块，以免豆瓣封你IP
import io

with open('C:/Users/tesla/Desktop/book','wb',encoding='utf-8') as file:

    url = 'https://book.douban.com/top250'
    data = requests.get(url).text
    topbooks = etree.HTML(data)
    books = topbooks.xpath('//*[@id="content"]/div/div[1]/div/table')

    for book in books:
        name = book.xpath('./tr/td[2]/div[1]/a/@title')  # @title
        score = book.xpath('./tr/td[2]/div[2]/span[2]/text()')
        print('{} 的评分是: {}'.format(name,score))
        # file.write('{} 的评分是: {}\n'.format(name,score))   #写入文件

    time.sleep(1) #加个睡眠，防止IP被封

# //*[@id="content"]/div/div[1]/div/table[1]/tr/td[1]/a/img
# //*[@id="content"]/div/div[1]/div/table[9]/tr/td[2]

# //*[@id="content"]/div/div[1]/div/table[1]//tr/td[1]/a/img 图片

# //*[@id="content"]/div/div[1]/div/table[22]/tr/td[2]/div[1]/a/@title
# //*[@id="content"]/div/div[1]/div/table[15]/tr/td[2]/div[1]/a

