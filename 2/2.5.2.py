# 2.5.2 比较运算符
# 不等于运算符 != 等同于<>  Python里一般使用 !=
# 比较运算符可连在一起：
# a<b<c<d 等同于： a<b and b<c and c<d
# x<y>z 等同于： x<y and y>z 同样有效

bumen1 = 76000  # 定义变量，存储部门1的销售额
bumen2 = 54000  # 定义变量，存储部门2的销售额
print("部门1的销售业绩是："+str(bumen1))
print("部门2的销售业绩是："+str(bumen2))
print("部门1==部门2的结果是："+str(bumen1==bumen2))     #判断等于
print("部门1!=部门2的结果是："+str(bumen1!=bumen2))     #判断不等于
print("部门1>部门2的结果是："+str(bumen1>bumen2))        #判断大于
print("部门1<部门2的结果是："+str(bumen1<bumen2))        #判断小于
print("部门1<=部门2的结果是："+str(bumen1<=bumen2))      #判断小于或等于
print("部门1>=部门2的结果是："+str(bumen1>=bumen2))      #判断大于或等于