#!/usr/bin/python3
"""Creation of a class Square"""


class Square:
    """Class square defines a square.
    -Private instance attribute: size
    -Instantiation with optional size
    Args:
    size(int): Size of the square
    Raises:
        TypeError: if size is not integer type
        ValueError: if size is less than 0"""
    def __init__(self, size=0):
        if not (size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
            self.__size = size

    def area(self):
        """Calculates the area of the squaare"""
        return(self.__size ** 2)
