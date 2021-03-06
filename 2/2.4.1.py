name = "张小明"  # 学生的姓名
print("学生姓名：" + name)

maths = 92.5  # 学生的数学成绩
print("数学成绩：" + str(maths))  # 成绩浮点数，需要转换成字符串数据类型
chinese = 65.5
print("语文成绩：" + str(chinese))
english = 80.5
print("英语成绩：" + str(english))

sum = maths + chinese + english
print("总成绩：" + str(sum))

avage = sum / 3
print("平均成绩：" + str(avage))

# 使用if语句判断学生成绩是否优秀
if avage < 60:
    print("该学生成绩较差！")
if 60 <= avage < 75:
    print("该学生成绩还行！")
if 75 <= avage < 90:
    print("该学生成绩良好！")
if avage > 90:
    print("该学生成绩优秀！")
