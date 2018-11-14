
import requests
from lxml import etree

#我们邀抓取的页面链接
url='https://book.douban.com/subject/1084336/comments/'

#用requests库的get方法下载网页
r=requests.get(url).text

#解析网页并且定位短评
s=etree.HTML(r)
file=s.xpath('//*[@id="comments"]/ul[1]/li/div[2]/p/span/text()')


#打印抓取的信息
print(file)

# with open('pinglun.txt','w',encoding='utf-8') as f:
#     for i in file:
#         print(i)
#         f.write(i)

import pandas as pd
df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')


# //*[@id="comments"]/ul[1]/li[1]/div[2]/p/span
# //*[@id="comments"]/ul[1]/li[9]/div[1]/a/img