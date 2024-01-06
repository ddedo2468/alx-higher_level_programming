#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    vals = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(vals).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        bodyMsg = res.read()
        print(bodyMsg.decode('utf-8'))
