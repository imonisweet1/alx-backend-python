#!/usr/bin/env python3
"""Contains a function with annotated parameters and return values
with appropriate types."""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each element and its length.

    Parameters:
        lst (Iterable[Sequence]): A collection of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
