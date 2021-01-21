#!/usr/bin/python3
"""
I/O module - task 9
"""


class Student:
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """init executed"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary description of the instance"""
        if attrs is not None:
            new = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new[key] = value
            return new
        else:
            return self.__dict__
