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
        while i < self.height:
            self.str += str(self.print_symbol) * self.__width + '\n'
            i += 1
        return self.str

    def __repr__(self):
        """representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """del actions"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new Rectangle with width and height equals"""
        return cls(size, size)
