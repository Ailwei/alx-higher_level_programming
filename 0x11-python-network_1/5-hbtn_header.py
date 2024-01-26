#!/usr/bin/python3
"""
Send a request to a URL and display
the value of variable X-request-id in response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # check if the header is present in the response
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
