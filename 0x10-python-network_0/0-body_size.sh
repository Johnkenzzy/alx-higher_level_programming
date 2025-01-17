#!/bin/bash
# Sends a request to s URL, and displays the size of the body of the response
echo $(curl -s "$1" | wc -c)
