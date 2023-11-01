#!/usr/bin/python3
"""
moudle of class reqtangle
"""

class Rectangle:
    """
    Just A Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initalize a rextangle
        
        Args:
            width (int): width of RQ
            height (int): height of Rq
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """return the width of Rq"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of RQ"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError ('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """return the hieght of RQ"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set the height of Rq"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError ('height must be >= 0')
        self.__height = value
