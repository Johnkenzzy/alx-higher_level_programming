#!/usr/bin/python3
"""
Module 4-inherits_from
Supplies inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    inherited(directly or indirectly) from a specified class

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        bool: True if it's an instance,else False
    """
    return (isinstance(obj, a_class))
