#!/usr/bin/python3
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representing the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file in JSON format.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        obj_list = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(obj_list))
