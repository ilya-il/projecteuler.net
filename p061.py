#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 61
"""

__author__ = 'ilya_il'

from utils import exec_time


def narayana_algorithm(input_iterable):
    """ Narayana algorithm of permutations
    https://ru.wikipedia.org/wiki/РђР»РіРѕСЂРёС‚Рј_РќР°СЂР°Р№Р°РЅС‹
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


def check_cycle(nums):
    print('Check cycle')
    # get all permutations
    perm = narayana_algorithm(nums)
    for pm in perm:
        # head to tail
        if pm[0][:2] == pm[len(pm) - 1][2:]:
            for i in range(len(pm) - 1):
                if pm[i][2:] != pm[i+1][:2]:
                    break
            else:
                print('Valid cycle')
                print(pm)
                return True

    return False


@exec_time
def solve_problem(upper_bound):
    t1 = []
    t2 = []
    s1 = []
    s2 = []
    p1 = []
    p2 = []
    hx1 = []
    hx2 = []
    hp1 = []
    hp2 = []
    o1 = []
    o2 = []

    # 8128, 2882, 8281 - example (triangle, pentagonal, square) - not ordered tri, pent, sq!!!

    for n in range(1, upper_bound):
        t = str(int(n * (n + 1) / 2))
        # start from 1431
        if len(t) == 4 and t[2] != '0':
            t1.append(t[:2])
            t2.append(t[2:])

        s = str(n**2)
        if len(s) == 4 and s[2] != '0':
            s1.append(s[:2])
            s2.append(s[2:])
        p = str(int(n * (3 * n - 1) / 2))

        if len(p) == 4 and p[2] != '0':
            p1.append(p[:2])
            p2.append(p[2:])

        hx = str(n * (2 * n - 1))
        if len(hx) == 4 and hx[2] != '0':
            hx1.append(hx[:2])
            hx2.append(hx[2:])

        hp = str(int(n * (5 * n - 3)/2))
        if len(hp) == 4 and hp[2] != '0':
            hp1.append(hp[:2])
            hp2.append(hp[2:])

        o = str(n * (3 * n - 2))
        if len(o) == 4 and o[2] != '0':
            o1.append(o[:2])
            o2.append(o[2:])

    for i in range(len(t1)):
        print(t1[i] + t2[i])
        t11 = t1[i]
        t22 = t2[i]
        for j in range(len(s1)):
            s11 = s1[j]
            s22 = s2[j]
            for k in range(len(p1)):
                p11 = p1[k]
                p22 = p2[k]
                for l in range(len(hx1)):
                    hx11 = hx1[l]
                    hx22 = hx2[l]
                    for m in range(len(hp1)):
                        hp11 = hp1[m]
                        hp22 = hp2[m]
                        for n in range(len(o1)):
                            pass
                            a1 = {t11, s11, p11, hx11, hp11, o1[n]}
                            a2 = {t22, s22, p22, hx22, hp22, o2[n]}
                            # # 1) first condition - 6 pairs of 2-digit numbers
                            if a1 == a2:
                                # 2) second condition - check real cycle of all combinations
                                if check_cycle([t1[i]+t2[i], s1[j]+s2[j], p1[k]+p2[k],
                                                hx1[l]+hx2[l], hp1[m]+hp2[m], o1[n]+o2[n]]):
                                    print('Magic - {t}, {s}, {p}, {hx}, {hp}, {o}'.
                                          format(t=t1[i]+t2[i], s=s1[j]+s2[j],
                                                 p=p1[k]+p2[k], hx=hx1[l]+hx2[l],
                                                 hp=hp1[m]+hp2[m], o=o1[n]+o2[n]))
                                break


@exec_time
def solve_problem3(upper_bound):
    t1 = []
    t2 = []
    s1 = []
    s2 = []
    p1 = []
    p2 = []

    # 8128, 2882, 8281 - example (triangle, pentagonal, square) - not ordered tri, pent, sq!!!

    for n in range(1, upper_bound):
        t = str(int(n * (n + 1) / 2))
        if len(t) == 4:
            # print(t)
            t1.append(t[:2])
            t2.append(t[2:])
        s = str(n**2)
        if len(s) == 4:
            s1.append(s[:2])
            s2.append(s[2:])
        p = str(int(n * (3 * n - 1) / 2))
        if len(p) == 4:
            p1.append(p[:2])
            p2.append(p[2:])

    for i in range(len(t1)):
        t11 = t1[i]
        t22 = t2[i]
        for j in range(len(s1)):
            s11 = s1[j]
            s22 = s2[j]
            for k in range(len(p1)):
                n1 = {t11, s11, p1[k]}
                n2 = {t22, s22, p2[k]}
                # break
                if n1 == n2:
                    if check_cycle([t11+t22, s11+s22, p1[k]+p2[k]]):
                        print('Magic - {t}, {s}, {p}'.format(t=t11+t22, s=s11+s22, p=p1[k]+p2[k]))
                    break


solve_problem(200)
