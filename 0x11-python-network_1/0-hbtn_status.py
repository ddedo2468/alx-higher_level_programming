#!/usr/bin/python3
""" Python Script that fetches an url usuing urlib """

import urllib.request


if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as res:
        bodymsg = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodymsg)))
        print("\t- content: {}".format(bodymsg))
        print("\t- utf8 content: {}".format(bodymsg.decode('utf-8')))
