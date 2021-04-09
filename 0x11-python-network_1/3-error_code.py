#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays the body of the response"""


import urllib
import sys

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('ascii'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
