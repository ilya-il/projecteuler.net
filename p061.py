#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 61
"""

__author__ = 'ilya_il'

from utils import exec_time


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

    for n in range(2, upper_bound):
        t = str(int(n * (n + 1) / 2))
        if len(t) == 4 and t.find('0') == -1:
            t1.append(t[:2])
            t2.append(t[2:])
        s = str(n**2)
        if len(s) == 4 and s.find('0') == -1:
            s1.append(s[:2])
            s2.append(s[2:])
        p = str(int(n * (3 * n - 1) / 2))
        if len(p) == 4 and p.find('0') == -1:
            p1.append(p[:2])
            p2.append(p[2:])
        hx = str(n * (2 * n - 1))
        if len(hx) == 4 and hx.find('0') == -1:
            hx1.append(hx[:2])
            hx2.append(hx[2:])
        hp = str(int(n * (5 * n - 3)/2))
        if len(hp) == 4 and hp.find('0') == -1:
            hp1.append(hp[:2])
            hp2.append(hp[2:])
        o = str(n * (3 * n - 1))
        if len(o) == 4 and o.find('0') == -1:
            o1.append(o[:2])
            o2.append(o[2:])

    for i in range(len(t1)):
        print(t1[i] + t2[i])
        for j in range(len(s1)):
            for k in range(len(p1)):
                for l in range(len(hx1)):
                    for m in range(len(hp1)):
                        for n in range(len(o1)):
                            a1 = {t1[i], s1[j], p1[k], hx1[l], hp1[m], o1[n]}
                            a2 = {t2[i], s2[j], p2[k], hx2[l], hp2[m], o2[n]}
                            if a1 == a2:
                                # print(n)
                                if t1[i] != t2[i] and s1[j] != s2[j] and p1[k] != p2[k] and hx1[l] != hx2[l] and\
                                        hp1[m] != hp2[m] and o1[n] != o2[n]:
                                    print('Magic - {t}, {s}, {p}, {hx}, {hp}, {o}'.format(t=t1[i]+t2[i], s=s1[j]+s2[j],
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

    for n in range(2, upper_bound):
        t = str(int(n * (n + 1) / 2))
        if len(t) == 4 and t.find('0') == -1:
            # print(t)
            t1.append(t[:2])
            t2.append(t[2:])
        s = str(n**2)
        if len(s) == 4 and t.find('0') == -1:
            s1.append(s[:2])
            s2.append(s[2:])
        p = str(int(n * (3 * n - 1) / 2))
        if len(p) == 4 and p.find('0') == -1:
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
                    print(n1)
                    print(n2)
                    print('Magic - {t}, {s}, {p}'.format(t=t11+t22, s=s11+s22, p=p1[k]+p2[k]))
                    break


solve_problem(200)
