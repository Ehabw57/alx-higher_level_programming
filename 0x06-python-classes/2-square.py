#!/usr/bin/python3
"""Make an object of a square class"""


class Square:
    """a Class of Squares"""

    def __init__(self, size=0):
        """
        Intialize a new inctance of sqaure

        Args:
            size (int): The size of the sqare

        Attributes:
            size (int): Size of the object from Square class
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
