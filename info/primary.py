
name = 'k'
print('hi!',name)

if name != 'k':
    print(False)
else:
    print(2>1)

print('''字符
布尔
数字''')

PI = 3.1415926


friends = ['alice','smith','kevin']   #list
print(len(friends))         #索引最大值：len(friends)-1
friends.append('bentat')    #insert()、pop()
print(len(friends))
list[range(5)]
list[range(1,5)]

hero = ('captain','thor','zeus')     #tuple:没有方法,不可修改(tuple的每个元素，指向永远不变)
hero_num = (1,)             #加逗号

heros = {'captain':90,
         'thor':95,
         'ironman':55
         }                   #dict的key必须是不可变对象。
print(heros['thor'])


#两种字符串格式化的方法
print("hello,%s,I'm %s" % ('accurate','type'))
print("hello,{},I'm {}".format('niko','simple'))

def check_ticket(price):
    if(price>200):
        print('长途')
    else:
        print('短途')

price1 = int(input())

check_ticket(price1)







