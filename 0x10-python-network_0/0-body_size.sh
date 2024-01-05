#!/bin/bash
# takes in a URL, sends a request to that URL,
curl -s -o /dev/null -w '%{size_download}\n' "$1"
