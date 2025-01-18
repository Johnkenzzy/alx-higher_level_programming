#!/usr/bin/python3
"""
This script checks for GitHub commits (ownername and reponame)
and uses the GitHub API to display name of users with commit id
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        resp = requests.get(url)
        commits = resp.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except Exception as e:
        print(f"Error: {e}")
