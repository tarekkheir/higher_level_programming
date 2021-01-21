#!/usr/bin/python3
"""
I/O module - task 12
"""


def pascal_triangle(n):
    """returns a list of lists of
    integers representing the Pascal’s triangle of n"""

    lists = []

    if n <= 0:
        return lists

    for i in range(1, n + 1):

        new_list = []

        for j in range(0, i):
            if j == 0 or j == i - 1:
                new_list.append(1)
            elif j == 1:
                new_list.append(i - 1)
            else:
                if lists[i - 2][j] == 1:
                    new_list.append(lists[i - 2][j] + j)
                else:
                    new_list.append(lists[i - 2][j] + j + 1)
        lists.append(new_list)

    return lists
