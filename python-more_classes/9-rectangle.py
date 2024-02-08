#!/usr/bin/python3


"""create class 'rectangle'"""


class Rectangle:
    """class rectangle"""

    """public class attribute"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """private instantiation"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    """decorators for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
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

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return an informal string version of the object"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)
        for row in range(self.__height):
            for column in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        string = string[:-1]
        return string

    def __repr__(self):
        """return an official string version of the objetc"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """print message when delete an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance """
        height = size
        width = size
        return cls(height, width)
