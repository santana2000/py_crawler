import requests
import re

# url = 'https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki'
# url = 'https://www.amazon.cn/dp/B073LJR2JF?_encoding=UTF8&ref_=pc_cxrd_658390051_bestTab_658390051_a_best_2&pf_rd_p=4419e7f6-8c88-423f-8995-dc43fb93c01d&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=658390051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=NJBBF6CNBRD58ATEEA3H&pf_rd_r=NJBBF6CNBRD58ATEEA3H&pf_rd_p=4419e7f6-8c88-423f-8995-dc43fb93c01d'
# code status有问题时，看header返回的信息，添加user agent

# 寻找爬取接口的url规律
# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&
# sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&
# sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&
# ntoffset=3&p4ppushleft=1%2C48&s=44

# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&
# sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&
# ntoffset=0&p4ppushleft=1%2C48&s=88

# "raw_title":"美国代购Chiara Ferragni女包新款CF眨眼睛亮片双肩书包链条背包"
# "view_price":"1020.00"

def get_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('出现异常1')

def parse_html(ulist,html):
    try:
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)        #从解析所得的页面内容(html)中寻找指定内容
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        for i in range(len(tlt)):
            title = eval(tlt[i].split(':')[1])
            price = eval(plt[i].split(':')[1])
            ulist.append([title,price])
    except:
        print('出现异常2')

def print_list(ulist):
    temp = '{:4}\t{:8}\t{:30}'         #打印模板
    print(temp.format('ID', 'Name', 'Price'))
    count = 0
    for i in ulist:
        count += 1
        print(temp.format(count, i[0], i[1]))


def main():
    name = '书包'
    depth = 3
    goodslist = []
    starturl = 'https://s.taobao.com/search?q='+ name
    for i in range(depth):
        try:
            url = starturl + '&s=' + str(i*44)
            html = get_url(url)
            parse_html(goodslist,html)
        except:
            continue
    print_list(goodslist)

main()


