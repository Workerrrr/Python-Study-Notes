age = input("请输入年龄:")
height = input("请输入身高:")

age = int(age)
height = int(height)

if age <= 12:
    if height <= 140:
        print("儿童票")
    else :
        print("成人票")