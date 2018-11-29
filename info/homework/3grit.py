# 三天打鱼两日晒网

def day_work(factor):
    dayup = 1
    for i in range(365):
        if (i % 5) in [0, 4]:
            dayup = dayup
        else:
            dayup = dayup + factor
    return dayup

def how_many(factor):
    while day_work(factor) < 37.78:
        factor = factor + 0.001
    print('{:.2f}'.format(factor))

how_many(0.01)