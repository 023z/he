# 2.8.2 第二章实战2    根据身高和体重计算BMI

tz1=float(input('请输入您的体重（斤）:'))
sg1=float(input('请输入您的身高（厘米）:'))
tz=tz1/2    #体重换算成公斤
sg=sg1/100  #身高换算成米

bmi=(tz/(sg*sg))   #计算BMI值
print('您的BMI指数是：',bmi)
if bmi<18.5:
    print('您的体重太轻了！')
elif 18.5<=bmi<24.9:
    print('您的身材很完美！')
elif 24.9 <= bmi < 29.9:
    print('您的身材很完美！')
elif bmi>=29.9:
    print('Oh My God! 你太胖啦!!! 赶紧减肥吧！')