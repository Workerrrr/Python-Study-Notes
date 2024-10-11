# 求1-100之间所有数字之和
i = 1 # 循环控制变量
sum = 0 # 累加器的初值必须为0
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum)