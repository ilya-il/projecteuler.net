#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 22

    ord('A') = 65
    ord('Z') = 90
"""

__author__ = 'ilya_il'

import os

ih = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res\p022_names.txt'))
data = ih.read()
ih.close()

names = sorted([n.strip('"') for n in data.split(',')])

res = 0
for i in range(0, len(names)):
    r1 = 0
    for j in names[i]:
        r1 += (ord(j) - 64)
    r1 *= (i + 1)
    res += r1

print(res)
