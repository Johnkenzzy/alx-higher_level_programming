#!/usr/bin/python3
"""
This script sends a request to the url given as argument.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    print(f'{resp.headers.get("X-Request-Id", None)}')
