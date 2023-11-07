#!/usr/bin/python3
"""moudle for json_string function"""
from json import dumps as json_dumps


def to_json_string(my_obj):
    """
    Returns an object of an str represnted by json
    Args:
    my_obj (any): Object to retrun ad string
    """
    return json_dumps(my_obj)
