#!/usr/bin/python3
"""
This script sends a request to the url given as argument.
"""
import sys
import urllib.request


url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    headers = response.getheaders()

    print(f'{dict(headers)["X-Request-Id"]}')
