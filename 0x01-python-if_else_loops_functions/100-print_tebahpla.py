#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{:c}".format(i - ((i % 2) * 32)), end='')
