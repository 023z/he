# 3.6 实战训练
# 3.6.1 实现数字猜谜游戏

# 使用if实现猜谜、while实现循环效果、if···elif实现多个条件判断

b=8
print("数字猜谜游戏开始！")
a=0

while a!=b:
    a = int(input("请输入你猜的数字："))
    if a<b:
        print("您猜的数字小了")
    else:
        print("您猜的数字大了")

if a==b:
    print("恭喜您猜对了！")
