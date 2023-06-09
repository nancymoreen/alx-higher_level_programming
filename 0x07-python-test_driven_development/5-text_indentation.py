#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of ., ? and :

    Args:
        text: string

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ['.', ',', '?', ':']:
            result += '\n\n'
    print(result.strip())
