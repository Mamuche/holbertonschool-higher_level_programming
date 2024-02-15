#!/usr/bin/python3
"""function that returns the list"""


def read_file(filename=""):
    """returns the list of available attributes and methods of an object"""
    with open(filename) as f:
        content = f.read()
        print(content, end="")
