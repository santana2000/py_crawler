#蒙特卡洛 ---- 工程方法
#计算思维 ---- 数学思维
from random import random
import time

sum_num = 1000 * 1000
in_area = 0
start = time.perf_counter()

for i in range(sum_num):
    x = random()
    y = random()
    distance = pow(x**2+y**2, 0.5)
    if distance <= 1.0:
        in_area = in_area + 1

x = 4 * (in_area/sum_num)
dur = time.perf_counter() - start
print('计算所得的圆周率是:{:.6f} 所用时间为:{:.2f}'.format(x,dur))