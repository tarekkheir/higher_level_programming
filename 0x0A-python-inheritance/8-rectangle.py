#!/usr/bin/python3
"""
Inheritance module - task 4
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry"""

    def __init__(self, width, height):
        """Init execution"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
