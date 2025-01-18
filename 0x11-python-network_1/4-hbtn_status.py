#!/usr/bin/python3
"""
This script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
req = requests.get(url)

print('Body response:')
print(f'\t- type: {type(req.text)}')
print(f'\t- content: {req.text}')
