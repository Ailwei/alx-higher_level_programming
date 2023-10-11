#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    found = False
    for existing_key in a_dictionary:
        if existing_key == key:
            a_dictionary[existing_key] = value
            found = True
            break

    if not found:
        a_dictionary[key] = value
