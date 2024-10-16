#!/usr/bin/python3
"""Module 1-write_file
Contains write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """Writes a text to a file and returns the number of chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
