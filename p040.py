#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 40
"""

__author__ = 'ilya_il'


def solve_problem():
    # d1 x d10 = 1
    res = 1
    # start from d10
    pointer = 10
    total_len = 0
    # cycle with frame = 7
    for n in range(1, 1000000, 7):
        # generate string for 7 numbers
        s = ''.join([str(x) for x in range(n, n + 7)])
        total_len += len(s)
        if total_len > pointer:
            # extract from string s digit with proper index
            d = int(s[-total_len + pointer - 1])
            res *= d
            print('p - {p}, d - {d}'.format(p=pointer, d=d))
            if pointer == 1000000:
                break
            else:
                # to next d()
                pointer *= 10

    print(res)


solve_problem()
