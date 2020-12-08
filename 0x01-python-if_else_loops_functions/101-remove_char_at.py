#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    if n >= 0 and n <= len(str):
        new = str.replace(str[n], '')
    else:
        new = str
    return new
