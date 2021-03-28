#!/usr/bin/python3
"""
I/O module - task 6
"""


import json


def load_from_json_file(filename):
    """function that creates
    an Object from a “JSON file”"""
    with open(filename, "r") as f:
        data = json.load(f)
    return data
