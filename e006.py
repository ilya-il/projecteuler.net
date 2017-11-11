#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 6
"""

__author__ = 'ilya_il'

sum_sq = 0
sq_sum = 0
for i in range(1, 101):
    sum_sq += i**2
    sq_sum += i

print(sq_sum**2 - sum_sq)
