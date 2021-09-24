"""
function:Realize the swap of dollar and RMB
date:09/19/2021
version:5.0
结构化程序,引入lamdb函数
"""


# 主程序
def main():
    USD_RMB = 6.77
    while 1:
        p_cur = input('输入带单位的金额或输入n退出:')
        if p_cur == 'n' or p_cur == 'N':
            print('已退出')
            break
        unit = p_cur[-3:]  # 截取单位
        p_val = eval(p_cur[:-3])  # 截取数值
        if unit == 'CNY':
            ex_rate = 1/USD_RMB;
            t_unit='USD'
        elif unit == 'USD':
            ex_rate = USD_RMB;
            t_unit='CNY'
        else:
            print("输入错误,请从新输入:\n")
            continue
        currency_converter_lambda = lambda x : x * ex_rate#定义lambda函数
        t_cur = str(currency_converter_lambda(p_val))+t_unit
        print(p_cur + "->" + t_cur)

# 调用mian函数
if __name__ == '__main__':
    main()
