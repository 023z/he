# 2.5.6 成员运算符
# "in" 和 "not in"

a = "苹果"
b = "香蕉"
fruit = ["苹果", "荔枝", "橘子", "橙子", "柚子"]
# 方括号 代表"list"列表数据类型，是一种可变序列;
# 小括号 代表"Tuple"元祖数据类型，不可变序列;

# 使用in成员运算符
if (a in fruit):
    print("变量a在给定的列表fruit中")
else:
    print("变量a不在给定的列表fruit中")

#使用not in成员运算符
if (b not in fruit):
    print("变量b不在给定的列表fruit中")
else:
    print("变量b在给定的列表fruit中")

#修改变量a的值，再使用in成员运算符：
a="白菜"
if (a in fruit):
    print("变量a在给定的列表fruit中")
else:
    print("变量a不在给定的列表fruit中")
