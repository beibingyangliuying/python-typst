"""Decorators used in `functions` module."""

from enum import Enum, auto
from typing import Callable, Optional


def attach_func(func: Callable, name: Optional[str] = None) -> Callable:
    def wrapper(_func: Callable) -> Callable:
        _name = name if name else _func.__name__
        if _name.startswith("_"):
            raise ValueError(f"Invalid name: {_name}.")
        setattr(_func, _name, func)
        return _func

    return wrapper


class ImplementType(Enum):
    STANDARD = auto()
    NOTSTANDARD = auto()


def implement_type(implement_type: ImplementType) -> Callable:
    def wrapper(_func: Callable) -> Callable:
        setattr(_func, "_implement_type", implement_type)
        return _func

    return wrapper
