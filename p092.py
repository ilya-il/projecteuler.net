#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 92
"""

__author__ = 'ilya_il'


from utils import exec_time


square_dict = {
    '0': 0,
    '1': 1,
    '2': 4,
    '3': 9,
    '4': 16,
    '5': 25,
    '6': 36,
    '7': 49,
    '8': 64,
    '9': 81
}


def get_next_number(n):
    # return sum([int(x)**2 for x in str(n)])
    return sum([square_dict[x] for x in str(n)])


# 100000 - 1.4s - int(x)**2
# 100000 - 0.5s - square_dict

# 1000000 - 14.4s - int(x)**2
# 1000000 - 5.6s - square_dict

# 10000000 - 59,2s - square_dict
@exec_time
def solve_problem():
    res = 0
    for n in range(1, 1000000):
        n1 = n
        while True:
            n1 = get_next_number(n1)
            if n1 == 1:
                break
            elif n1 == 89:
                res += 1
                break

    print(res)


solve_problem()
