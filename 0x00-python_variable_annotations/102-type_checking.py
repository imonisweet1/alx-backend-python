#!/usr/bin/env python3
"""
Contains a function that returns a list of integers
multiplied by a certain factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """Returns a list of integers multiplied by a certain factor.

    Args:
        lst (Tuple[int]): A tuple of integers.
        factor (int): An integer used as the multiplication factor.

    Returns:
        List[int]: A list of integers, where each integer from lst is
        repeated factor times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
