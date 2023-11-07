#!/usr/bin/python3
"""Moudle for write function"""


def write_file(filename="", text=""):
    """
    Writes a sample text ot a file

    Args:
        filename (str): Name of the file
        text (str): Text to write
    """
    with open(filename, "w") as f:
        return f.write(text)
