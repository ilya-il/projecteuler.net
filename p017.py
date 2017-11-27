#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 17
"""

__author__ = 'ilya_il'

digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}


def get_number_in_words(num):
    if num == 1000:
        return 'one thousand'

    w = ''
    n1 = num // 100
    n2 = num % 100
    if n1 in digits.keys():
        w += digits[n1] + ' hundred'
    if n2 in teens.keys():
        if w != '':
            w += ' and '
        w += teens[n2]
        return w

    if n2 // 10 in tens.keys():
        if w != '':
            w += ' and '
        w += tens[n2 // 10]

    if n2 % 10 in digits.keys():
        if n2 // 10 in tens.keys():
            w += '-'
        else:
            if w != '':
                w += ' and '
        w += digits[n2 % 10]

    return w


res = 0
for i in range(1, 1001):
    word = get_number_in_words(i).replace('-', '').replace(' ', '')
    res += len(word)

print(res)
