#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    url = argv[1]
    data = {"email": argv[2]}
    respond = post(url, data=data)
    print(respond.text)
