#!/usr/bin/python3

def uppercase(str):
    for char in str:
        #Check if the character is a lowercase letter (ASCII values 97 to 122)
        if 'a' <= char <= 'z':
            #Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end="")
        else:
            # If the character is not a lowercase letter, print it as is
            print(char, end="")

            # Print a newline character to end the line
    print()
