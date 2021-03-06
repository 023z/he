# 3.2.2    if ... else 语句
# 例2: 根据输入的销售额计算奖金

sales=int(input('请输入本季度销售额:'))
if sales<10000:
    print('您本季度销售额:',sales,'元,销售额低于10000,本季度没有奖金')
elif 10000<=sales<100000:
    print('您本季度销售额:',sales,'元,奖金为:2000元')
elif 100000<=sales<1000000:
    print('您本季度销售额:',sales,'元,奖金为:5000元')
else:
    print('您本季度销售额:',sales,'元,奖金为:10000元')
