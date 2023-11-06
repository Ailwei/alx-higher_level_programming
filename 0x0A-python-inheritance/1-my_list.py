#!/usr/bin/python3
"""
this function print the list in sorted lis
"""


class MyList(list):
    def print_sorted(self):
        """
        this print the list in sorted
        """
        sorted_list = sorted(self)
        print(sorted_list)
import doctest

if __name__ == "__main__":
    doctest.testmod()
