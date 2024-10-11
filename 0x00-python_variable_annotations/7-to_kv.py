#!/usr/bin/env python3
"""
Contains a function that converts a Python variable to a key-value pair,
where the value is squared.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a numerical value.

    Parameters:
        k (str): The key for the key-value pair.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`,
        and the second element is the square of `v` as a float.
    """
    return k, v ** 2
