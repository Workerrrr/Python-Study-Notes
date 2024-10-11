# 猜数字小游戏
import random # 调用random模块
num = random.randint(1, 100) # 生成一个1-100内的整数

print("系统将随机生成一个100以内的自然数, 请猜出它") # 打印提示信息
while True: # 程序主循环
    n = int(input("请输入你要猜的数字:")) # 获取键盘输入
    if n == num: # 进行判断
        print("太棒了, 你猜对了!")
        break
    elif n > num:
        print("数字太大了!")
        continue
    elif n < num:
        print("数字太小了!")
        continue
