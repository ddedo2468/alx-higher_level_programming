#!/usr/bin/python3
"""
Fetch api data
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    aus = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    res = requests.get("https://api.github.com/user", auth=aus)

    print(res.json().get("id"))
