#!/usr/bin/python3


"""Write a class Square with private instance atribute """


class Square:
    """class square"""
    def __init__(self, size=0):
        """instantiation"""
        self.__size = size

    """decorators, define special methods when modifying the attributes"""
    @property
    def size(self):
        return self.__size

    """decorators, define special methods when modifying the attributes"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of square"""
        return self.__size * self.__size
