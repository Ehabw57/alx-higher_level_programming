#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


from requests import post
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(argv) > 1:
        data = {"q": argv[1]}
    respond = post(url, data=data)
    try:
        content = respond.json()
        if len(content) < 2:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except ValueError:
        print("Not a valid JSON")
