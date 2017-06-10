# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 16:28'
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
"""
str = raw_input("please input a string:")

alpha = 0
space = 0
digit = 0
others = 0

for i in str:
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print "alpha is %d, space is %d, digit is %d other is %d" %(alpha, space, digit, others)