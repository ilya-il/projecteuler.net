#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 102
"""

__author__ = 'ilya_il'

import math
import os


def get_len(d1, d2):
    """Get length"""
    return math.sqrt((d2[0] - d1[0])**2 + (d2[1] - d1[1])**2)


def get_square(a, b, c):
    # Geron's formula of triangle square
    # S = sqrt(p*(p-a)*(p-b)*(p-c))
    p = (a + b + c)/2

    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def check0(d1, d2, d3):
    """
    :param d1: (x1, y1)
    :param d2: (x2, y2)
    :param d3: (x3, y3)
    :return: True/False
    """
    a = get_len(d1, d2)
    b = get_len(d2, d3)
    c = get_len(d1, d3)

    fs = get_square(a, b, c)
    s1 = get_square(get_len((0, 0), d2), get_len(d2, d3), get_len((0, 0), d3))
    s2 = get_square(get_len(d1, (0, 0)), get_len((0, 0), d3), get_len(d1, d3))
    s3 = get_square(get_len(d1, d2), get_len(d2, (0, 0)), get_len(d1, (0, 0)))

    if math.fabs(fs - s1 - s2 - s3) < 0.0005:
        return True
    else:
        return False


def solve_problem():
    # print(check0((-340, 495), (-153, -910), (835, -947)))
    # print(check0((-175, 41), (-421, -714), (574, -645)))
    ih = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.join('res', 'p102_triangles.txt')))
    data = ih.readlines()
    ih.close()

    res = 0
    for d in data:
        dots = [int(x) for x in d.strip('\n').split(',')]

        if check0((dots[0], dots[1]), (dots[2], dots[3]), (dots[4], dots[5])):
            res += 1

    print(res)


solve_problem()
