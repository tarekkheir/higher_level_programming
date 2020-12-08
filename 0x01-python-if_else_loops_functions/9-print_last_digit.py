#!/usr/bin/python3
def print_last_digit(number):
    ld = ""

    if number > 0:
        ld = number % 10
        print("{:d}".format(ld), end='')

    elif number < 0:
        ld = (-number) % 10
        print("{:d}".format(ld), end='')

    elif number == 0:
        ld == 0
        print(number, end='')

    return ld
