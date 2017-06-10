# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 14:23'
"""
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数
"""
import time
for i in range(1,10):
    time.sleep(1)
    print
    for j in range(1, i + 1):
        print '%d*%d=%d' % (i, j, i * j),