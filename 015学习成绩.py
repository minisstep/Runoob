# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 16:17'
"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""
def score(n):
    if n >= 90:
        print 'get：A'
    elif 60 <= n <= 89:
        print 'get: B'
    else:
        print 'get: c'
score(59)