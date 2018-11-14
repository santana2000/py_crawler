# 原理
发送页面---请求页面---解析页面---下载内容---存储内容

list
dict
slice
os
io
requests
lxml


a. 通过URL或者文件获取网页
b. 分析要爬取的目标内容所在的位置
c. 用元素选择器快速提取(Raw) 目标内容
d. 处理提取出来的目标内容 （ 通常整理合成一个 Json）
e. 存储处理好的目标内容 （比如放到 MongoDB 之类的数据库，或者写进文件里）



Requests+Xpath 实现通用爬虫套路

scrapy

numpy 数据分析

//*[@id="topic-items"]/div/div[1]/div[2]/div/a
