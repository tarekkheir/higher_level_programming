#!/usr/bin/python3
"""
I/O module - task 2
"""


def append_write(filename="", text=""):
    """appends a string to a text file and
    returns the number of characters added"""
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
