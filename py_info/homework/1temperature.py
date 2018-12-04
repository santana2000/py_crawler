
temp = input('请输入要转换的温度值:')

if temp[-1] in ['f','F']:
    C = (eval(temp[0:-1]) - 32) / 1.8
    print('转换后的温度是: {:.2f} 摄氏度'.format(C))
elif temp[-1] in ['c','C']:
    F = eval(temp[0:-1])*1.8 + 32
    print('转换后的温度是: {:.2f} 华氏度'.format(F))
else:
    print('输入的格式有误')