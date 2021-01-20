#!/usr/bin/python3
"""
I/O module - task 0
"""


def read_file(filename=""):
    """open, read and print file"""
    with open(filename, "r") as f:
        file = f.read()
    print(file)
