#!/usr/bin/env python3
"""Contains augmented code with the correct duck-typed annotations."""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or None if the sequence is empty.

    Parameters:
        lst (Sequence[Any]): A sequence (like a list or tuple) from which
                             to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    return None
