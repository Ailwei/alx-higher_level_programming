#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int_value = int(value)  # Try to convert the value to an integer
        print("{:d}".format(int_value))  # Print it as an integer
        return True
    except (ValueError, TypeError):
        return False
