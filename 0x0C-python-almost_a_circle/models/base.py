#!/usr/bin/python3
"""
Module for the Base class
"""

class Base:
    """
    The Base class for managing id attribute in future classes
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): If provided, assign to the public instance attribute id;
                      otherwise, increment __nb_objects and assign it to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
