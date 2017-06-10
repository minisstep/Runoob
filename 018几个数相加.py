# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 16:54'
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
"""

def sum(x, y):
    m = 0
    n = 0
    for i in range(y):
        m += x * 10**i
        n += m
    print n
sum(2, 5)