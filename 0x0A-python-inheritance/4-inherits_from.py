#!/usr/bin/python3
"""moudle of somting"""


def inherits_from(obj, a_class):
    """return true if somthing"""
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False
