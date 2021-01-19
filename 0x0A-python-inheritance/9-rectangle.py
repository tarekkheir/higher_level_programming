#!/usr/bin/python3
"""
Inheritance module - task 4
"""


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """raise Exception"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """Raise conditions"""
        if not isinstance(name, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Init execution"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
