#!/usr/bin/python3
"""
Square module - init
"""


class Square:
    """
    Square class:

    Attributes:
    size
    """
    def __init__(self, size=0):
        """
        Square init: square parameters
        """
        if isinstance(size, int) is True:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
