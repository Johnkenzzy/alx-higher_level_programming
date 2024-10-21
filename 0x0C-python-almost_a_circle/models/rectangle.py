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
        print('\n' * self.y, end="")
        for h in range(self.height):
            if self.x > 0:
                print(" " * (self.x - 1), "#" * self.width)
            else:
                print("#" * self.width)

    def __str__(self):
        """Returns a custom Rectangle classs string"""
        x, y = self.x, self.y
        width, height = self.width, self.height
        return (f"[Rectangle] ({self.id}) {x}/{y} - {width}/{height}")

    def update(self, *args, **kwargs):
        """Assigns argument to each attributes"""
        if not args and len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
