#!/usr/bin/python3
""" Python script that takes in a URL, sends a
request to the URL and displays the body of the response."""


import requests
import sys


def main(url):

    resp = requests.get(url)

    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
