#!/usr/bin/python3
"""
Defines the find_peak function
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
