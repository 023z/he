# 3.2.2    if ... else 语句
# 例1: 判断两个数的差值

# PHP里面的else if， 在Python中被简写为： elif。
# elif 和 else 都必须搭配 if 使用。


a= int(input('请输入第一个数:'))
b= int(input('请输入第二个数:'))
if a<=b:
    print('它们的差值是:',b-a)
elif a>b:
    print('它们的差值是:',a-b)

