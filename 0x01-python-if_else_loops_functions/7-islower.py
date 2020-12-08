#!/usr/bin/python3
def islower(c):
    for i in range(97, 122):
        if ord(c) == i:
            return True
    for j in range(65, 90):
        if ord(c) == i:
            return False
