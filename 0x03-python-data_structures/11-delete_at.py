#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) <= idx or idx < 0:
        return my_list

    my_list.remove(my_list[idx])
    return my_list
