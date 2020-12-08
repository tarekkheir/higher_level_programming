#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print(chr(i - (i%2) * 32), end='')
