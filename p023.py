#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 23
"""

__author__ = 'ilya_il'


def get_factors_sum(num):
    s = 0
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            s += i

    return s


def solve_problem():
    # step 1) - all abundant numbers
    ab_nums = [j for j in range(1, 28123) if get_factors_sum(j) > j]
    # step 2) all nums to 28123
    nums = [x for x in range(1, 28123)]
    # step 3) get all possible sums of abundant numbers and remove these sums from all nums
    for i in range(len(ab_nums)):
        print(ab_nums[i])
        for j in range(i, len(ab_nums)):
            n = ab_nums[i] + ab_nums[j]
            # if sum is too big - next i
            if n > 28123:
                break
            if n in nums:
                nums.remove(n)

    print(nums)
    print(len(nums))
    print(sum(nums))


solve_problem()
