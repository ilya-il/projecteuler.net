#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 74
"""

__author__ = 'ilya_il'

from utils import exec_time


def get_fact(num):
    """Get number factorial"""
    if num == 0:
        return 1
    else:
        return num*get_fact(num-1)


def calc_facts():
    """Get factorials for numbers 0-9"""
    fact_dict = dict()

    for i in range(10):
        fact_dict[str(i)] = get_fact(i)

    return fact_dict


def get_next_number(n, f):
    """Get next number """
    res = 0
    for i in str(n):
        res += f[i]
    return res


def create_chain(n, f):
    """Create chain"""
    chain = list()
    num = n

    while num not in chain:
        chain.append(num)
        num = get_next_number(num, f)

    return chain


@exec_time
def solve_problem():
    # factorials from 0 to 9
    f = calc_facts()

    res = 0
    for n in range(1, 1000000):
        c = create_chain(n, f)
        if len(c) == 60:
            res += 1

    print(res)


solve_problem()
