#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        uppercase_char = char

        # Check if the character is a lowercase letter and convert it to uppercase
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result =+ uppercase_char

        print("{}".format(result))
