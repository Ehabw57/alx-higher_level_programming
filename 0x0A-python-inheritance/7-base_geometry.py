#!/usr/bin/python3
"""Module for the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related operations.

    This class provides a basic structure for geometry-related operations.
    It defines a placeholder method for calculating the area and a method for integer validation.
    """

    def area(self):
        """Calculate the area of the shape.

        This method is a placeholder and should be overridden by subclasses.
        It raises an exception to indicate that the area calculation is not implemented.

        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
