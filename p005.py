#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 5

"""

__author__ = 'ilya_il'

import time


def get_number2(init):
    # factors, skip 1 and 2 because of step 10 (number is even in any case)
    f = [x for x in range(3, init + 1)]
    for i in range(10, 1000000000, 10):
        for j in f:
            if i % j != 0:
                break
        else:
            print(i)
            break


# 232792560 @ 3.46 sec
st = time.time()
get_number2(20)
print("--- %s seconds ---" % (time.time() - st))
