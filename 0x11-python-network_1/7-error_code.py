#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
with error handling"""


if __name__ == "__main__":
    from requests import get
    from requests.exceptions import HTTPError
    from sys import argv
    try:
        respond = get(argv[1])
        respond.raise_for_status()
        print(respond.text)
    except HTTPError:
        print("Error code: {}".format(respond.status_code))
