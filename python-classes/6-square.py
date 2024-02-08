#!/usr/bin/python3


"""Write a class Square with private instance atribute """


class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
   

    def area(self):
        """return the area of square"""
        return self.__size * self.__size

    def my_print(self):
        """print in stdout the sqaure with #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
