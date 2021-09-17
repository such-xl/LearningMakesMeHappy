"""
function:Realize the swap of dollar and RMB
date:09/14/2021
version:3.0
"""
USD_RMB = 6.77;
# I:Enter currency amount
while 1:
    p_cur = input('输入带单位的金额或输入n退出:')
    if p_cur=='n'or p_cur=='N':
        print('已退出')
        break;
    unit = p_cur[-3:]#截取单位
    p_val = p_cur[:-3]#截取数值
    p_val = eval(p_val)#数字字符转换为数值
    if unit == 'CNY':
        t_val = p_val/USD_RMB
        t_cur = str(t_val)+"USD"
    elif unit == 'USD':
        t_val = p_val*USD_RMB
        t_cur = str(t_val)+"CNY"
    else:
        print("err")
        exit(1)
    print(p_cur + "->"+ t_cur)
