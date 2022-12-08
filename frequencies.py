"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    keys = range(4)
    values = str(items)
    for i in keys:
        for x in values:
            frequencies[i] = x
    return frequencies
