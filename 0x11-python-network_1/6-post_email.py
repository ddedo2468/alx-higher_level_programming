#!/usr/bin/python3
""" fetching urls data """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    values = {'email': sys.argv[2]}

    res = requests.post(url, data=values)

    print(res.text)
