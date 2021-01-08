#!/usr/bin/python3
"""
Module - text indentation
Method: text_indentation
Attribute: text
"""
def text_indentation(text):
    """
    print text by line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', ':', '?']:
            print(i + '\n')
        else:
            print(i, end='')