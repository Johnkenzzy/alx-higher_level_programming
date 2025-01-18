#!/usr/bin/python3
"""
This script sends a request to the url given as argument.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(f'{req.headers.get("X-Request-Id", None)}')
