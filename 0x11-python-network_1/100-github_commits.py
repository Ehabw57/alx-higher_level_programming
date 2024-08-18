#!/usr/bin/python3
"""fetch github commits based on input arguments from the user"""


from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    respond = get(url)
    content = respond.json()
    for i in range(10):
        commit = content[i]
        sha = commit.get("sha")
        name = commit.get("commit")
        name = name.get("author")
        print("{}: {}".format(sha, name.get("name")))
