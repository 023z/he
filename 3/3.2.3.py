# 3.2.3 if嵌套
# 判断输入的成绩是否考上大学

print('欢迎进入高考录取查询系统')
fenshu=int(input('请输入您的高考分数:'))  #获取分数,并转换为整形
if fenshu<410:                       #分数低于410,没有考上大学.
    print('很遗憾,您没有考上大学!')
else:                                #分数到达410,考上大学,下面判断是专科，还是一本、二本
    if 410<=fenshu<430:
        print('恭喜您,您考上了大学,达到专科录取线!')
    elif 430<=fenshu<460:
        print('恭喜您,您考上了大学,达到二本录取线!')
    else:
        print('恭喜您,您考上了大学,达到一本录取线!')