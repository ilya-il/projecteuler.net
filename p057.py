#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 57
"""

__author__ = 'ilya_il'


def solve_problem():
    # https://ru.wikipedia.org/wiki/Непрерывная_дробь
    # Подходящие дроби
    a = 2
    p = [1, 1]
    q = [0, 1]

    res = 0
    for i in range(1000):
        pn = a*p[i+1] + p[i]
        qn = a*q[i+1] + q[i]
        p.append(pn)
        q.append(qn)

        if len(str(pn)) > len(str(qn)):
            res += 1

    print(res)


solve_problem()
