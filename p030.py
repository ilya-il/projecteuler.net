#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 30
"""

__author__ = 'ilya_il'

res = 0
for n in range(10, 10000000):
    if n == sum([int(x)**5 for x in str(n)]):
        res += n
        print(n)

print(res)
