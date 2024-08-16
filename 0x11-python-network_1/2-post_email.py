#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    post_dict = {"email": argv[2]}
    url_encoded_data = urlencode(post_dict)
    data = url_encoded_data.encode("utf-8")
    request = Request(url, data=data)
    with urlopen(request) as respond:
        body = respond.read()
        print(body.decode("utf-8"))
