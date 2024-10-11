#!/usr/bin/env python3
"""
Complex types - functions

Write a type-annotated function 'make_multiplier' that takes a float
multiplier as an argument and returns a function that multiplies a
float by the multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
        multiplier (float): The multiplier to apply to the float.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def fn(num: float) -> float:
        return num * multiplier
    return fn
