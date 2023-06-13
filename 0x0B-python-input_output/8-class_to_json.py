#!/usr/bin/python3
"""Module that returns the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Function that eturns the dictionary description with simple data
    structure for JSON serialization of an object.
    """
    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, valuein obj.items()}
    else:
        return obj.__dict__
