# 使用global关键字声明全局变量
def fun():
    global x
    # 在函数内部声明一个全局变量
    x = 10
    return

fun()
x = 20
# 在任意作用域都可以访问全局变量
print(x)