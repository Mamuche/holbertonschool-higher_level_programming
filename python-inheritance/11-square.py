#!/usr/bin/python3
"""define class rectangle from class BasseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new class inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """return the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
