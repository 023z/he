# 3.4 循环控制语句
# 3.4.1 while语句

# while else配合使用:
# 输入一个数字，查找输出所有小于输入数字的所有整数

n=int(input("请输入一个整数："))
x=1
while x<n:
    print(x,"小于n")
    x=x+1
else:            # while语句的条件表达式为False时，执行else语句块。
    print("小于n的整数查找完毕！")
