#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
