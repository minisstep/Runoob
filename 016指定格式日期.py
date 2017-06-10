# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 16:21'
"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""
import datetime
print datetime.date.today()
print datetime.date.today().strftime("%y/%m/%d")
print datetime.date.today().strftime("%m/%d/%y")
print datetime.date.today().strftime("%d/%m/%y")