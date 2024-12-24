from typing import NoReturn

from ..typings import Predicate
from .concepts import instance, normal, positional, post_series, pre_series
from .decorators import attach_func, implement


def pad(s: str, /) -> str:
    """Pad a string with double quotes.

    Args:
        s (str): The string to be padded.

    Returns:
        str: The padded string.
    """
    return f'"{s}"'


def is_valid(*predicates: Predicate) -> NoReturn | None:
    """Check if all predicates are satisfied and throw `ValueError` if not.

    Raises:
        ValueError: If any predicate is not satisfied.

    Returns:
        NoReturn | None: None if all predicates are satisfied, otherwise raises ValueError.
    """
    for predicate in predicates:
        if not predicate():
            freevars = predicate.__code__.co_freevars
            closure = (
                predicate.__closure__
            )  # Closure exists if and only if freevars is not empty
            raise ValueError(
                f'Invalid parameters: {', '.join(f'{i} = {j.cell_contents}' for i, j in zip(freevars, closure))}'  # type:ignore
            )
    return None


__all__ = (
    [
        'instance',
        'normal',
        'positional',
        'post_series',
        'pre_series',
    ]
    + [
        'attach_func',
        'implement',
    ]
    + ['pad', 'is_valid']
)
