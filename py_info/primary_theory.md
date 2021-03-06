## 原理
发送页面---请求页面---解析页面---下载内容---存储内容  
通过程序模拟浏览器请求站点的行为

## 知识储备
list  
dict  
slice  
os  
io---stream是单向的，从磁盘到内存或者反之  
requests  
lxml

## 流程
a. 通过URL或者文件获取网页  
b. 分析要爬取的目标内容所在的位置  
c. 用元素选择器快速提取(Raw) 目标内容  
d. 处理提取出来的目标内容 （ 通常整理合成一个 Json）  
e. 存储处理好的目标内容 （比如放到 MongoDB 之类的数据库，或者写进文件里）  



* Requests+Xpath 实现通用爬虫套路  

> 不同库实现打开url,读取url内容的方式有所不同  
> 图片用库里的函数下载或者原生的xx.write(xx.content)

> __name__ 作为模块的内置属性，即".py"文件的调用方式。如果等于“__main__"就直接执行本文件， 如果是别的就是作为模块被调用
> 爬取接口的获取 & 翻页的实现
## 细节
缺失值处理：对缺失数据行进行删除或填充  
重复值处理：重复值的判断与删除  
空格和异常值处理：清楚不必要的空格和极端、异常数据  
分组：数据划分、分别执行函数、数据重组  

scrapy是一个功能非常强大的爬虫框架，它不仅能便捷地构建request，
还有强大的 selector 能够方便地解析 response，
然而它最让人惊喜的还是它超高的性能，让你可以将爬虫工程化、模块化。

MongoDB可以方便你去存储一些非结构化的数据，
比如各种评论的文本，图片的链接等等。
你也可以利用PyMongo，更方便地在Python中操作MongoDB。

numpy 数据分析

