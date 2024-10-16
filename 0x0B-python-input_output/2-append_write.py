#!/usr/bin/python3
"""Module 2-append_write
Contains append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """appends a text to a file and returns the number of chars appended"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
