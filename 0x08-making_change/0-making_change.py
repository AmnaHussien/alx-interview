#!/usr/bin/python3
""" make change"""


def makeChange(coins, total):
    """function that return minimum change"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    numb_change = 0
    summ_change = 0
    for c in coins:
        while summ_change < total:
            summ_change += c
            numb_change += 1
        if summ_change == total:
            return numb_change

        summ_change -= c
        numb_change -= 1
    return -1
