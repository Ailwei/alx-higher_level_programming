#!/usr/bin/python3
"""
Uses Basic Authentication with the github api to display the user's id
"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data['id'])
    except ValueError:
        print(None)
