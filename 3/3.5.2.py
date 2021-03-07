# 3.5 新手疑难问题解答
# 3.5.2 range()函数的使用方法

# range()函数春建一个证书列表，一般用在 for 循环中，格式如下：
# range(start,stop[,step])             start 和 step 为可选参数，默认为 0，1
#       start: 开始数，默认从0开始。       例：range(5)等价于range(0,5)
#       stop: 计数到stop结束，不包含stop。 例：range(0,5)是[0,1,2,3,4]没有5
#       step: 步长(增量)，默认为1，可为负数。             例：range(0,5)等价于range(0,5,1)

print("设'for a in range(5)'，a 的结果：")
for a in range(5):
    print(a)

print("设'for n in range(5,9)'，n 的结果：")
for n in range(5,9):
    print(n)

print("设'for m in range(0,10,2)'，m 的结果：")
for m in range(0,10,2):
    print(m)

print("设'for t in range(0,10,2)'，t 的结果：")
for t in range(0, -10, -2):
    print(t)
