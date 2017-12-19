#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 102
"""

__author__ = 'ilya_il'


def check_line(d1, d2, d3):
    """
    :param d1: (x1, y1)
    :param d2: (x2, y2)
    :param d3: (x3, y3)
    :return: True/False
    """
    #
    # https://ru.wikipedia.org/wiki/Прямая
    # x = x1 + (x2-x1)*(y-y1)/(y2-y1)
    # y = y1 + (x-x1)*(y2-y1)/(x2-x1)
    #
    # (0, n) - line crosses Y-line
    # (m, 0) - line crosses X-line
    #
    # m = x1 + (x2-x1)*(0-y1)/(y2-y1)
    # n = y1 + (0-x1)*(y2-y1)/(x2-x1)

    return True


def solve_problem():
    pass


solve_problem()
