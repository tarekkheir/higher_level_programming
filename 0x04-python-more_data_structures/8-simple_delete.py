#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = sorted(a_dictionary)
    for i in range(0, len(a_dictionary)):
        if key == keys[i]:
            del a_dictionary[keys[i]]
            return a_dictionary

    return a_dictionary
