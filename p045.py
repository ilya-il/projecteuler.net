#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 45
"""

__author__ = 'ilya_il'


def brute_nums():
    # T285 = P165 = H143 = 40755
    upper_bound = 100000

    t = []
    p = []
    h = []
    for n in range(2, upper_bound):
        t.append(int(n * (n + 1) / 2))
        p.append(int(n * (3 * n - 1) / 2))
        h.append(int(n * (2 * n - 1)))

    print(set(t) & set(p) & set(h))


brute_nums()
