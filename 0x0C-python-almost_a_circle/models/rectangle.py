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

    def check_type(attr, value):
        """ check type of attributes"""

        a = ["width", "height"]
        b = ["x", "y"]

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        for attr in a and value < 0:
            raise ValueError("{} must be > 0".format(attr))
        for attr in b and value < 0:
            raise ValueError("{} must be >= 0".format(attr))

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
        check_type("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        check_type("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        check_type("x", value)
        self._x = value

    @y.setter
    def y(self, value):
        """set y"""
        check_type("y", value)
        self._y = value
