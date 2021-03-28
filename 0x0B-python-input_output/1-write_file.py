#!/usr/bin/python3
"""
I/O module - task 1
"""


def write_file(filename="", text=""):
    """write string in a file
    and return number of characters written"""
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
