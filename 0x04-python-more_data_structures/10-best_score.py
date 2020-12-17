#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    new = sorted(a_dictionary)
    result = 0
    for i in range(0, len(a_dictionary)):
        if a_dictionary[new[i]] > result:
            result = a_dictionary[new[i]]
            key = new[i]

    return key
