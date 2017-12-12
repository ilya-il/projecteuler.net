#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 23
"""

__author__ = 'ilya_il'


def solve_problem():
    # x = 2f*a + 1f*b + 50p*c + 20p*d + 10p*e + 5p*f + 2p*g + 1p*h == 2f

    res = 0
    for a in range(2):
        for b in range(3):
            for c in range(5):
                for d in range(11):
                    for e in range(21):
                        for f in range(41):
                            for g in range(101):
                                for h in range(201):
                                    x = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g + 1*h
                                    if x > 200:
                                        break
                                    if x == 200:
                                        res += 1
    print(res)


solve_problem()
