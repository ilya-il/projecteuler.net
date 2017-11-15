#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 10

"""

__author__ = 'ilya_il'

import time


def get_prime_numbers(upper_bound):
    prime_numbers = [2, ]
    n = 3

    while n < upper_bound:
        for pn in prime_numbers:
            if n % pn == 0:
                break
        else:
            prime_numbers.append(n)
        n += 2

    print(prime_numbers)
    return sum(prime_numbers)


def get_prime_numbers2(upper_bound):
    # https://ru.wikipedia.org/wiki/Решето_Эратосфена
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

    return sum(nums)


# ~9.7 sec @ 200000
# st = time.time()
# print(get_prime_numbers(200000))
# print("--- %s seconds ---" % (time.time() - st))

# ~0.5 sec @ 2000000
st = time.time()
print(get_prime_numbers2(2000000))
print("--- %s seconds ---" % (time.time() - st))
