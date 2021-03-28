#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(sorted(a_dictionary.keys()))
    new = a_dictionary.copy()
    for i in range(0, len(a_dictionary)):
        new[keys[i]] = new[keys[i]] * 2
    return new
