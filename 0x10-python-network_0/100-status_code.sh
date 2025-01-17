#!/bin/bash
# sends a request and displays the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
