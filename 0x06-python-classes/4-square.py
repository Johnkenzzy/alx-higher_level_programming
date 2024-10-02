#!/usr/bin/python3
"""This module contains a class square (based on 3-square.py)
"""


class Square:
    """A shape with 4 equal sides."""

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of a square object

        Returns:
            int: The size of the class instance
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the square size of a class instance.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
