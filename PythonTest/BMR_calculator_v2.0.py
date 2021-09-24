"""
    作者：夏乐
    时间：2021/09/24
    功能:计算BMR(Basal Metabolic Rate 基础代谢率)
    version:2.0
        --2.0新增功能:从键盘输入数据，并由用户选择是否退出
"""


def main():
    flag = input("输入y继续,其他输入则退出: ")
    while flag == 'y' or flag == 'Y':
        sex = input("性别: ")
        height = float(input("身高(cm): "))
        weight = float(input("体重(Kg): "))
        age = int(input("年龄: "))
        if sex == '男':
            print("BMR is {}".format(13.7 * weight + 5 * height - 6.8 * age + 66))
        elif sex == '女':
            print("BMR is {}".format(9.6 * weight + 1.8 * height - 4.7 * age + 66))
        else:
            print("不支持的性别输入！！！")
        flag = input("输入y继续,其他输入则退出")


if __name__ == '__main__':
    main()
