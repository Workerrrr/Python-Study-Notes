"""
这是一个简单的ATM存取款机程序, 它功能单一切并不完善, 某些地方还存在问题, 仅作为学习使用
"""

def login():
    """
    login函数为登录函数, 提示客户输入姓名并进行验证
    :return: 没有返回值
    """
    global money
    money = 500000
    # 定义全局变量money储存系统余额, 初始值为500000

    global name
    name = "王小二"
    # 定义全局变量name储存客户姓名, 初始值为"王小二"

    while True:
        print("--------------------")
        print("\t欢迎使用ATM系统")
        print("--------------------")
        input_name = input("请输入客户姓名:")
        if input_name == name :
            break
        else :
            print("未知用户!")
    main()


def main():
    """
    main函数为程序主菜单函数, 打印主菜单信息, 提供功能选项
    :return: 没有返回值
    """
    global money
    global name
    # 声明全局变量
    while True:
        print("--------------------")
        print(f"\t欢迎您, {name}")
        print("请选择业务")
        print("1,存款\t2,取款")
        print("3,查询余额\t4,退出")
        print("--------------------")
        choice = input("请选择业务:")
        if choice == "1":
            save()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            query()
        else :
            break

    print("程序退出!")


def save():
    """
    save函数用于客户存款, 要求客户输入两次存款金额, 并重新计算余额
    :return: 没有返回值
    """
    global money
    global name
    # 声明全局变量
    while True:
        print("--------------------")
        amount = int(input("请输入存款金额:"))
        check = int(input("请确认存款金额:"))
        # 两次验证存款金额
        if amount <= 0 :
            # 验证存款金额是否有效
            print("无效金额!")
            continue
        elif amount != check :
            # 验证两次输入是否一致
            print("金额验证失败!")
            continue
        else :
            break
    money += amount
    print("存款成功!")
    # 重新计算余额

def withdraw():
    """
    withdraw函数用于客户取款, 要求用户输入一次取款金额, 并输入两次密码进行验证, 然后重新计算金额
    :return: 没有返回值
    """
    global money
    global name
    # 声明全局变量
    while True:
        print("--------------------")
        amount = int(input("请输入取款金额:"))
        if amount <= 0 :
            print("无效金额!")
            continue
        elif amount > money :
            print("余额不足!")
            continue
        else :
            while True:
                password = input("请输入您的密码:")
                check = input("请输入您的密码:")
                if check == password:
                    money -= amount
                    break
                else :
                    print("密码验证错误!")
                    continue
        print("取款完成!")
        break


def query():
    """
    query函数用于客户查询现有系统余额, 系统自动打印余额信息
    :return: 没有返回值
    """
    global money
    global name
    # 声明全局变量
    print("--------------------")
    print(f"{name},您现在的余额是:{money}")
    input("按任意键继续...")

login()
# 调用登录函数, 启动程序