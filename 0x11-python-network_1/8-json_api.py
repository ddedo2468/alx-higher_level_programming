#!/usr/bin/python3
"""Search API"""
import requests
import sys

if __name__ == "__main__":
    arg = ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": arg}
    res = requests.post(url, data=values)

    try:
        jsonF = res.json()
        if not jsonF:
            print("No result")
        else:
            print("[{}] {}".format(jsonF.get('id'), jsonF.get('name')))
    except ValueError:
        print("Not a valid JSON")
