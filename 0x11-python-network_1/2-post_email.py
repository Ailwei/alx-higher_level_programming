#!/usr/bin/python3
"""
Sends a POST request to a URL with a email parameter
"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    dt = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, dt)

    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print("hr@holbertonschool.com:", body)
    except urllib.error.HTTPError as e:
            print("Error code:", e.code)
    except urllib.error.URLError as e:
            print("Error: {}".format(e.reason))
