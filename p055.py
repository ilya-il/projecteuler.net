#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 55
"""

__author__ = 'ilya_il'


def solve_problem():
    res = []
    # check numbers
    for n in range(1, 10000):
        # 50 times iteration
        p = n
        for i in range(50):
            # reverse n and add
            p = p + int(str(p)[::-1])
            # check palindrome
            if str(p) == str(p)[::-1]:
                break
        else:
            # Lychrel number found - not a palindrome after 50 iterations
            res.append(n)

    print(res)
    print(len(res))


solve_problem()
