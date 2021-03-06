# 2.5.8 运算符的优先级

# "."点符号用来存取对象的属性和方法，举例：调用 t 对象的 append 方法，在结尾加一个字符"z"
t = ['P', 'a', 'r', 'r', 'o']  # 给对象 t 赋值一个可变序列
t.append("z")

print('设:')
print("t=['P','a','r','r','o']")  # 单引号和双引号可相互嵌套，可不使用转义字符\
print("t.append('z')")
print('那么 t=', t)
print('\n')

a, b, c, d, e = 5, 8, 4, 2, 0
print('设：a=5, b=8, c=4, d=2, e=0')

e=(a+b)*c/d     # (5+8)*4/2
print('(a+b)*c/d 的运算结果为:',e)

e=((a+b)*c)/d     # (5+8)*4/2
print('((a+b)*c)/d 的运算结果为:',e)

e=(a+b)*(c/d)     # (5+8)*4/2
print('(a+b)*(c/d) 的运算结果为:',e)

e=a+(b*c)/d     # (5+8)*4/2
print('a+(b*c)/d 的运算结果为:',e)
