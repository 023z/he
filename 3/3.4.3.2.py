# 3.4 循环控制语句
# 3.4.3 continue 语句和 else语句

# for、break 和 else 语句的配合使用

a="万树鸣蝉隔岸虹，乐游原上有西风。"
for b in a:               # 遍历a中的文字
    if b=='乐':            # 如果找到文字“乐”的时候
        print("当前文字是：",b)
        break              # 不再输出下面的文字
    else:                  # 否则就一直不停地重复遍历，重复输出！
        print('没有发现对应的文字！')

# for 执行完毕或 while 为 False 时，才会执行 else
# 如果循环被 break 终止，那么 else 不会执行！