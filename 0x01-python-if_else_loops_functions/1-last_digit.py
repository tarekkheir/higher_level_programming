#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
else:
    ld = -((-number) % 10)

print("Last digit of {:d}".format(number), end=' ')

if ld > 5:
    print("is {:d} and is greater than 5".format(ld))
elif ld == 0:
    print("is {:d} and is 0".format(ld))
elif ld < 6 and ld != 0:
    print("is {:d} and is less than 6 and not 0".format(ld))
