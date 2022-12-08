"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    value=str(items)
    frequencies = {key: value}
    counter = Counter(frequencies.values())
    frequencies = {key: counter}

    return frequencies
