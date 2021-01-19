#!/usr/bin/python3
"""
MyInt module - task 12
"""


class MyInt(int):
    """ Class MyInt """

    def __init__(self, value):
        """ Init execute"""
        self.var = value

    def __ne__(self, other):
        """ not equal method"""
        if self.var != other:
            return True
        return False

    def __eq__(self, other):
        """ equal method"""
        if self.var == other:
            return False
        return True
