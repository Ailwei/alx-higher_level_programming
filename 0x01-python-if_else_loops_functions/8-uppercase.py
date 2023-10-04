#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = char

        # Check if the character is a lowercase letter and convert it to uppercase
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)

        print(uppercase_char, end='')

    print()  # Print a newline character to end the line
