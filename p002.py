#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 2
"""

__author__ = 'ilya_il'

fib = [1, 2, 3]

# fib's numbers on even places in sequence
# res = 2
# while fib[3] < 20000:
#     # add last fib to res and shift left for 2 steps, appending new fib's numbers
#     print(fib)
#     res += fib[3]
#     fib.pop(0)
#     fib.append(fib[2] + fib[1])
#     fib.pop(0)
#     fib.append(fib[2] + fib[1])

# fib's numbers are even
res = 2
while fib[2] < 4000000:
    fib.pop(0)
    fib.append(fib[1] + fib[0])
    if fib[2] % 2 == 0:
        res += fib[2]

print(res)
