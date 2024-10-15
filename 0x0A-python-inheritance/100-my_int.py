#!/usr/bin/python3
"""
Module 100-my_int
Supplies MyInt class
Inherits from int
"""


class MyInt(int):
    """A rebel integer class that inverts == and != operators."""

    def __eq__(self, other):
        """Invert equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality operator."""
        return super().__eq__(other)
