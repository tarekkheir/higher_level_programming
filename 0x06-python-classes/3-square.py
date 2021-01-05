#!/usr/bin/python3
"""
Square module - init
"""


class Square:
    """
    Square class:

    Attributes: size
    """
    def __init__(self, size=None):
        """
        Square init: square parameters
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
                self.__size = size

    def area(self):
        """
        Method return area
        """
        return (self.__size * self.__size)
