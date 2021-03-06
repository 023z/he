# 2.7.1 疑难唯独
# print()语句自动换行的问题

x=1010
y=2020
z=3030

print(x)
print(y)
print(z)
print(x,y,z)   # 逗号分隔可实现不换行输出
print(x,end=" ")    #将行尾默认结束符修改为空格，也可实现不换行输出
print(y,end=" ")
print(z,end=" ")