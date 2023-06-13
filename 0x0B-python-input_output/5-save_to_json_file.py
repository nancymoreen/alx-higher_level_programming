#!/usr/bin/python3
"""Module that writes an Object to a text file, using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using JSON representation
    """
    with open(filename, 'w') as fie:
        json.dump(my_obj, file)
