#!/usr/bin/python3
"""Module 0-read_file
Contains read_file(filename="")
"""


def read_file(filename=""):
    """Reads a file's content and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
