#!/usr/bin/python3
"""This module contains a class square (based on 2-square.py)
"""


class Square:
    """A shape with 4 equal sides."""

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
