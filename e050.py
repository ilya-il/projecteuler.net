#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 50
"""

__author__ = 'ilya_il'


def get_prime_numbers2(upper_bound):
    # get prime numbers
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

    # reduce list - leave only prime numbers
    nums = [x for x in nums if x != 0]

    res_sum = 0
    res_count = 0
    for i in range(int(len(nums)/2) + 1):
        for j in range(i + 1, int(len(nums)/2) + 1):
            res = sum(nums[i:j])

            # sum must be less then upper_bound
            if res > upper_bound:
                break

            # sum of numbers is prime number
            if res in nums and len(nums[i:j]) > res_count:
                res_sum = res
                res_count = len(nums[i:j])

    print('prime count, sum is - {count}, {sum}'.format(count=res_count, sum=res_sum))


get_prime_numbers2(1000000)
