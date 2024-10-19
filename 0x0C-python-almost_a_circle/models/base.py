#!/usr/bin/python3
"""
Module base.

This module defines the class Base.

The Base class will be the parent class for subsequent child classes
in this project.
"""


class Base:
    """Manages id attributes in classes derived from Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
