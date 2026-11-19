#!/usr/bin/env python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
