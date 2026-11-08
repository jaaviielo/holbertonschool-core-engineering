#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_value = max(a_dictionary.values())

    for key, value in a_dictionary.items():
        if value == best_value:
            return key
