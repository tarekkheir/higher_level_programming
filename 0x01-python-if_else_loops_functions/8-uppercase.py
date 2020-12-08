#!/usr/bin/python3
def isnumber(n):
    for i in range(0, 10):
        if n == i:
            return True
    return False

def islower(c):
    for i in range(97, 122):
        if ord(c) == i:
            return True
    for j in range(65, 90):
        if ord(c) == i:
            return False

def uppercase(str):
    s = ""
    for i in range(0, len(str)):
        if islower(str[i]) == True and isnumber(str[i]) == False:
            s = s + chr(ord(str[i]) - 32)
        else:
            s = s + str[i]
    print(s)
