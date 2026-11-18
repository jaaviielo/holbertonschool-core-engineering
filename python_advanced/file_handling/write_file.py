#!/usr/bin/env python3
"""Module for writing text into files."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        characters_written = file.write(text)

    return characters_written
