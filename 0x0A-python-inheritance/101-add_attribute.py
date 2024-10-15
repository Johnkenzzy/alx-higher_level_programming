#!/usr/bin/python3
"""
Module 101-add_attr
add_arr
"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, '__slots__') or not isinstance(obj, (list, dict, object)):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
