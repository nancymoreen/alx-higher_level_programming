#!/usr/bin/python3
"""takes Github credentials to display id"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    token = f"{username}:{password}"
    encoded_token = token.encode("utf-8").b64encode().decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded_token}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(user_id)
    else:
        print(None)

