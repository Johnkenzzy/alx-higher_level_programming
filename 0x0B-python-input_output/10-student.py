#!/usr/bin/python3
"""
Module 10-student
Defines the class Student (based on 9-studenit)
"""


class Student:
    """The class of Students"""
    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return (self.__dict__)
        else:
            return ({t: self.__dict__[t] for t in attrs if t in self.__dict__})
