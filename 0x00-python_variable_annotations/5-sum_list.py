#!/usr/bin/env python3
"""
Complex types - list of floats

Write a type-annotated function 'sum_list' that takes a list of floats
as an argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all numbers in input_list.
    """
    return sum(input_list)
