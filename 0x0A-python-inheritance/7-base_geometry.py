#!/usr/bin/python3
"""
7-base_geometry.py: Geometry module: with public instance method area and integer_validation
"""


class BaseGeometry:
    """create a class: integer_validator(self, name, value)"""
    pass

    def area(self):
        """public instance method for calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method  that validates value"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
