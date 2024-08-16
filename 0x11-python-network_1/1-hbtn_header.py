#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id header"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as respond:
        header = respond.headers
        print(header["X-Request-Id"])
