#!/usr/bin/python3
"""
fetch hhtps://alx-intranet.hbtn.io/status.
"""
import urllib.request


def fetch_status(url):
    """
    function to fetch status
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
    return body


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status_body = fetch_status(url)

    print("Body response:")
    print("\t- type:", type(status_body))
    print("\t- content:", status_body)
    print("\t- utf8 content:", status_body.decode('utf8'))
