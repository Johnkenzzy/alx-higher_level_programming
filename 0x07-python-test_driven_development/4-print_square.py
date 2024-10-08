#!/usr/bin/python3
"""
This is module 4-print_square

This module supplies the print_square function
"""


def print_square(size):
    """Prints a square with the character '#' of a given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
