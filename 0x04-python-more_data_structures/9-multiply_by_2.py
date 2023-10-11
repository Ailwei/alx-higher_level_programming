#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_value = {}
    for key, value in a_dictionary:
        new_value[key] = value * 2
    return new_value

