#!/usr/bin/python3
"""Module for defining a Student
"""


class Student:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self) -> dict:
            """Dictionary representation of Student instance.
            """
            return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
