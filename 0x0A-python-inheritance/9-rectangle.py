#!/usr/bin/python3
"""
Module 8-rectangle
Defines the class Rectangle
Inherits from class BaseGeometry (7-base_geometry)
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A shape with 2 equal adjacent sides"""
    def __init__(self, width, height):
        """Instantiation of instance attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
