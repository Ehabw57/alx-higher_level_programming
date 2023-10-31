#!/usr/bin/python3
"""
a moulde for print squar
"""


def print_square(size):
    """
    prints a sqaure of #

    Args:
        size (int): size of the sqaure

    Raises:
        TypeError: if size is not int
    """
    if type(size) not in [int, float] or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
