#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation = 0

    for char in text:
        print(char, end="")

        if char in ".?:":
            print("\n" + " " * indentation, end="")
            indentation = 0
        elif char.isspace():
            indentation += 1
