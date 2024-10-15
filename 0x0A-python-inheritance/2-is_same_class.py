#!/usr/bin/python3
"""
Module 2-is_same_class
Supplies is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Checks if an object is directly an instance of a class
 
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
    
    Returns:
        bool: True if it's an instance,else False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
