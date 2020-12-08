#!/usr/bin/python3
def pow(a, b):

    if b > 0 and a > 0:
        tmp = a
        for i in range(1, b):
            a = a * tmp
    if b == 0 and a > 0:
        a = 1

    if b < 0 and a > 0:
        tmp = a
        a = 1
        for i in range(0, (-b)):
            a = a / tmp

    if a < 0 and b > 0:
        tmp = a
        for i in range(1, b):
            a = a * tmp

    return a
