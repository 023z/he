# 3.2.4 多重条件判断

a=int(input('请输入三角形的第一条边:'))
b=int(input('请输入三角形的第二条边:'))
c=int(input('请输入三角形的第三条边:'))

if a==b and b==c:
    print('等边三角形')
elif a==b or a==c or b==c:
    print('等腰三角形')
elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print('直角三角形')
else:
    print('一般三角形')