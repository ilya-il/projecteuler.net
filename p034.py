#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 34
"""

__author__ = 'ilya_il'


# TODO: SOLVE strange problem - there are infinite amount of numbers
#   1! + 4! + 5! = 145
#   1! + 5! + 0!*24 = 15*10^24

def get_fact(num):
    if num == 0:
        return 1
    else:
        return num*get_fact(num-1)


def calc_facts():
    fact_dict = dict()

    # pass 1 - get factorials from 1 to 9
    for i in range(1, 10):
        fact_dict[i] = get_fact(i)

    print(fact_dict)


calc_facts()
