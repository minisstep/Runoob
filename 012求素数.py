# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 14:55'
"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
import math
leap = 1
count = 0
for i in range(101, 201):
    j = int(math.sqrt(i))
    for k in range(2, j+1):
        if i % k == 0:
            leap = 0
            break
    if leap == 1:
        count += 1
        print i, count
    leap = 1