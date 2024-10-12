# 统计一段英文里有几个字母a
count = 0 # 计数器初值为0
text = input("请输入一段英文:")

for value in text:
    if value == 'a':
        count += 1
else :
    print("遍历完成!")
print(f"总共有{count}个字母a!")