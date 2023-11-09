#!/usr/bin/python3
"""module for Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """simple chield class"""

    def __init__(self, width, height):
        """intilize new reqtangle instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
