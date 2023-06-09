#!/usr/bin/python3

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: length of the square.

    Raises:
        ValueError: If size is less than 0.
        TypeError: If size is not an integer.
        TypeError: If size is a float and is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for - in range(size):
        print("#" * size)
