#!/usr/bin/python3
"""
Module - print square
Method: print_square
Attribute: size
"""
def print_square(size):
    """
    print square
    """
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size, end='')
        print()