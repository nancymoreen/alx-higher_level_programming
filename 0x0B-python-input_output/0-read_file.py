#!/usr/bin/python3
"""Module that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """Function that reads a gtext file and prints it to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
