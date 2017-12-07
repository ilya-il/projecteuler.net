#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 24
"""

__author__ = 'ilya_il'


def narayana_algorithm(input_str):
    """ Narayana algorithm of permutations
    https://ru.wikipedia.org/wiki/Алгоритм_Нарайаны
    :param input_str: list on symbols (or string) - initial permutation
    :return: list of all permutations
    """
    count = 1

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

        count += 1
        # find 1000000 permutation
        if count == 1000000:
            print(''.join(a))
            break


narayana_algorithm('0123456789')
