#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 42

    ord('A') = 65
    ord('Z') = 90
"""

__author__ = 'ilya_il'

import os

ih = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res\p042_words.txt'))
data = ih.read()
ih.close()

# max word value - 192
words = sorted([n.strip('"') for n in data.split(',')])

# find triangle numbers
tn = [1, ]
while max(tn) <= 192:
    tn.append(int((len(tn) + 2)*(len(tn) + 1) / 2))

print(tn)

res = 0
for i in range(0, len(words)):
    r1 = 0
    for j in words[i]:
        r1 += (ord(j) - 64)

    if r1 in tn:
        res += 1

print(res)
