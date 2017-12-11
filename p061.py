#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 61
"""

__author__ = 'ilya_il'


def narayana_algorithm(input_iterable):
    """ Narayana algorithm of permutations
    https://ru.wikipedia.org/wiki/Алгоритм_Нарайаны
    :param input_iterable: list (or string) - initial permutation
    :return: list of all permutations
    """
    res = []

    # sort initial to work properly
    a = sorted(input_iterable)
    b = list(a[::-1])
    c = len(a)

    # append COPY of a
    res.append(a[:])

    while a != b:
        # step 1
        j = -1
        for i in range(c - 2, -1, -1):
            if a[i + 1] > a[i]:
                j = i
                break

        # step 2
        k = -1
        for i in range(c - 1, -1, -1):
            if a[i] > a[j]:
                k = i
                break

        # swap
        a[j], a[k] = a[k], a[j]

        # step 3
        x = a[j+1:c][::-1]
        y = a[0:j+1]
        a = y + x

        # append COPY of a
        res.append(a[:])

    return res


def solve_problem(upper_bound):
    t = []
    s = []
    p = []
    hx = []
    hp = []
    o = []

    # 8128, 2882, 8281 - example (triangle, pentagonal, square) - not ordered tri, pent, sq!!!

    for n in range(2, upper_bound):
        t1 = str(int(n * (n + 1) / 2))
        if len(t1) == 4:
            t.append(t1)
        s1 = str(n**2)
        if len(s1) == 4:
            s.append(s1)
        p1 = str(int(n * (3 * n - 1) / 2))
        if len(p1) == 4:
            p.append(p1)
        hx1 = str(n * (2 * n - 1))
        if len(hx1) == 4:
            hx.append(hx1)
        hp1 = str(int(n * (5 * n - 3)/2))
        if len(hp1) == 4:
            hp.append(hp1)
        o1 = str(n * (3 * n - 1))
        if len(o1) == 4:
            o.append(o1)

    t = ['8128', ]
    s = ['8281', ]
    p = ['2882', ]

    for t1 in t:
        for s1 in s:
            for p1 in p:
                perm = narayana_algorithm([t1, s1, p1])
                # check all combinations of t1, s1, p1
                for pm in perm:
                    # check each combination
                    if pm[0][2:] == pm[1][:2] and pm[1][2:] == pm[2][:2] and pm[2][2:] == pm[0][:2]:
                        print('Magic - {t}, {s}, {p}'.format(t=t1, s=s1, p=p1))

    print(t)
    print(s)
    print(p)


print(narayana_algorithm('123'))
print(narayana_algorithm(['2882', '8128', '8281']))
solve_problem(10000)
