# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 14:26'
"""
题目：暂停一秒输出，并格式化当前时间。
"""
import time

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
time.sleep(1)
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())