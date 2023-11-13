#!/usr/bin/python3
"""This module defines the Rectangle class."""


from models.base import Base

class Rectangle(Base):
    """The Rectangle class represents a rectangle object."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If the x-coordinate is not an integer.
            ValueError: If the x-coordinate is less than 0.
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If the y-coordinate is not an integer.
            ValueError: If the y-coordinate is less than 0.
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def display(self):
        """Display the rectangle on the console."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Variable number of arguments. The expected order is id, width, height, x, y.
            **kwargs: Variable number of keyword arguments. The keys should match the attribute names.

        Note:
            If both *args and **kwargs are passed, *args takes precedence.

        Raises:
            IndexError: If *args is provided but not all the expected arguments areincluded.
"""
        largs = kwargs.values()
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
