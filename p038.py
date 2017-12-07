#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 38
"""

__author__ = 'ilya_il'


def check_pandigital_number(s):
    if len(s) == 9 and len(set(s)) == 9 and s.find('0') == -1:
        return True
    else:
        return False


def solve_problem():
    for m in range(1, 100000):
        s = ''
        for n in range(1, 20):
            s += str(m*n)
            # print(s)

            if len(s) < 9:
                # next n
                pass
            elif len(s) > 9:
                # too much, next m
                break
            else:
                # found len(s) == 9, check if s is pandigital number
                if check_pandigital_number(s):
                    print('{s}, {m}, {n}'.format(s=s, m=m, n=n))


solve_problem()
