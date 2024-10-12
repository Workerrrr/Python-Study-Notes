# 投掷5次骰子, 选择是否向小美表白
import random
for i in range(1, 6):
    point = random.randint(1, 6)
    print(f"投掷第{i}次骰子, 点数是{point}")
    if point == 1:
        print("不表白, 先买一束花")
    elif point == 2:
        print("不表白, 先买一个玩偶")
    elif point == 3:
        print("不表白, 先买一件衣服")
    elif point == 4:
        print("不表白, 先发一个朋友圈")
    elif point == 5:
        print("不表白, 先给小美汇款")
    elif point == 6:
        print("不表白, 承认自己不够优秀")
else :
    print("我还是没敢向小美表白")