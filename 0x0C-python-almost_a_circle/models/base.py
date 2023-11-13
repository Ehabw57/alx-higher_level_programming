#!/usr/bin/python3
"""This module defines the Base class."""
class Base:
    """The Base class represents a base object."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The ID of the object. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
