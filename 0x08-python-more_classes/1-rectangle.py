#!/usr/bin/python3
"""
Create a class Rectangle that defines a rectangle
"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter for the private instance width attribute"""
        if type(value) is not int:
            raise typeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """hieght"""
        return self.__height
    @height.setter
    def height(self, value):
        """to set the attribute"""
        if type(value) is not int:
            raise typeError("height must be an integer");
        if value < 0:
            raise valueError("height must be >= 0")
        self.__height = value
