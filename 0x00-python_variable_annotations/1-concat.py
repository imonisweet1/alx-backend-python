#!/usr/bin/env python3
"""
Basic Annotations - concat

This script defines a type-annotated function 'concat' that takes two strings
as arguments and returns their concatenation.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Parameters:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return str1 + str2
