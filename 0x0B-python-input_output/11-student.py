#!/usr/bin/python3
"""
Module 11-student
Defines the class Student (based on 10-studenit)
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
            t = attrs
            return ({t: self.__dict__[t] for t in t if t in self.__dict__})

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
