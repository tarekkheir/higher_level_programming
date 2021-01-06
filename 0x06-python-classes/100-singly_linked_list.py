#!/usr/bin/python3
"""
Node module
"""


class Node:
    """
    Node class:
    Attribute: data, next_node
    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    """
    Method set data
    """
    def data(self, value):
        if isinstance(int, value):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """
    Method return data of node
    """
    def data(self):
        return self.__data

    """
    Method set node
    """
    def next_node(self, value):
        if isinstance(Node, value):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
    
    """
    Method return next_node
    """
    def next_node(self):
        return self.__next_node