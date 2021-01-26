#!/usr/bin/python3
"""
I/O module - task 5
"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
    using a JSON representation"""
    with open(filename, "w") as f:
        f.seek(0)
        json_file = json.dump(my_obj, f)
    return json_file
