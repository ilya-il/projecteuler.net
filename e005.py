#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 5

"""

# TODO: SOLVE

__author__ = 'ilya_il'


def get_factors(num):
    fact = list()
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            fact.append(i)

    # fact.append(num)
    return fact


def get_number(init):
    res = 1
    nums = [x for x in range(init, 0, -1)]
    # nums = [x for x in range(1, init + 1)]
    for n in nums:
        f = get_factors(n)
        if n != 3 and len(f) < 2:
            res *= n
        print('{p1} - {p2}'.format(p1=n, p2=get_factors(n)))
    print(nums)
    print(res)


get_number(20)
