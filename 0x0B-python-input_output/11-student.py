#!/usr/bin/python3
"""
Represents a class student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that returns dictionary representation
of requested attributes or all if none were requested
"""


class Student():
    """
        A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    result[att] = self.__dict__[att]
            return result
