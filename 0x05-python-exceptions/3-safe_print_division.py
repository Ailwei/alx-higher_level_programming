#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None  # Set result to None if division by zero occurs
    except Exception:
        result = None  # Set result to None for other exceptions
    print("Inside result: {:.1f}".format(result))  # Print the result
    return result
