#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status"""


import requests


if __name__ == "__main__":

    req = requests.get("https://intranet.hbtn.io/status")
    html = req.text

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
