#!/usr/bin/python3


"""Write a class Square with private instance atribute """


class Square:
    """class square"""
    def __init__(self, size=0):
        """instantiation"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
