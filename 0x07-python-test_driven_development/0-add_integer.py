#!/usr/bin/python3
"""
The module of add_integer function
"""


def add_integer(a, b=98):
    """Add tow ingers or flaots

    Args: a (int): the first elment to add
        b (int): the sec enment to add

    Return:
        The sum of both a and b
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
