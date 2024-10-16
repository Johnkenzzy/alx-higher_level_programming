#!/usr/bin/python3
"""Module 3-to_json_string
Contains to_json_string(my_obj)
"""
json = __import__("json")


def to_json_string(my_obj):
    new_obj = json.dumps(my_obj)
    return (new_obj)
