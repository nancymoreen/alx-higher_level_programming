#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
     prints My name is <first name> <last name>.

     Args:
        first_name: The first name
        last_name: The last name

    Raises:
        TypeError: If first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
