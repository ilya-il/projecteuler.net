#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 52
"""

__author__ = 'ilya_il'


def solve_problem():
    for n in range(1, 1000000):
        n1 = str(n)
        n2 = str(n*2)
        n3 = str(n*3)
        n4 = str(n*4)
        n5 = str(n*5)
        n6 = str(n*6)

        if len(n1) == len(n2) and \
           len(n2) == len(n3) and \
           len(n3) == len(n4) and \
           len(n4) == len(n5) and \
           len(n5) == len(n6) and \
           len(set(n1)) == len(set(n2)) and \
           len(set(n2)) == len(set(n3)) and \
           len(set(n3)) == len(set(n4)) and \
           len(set(n4)) == len(set(n5)) and \
           len(set(n5)) == len(set(n6)) and \
           set(n2) & set(n3) & set(n4) & set(n5) & set(n6) == set(n1):

            print('Found number - {}'.format(n))


solve_problem()
