#!/usr/bin/python3
"""module of append write functon"""


def append_write(filename="", text=""):
    """
    Append writing to a file

    Args
        filename (str): Name of the file
        text (str): Text to append writnig to file
    """
    with open(filename, "a") as f:
        return f.write(text)
