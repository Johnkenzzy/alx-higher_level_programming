#!/usr/bin/python3
"""Module 6-load_from_json_file
Contains load_from_json_file(filename)
"""
json = __import__("json")


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)
        return (obj)
