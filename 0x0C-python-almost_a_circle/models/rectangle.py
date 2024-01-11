#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(base):
    """class"""

    def __init__(self,width,height,x=0,y=0,id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """width of the class"""
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value
    @property
    def height(self):
        """hegiht of the class"""
        return self.__height
    @height.setter
    def height(self,value):
        self.height = value
    @property
    def x(self):
        """x of this class"""
        return self.__x
    @x.setter
    def x(self,value):
        self.__x = value
    @property
    def y(self):
        """y of this class"""
        return self.__y
    @y.setter
    def y(self,value):
        self.__y = value
