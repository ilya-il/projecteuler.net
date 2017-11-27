#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 35
"""

__author__ = 'ilya_il'

import time


def get_shift(num):
    # TODO: very slow function!!! see get_shift2 in e037 for the same upper_bound
    shift_list = list()
    digit_list = list(str(num))

    for i in range(0, len(digit_list)):
        # digit_list = digit_list[1:] + digit_list[:1]
        # shift_list.append(int(''.join(digit_list)))
        #
        # adding two lists with the same 'i' is very slow digit_list[i:] + digit_list[:i]
        # or may be adding of lists() is very slow itself
        #
        shift_list.append(int(''.join(digit_list[i:] + digit_list[:i])))

    return sorted(shift_list)


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

    # get shifts for prime numbers and check them for prime
    res = 0
    for i in range(0, len(nums)):
        shift_list = get_shift(nums[i])
        for j in range(len(shift_list)):
            # shift list is sorted, so we need to check prime numbers just till 'shift_list[j]'
            if shift_list[j] not in nums[:shift_list[j]]:
                break
        else:
            res += 1
    print(res)


# 1000000 @ 452 sec
st = time.time()
get_prime_numbers2(1000000)
print("--- %s seconds ---" % (time.time() - st))
