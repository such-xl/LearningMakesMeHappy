"""
    作者：夏乐
    时间：2021/09/24
    功能:计算BMR(Basal Metabolic Rate 基础代谢率)
    version:4.0
        --2.0新增功能:从键盘输入数据，并由用户选择是否退出
        --3.0新增功能:用户可以在一行输入所有信息, 输出时的结果有对应单位
        --4.0新增功能:引入异常处理机制
"""


def main():
    flag = input("输入y继续,其他输入则退出: ")
    while flag == 'y' or flag == 'Y':
        print("请输入依次输出性别(男/女)、年龄、身高(cm)、体重(kg),并键入空格以分隔:")
        str_list = input().split(" ")
        try:
            sex = str_list[0]
            age = int(str_list[1])
            height = float(str_list[2])
            weight = float(str_list[3])
            if sex == '男':
                print("BMR is {}大卡".format((13.7 * weight + 5 * height - 6.8 * age + 66)))
            elif sex == '女':
                print("BMR is {}大卡".format(9.6 * weight + 1.8 * height - 4.7 * age + 66))
            else:
                print("不支持的性别输入！！！")
        except ValueError:  # 值输入错误
            print("输入数据不合法!!!")
        except IndexError:
            print("输入格式错误或信息不足！！！！")
        except:
            print("未知异常！！！")
        finally:
            flag = input("输入y继续,其他输入则退出")
    print("已退出")


if __name__ == '__main__':
    main()
