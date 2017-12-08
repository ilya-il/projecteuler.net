#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    ProjectEuler Problem 54
"""

__author__ = 'ilya_il'

import os

# TODO: SOLVE

"""
    Hand value in a list
        [<combination rank>, <max card in combination>, [<additional cards ranks>]]
        
        - combination rank (10-1): royal flush(10) - high card(1)
        - max card in combination(!) (14-2): A(14) - 2(2)
        - additional cards ranks (list): list of additional cards ranks - these cards are not in matched hand
        
        ex:
            hands:
                royal flush: [10, 0, []]
                straight on jacks + ten: [5, 11, [10]]
                pair on queens + two, queen, jack: [2, 2, [2, 12, 11]]  
            
            suit check:
                same suit       - ['C', 'C', 'C', 'C', 'C'] - len(set(suit_list)) == 1
                different suits - ['C', 'S', 'A', 'C', 'A'] - len(set(suit_list)) == 3
            
            rank check:
                consecutive values (ranks) - [10, 11, 12, 13, 14] 
                    - sorted[values] == [x for x in range(min(values), min(values) + 5)]
"""

cards_rank = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def test_hands():
    # royal-flush
    print(parse_hand(['TC', 'JC', 'QC', 'KC', 'AC']))
    print(parse_hand(['TC', 'JC', 'QC', '8C', 'AC']))
    # straight-flush
    print(parse_hand(['2C', '6C', '4C', '5C', '3C']))
    print(parse_hand(['2C', '6C', '4C', '5C', '9C']))
    print(parse_hand(['2C', '6C', '4C', '5C', '2A']))
    # four in hand
    print(parse_hand(['2C', '2C', '4C', '2C', '2A']))
    print(parse_hand(['2C', '5C', '4C', '2C', '2A']))


def check_royal_flush(hand):
    """royal flush - from T to A same suit"""
    res = []
    ranks = [cards_rank[x[0]] for x in hand]
    suits = [x[1] for x in hand]

    if sorted(ranks) == [x for x in range(10, 15)] and len(set(suits)) == 1:
        res = [10, 0, []]

    return res


def check_straight_flush(hand):
    """straight flush - any consecutive values same suit"""
    res = []
    ranks = [cards_rank[x[0]] for x in hand]
    suits = [x[1] for x in hand]

    if sorted(ranks) == [x for x in range(min(ranks), min(ranks) + 5)] and len(set(suits)) == 1:
        res = [9, max(ranks), []]

    return res


def check_four(hand):
    """
    four of a kind - four cards same rank
    1) sort ranks - [2, 2, 2, 2, 10] or [2, 10, 10, 10, 10]
    2) get [:4] - first four or [1:] - last four and check it
    """
    ranks = sorted([cards_rank[x[0]] for x in hand])

    if len(set(ranks[:4])) == 1:
        res = [8, max(ranks[:4]), ranks[4:]]
    elif len(set(ranks[1:])) == 1:
        res = [8, max(ranks[1:]), ranks[:1]]
    else:
        res = []

    return res


def parse_hand(hand):
    print(hand)

    func = (check_royal_flush, check_straight_flush, check_four)
    for f in func:
        res = f(hand)
        if res:
            return res

    return []


def compare_hands(h1, h2):
    """
    Compare hands
    :param h1: Player1 hand
    :param h2: Player2 hand
    :return: 0 - equal hands, 1 - hand1 > hand2, -1 - hand1 < hand2
    """
    return 0


def solve_problem():
    ih = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res\p054_poker.txt'))
    data = ih.readlines()
    ih.close()

    # parse players
    p1 = []
    p2 = []
    for d in data:
        cards = d.strip('\n').split(' ')
        p1.append(cards[:5])
        p2.append(cards[5:])

    res = 0
    for i in range(len(p1)):
        print(parse_hand(p1[i]))
        break
        # if compare_hands(p1[i], p2[i]) > 0:
        #     res += 1

    print(res)


test_hands()
