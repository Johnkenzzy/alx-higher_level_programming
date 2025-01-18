#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': q}

    try:
        resp = requests.post(url, data=data)
        resp_json = resp.json()

        if resp_json:
            id = resp_json.get("id", None)
            name = resp_json.get("name", None)
            print(f'[{id}] {name}')
        else:
            print(f'No result')
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
