#!/usr/bin/python3
"""Script to add items to a Python list and save them to a JSON file"""

import sys

# Check if the file 'add_item.json' exists, and load its content if it does
if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

try:
    existing_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_data = []

# Add command-line arguments to the list
for arg in sys.argv[1:]:
    existing_data.append(arg)

# Save the updated list to 'add_item.json'
save_to_json_file(existing_data, 'add_item.json')
