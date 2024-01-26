#!/usr/bin/python3
"""
Sends a post request to url with an email parameter
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("your email is:", response.text)
