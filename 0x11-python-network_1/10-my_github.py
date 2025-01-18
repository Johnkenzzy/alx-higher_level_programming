#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        resp = requests.get(url, auth=(username, token))
        if resp.status_code == 200:
            print(resp.json().get("id"))
        else:
            print("None")
    except Exception as e:
        print("Error:", e)
