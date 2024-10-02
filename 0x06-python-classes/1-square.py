#!/usr/bin/python3
"""This module contains a class square (based on 0-square.py)
"""


class Square:
    """A shape with 4 equal sides."""

    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """

        self.__size = size
