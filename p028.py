#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 28
"""

__author__ = 'ilya_il'

# spiral size
sp_size = 1001
# result
res = 1
# start diagonal number
n1 = 1
# delta to count corners
delta = 2

while delta <= (sp_size - 1):
    for i in range(1, 5):
        n1 += delta
        res += n1
    delta += 2

print(res)
