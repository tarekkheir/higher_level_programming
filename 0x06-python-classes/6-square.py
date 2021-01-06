#!/usr/bin/python3
"""
Square module - init
"""


class Square:
    """
    Square class:
    Attributes: size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Square init: square parameters
        """
        self.size = size
        self.position = position

    def size(self):
        """
        Method return size of square
        """
        return self.__size

    def size(self, value):
        """
        Method set size
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Method return area
        """
        if isinstance(self.size, int) is True:
            return (self.size * self.size)
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        Methode print square
        """
        if self.size != 0:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(' ' * self.position[0], end='')
                print("#" * self.size, end='')
                print()
        else:
            print()

    def position(self, value):
        """
        Method set position
        """
        if len(position) == 2:
            if isinstance(tuple, position):
                if isinstance(int, position[0]):
                    if isinstance(int, position[1]):
                        self.position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def position(self):
        """
        Method return position
        """
        return self.position
