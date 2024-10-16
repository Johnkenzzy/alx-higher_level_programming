#!/usr/bin/python3
"""Module 3-to_json_string
Contains to_json_string(my_obj)
"""
json = __import__("json")


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    new_str = json.dumps(my_obj)
    return (new_str)
