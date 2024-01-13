#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The size to set.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        
        Args:
            value (tuple): The position to set.
        
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""
        result = ""
        if self.__size == 0:
            return result
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()

# Example usage:
# square = Square(5, (2, 1))
# square.my_print()
# print(square)
