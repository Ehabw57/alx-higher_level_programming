#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen
with urlopen("https://alx-intranet.hbtn.io/status") as respond:
    body = respond.read()
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode("utf-8")))
