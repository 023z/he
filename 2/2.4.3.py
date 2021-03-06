ranges = 5.6  # 乘车距离
moneys = 8 + (ranges - 3) * 2  # 起步价￥8，3公里起按2元/公里计算
print("本次车费是：" + str(moneys))
real_moneys = int(moneys)  # 取整
print("本次实付车费是：" + str(real_moneys))  # 打印
