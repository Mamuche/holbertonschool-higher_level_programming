#!/usr/bin/python3


"""create class 'rectangle'"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """private instantiation"""
        self.__width = width
        self.__height = height

    """decorators for width"""
    @property
    def width(self):
        """get private instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """decorators for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
