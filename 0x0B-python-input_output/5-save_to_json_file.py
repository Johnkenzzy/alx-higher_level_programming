#!/usr/bin/python3
"""Module 5-save_to_json_file
Contains save_to_json_file(my_obj, filename)
"""
json = __import__("json")


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
