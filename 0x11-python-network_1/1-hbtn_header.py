#!/usr/bin/python3
"""
fetches a URL, sends a request, and displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    """
    """
    if len(sys.argv) != 2:
            print("Usage: {} <URL>".format(sys.argv[0]))
            sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            header_value = response.getheader('X-Request-Id')
            print(header_value)
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))
        sys.exit(1)
