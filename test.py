# 数据容器的排序操作
list_1 = [1, 2, 3]
tuple_1 = ('a', 'b', 'c')
str_1 = "Worker"
dict_1 = {'A': 1, 'B': 2, 'C': 3}

print(sorted(list_1))   # 结果为[1, 2, 3]
print(sorted(tuple_1))  # 结果为['a', 'b', 'c']
print(sorted(str_1, reverse = True))    # 结果为['r', 'r', 'o', 'k', 'e', 'W']
print(sorted(dict_1, reverse = True))   # 结果为['C', 'B', 'A']