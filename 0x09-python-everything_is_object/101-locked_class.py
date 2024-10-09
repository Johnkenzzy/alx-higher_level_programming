#!/usr/bin/python3
"""
Module 101-locked_class

Supplies the LockedClass class
"""


class LockedClass:
    """limit the creation of new attributes to first_name"""
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """Inntializes the instance attribute"""
        self.first_name = first_name
