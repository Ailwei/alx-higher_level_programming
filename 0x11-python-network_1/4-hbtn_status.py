#!/usr/bin/python3
"""
Fetches a URL using the requests package and
displays information about response.
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
