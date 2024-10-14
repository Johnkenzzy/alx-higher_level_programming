#!/usr/bin/python3
"""
Module 1-my_list
This module supplies MyList class
"""


class MyList(list):
    """A derived class that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
