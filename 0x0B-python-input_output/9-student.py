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

    def to_json(self):
        """Returns dictionary description of the instance"""
        return self.__dict__
