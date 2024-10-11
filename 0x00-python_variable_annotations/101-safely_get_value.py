#!/usr/bin/env python3
"""Contains a method that safely gets a value from a dictionary."""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """Safely gets a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): Dictionary to get the value from.
        key (Any): Key to look up in the dictionary.
        default (Optional[T]): Default value to return if the key is not found.

    Returns:
        Union[Any, T]: Value from the dictionary if found; otherwise,
        the default value.
    """
    if key in dct:
        return dct[key]
    return default
