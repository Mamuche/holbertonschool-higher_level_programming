#!/usr/bin/python3
"""add public instance method def integer_validator"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """define the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
