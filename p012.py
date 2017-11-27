#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 12

    triangle num - 76576500
    num pos - 12376
    number of factors - 576
    --- 2302.319999933243 seconds ---
"""

__author__ = 'ilya_il'

import time


def get_factors(num):
    fact = list()
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            fact.append(i)

    fact.append(num)
    return fact


def find_num(upper_bound):
    triangle_num = 1

    for j in range(2, upper_bound):
        # may be (very may be) triangle num with max factors count should end on '0'
        # но это не точно
        if triangle_num % 10 == 0:
            f = get_factors(triangle_num)
            if len(f) > 500:
                print(triangle_num)
                print(j)
                print(len(f))
                break
        triangle_num += j
    print(triangle_num)


st = time.time()
find_num(15000)
print("--- %s seconds ---" % (time.time() - st))
