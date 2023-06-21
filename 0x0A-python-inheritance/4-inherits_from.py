#!/usr/bin/python3
"""Module for checking if an object is an instance of a  class
that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Function returns true if the above condition is satisfied.
    Otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
