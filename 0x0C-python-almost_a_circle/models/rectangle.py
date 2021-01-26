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
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init execution"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_type(attr, value):
        """check type of attribute"""
        a = ["width", "height"]
        b = ["x", "y"]

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))
        if attr in a and value <= 0:
            raise ValueError("{} must be > 0".format(attr))
        if attr in b and value < 0:
            raise ValueError("{} must be >= 0".format(attr))

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.x):
            print()
        for i in range(0, self.height):
            print(" " * self.y, end='')
            print("#" * self.width)

    def update(self, *args, **kwargs):

        attr = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(0, len(args)):
                setattr(self, attr[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        new_dict = {
            "width": self.__width, "height": self.__height,
            "x": self._x, "y": self._y, "id": self.id
            }
        return new_dict

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @width.setter
    def width(self, value):
        Rectangle.check_type("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        Rectangle.check_type("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        Rectangle.check_type("x", value)
        self._x = value

    @y.setter
    def y(self, value):
        Rectangle.check_type("y", value)
        self._y = value
