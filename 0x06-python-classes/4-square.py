#!/usr/bin/python3
"""
Square module - init
"""


class Square:
    """
    Square class:

    Attributes: size
    """
    def __init__(self, size=0):
        """
        Square init: square parameters
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def size(self):
        return self.size

    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    def area(self):
        """
        Method return area
        """
        if isinstance(self.size, int) is True:
            return (self.size * self.size)
        else:
            raise TypeError("size must be an integer")
