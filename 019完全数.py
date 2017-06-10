# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 17:17'
"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：请参照程序Python 014分解质因数。
"""
list1 = []
for i in range(1, 1001):
    list2 = []
    for j in range(1, int(i / 2) + 1):
        if i % j == 0:
            list2.append(i)
    if i == sum(list2):
        print i
