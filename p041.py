#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 41
"""

__author__ = 'ilya_il'


def check_pandigital_number(s):
    if len(s) == 9 and len(set(s)) == 9 and s.find('0') == -1:
        return True
    else:
        return False


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


def solve_problem():
    nums = get_prime_numbers2(200000)
    for i in range(3, 11):
        s = [str(x) for x in range(1, i)]
        perm = narayana_algorithm(s)
        # print(perm)
        for n in perm:
            if check_prime(int(n), nums):
                print('Prime number - {}'.format(n))


solve_problem()

