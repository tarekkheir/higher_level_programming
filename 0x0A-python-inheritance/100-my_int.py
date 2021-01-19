#!/usr/bin/python3
"""
MyInt module - task 100
"""


class MyInt(int):
    """ Class MyInt """

    def __init__(self, state):
        """ Init execute"""
        self.var = state

    def __eq__(self, state):
        """ equal method"""
        return self.state = other.state

    def __ne__(self, state):
        """ not equal method"""
        return not self.__eq__(other)
