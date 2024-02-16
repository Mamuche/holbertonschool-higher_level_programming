#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """write sting and count character"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
