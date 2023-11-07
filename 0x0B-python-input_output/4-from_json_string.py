#!/usr/bin/python3
"""moudle """
from json import loads as json_loads


def from_json_string(my_str):
    """
    Returns the JSON representation of an object (string)
    Args:
    my_obj (any): Object to retrun ad string
    """
    return json_loads(my_str)
