#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 4
"""

__author__ = 'ilya_il'

res = 0
for i in range(500, 999):
    for j in range(i, 999):
        s1 = str(i*j)
        if s1[:3] == s1[:2:-1] and i*j > res:
            res = i*j

print(res)
