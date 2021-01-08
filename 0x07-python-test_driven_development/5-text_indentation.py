#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', ':', '?']:
            print(i + '\n')
        else:
            print(i, end='')