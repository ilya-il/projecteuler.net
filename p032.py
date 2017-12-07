#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 32
"""

__author__ = 'ilya_il'


def get_pandigital_products():
    prod = []
    for a in range(1, 2000):
        for b in range(1, 2000):
            # combine all numbers
            s = '{a}{b}{p}'.format(a=a, b=b, p=a*b)
            # set(s) - gives only unique digits
            # don't use '0' cause to problem definition
            if len(s) == 9 and len(set(s)) == 9 and a <= b and s.find('0') == -1:
                print('a - {a}, b - {b}, p - {p}'.format(a=a, b=b, p=a*b))
                if a*b not in prod:
                    prod.append(a*b)

    print('Res - {}'.format(sum(prod)))


get_pandigital_products()
