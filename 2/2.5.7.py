# 2.5.7 身份运算符
# "is"和"is not"
# 相对于2.5.2章节的==运算符，"is"和"is not"会比较两个变量的地址，"=="只判断变量的值是否一样

a = "苹果"
b = "苹果"

#使用is身份运算符
if (a is b):
    print("a和b具有相同的标识")
else:
    print("a和b不具有相同的标识")

#使用not is身份运算符
if (a is not b):
    print("a和b不具有相同的标识")
else:
    print("a和b具有相同的标识")

#修改变量a的值后再判断,那么结果就不一样了
a="香蕉"
if (a is b):
    print("a和b具有相同的标识")
else:
    print("a和b不具有相同的标识")