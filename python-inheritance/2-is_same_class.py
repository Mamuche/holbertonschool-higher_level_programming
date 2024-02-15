#!/usr/bin/python3
"""function for is_same_class"""


def is_same_class(obj, a_class):
    """return true if the object is exactly
    an instance of the class,  or false"""
    return type(obj) == a_class
