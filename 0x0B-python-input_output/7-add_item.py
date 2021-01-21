#!/usr/bin/python3
"""
I/O module - task 7
"""


import sys
import os


if __name__ == "__main__":
    """ main code executed"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    f = open(filename, "r+")

    if os.path.exists(filename):

        if len(sys.argv) > 1:
            data = load_from_json_file(filename)
            for i in range(1, len(sys.argv)):
                data.append(sys.argv[i])
    else:
        data = []
    save_to_json_file(data, filename)

    f.close()
