#!/usr/bin/python3
# coding: utf-8
# IL 30.10.2017

"""
    Some utils functions
"""

__author__ = 'ilya_il'

import time


def exec_time(fn):
    """Check function's time of execution"""
    def wrapper(*args):
        st = time.time()
        fn(*args)
        print("--- %s seconds ---" % (time.time() - st))
    return wrapper
