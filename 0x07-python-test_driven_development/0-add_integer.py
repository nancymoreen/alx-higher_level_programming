#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns a result of an integer.

    Args:
     a: first number
     b: second number with default value 98.

    Raises:
     TypeError: if a or b is not an integer or float.

    Returns:
        Sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
