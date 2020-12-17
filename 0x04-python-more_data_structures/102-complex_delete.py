#!/usr/bin/python3
#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = sorted(a_dictionary)
    for i in range(0, len(a_dictionary)):
        if a_dictionary[keys[i]] == value:
            del a_dictionary[keys[i]]

    return a_dictionary
