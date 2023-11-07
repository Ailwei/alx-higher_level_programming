#!/usr/bin/python3
"""
module defines a json file
"""
import json


def load_from_json_file(filename):
    """
    create a python obj from json file
    """
    with open(filename) as f:
        return json.load(f)
