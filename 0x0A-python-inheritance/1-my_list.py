#!/usr/bin/python3
"""
Inheritance module - task 1
"""


class MyList(list):
    """Mylist inherite from from list"""

    def print_sorted(self):
        """Printed sorted list"""
        print(sorted(self))
