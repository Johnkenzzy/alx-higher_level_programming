#!/usr/bin/python3
"""
Module 5-text_indentation

Supplies the text_indentation function
"""


def text_indentation(text):
    """Prints a text with two new lines after each of ., ? and :.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in {'.', '?', ':'}:
            print(result.strip() + "\n")
            result = ""

    if result.strip():
        print(result.strip(), end="")
