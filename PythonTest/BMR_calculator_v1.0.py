"""
    作者：夏乐
    时间：2021/09/24
    功能:计算BMR(Basal Metabolic Rate 基础代谢率)
    version:1.0
"""


def main():
    sex = '男'
    age = 25  # year
    height = 175.5  # cm
    weigth = 55.0  # Kg
    print("BMR is {}".format(13.7 * weigth + 5 * height - 6.8 * age + 66))


if __name__ == '__main__':
    main()
