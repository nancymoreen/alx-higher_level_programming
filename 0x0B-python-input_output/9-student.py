#!/usr/bin/python3
"""Module that defines Student class
"""


class Student:
    """Class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """Function that defines Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict representation of Student class
        """
        return self.__dict__.copy()
