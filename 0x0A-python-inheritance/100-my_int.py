#!/usr/bin/python3
"""
MyInt module - task 100
"""


class MyInt(int):
    """ Class MyInt """

    def __init__(self, state):
        """ Init execute"""
        self.var = state

    def __ne__(self, other):
        '''not equal method'''
        if self.a != other:
            return False
        return True

    def __eq__(self, other):
        '''equal method'''
        if self.a == other:
            return False
        return True