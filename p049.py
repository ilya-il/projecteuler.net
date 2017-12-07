#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 49

    How to check arithmetic sequence

    1487, 4817, 8147
    1) Substract first number from all numbers: 0, 3300, 6660
    2) Start from second number (3300), multiple it for 2, and check if it exists in list from 1):
       3300*2 in (0, 3300, 6600) - match!
"""

__author__ = 'ilya_il'


def narayana_algorithm(input_str):
    """ Narayana algorithm of permutations
    https://ru.wikipedia.org/wiki/Алгоритм_Нарайаны
    :param input_str: list on symbols (or string) - initial permutation
    :return: list of all permutations
    """
    res = []

    # sort initial to work properly
    a = sorted(input_str)
    b = list(a[::-1])
    c = len(a)

    res.append(''.join(a))

    while a != b:
        # step 1
        j = -1
        for i in range(c - 2, -1, -1):
            if a[i + 1] > a[i]:
                j = i
                break

        # step 2
        k = -1
        for i in range(c - 1, -1, -1):
            if a[i] > a[j]:
                k = i
                break

        # swap
        a[j], a[k] = a[k], a[j]

        # step 3
        x = a[j+1:c][::-1]
        y = a[0:j+1]
        a = y + x

        res.append(''.join(a))

    return res


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


def solve_problem():
    nums = get_prime_numbers2(10000)
    for n in range(1234, 9999):
        # find prime numbers in permutations
        # skip numbers with zeros
        if str(n).find('0') == -1:
            perm = narayana_algorithm(str(n))
            pn = [int(x) for x in perm if check_prime(int(x), nums)]
            # sequence len >= 3
            if len(pn) >= 3:
                # check for arithmetic sequence - see header for more
                # start check for 2nd number in sequence (pn[1])
                pn1 = [x - pn[1] for x in pn]
                # check all numbers above 2nd number
                for i in range(2, len(pn1)):
                    if pn1[i]*2 in pn1:
                        print(pn)
                        print('Match')


solve_problem()
