#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 14
"""

__author__ = 'ilya_il'


def collatz_len(start_num):
    # length
    cl = 0
    n = start_num
    while n != 1:
        if n % 2 == 0:
            # even
            n = n/2
        else:
            n = 3*n + 1
        cl += 1

    # count start number
    cl += 1
    return cl


res_len = 0
res_num = 0
for i in range(1, 1000000):
    collen = collatz_len(i)
    if res_len < collen:
        res_len = collen
        res_num = i

print(res_len)
print(res_num)
