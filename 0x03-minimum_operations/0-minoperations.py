#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates
    the fewest number of operations needed to result in exactly n H characters
    in the file
    """
    if n <= 1:
        return 0
    h = 2
    num = 0
    while n > 1:
        if n % h == 0:
            n = n / h
            num = num + h
        else:
            h += 1
    return num
