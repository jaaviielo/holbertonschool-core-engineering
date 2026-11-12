#!/usr/bin/env python3
"""Module containing the VerboseList class."""


class VerboseList(list):
    """A list subclass that prints notifications when modified."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print the number of added items."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item, printing a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
