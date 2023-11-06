#!/usr/bin/python3
"""
Inviert int operators
"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Replace == operators with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Replace != operators with == behavior."""
        return self.real == value
