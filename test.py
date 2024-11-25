with open(".\practice\essay.txt", "r", encoding = "UTF-8") as f:    # 打开文件
    count : int = 0
    for line in f:
        for word in line.split():
            if word == "to":
                count += 1
print(count)    # 输出为12