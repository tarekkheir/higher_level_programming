#!/usr/bin/python3
"""
Square module - task 11
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Class square"""

    def __init__(self, size):
        """ Init execution"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return str of Square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
