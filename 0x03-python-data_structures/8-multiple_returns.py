#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None

    for char in sentence:
        length += 1
        if first_char is None:
            first_char = char
            if length == 0:
                return (length, None)
            return (length, first_char)
