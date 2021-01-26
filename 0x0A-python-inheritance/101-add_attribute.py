#!/usr/bin/python3
"""
Add module - task 101
"""


def add_attribute(obj, name, attr):
    """ Add an attribute if its possible"""
    if "__dict__" in dir(obj):
        setattr(obj, name, attr)
    else:
        raise TypeError("can't add new attribute")
