#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    new_str = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_list.append(my_string[i])
    for i in range(0, len(new_list)):
        new_str = new_str + new_list[i]
    return new_str
