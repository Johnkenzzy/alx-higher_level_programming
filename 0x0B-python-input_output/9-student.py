#!/usr/bin/python3
"""
Module 9-student
Defines the class Student
"""


class Student:
    """The class of Students"""
    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return (self.__dict__)
