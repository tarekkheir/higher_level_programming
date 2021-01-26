#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


"""
Rectangle class
"""


class Rectangle(Base):
    """
    class Rectangle inherit from Base
    attributes: __width, __height, x and y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init execution"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """display rectangle with #"""
        for i in range(self.y):
            print()
        for i in range(0, self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """updtae rectangle with attributes"""
        attr = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(0, len(args)):
                setattr(self, attr[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionnary"""
        new_dict = {
            "width": self.__width, "height": self.__height,
            "x": self._x, "y": self._y, "id": self.id
            }
        return new_dict

    def __str__(self):
        """return str of rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self._x

    @property
    def y(self):
        """get y"""
        return self._y

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self._y = value
