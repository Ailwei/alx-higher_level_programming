#!/usr/bin/python3

import marshal
import sys


def extract_names(code_object):
    # Extract the names defined in the code object
    names = [
            name for name in code_object.co_names
            if not name.startswith('__')
            ]

    return names


if __name__ == "__main__":
    try:
        pyc_filename = 'hidden_4.pyc'

        # Read the compiled code from the .pyc file
        with open(pyc_filename, 'rb') as pyc_file:
            pyc_data = pyc_file.read()

        # Unmarshal the compiled code to get the code object
        code_object = marshal.loads(
            pyc_data[16:]
        )

        # Extract and print the names defined in the module
        names = extract_names(code_object)
        for name in sorted(names):
            print(name)

    except Exception as e:
        print("Error:", e)
