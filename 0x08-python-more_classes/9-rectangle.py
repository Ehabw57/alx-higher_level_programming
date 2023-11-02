#!/usr/bin/python3
"""
moudle of class reqtangle
"""


class Rectangle:
    """
    Just A Rectangle class

    Attributes:
        Number_of_instance (int):
        print_symbol (string):
    """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """intialize a new rq as sqr"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        initalize a rextangle

        Args:
            width (int): width of RQ
            height (int): height of Rq
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return the width of Rq"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of RQ"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the hieght of RQ"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of Rq"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of Reqtangle"""
        return self.height * self.width

    def perimeter(self):
        """Return the perimeter of Reqtangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Print symbol based on the Reqtangle"""
        if self.height == 0 or self.width == 0:
            return ""

        s = (str(self.print_symbol) * self.width) + "\n"
        string = s * (self.height - 1)
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """Returns the diminstions of Rq"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delet an instance of a class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest req based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
