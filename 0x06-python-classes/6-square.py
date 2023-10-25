#!/usr/bin/python3
"""Make an object of a square class"""


class Square:
    """a Class of Squares"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Intialize a new inctance of sqaure

        Args:
            size (int): The size of the sqare
            position (tuple): The positon of the sqare

        Attributes:
            size (int): Size of the object from Square class
            position (tuple): Where the hashed sould be printed
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (
            len(position) != 2
            or type(position[1]) is not int
            or type(position[0]) is not int
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Acsscing the data of postion attribute

        Return the value of postion attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of postion attribute
        """
        if (
            len(value) != 2
            or type(value[1]) is not type(value[0]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def my_print(self):
        """
        Prints as many '#' as the size attribute value
        """
        if self.size == 0:
            print("")
            return None

        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        for i in range(self.size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
