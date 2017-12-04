#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 26
"""

__author__ = 'ilya_il'


def get_fraction(n):
    """Get fraction 1/n"""
    res = ''
    d = 1
    # 100 - fraction len
    for i in range(1, 10000):
        res += str(d//n)
        d = d % n*10

    # [1:0] - pure periodic - 0,(123)
    # [n:0] - mixed periodic, n > 1 - 0,0(123)
    # [3:0] - valid for right answer
    return res[3:]


def get_cycles(upper_bound):
    max_frame_len = 0
    max_n = 0
    for n in range(2, upper_bound):
        # only fraction
        s = get_fraction(n)

        frame_len = 0
        for i in range(1, int(len(s))):
            # find first cycle for n
            if s[0:i] == s[i: i*2] and i > frame_len:
                frame_len = i
                break

        if frame_len > max_frame_len:
            max_frame_len = frame_len
            max_n = n

    print(max_n)
    print(max_frame_len)


get_cycles(1000)
