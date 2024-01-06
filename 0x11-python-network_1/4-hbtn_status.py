#!/usr/bin/python3
"""
Python script that fetches "https://alx-intranet.hbtn.io/status"
"""

import requests


if __name__ == "__main__":
    url = " https://alx-intranet.hbtn.io/status"

    respose = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(respose.text)))
    print("\t- content: {}".format(respose.text))
