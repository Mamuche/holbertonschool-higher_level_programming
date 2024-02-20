#!/usr/bin/python3
"""create class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """decorators for width"""
    @property
    def width(self):
        return self.__width

    """setter for widht"""
    @width.setter
    def width(self, width):
        self.__width = width

    """decorators for height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, height):
        self.__height = height

    """decorators for x"""
    @property
    def x(self):
        return self.__x

    """setter for x"""
    @x.setter
    def x(self, x):
        self.__x = x

    """decorators for y"""
    @property
    def y(self):
        return self.__y

    """setter for y"""
    @y.setter
    def y(self, y):
        self.__y = y
