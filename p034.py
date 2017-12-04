#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 34
"""

__author__ = 'ilya_il'


def get_fact(num):
    if num == 0:
        return 1
    else:
        return num*get_fact(num-1)


def calc_facts():
    fact_dict = dict()

    # pass 1 - get factorials from 0 to 9
    for i in range(10):
        fact_dict[str(i)] = get_fact(i)

    print(fact_dict)

    res = 0
    # pass 2 - brute all numbers to 10000000
    for n in range(3, 1000000):
        # find factorials in dict for each digit
        s = sum([fact_dict[j] for j in str(n)])
        if s == n:
            res += n
            print(n)

    print(res)


calc_facts()
