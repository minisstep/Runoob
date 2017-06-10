# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 12:00'
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(raw_input("year:"))
month = int(raw_input("month:"))
day = int(raw_input("day:"))

if year % 4 == 0 and year % 400 == 0 and not year % 100 == 0:
    days = sum(months[:month-1]) + day + 1
else:
    days = sum(months[:month - 1]) + day
print days
