#!/usr/bin/python3
"""
Square module
"""


from models.rectangle import Rectangle


"""
class Square
"""


class Square(Rectangle):
    """
    class Square inherit from Rectangle
    attributes: size, size, x and y
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init execution"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.height

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update Square with arguments"""
        attr = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i in range(0, len(args)):
                setattr(self, attr[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ return str of square class"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """return dictionnary"""
        new_dict = {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
        return new_dict

    def area(self):
        """return area of square"""
        return self.size * self.size

    def display(self):
        """display square with #"""
        for i in range(self.y):
            print()
        for i in range(0, self.size):
            print(" " * self.x, end='')
            print("#" * self.size)
