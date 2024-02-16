#!/usr/bin/python3
"""function for is_same_class"""


def is_same_class(obj, a_class):
    """return true if the object is exactly
    an instance of the class,  or false"""
    if type(obj) is a_class:
        return True
    else:
        return False
