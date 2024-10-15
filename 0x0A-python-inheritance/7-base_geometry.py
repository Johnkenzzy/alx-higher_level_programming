#!/usr/bin/python3
"""
Module 7-base_geometry (based on 6-base_geometry)
Defines the class BaseGeometry
"""


class BaseGeometry:
    """A class of geometrical shapes"""
    def __init__(self):
        """Instantiation of instance attributes"""

    def area(self):
        """the measure of the parameters of an object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
