#!/usr/bin/python3
"""Creation of a class Square"""


class Square:
    """Class Square that defines a square
    -Private instance attribute: size
    -Property accessors: getters and setters"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return(self.__size**2)
