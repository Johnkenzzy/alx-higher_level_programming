#!/usr/bin/python3
"""
This script sends a request to the url given as argument
and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    print(f'{resp.headers.get("X-Request-Id", None)}')

    if resp.status_code >= 400:
        print(f'Error code: {resp.status_code}')
