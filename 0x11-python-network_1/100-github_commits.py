#!/usr/bin/python3
"""Fetch Github api"""

import requests
import sys


if __name__ == "__main__":

    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'

    response = requests.get(url)

    udata = response.json()
    for i in range(0, 10):
        print(f'{udata[i].get("sha")}: '
              f'{udata[i].get("commit").get("author").get("name")}')
