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

    def area(self):
        """
        Claculates the Area of an object

        Args:
        -------

        Returns:
        The size multiply it self wich is the result of area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Accessing the attribute size value of the object self

        Args:
        --------

        Returns:
            The value of self.size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size attribute equal to value

        Args:
        value (int): New value of size attribute

        Args:
        --------
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints as many '#' as the size attribute value
        """
        if self.size == 0:
            print("")
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print("")
