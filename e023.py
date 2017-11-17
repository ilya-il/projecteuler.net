#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 23
"""

__author__ = 'ilya_il'

# TODO: SOLVE


def get_factors_sum(num):
    s = 0
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            s += i

    return s


res = 0
# all abundant numbers
nums = list()
# not sure about upper bound
for j in range(1, 28123):
    if get_factors_sum(j) > j:
        nums.append(j)

print(nums)
