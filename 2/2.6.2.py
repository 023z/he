# 2.6 Python得输入和输出
# 2.6.2  print 函数：输出
# print(值,...sep=' ',end='\n')   sep分隔符，默认为空格,end为每个print后自动添加的,默认为换行符，

print("离离原上草","谁知盘中餐")
print("离离原上草","谁知盘中餐",sep="*")  #将默认分隔符修改为 " * "
print("离离原上草","谁知盘中餐",end="&")  #将默认结束符修改为 " & "
print("离离原上草","谁知盘中餐")          #再次输出原文，因上一句默认的换行符变成了&，所以挤在一行了
print("\r")   #直接\n的话，因为是在新的一行输入的"\n"，再换行，会变成两个空行。所以这里用"\r"
print('测试换行结束')