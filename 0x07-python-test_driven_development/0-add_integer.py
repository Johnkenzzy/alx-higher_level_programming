#!/usr/bin/python3
"""
This is the "0-add_integer" module

This module supplies one function, add_integer()
"""


def add_integer(a, b=98):
    """
    Adds two integers (or floats which are cast to integers).

    Args:
        a: The first number (must be an integer or float).
        b: The second number (default is 98, must be an integer or float).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """

    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return
    else:
        return (int(a) + int(b))
