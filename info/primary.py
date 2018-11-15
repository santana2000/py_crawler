
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
print(len(friends))
friends.append('bentat')
print(len(friends))

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




