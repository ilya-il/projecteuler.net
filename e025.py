#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 25
"""

__author__ = 'ilya_il'

fib = [1, 1]

f3 = 2
pos = 2
while len(str(f3)) < 1000:
    f3 = fib[0] + fib[1]
    pos += 1
    fib.pop(0)
    fib.append(f3)

print(pos)
