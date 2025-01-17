#!/usr/bin/env bash
# Sends a request to s URL, and displays the size of the body of the response

if [ "$#" -ne 1 ]; then
    exit 1
fi

URL=$1
size=$(curl -s "$URL" | wc -c)

echo "$size"
