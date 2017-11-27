#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 1
"""

__author__ = 'ilya_il'

res = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        res += i

print(res)
