#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for char in text:
        if i == 0:
            if char == " ":
                continue
            else:
                i = 1
        if i == 1:
            if char in [".", "?", ":"]:
                print((char))
                print()
                i = 0
            else:
                print((char), end=(""))
        