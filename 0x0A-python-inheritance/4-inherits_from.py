#!/usr/bin/python3
"""
Inheritance module - task 4
"""


def inherits_from(obj, a_class):
    """check if obj is an instance of a_class 
    that inherited from the specified class
    """
    if type(obj) == a_class:
        return Falsen
    return isinstance(obj, a_class)
