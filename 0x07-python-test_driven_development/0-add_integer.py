#!/usr/bin/python3
"""
Module - add integer
Method: add_integer
Attributes: a and b
"""


def add_integer(a, b=98):
    """
    Return the addition of two integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        elif type(b) is float:
            b = int(b)
        return a + b
