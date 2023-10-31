#!/usr/bin/python3
def LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
        super().__setattr__(name, value)
