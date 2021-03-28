#!/usr/bin/python3
def print_last_digit(number):
    ld = number % 10

    if number > 0:
        print("{:d}".format(ld), end='')

    elif ld != 0 and number < 0:
        ld = 10 - ld
        print("{:d}".format(ld), end='')

    elif number == 0:
        ld == 0
        print(number, end='')

    return ld
