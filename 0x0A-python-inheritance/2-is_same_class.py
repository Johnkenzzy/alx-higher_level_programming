#!/usr/bin/python3
"""
Module 2-is_same_class
Supplies is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Checks if an object is directly an instance of a class
        
    Return (bool):
            True if it's an instance,else False
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
