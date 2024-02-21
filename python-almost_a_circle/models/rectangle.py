#!/usr/bin/python3
"""create class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.validator(width=width, height=height, x=x, y=y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def validator(**kwargs):
        """ Function for validate the arg of the init function
            and for set value """
        for k, v in kwargs.items():
            if k == "width" or k == "height":
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v <= 0:
                    raise ValueError("{} must be > 0".format(k))
            else:
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v < 0:
                    raise ValueError("{} must be >= 0".format(k))

    """decorators for width"""
    @property
    def width(self):
        return self.__width

    """setter for widht"""
    @width.setter
    def width(self, width):
        self.validator(width=width)
        self.__width = width

    """decorators for height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, height):
        self.validator(height=height)
        self.__height = height

    """decorators for x"""
    @property
    def x(self):
        return self.__x

    """setter for x"""
    @x.setter
    def x(self, x):
        self.validator(x=x)
        self.__x = x

    """decorators for y"""
    @property
    def y(self):
        return self.__y

    """setter for y"""
    @y.setter
    def y(self, y):
        self.validator(y=y)
        self.__y = y

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        for vertical in range(self.y):
            print("")
        for row in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def __str__(self):
        """return the rectangle description"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    """def update(self, *args):"""
