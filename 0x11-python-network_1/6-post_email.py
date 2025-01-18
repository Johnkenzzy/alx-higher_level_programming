#!/usr/bin/python3
"""
This script sends a POST request to the url given as argument
and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    resp = request.post(url, data=payload)
    print(f'{resp.text}')
