#!/usr/bin/python3
"""Module that writes a string to a text file and returns the number of
characters written.
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and returns the number of
    characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
