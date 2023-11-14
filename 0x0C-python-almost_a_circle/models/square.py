#!/usr/bin/python3
"""some docstring goes here"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square object,
    which is a special case of a rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The ID of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
                Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) ({self.x})/({self.y}) - ({self.width})"

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.

        Note:
            This method also updates the width and height attributes
            to maintain square proportions.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable number of arguments.
                The expected order is id, size, x, y.
            **kwargs: Variable number of keyword arguments.
                The keys should match the attribute names.

        Note:
            This method overrides the base class update method and calls
            it using super().
            If both *args and **kwargs are passed, *args takes precedence.
        """
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """
        Convert the Square object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the Square object.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
