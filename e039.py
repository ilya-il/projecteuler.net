#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 39
"""

__author__ = 'ilya_il'

# a + b + c <= 1000
#
# a^2 + b^2 = c^2
# a < c, b < c
# a + b > c
# a <= b

from utils import exec_time


def brute_triangle(p):
    res = []
    for c in range(1, int(p/2)):
        for b in range(1, c):
            a = p - b - c
            if a >= b and a**2 + b**2 == c**2:
                res.append([a, b, c])

    return res


@exec_time
def brute_all():
    max_res = list()
    max_p = 0
    for i in range(1, 1001):
        r = brute_triangle(i)
        if len(r) > len(max_res):
            max_res = r
            max_p = i

    print(max_p)
    print(max_res)


brute_all()
