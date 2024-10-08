#!/usr/bin/python3
"""
This is the 2-rectangle module

This module defines the Rectangle class (based on 1-rectangle.py)
"""


class Rectangle:
    """This is the rectangle class, a 2 equal opposite sides polygon"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a given width.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of the instance width"""
        return (self.__wdith)

    @width.setter
    def width(self, value):
        """Sets the value of the instance with

        Arg:
            value (int): The value of the rectangle width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the instance height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of the instance height

        Arg:
            value (int): The value of the rectangle height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the triangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))
