#!/usr/bin/env python3
"""Defines a Square class."""

Square = __import__('1-square').Square


class Square(Square):
    """Represents a square."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
