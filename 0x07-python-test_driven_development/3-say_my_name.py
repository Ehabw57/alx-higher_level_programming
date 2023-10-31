#!/usr/bin/python3
"""
A moudle of say_my_name function

Attribute:
    say_my_name(str, str)
"""


def say_my_name(first_name, last_name=""):
    """
    Display the first and last name

    Args:
        first_name (str): First name
        last_name  (str): Last name
    Rasises:
        TypeError: If the first or last name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
