import jieba
import wordcloud

with open('threekingdoms.txt','r',encoding='utf-8') as ftxt:
    content = ftxt.read()

    ls = jieba.lcut(content)

    str_word = ' '.join(ls)      #join前无括号

# 1.配置词云
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"
    )
# 2.生成词云
w.generate(str_word)
# 3.输出词云
w.to_file("grwordcloud.png")




# 4.掩膜
# from scipy.misc import imread
# mask = imread("chinamap.jpg")