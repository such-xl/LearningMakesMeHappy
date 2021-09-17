"""
function:Realize the swap of dollar and RMB
date:09/17/2021
version:4.0
将汇率换算封装函数
"""
#定义换算函数
def currency_converter(p_val,rate):
    return p_val*rate;

#主程序
USD_RMB = 6.77;
while 1:
    p_cur = input('输入带单位的金额或输入n退出:')
    if p_cur=='n'or p_cur=='N':
        print('已退出')
        break;
    unit = p_cur[-3:]#截取单位
    p_val =eval(p_cur[:-3])#截取数值
    if unit == 'CNY':
        #t_val = p_val/USD_RMB
        t_val=currency_converter(p_val,1/USD_RMB)
        t_cur = str(t_val)+"USD"
    elif unit == 'USD':
        #t_val = p_val*USD_RMB
        t_val=currency_converter(p_val,USD_RMB)
        t_cur = str(t_val)+"CNY"
    else:
        print("输入错误,请从新输入:\n")
        continue;
    print(p_cur + "->"+ t_cur)
