#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 32
"""

__author__ = 'ilya_il'


def check_currious_fraction(a, b):
    if a == b:
        return False

    for i in range(1, 10):
        # remove identical digits
        if str(i) in str(a) and str(i) in str(b):
            a1 = str(a).replace(str(i), '')
            b1 = str(b).replace(str(i), '')

            # a1/b1 is new fraction
            # a != a1 - make sure of new fraction
            # a*b1 == a1*b - compare fractions
            if len(a1) > 0 and len(b1) > 0 and a != a1 and a*int(b1) == int(a1)*b:
                return True

    return False


def get_fractions():
    # all numerators
    n = []
    # all denominators
    d = []
    # only two digits
    for a in range(10, 100):
        for b in range(11, 100):
            # problem definition - fraction less then 1 (a < b)
            # problem definition - skip trivial fraction, ex. 30/50 (a%10, b%10)
            if a < b and a % 10 != 0 and b % 10 != 0 and check_currious_fraction(a, b) is True:
                n.append(a)
                d.append(b)

    print(n)
    print(d)

    a2 = 1
    b2 = 1
    for i in range(0, 4):
        a2 *= n[i]
        b2 *= d[i]

    print(a2)
    print(b2)


get_fractions()
