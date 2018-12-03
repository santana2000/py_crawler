
# 计算一组数的统计值 方差、中位数
def get_num():
    num_str = input('输入数值，回车结束：')
    num = []
    while num_str!='':
        num.append(eval(num_str))
        num_str = input('输入数值，回车结束：')      #注意while循环里的这个位置

    return num


def mean(num):
    sum = 0
    for item in num:
        sum = sum + item
    num_mean = sum/len(num)
    return num_mean

def dev(num,num_mean):
    sum_dev = 0
    for i in num:
        sum_dev = sum_dev + (i-num_mean)**2

    return pow(sum_dev/len(num), 0.5)

def middle(num):
    num_sort = sorted(num)
    size = len(num_sort)
    if len(num_sort) % 2 == 0:
        return (num_sort[size//2-1]+num_sort[size//2]) / 2
    else:
        return num_sort[size//2]

def main():
    num1 = get_num()
    mean1 = mean(num1)
    dev1 = dev(num1,mean1)
    middle1 = middle(num1)
    print('平均数是：{0}\n方差是：{1:.2f}\n中位数是：{2}'.format(mean1,dev1,middle1))

main()
