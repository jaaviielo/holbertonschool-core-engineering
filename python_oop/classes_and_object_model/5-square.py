#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        self.size = size

    def my_print(self):
        """Print the square using the # character."""
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            print("#" * self.size)
