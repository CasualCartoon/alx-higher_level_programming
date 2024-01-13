#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private.
        """
        self.__size = size
