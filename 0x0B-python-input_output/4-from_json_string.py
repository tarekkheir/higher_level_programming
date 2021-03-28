#!/usr/bin/python3
"""
I/O module - task 4
"""


import json


def from_json_string(my_str):
    """unction that returns
    an object represented by a JSON string"""
    return json.loads(my_str)
