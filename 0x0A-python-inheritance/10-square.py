#!/usr/bin/python3
"""moudle of class rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square.

    This class inherits from the Rectangle class and represents a square shape.
    It provides methods to calculate the area and a string representation of the square.
    """

    def __init__(self, size):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square's sides.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def __str__(self):
        """Get a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
