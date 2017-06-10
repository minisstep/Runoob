# -*- encoding: utf-8 -*-
__author__ = 'xgj1010'
__date__ = '2017/6/1 13:15'
"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

a = int(raw_input("number:"))
b = int(raw_input("number:"))
c = int(raw_input("number:"))
# 一
# if a <  b < c:
#     print a, b, c
# elif a < c < b:
#     print a, c, b
# elif b < a < c:
#     print b, a, c
# elif b < c < a:
#     print b, c, a
# elif c < a < b:
#     print c, a, b
# else:
#     print c, b, a

# 二
if a > b:
    a, b = b, a
elif a > c:
    a, c = c, a
elif b > c:
    b, c = c, b
print a, b, c
