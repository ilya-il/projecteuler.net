#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 58
"""

__author__ = 'ilya_il'


def check_prime(n, pn_list):
    """
    Check if number is prime by dividing it by real prime numbers in cycle (see problem 3)
    :param n: number to check
    :param pn_list: list of prime numbers
    :return: False/True
    """
    for i in pn_list:
        if n % i == 0 and n != i:
            return False

    return True


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
    return nums


def solve_problem():
    # spiral size
    sp_size = 30000
    # start diagonal number
    n1 = 1
    # delta to count corners
    # delta is distance between two corners, delta+1=size_size
    delta = 2

    pn = get_prime_numbers2(2000000)
    all_count = 1
    prime_count = 0

    while delta <= (sp_size - 1):
        for i in range(1, 5):
            n1 += delta
            if check_prime(n1, pn):
                prime_count += 1
            all_count += 1

        # check ratio
        if prime_count / all_count < 0.1:
            print('Check!')
            print(delta + 1)
            break

        delta += 2


solve_problem()
