#!/usr/bin/python3

"""Create a class Rectangle that defines a rectangle"""

class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    def width(self):
        """retreive attribute"""
        return self.__width
    def height(self):
        return self.__height
    def width(self, value):
        self.__width = value
    def height(self, value):
        """to set the attribute"""
        if type(value) is not int:
            raise typeError("height must be an integer");
        if value < 0:
            raise valueError("height must be >= 0")
        self.__height = value
