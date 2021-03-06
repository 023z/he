# 3.4 循环控制语句
# 3.4.1 while语句

# 判断输入数，是不是回文数，奇数位才可能是回文数，比如3位数、5位数、7位数

n=input("请输入需要判断的5位数：")
a=0
b=len(n)-1
flag=True
while a<b:
    if n[a]!=n[b]:
        print("您输入的数不是回文数")
        flag=False
        break
    a,b=a+1,b-1
    if flag:
        print("您输入的数是回文数")
