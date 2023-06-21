#!/usr/bin/python3
"""Module for checking if an object is the instanceof a class.
"""


def is_same_class(obj, a_class):
    """Function returns True if the condition is satisfied. Otherwise False.
    """
    return type(obj) is a_class
