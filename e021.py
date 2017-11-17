#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 21
"""

__author__ = 'ilya_il'


def get_factors(num):
    fact = list()
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            fact.append(i)

    return fact


def d(num):
    return sum(get_factors(num))


res = 0
for i in range(1, 10001):
    if i == d(d(i)) and i < d(i):
        res += i + d(i)
        print('{a}, {b}'.format(a=i, b=d(i)))
print(res)
