#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 53
"""

__author__ = 'ilya_il'


def get_fact(num):
    if num == 0:
        return 1
    else:
        return num*get_fact(num-1)


def solve_problem():
    fact = dict()
    res = 0

    # step 1 - get all factorials from 1 to 100
    for i in range(0, 101):
        fact[i] = get_fact(i)

    # step 2 - brute all
    for n in range(1, 101):
        for r in range(1, n + 1):
            c = fact[n]/(fact[r]*fact[n - r])
            if c > 1000000:
                res += 1

    print(res)


solve_problem()
