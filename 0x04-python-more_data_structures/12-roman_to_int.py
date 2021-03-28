#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return None
    key = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    value = [1, 5, 10, 50, 100, 500, 1000]
    count = 0

    for i in range(0, len(roman_string)):
        for j in range(len(roman_string)):
            if key[i] == roman_string[j]:
                count += value[i]

    return count
