#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 19

"""

__author__ = 'ilya_il'

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_year_days(year):
    """Get all days of the year"""
    days = list()
    for i in months:
        days += [x for x in range(1, months[i] + 1)]
        if i == 2 and is_leap_year(year):
            days += [29, ]

    return days


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def count_sundays(days):
    # first sunday ()
    i = 6
    sun = 0
    while i < len(days):
        # first day of month
        if days[i] == 1:
            sun += 1
        i += 7

    return sun


# 01.01.1900 - monday, num of sundays in 1900 - 2
print(len(get_year_days(1900)))
print(count_sundays(get_year_days(1900)))

all_days = list()
for y in range(1900, 2001):
    all_days += get_year_days(y)

print(count_sundays(all_days) - 2)
