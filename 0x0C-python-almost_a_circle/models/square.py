#!/usr/bin/python3
"""
Module square.

This module defines the Square class.

The Square class inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Rectangle with the same width and height"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance attributes"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of Square"""
        id = self.id
        x, y = self.x, self.y
        size = self.size
        return (f"[Square] ({id}) {x}/{y} - {size}")

    @property
    def size(self):
        """Gets the size of the Square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute"""
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

    def to_dictionary(self):
        """Returns a dictionary representation of a Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
