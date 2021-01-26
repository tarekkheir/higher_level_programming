#!/usr/bin/python3
"""
I/O module - task 12
"""


def factoriel(n):
    if n == 0:
        return 1
    else:
        nb = 1
        for i in range(2, n+1):
            nb = nb * i
        return nb


def pascal_triangle(n):
    """returns a list of lists of
    integers representing the Pascal’s triangle of n"""

    lists = []

    if n <= 0:
        return lists

    for i in range(0, n):

        new_list = []
        if i == 0:
            new_list.append(1)
        for j in range(0, i):

            nb = factoriel(i) / (factoriel(i - j) * factoriel(j))
            new_list.append(int(nb))

        if i != 0:
            new_list.append(1)
        lists.append(new_list)

    return lists
