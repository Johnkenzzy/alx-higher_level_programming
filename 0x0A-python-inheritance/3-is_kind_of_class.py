#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Supplies is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class inherited from the class

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if it's an instance,else False
    """
    return (isinstance(obj, a_class))
