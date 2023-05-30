#!/usr/bin/python3

"""Creation of class Square"""


class Square:
    """Class Square efines a square:
    -Private instanmce attribute: size
    -Instantiation with size(no type/value verification))
    Args:
    size: Size of the square"""
    def __init__(self, size):
        self.__size = size
