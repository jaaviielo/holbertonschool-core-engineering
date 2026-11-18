#!/usr/bin/env python3
"""Module for reading text files."""


def read_file(filename=""):
    """Reads a text file and prints its contents."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
