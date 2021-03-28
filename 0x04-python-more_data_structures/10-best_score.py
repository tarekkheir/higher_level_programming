#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    if a_dictionary is None:
        return None
    result = 0
    key = 0
    new = sorted(a_dictionary)
    for i in range(0, len(a_dictionary)):
        if a_dictionary[new[i]] > result:
            result = a_dictionary[new[i]]
            key = new[i]
    return key
