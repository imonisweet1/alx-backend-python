#!/usr/bin/env python3
"""
Complex types - mixed list of integers and floats

This script defines a function that takes a mixed list of integers and
floats, returning the sum of all numbers in the list as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of all numbers in mxd_lst as a float.
    """
    return sum(mxd_lst)
