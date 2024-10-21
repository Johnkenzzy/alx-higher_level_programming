#!/usr/bin/python3
"""
Module rectangle.

This module defines the Rectangle class.

The Rectangle class inherits from the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """A 3-sided polygon formed by 3 straight line segments"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the instance width value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the instance width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the instance height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the instance height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the instance x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the instance x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the instance y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the instance y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the value of the rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Prints Rectangle instance with character #"""
        for h in range(self.height):
                print("#" * self.width)
