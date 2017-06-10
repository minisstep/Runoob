# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 13:29'
"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""
k = {0: 0, 1: 1}
def fib(n):
    if n in k:
        return k[n]
    k[n] = fib(n - 1) + fib(n -2)
    return k[n]


if __name__ == '__main__':
    n = 40
    print 'fib(%d)=%d' % (n, fib(n) )



