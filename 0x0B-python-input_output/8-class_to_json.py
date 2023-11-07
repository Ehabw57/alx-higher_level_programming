#!/usr/bin/python3
"""module for class to json functoin"""


def class_to_json(obj):
    """
    Rreturns the dictionary description with simple data structure

    Args:
    obj (inctance of class): the object to retrun data from
    """
    return obj.__dict__
