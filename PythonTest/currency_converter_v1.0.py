"""
function:Convert RMB to USD
date:09/07/2021
version:1.0
"""
# I:Enter RMB amount
rmb = input('please enter the RMB amount from the keyboard:')
# P:Convert RMB to USD
usd = eval(rmb) / 6.77
# O:Output dollar amount
print('The dollar amount after the exchanges is:', usd)
