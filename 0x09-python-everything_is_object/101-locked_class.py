#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """no public instance attribute"""
    def __init__(self):
        pass
    __slots__ = ['first_name']
