#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays the body of the response"""


from urllib import request, error
import sys

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('ascii'))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
