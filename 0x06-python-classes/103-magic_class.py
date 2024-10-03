#!/usr/bin/python3
"""Magic clas module"""
import math

class MagicClass:
    """A class to represent a circle and calculate its area and circumference."""
    
    def __init__(self, radius=0):
        """Initializes the MagicClass with a given radius.
        
        Args:
            radius (int or float): The radius of the circle. Defaults to 0.
            
        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle.
        
        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.
        
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

