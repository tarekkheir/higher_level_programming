#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]
    for i in range(min(2, len(tuple_a))):
        list_a[i] = tuple_a[i]
    for i in range(min(2, len(tuple_b))):
        list_b[i] = tuple_b[i]
    a = list_a[0] + list_b[0]
    b = list_a[1] + list_b[1]
    return (a, b)
