#!/usr/bin/python3
"""
Module 10-square
Supplies the Suare class
Inherits from the Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the square with size, validated"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square"""
        return self._Rectangle__width * self._Rectangle__height
