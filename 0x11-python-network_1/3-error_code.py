#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
with error handling"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as respond:
            body = respond.read()
            print(body.decode("utf-8"))
    except HTTPError as Error:
        print("Error code: {}".format(Error.status))
