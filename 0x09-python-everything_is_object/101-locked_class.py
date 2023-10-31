#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
     """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
        super().__setattr__(name, value)
