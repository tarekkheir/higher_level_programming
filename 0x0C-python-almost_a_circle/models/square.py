#!/usr/bin/python3
"""
Square module
"""


from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.height
    @size.setter
    def size(self, value):
        """attr = ["width", "height"]
        self.check_type(attr[0], value)
        self.check_type(attr[1], value)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        attr = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i in range(0, len(args)):
                setattr(self, attr[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        new_dict = {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
        return new_dict
    
    def area(self):
        return self.size * self.size

    def display(self):
        for i in range(self.x):
            print()
        for i in range(0, self.size):
            print(" " * self.y, end='')
            print("#" * self.size)

        
