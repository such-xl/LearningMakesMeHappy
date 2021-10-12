"""
    作者:夏乐
    日期:2021/10/12
    版本:2.0
    功能:从键盘输入一个日期，判断是这一年的第几天
    2.0新增:用列表实现,并将判断是否是闰年封装成函数
"""
import datetime  # 导入datetime库


def isleapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def main():
    # 从键盘输入一个日期
    date_str = input("从键盘输入一个日期(yyyy/mm/dd): ")

    # 将date_str 字符串转换为日期型数据
    # strptimt（）字符串类型转换为日期型
    date_after = datetime.datetime.strptime(date_str, '%Y/%m/%d')

    # 分别得到日期的年,月,日
    year = date_after.year
    month = date_after.month
    day = date_after.day

    # 计算日期之前月份的所有天数
    # 定义一个列表
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 判断是否为闰年
    if isleapyear(year):
        month_day_list[1] = 29
    days = sum(month_day_list[:month - 1]) + day
    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()