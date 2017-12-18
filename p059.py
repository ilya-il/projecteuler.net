#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 59
"""

__author__ = 'ilya_il'

import os


def decrypt(crypto_text, key):
    freq_dict = dict()
    open_text = []
    # letters
    sl = [chr(x) for x in range(97, 123)]

    def xor(x, y):
        z = chr(x ^ y)
        # collect only letters
        if z.lower() in sl:
            if z not in freq_dict.keys():
                freq_dict[z.lower()] = 1
            else:
                freq_dict[z.lower()] += 1

        return z

    clen = len(crypto_text)
    klen = len(key)

    rounds = clen // klen
    last_round = 0 if clen % klen == 0 else 1

    # in cycle xor a part of cryto_text by key
    for i in range(rounds + last_round):
        if i == rounds:
            # last round if len(crypto)%len(key) != 0
            a = list(map(xor, crypto_text[i * klen:], key))
            # check if the result contains only letters
        else:
            a = list(map(xor, crypto_text[i * klen: i * klen + 3], key))
        open_text += a

    # https://en.wikipedia.org/wiki/Frequency_analysis
    letters = sorted(freq_dict, key=freq_dict.__getitem__, reverse=True)
    if ''.join(open_text).lower().find('the') != -1 and ''.join(open_text).lower().find('and') != -1 \
            and letters[0] in ['e', 'a', 'o', 'i']:
        print(''.join(open_text[:50]))

        res = sum([ord(x) for x in open_text])
        print(res)

        return True
    else:
        return False


def solve_problem():
    ih = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.join('res', 'p059_cipher.txt')))
    data = ih.read()
    ih.close()

    crypto_text = [int(x) for x in data.split(',')]

    # ord('a') == 97, ord('z') == 122
    # ord('A') == 65, ord('Z') == 90
    # possible values of key items ('a'- 'z')
    key_items = [x for x in range(97, 123)]

    for k1 in key_items:
        print(chr(k1))
        for k2 in key_items:
            # print(chr(k2))
            for k3 in key_items:
                # print(chr(k3))
                if decrypt(crypto_text, [k1, k2, k3]):
                    print('Match key - {k1}{k2}{k3}'.format(k1=chr(k1), k2=chr(k2), k3=chr(k3)))


solve_problem()
