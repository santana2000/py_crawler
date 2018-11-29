import time


print('开始打印'.center(40,'='))
print('\n')

scale = 50

for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    print('\r{2}%[{0}>{1}]'.format(a,b,c), end='')
    time.sleep(0.1)

print('\n')
print('打印结束'.center(40,'='))
