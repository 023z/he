# 3.4 循环控制语句
# 3.4.2 for语句

# 数字123组成不同且不重复的3位数

tm=0
for i in range(1,4):            #range函数遍历数字1、2、3
    for j in range(1,4):        #使用for循环输出所有的组合数字
        for k in range(1,4):
          if ((i!=j) and (j!=k) and (k!=i)):      #把重复的数字去掉
                print(i,j,k)
                tm+=1
print('1,2,3可组成',tm,'个不重复的数字')