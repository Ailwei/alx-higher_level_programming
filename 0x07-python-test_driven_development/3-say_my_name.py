#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first name and last name.

    Args:
        first_name (str): The first name to be included in the message.
        last_name (str, optional): The last name to be included in the message. Default is an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith

    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string$")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
