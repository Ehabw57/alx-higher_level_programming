#!/usr/bin/python3
""" hi iam gay """
from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth

url = "https://api.github.com/user"
if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    respond = get(url, auth=auth)
    print(respond.json().get("id"))
