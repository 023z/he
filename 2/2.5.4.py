#逻辑运算符 and or not

print("学生信息管理系统，开始登录")
#使用input函数接收输入内容
num=input("请输入学号：")
number=int(num) #将输入的编号转换为整数类型
password=input("请输入密码：")

if (number==1000 and password=="大学生") or (number==1001 and password=="小学生"):
    print("恭喜你，密码正确，登陆成功")
else:
    print("对不起，密码错误，请重试")