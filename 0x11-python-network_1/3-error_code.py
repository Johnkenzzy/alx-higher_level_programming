#!/usr/bin/python3
"""
This script sends a request to the url given as argument
and displays the body of the response
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            headers = response.getheaders()

            print(f'{dict(headers).get("X-Request-Id", None)}')
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
