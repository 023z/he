# 3.4 循环控制语句
# 3.4.1 while语句

# 求1-100的和， (避免无限循环)

a=100
sum=0
b=1
while b<=a:
    sum=sum+b
    b+=1
    print("1到%d之和为：%d" % (a,sum))