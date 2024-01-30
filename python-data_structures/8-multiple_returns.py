#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0:1]
    length = (len(sentence))
    if not sentence:
        first = None
    return (length, first)
