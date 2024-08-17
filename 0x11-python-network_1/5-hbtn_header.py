#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id header"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    respond = get(argv[1])
    print(respond.headers["x-request-id"])
