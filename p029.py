#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 29
"""

__author__ = 'ilya_il'


def calc_powers(upper_bound):
    pwrs = list()
    for a in range(2, upper_bound + 1):
        for b in range(2, upper_bound + 1):
            p = a**b
            if p not in pwrs:
                pwrs.append(p)

    print(len(pwrs))


calc_powers(100)
