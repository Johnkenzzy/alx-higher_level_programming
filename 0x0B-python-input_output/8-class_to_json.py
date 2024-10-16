#!/usr/bin/python3
"""
Module 8-class_to_json
Supplies class_to_json(obj)
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return (obj.__dict__)
