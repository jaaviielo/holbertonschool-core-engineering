#!/usr/bin/env python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents a geometric figure."""

    def area(self):
        """Calculate the are of the figure."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
