#!/bin/bash/python3
"""
"""

import urllib.request
import sys


if __name__ == "__main__":
    """

    """
    url =sys.argv[1]

    req = urllib.request.Reqquest(url)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        x_request_id = headers['X-Request-Id']
        print(x_request_id)
