#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 20
"""

__author__ = 'ilya_il'


def get_fact(num):
    if num == 0:
        return 1
    else:
        return num*get_fact(num-1)


print(sum([int(x) for x in str(get_fact(100))]))
