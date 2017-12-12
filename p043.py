#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 43
"""

__author__ = 'ilya_il'


def check_divisibility(n):
    n1 = int(n[1:4])
    n2 = int(n[2:5])
    n3 = int(n[3:6])
    n4 = int(n[4:7])
    n5 = int(n[5:8])
    n6 = int(n[6:9])
    n7 = int(n[7:10])

    if n1 % 2 == 0 and n2 % 3 == 0 and n3 % 5 == 0 and n4 % 7 == 0 and n5 % 11 == 0 and n6 % 13 == 0 and n7 % 17 == 0:
        return True
    else:
        return False


def narayana_algorithm(input_str):
    """ Narayana algorithm of permutations
    https://ru.wikipedia.org/wiki/Алгоритм_Нарайаны
    :param input_str: list on symbols (or string) - initial permutation
    :return: list of all permutations
    """
    res = 0

    # sort initial to work properly
    a = sorted(input_str)
    b = list(a[::-1])
    c = len(a)

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

        n = ''.join(a)

        if check_divisibility(n):
            res += int(n)

    return res


def solve_problem():
    print(narayana_algorithm('0123456789'))


solve_problem()
