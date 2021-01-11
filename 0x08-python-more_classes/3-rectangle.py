#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Attributes: width and heigth"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.str = ""

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """set the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """set the width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.__height) * 2 + (self.__width * 2))

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        i = 0
        self.str = ""
        while i < self.height:
            self.str = self.str + ("#" * self.__width) + '\n'
            i += 1
        return self.str[:-1]
