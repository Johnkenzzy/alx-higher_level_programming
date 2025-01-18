#!/usr/bin/python3
"""
This script sends a POST request to the url given as argument
and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}

    encoded_data = urllib.parse.urlencode(value).encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data)
    with urllib.request.urlopen(request) as response:
        body = response.read()

        print(f'{body.decode("utf-8")}')
