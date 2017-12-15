#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 36
"""

__author__ = 'ilya_il'

res = 0
for i in range(1000000):
    d = str(i)
    b = bin(i)[2:]
    if d == d[::-1] and b == b[::-1]:
        res += i

print(res)
