#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 7

"""

__author__ = 'ilya_il'


def get_prime_numbers(upper_bound):
    prime_numbers = [2, ]

    for n in range(3, upper_bound, 2):
        for pn in prime_numbers:
            if n % pn == 0:
                break
        else:
            prime_numbers.append(n)

    return prime_numbers


def get_prime_number_by_pos(pos):
    prime_numbers = [2, ]
    n = 3

    while len(prime_numbers) < pos:
        for pn in prime_numbers:
            if n % pn == 0:
                break
        else:
            prime_numbers.append(n)

        n += 2

    # return last number in list
    return prime_numbers[-1]


print(get_prime_number_by_pos(10001))

