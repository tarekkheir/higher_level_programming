#!/usr/bin/python3
"""
Square module
"""


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        self.check_type("width", value)
        self.check_type("height", value)
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        new_dict = {"size": self._size, "x": self._x, "y": self._y, "id": self._id}
        return new_dict