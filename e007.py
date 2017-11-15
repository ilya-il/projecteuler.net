#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 7

"""

__author__ = 'ilya_il'

import time


def get_prime_numbers(upper_bound):
    prime_numbers = [2, ]

    for n in range(3, upper_bound, 2):
        for pn in prime_numbers:
            if n % pn == 0:
                break
        else:
            prime_numbers.append(n)

    return prime_numbers


def get_prime_number_by_pos(pos):
    prime_numbers = [2, ]
    n = 3

    while len(prime_numbers) < pos:
        for pn in prime_numbers:
            if n % pn == 0:
                break
        else:
            prime_numbers.append(n)

        n += 2

    # return last number in list
    return prime_numbers[-1]


def get_prime_number_by_pos2(pos):
    upper_bound = 105000
    nums = [n for n in range(2, upper_bound)]

    # get prime numbers
    n = 0
    while nums[n]**2 <= upper_bound:
        if nums[n] != 0:
            # n - index of prime number
            # pn - prime number
            pn = nums[n]

            for i in range(pn + n, upper_bound - 2, pn):
                nums[i] = 0

        n += 1

    # count prime numbers
    n = 0
    res = 0
    print(nums)
    for i in range(0, upper_bound - 2):
        if nums[i] != 0:
            n += 1
        if n == pos:
            res = nums[i]
            print(pos)
            break

    # return last number in list
    return res


st = time.time()
print(get_prime_number_by_pos2(10001))
print("--- %s seconds ---" % (time.time() - st))
