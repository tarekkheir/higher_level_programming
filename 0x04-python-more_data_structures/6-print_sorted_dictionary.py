#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary)
    for i in range(0, len(a_dictionary)):
        print("{:s}: {}".format(key[i], a_dictionary[key[i]]))
