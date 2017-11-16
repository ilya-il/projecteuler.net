#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 19

"""

__author__ = 'ilya_il'


# TODO: SOLVE


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(2000))
