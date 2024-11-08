# 我为了在向小美表白时不出现失误, 所以编写了这一款表白器
def main() -> None:
    """
    main函数为程序主函数, 维持程序运行
    :return: 无返回值
    """
    # 定义字典储存小美的基本信息
    mei_info = {
        '名字': "美芷若",
        '年龄': 18,
        '身高': 185,
        '体重': "未知",
        '爸爸': "美我帅",
        '妈妈': "美我美",
        '哥哥': "美我高",
        '爱好': "拳击",
        '最爱的食物': "羊头",
        '最爱的东西': "皮卡车",
        '最爱的人': "未知"
    }

    # 将字典的键转换为一个集合
    quests_set = set(mei_info.keys())

    # 计数变量
    count = 0

    # 使用循环结构连续答题
    while quests_set:
        # 利用集合中pop()方法的特性, 随机弹出一个元素作为题目
        quest : str = quests_set.pop()

        # 打印题目并接收输入
        print(f"小美的{quest}是:")
        answer : str = input("")

        # 纠正变量类型
        if type(mei_info[quest]) == int :
            answer : int = int(answer)

        # 统计答案
        if answer == mei_info[quest]:
            print("正确!")
            count += 1
        else :
            print("错误!")

    if count >= 5:
        print("\n准备充分, 前去表白!")
    else :
        print("\n我对小美还不够了解, 不能表白!")

# 调用主函数启动程序
main()