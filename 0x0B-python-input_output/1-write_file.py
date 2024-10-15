#!/usr/bin/python3
"""Module 1-write_file
Contains write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """Reads a file's content and prints it to stdout"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
