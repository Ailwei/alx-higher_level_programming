#!/usr/bin/python3
"""
Sends a post requests to a URL and processes the JSON response
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
