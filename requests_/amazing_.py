import requests

# url = 'https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki'
url = 'https://www.amazon.cn/dp/B073LJR2JF?_encoding=UTF8&ref_=pc_cxrd_658390051_bestTab_658390051_a_best_2&pf_rd_p=4419e7f6-8c88-423f-8995-dc43fb93c01d&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=658390051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=NJBBF6CNBRD58ATEEA3H&pf_rd_r=NJBBF6CNBRD58ATEEA3H&pf_rd_p=4419e7f6-8c88-423f-8995-dc43fb93c01d'

r = requests.get(url)
print(r.status_code)
print(r.headers)


# code status有问题时，看header返回的信息，添加user agent