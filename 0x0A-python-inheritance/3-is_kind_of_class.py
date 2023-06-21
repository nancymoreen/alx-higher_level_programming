#!/usr/bin/python3
"""Module for checking if the object is an instance of, or an
instance of the class it was inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the condition is met. Otherwise False
    """
    return isinstance(obj, a_class)
