#!/usr/bin/python3
"""Module that returns the JSON representation of an object.
"""


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object.
    """
    try:
        return json.dumps(my_obj)
    except TypeError as e:
        return str(e)
