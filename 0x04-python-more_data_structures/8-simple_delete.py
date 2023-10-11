#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys_to_delete = []
    for x in a_dictionary:
        if x == key:
            keys_to_delete.append(k)
    for x in keys_to_delete:
        del a_dictionary[x]
