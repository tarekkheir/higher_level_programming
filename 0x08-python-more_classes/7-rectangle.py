#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Class Attributes: number_of_instances and print_symbol"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """private instances: width, height and str"""
        self.width = width
        self.height = height
        self.str = ""
        Rectangle.number_of_instances += 1

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
        """return perimeter of area"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.__height) * 2 + (self.__width * 2))

    def __str__(self):
        """image of rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        i = 0
        self.str = ""
        while i < self.__height:
            self.str += str(self.print_symbol) * self.__width + '\n'
            i += 1
        return self.str[:-1]

    def __repr__(self):
        """representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del actions"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
