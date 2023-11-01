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
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
