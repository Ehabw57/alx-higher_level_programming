#!/usr/bin/python3
"""Apython module for reaiing function"""


def read_file(filename=""):
    """
    Reads a file and print it to stdout

    Args:
    filename (str): the file name or path
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
