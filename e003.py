#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 3

"""

__author__ = 'ilya_il'

import math


def get_prime_numbers2(big_num):
    # https://ru.wikipedia.org/wiki/Решето_Эратосфена
    upper_bound = int(math.floor(math.sqrt(big_num)))
    nums = [n for n in range(2, upper_bound)]

    n = 0
    while nums[n]**2 <= upper_bound:
        if nums[n] != 0:
            # n - index of prime number
            # pn - prime number
            pn = nums[n]
            for i in range(pn + n, upper_bound - 2, pn):
                nums[i] = 0

        n += 1

    # start from the end of nums, find prime number factor
    res = 0
    for i in range(-1, - upper_bound + 2, -1):
        if nums[i] != 0 and big_num % nums[i] == 0:
            res = nums[i]
            break

    return res


print(get_prime_numbers2(600851475143))
