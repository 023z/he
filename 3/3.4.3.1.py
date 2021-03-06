# 3.4 循环控制语句
# 3.4.3 continue 语句和 else 语句

# 输出10开始递减的整数，间隔2，最小数0

a= 10
while a>0:
    a=a-2
    if a==6:            #变量为6时跳过输出
        continue
    print(a,"大于或等于0")
