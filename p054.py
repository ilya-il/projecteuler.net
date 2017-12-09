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
        [<combination value>, <max card in combination1>, <max card in combination2>, [<additional cards values>]]
        
        - combination value (10-1): royal flush(10) - high card(1)
        - max card in combination1 (14-2): A(14) - 2(2)
        - max card in combination2 (14-2): A(14) - 2(2)        
        - additional cards values (list): list of additional cards values - these cards are not in matched hand
        
        ex:
            hands:
                royal flush: [10, 0, 0, []]
                straight on jacks + ten: [5, 11, 0, [10]]
                pair on queens + two, ten, jack: [2, 12, 0, [2, 10, 11]]
                full house on three queens and pair of two: [7, 12, 2, []]  
            
            suit check:
                same suit       - ['C', 'C', 'C', 'C', 'C'] - len(set(suit_list)) == 1
                different suits - ['C', 'S', 'A', 'C', 'A'] - len(set(suit_list)) == 3
            
            values check:
                consecutive values - [10, 11, 12, 13, 14] 
                    - sorted[values] == [x for x in range(min(values), min(values) + 5)]
"""

card_values = {
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
    print(parse_hand(['2C', '6C', '4C', '5C', '2H']))
    # four in hand
    print(parse_hand(['2H', '2C', '4D', '2S', '2D']))
    print(parse_hand(['2C', '5C', '4C', '2D', '2H']))
    # full house
    print(parse_hand(['4H', '2C', '4C', '2D', '2H']))
    print(parse_hand(['8C', '2H', '2S', '2C', '8D']))
    print(parse_hand(['3C', '2H', '2S', '2C', '8D']))
    # flush
    print(parse_hand(['4C', '2C', '5C', 'AC', '8C']))
    print(parse_hand(['4C', '2C', '5C', 'AC', '8S']))
    # straight
    print(parse_hand(['4C', '2C', '5C', '3C', '6D']))
    print(parse_hand(['4C', '2C', '5C', '3C', '8S']))
    # three in hand
    print(parse_hand(['4C', '4H', '5C', '3C', '4D']))
    print(parse_hand(['4C', '4H', '8C', '5S', '4D']))
    print(parse_hand(['4C', '2C', '4S', '4D', '3D']))
    print(parse_hand(['4C', '2C', '5C', '3C', '8S']))
    # check two pairs
    print(parse_hand(['4C', '4H', '5C', '5C', '8D']))
    print(parse_hand(['4C', '4H', '8C', '5S', '5D']))
    print(parse_hand(['4C', '2C', '2S', '5S', '5D']))
    print(parse_hand(['4C', '2C', '5C', '3C', '8S']))
    # check pair
    print(parse_hand(['4C', '4H', '5C', '3C', '8D']))
    print(parse_hand(['4C', '8H', '8C', '5S', 'TD']))
    print(parse_hand(['3C', '2C', '4S', '4D', 'TD']))
    print(parse_hand(['4C', '2C', '5C', '8C', '8S']))
    print(parse_hand(['4C', '2C', '5C', '3C', '8S']))
    # check high
    print(parse_hand(['4C', '2H', '5C', '3C', '8D']))


def check_royal_flush(hand):
    """royal flush - from T to A in same suit

    If both players have royal flush, no more card check
    """
    values = [card_values[x[0]] for x in hand]
    suits = [x[1] for x in hand]

    if sorted(values) == [x for x in range(10, 15)] and len(set(suits)) == 1:
        res = [10, 14, 0, []]
    else:
        res = []

    return res


def check_straight_flush(hand):
    """straight flush - any consecutive values of same suit
    If both players have straight flush check max card value
    """
    values = [card_values[x[0]] for x in hand]
    suits = [x[1] for x in hand]

    if sorted(values) == [x for x in range(min(values), min(values) + 5)] and len(set(suits)) == 1:
        res = [9, max(values), 0, []]
    else:
        res = []

    return res


def check_four(hand):
    """
    four of a kind - four cards of the same value
    1) sort values - [2, 2, 2, 2, 10] or [2, 10, 10, 10, 10]
    2) get [:4] - first four or [1:] - last four and check it

    If both players have four in hand check max value or four or (if four in hand are equal) check value on fifth card
    """
    values = sorted([card_values[x[0]] for x in hand])

    if len(set(values[:4])) == 1:
        res = [8, max(values[:4]), 0, values[4:]]
    elif len(set(values[1:])) == 1:
        res = [8, max(values[1:]), 0, values[:1]]
    else:
        res = []

    return res


def check_full_house(hand):
    """
    Full house - three of a kind and a pair
    1) sort values - [2, 2, 8, 8, 8] or [2, 2, 2, 8, 8]
    2) get [:2] and [2:] or [:3] and [3:] and check it

    If both players have full house check max value of three or (if three in hand are equal) check max value of two
    """
    values = sorted([card_values[x[0]] for x in hand])

    if len(set(values[:2])) == 1 and len(set(values[2:])) == 1:
        # [7, max value of three, max_value of two, []]
        res = [7, max(values[2:]), max(values[:2]), []]
    elif len(set(values[:3])) == 1 and len(set(values[3:])) == 1:
        res = [7, max(values[:3]), max(values[3:]), []]
    else:
        res = []

    return res


def check_flush(hand):
    """All cards of the same suit

    If both players have equal flush check values of cards"""
    values = sorted([card_values[x[0]] for x in hand])
    suits = [x[1] for x in hand]

    if len(set(suits)) == 1:
        res = [6, 0, 0, values]
    else:
        res = []

    return res


def check_straight(hand):
    """All cards are consecutive values

    If both players have straight check max card value"""
    values = [card_values[x[0]] for x in hand]

    if sorted(values) == [x for x in range(min(values), min(values) + 5)]:
        res = [5, max(values), 0, []]
    else:
        res = []

    return res


def check_three(hand):
    """Three cards of the same value
    1) sort values - [2, 2, 2, 8, 10], [2, 8, 8, 8, 10], [2, 3, 8, 8, 8]
    2) get slice and check it

    If both players have three in a hand check max of three or (if three in hand are equal) check rest cards
    """
    values = sorted([card_values[x[0]] for x in hand])

    if len(set(values[:3])) == 1:
        res = [4, max(values[:3]), 0, values[3:]]
    elif len(set(values[1:4])) == 1:
        res = [4, max(values[1:4]), 0, [values[0], values[4]]]
    elif len(set(values[2:])) == 1:
        res = [4, max(values[2:]), 0, values[:2]]
    else:
        res = []

    return res


def check_two_pairs(hand):
    """Two different pairs

    1) sort values - [2, 2, 3, 3, 8], [2, 2, 3, 8, 8], [2, 3, 3, 8, 8]
    2) check slices

    If both players have two pairs
    """
    values = sorted([card_values[x[0]] for x in hand])

    if len(set(values[:2])) == 1 and len(set(values[2:4])) == 1\
            and set(values[:2]) != set(values[2:4]):
        res = [3, max(values[:2] + values[2:4]), min(values[:2] + values[2:4]), values[4:5]]
    elif len(set(values[:2])) == 1 and len(set(values[3:])) == 1\
            and set(values[:2]) != set(values[3:]):
        res = [3, max(values[:2] + values[3:]), min(values[:2] + values[3:]), values[2:3]]
    elif len(set(values[1:3])) == 1 and len(set(values[3:])) == 1\
            and set(values[1:3]) != set(values[3:]):
        res = [3, max(values[1:3] + values[3:]), min(values[1:3] + values[3:]), values[0:1]]
    else:
        res = []

    return res


def check_pair(hand):
    """Two cards of the same value
    1) sort values - [2, 2, 3, 4, 5], [2, 3, 3, 4, 5], [2, 3, 4, 4, 5], [2, 3, 4, 5, 5]
    2) check slices

    If both players have pairs - check max in pair or (if pairs are equal) check other cards
    """
    values = sorted([card_values[x[0]] for x in hand])

    if len(set(values[:2])) == 1:
        res = [2, max(values[:2]), 0, values[2:]]
    elif len(set(values[1:3])) == 1:
        res = [2, max(values[1:3]), 0, values[0:1] + values[3:]]
    elif len(set(values[2:4])) == 1:
        res = [2, max(values[2:4]), 0, values[:2] + values[4:]]
    elif len(set(values[3:5])) == 1:
        res = [2, max(values[3:5]), 0, values[:3]]
    else:
        res = []

    return res


def check_high(hand):
    """Highest value card"""
    values = sorted([card_values[x[0]] for x in hand])

    res = [1, values[4], 0, values[:4]]

    return res


def parse_hand(hand):
    print(hand)

    func = (check_royal_flush, check_straight_flush, check_four, check_full_house, check_flush, check_straight,
            check_three, check_two_pairs, check_pair, check_high)
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
        h1 = parse_hand(p1[i])
        h2 = parse_hand(p2[i])

        print(h1)
        print(h2)
        break
        # if compare_hands(p1[i], p2[i]) > 0:
        #     res += 1

    print(res)


test_hands()
