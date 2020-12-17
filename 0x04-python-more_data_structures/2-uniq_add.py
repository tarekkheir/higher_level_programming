#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in range(0, len(my_list)):
        count = my_list.count(my_list[i])
        if count != 1:
            my_list.pop(i)

    for i in range(0, len(my_list)):
        result += my_list[i]
    return result
