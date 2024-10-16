#!/usr/bin/python3
"""Module 4-from_json_string
Contains from_json_string(my_obj)
"""
json = __import__("json")


def from_json_string(my_str):
    """Re1turns an object (Python data structure) rep. by a JSON string"""
    new_obj = json.loads(my_str)
    return (new_obj)
