#!/usr/bin/python3
"""
Module for the Rectangle class
"""
from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class, inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle (default is 0).
            y (int): Y-coordinate of the rectangle (default is 0).
            id (int): If provided, assign to the public instance attribute id;
                      otherwise, use the id from the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.__validate_positive_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.__validate_positive_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.__validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.__validate_non_negative_int("y", value)
        self.__y = value

    def __validate_positive_int(self, attribute, value):
        """Private method to validate positive integers."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def __validate_non_negative_int(self, attribute, value):
        """Private method to validate non-negative integers."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute} must be >= 0")
