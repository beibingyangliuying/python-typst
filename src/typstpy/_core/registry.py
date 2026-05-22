from collections.abc import Callable
from dataclasses import dataclass
from typing import ClassVar, Self
from weakref import WeakKeyDictionary, WeakSet


@dataclass(frozen=True)
class _Implement:
    permanent: ClassVar[WeakKeyDictionary[Callable, Self]] = WeakKeyDictionary()
    temporary: ClassVar[WeakSet[Callable]] = WeakSet()

    original_name: str
    hyperlink: str | None = None
    version: str | None = None


def _function_label(func):
    implement = _Implement.permanent.get(func, None)
    if implement is not None:
        return implement.original_name
    return getattr(func, '__name__', repr(func))


def _keyword_defaults(func):
    return func.__kwdefaults__ or {}


def _raise_unknown_fields(func, kwargs):
    defaults = _keyword_defaults(func)
    invalid = sorted(set(kwargs) - set(defaults))
    if invalid:
        fields = ', '.join(invalid)
        raise TypeError(f'{_function_label(func)} does not accept field(s): {fields}')


def _validate_value(func, name, value, allowed):
    if value not in allowed:
        choices = ', '.join(repr(choice) for choice in sorted(allowed, key=repr))
        raise ValueError(
            f'{_function_label(func)} got invalid {name}={value!r}; expected one of: {choices}'
        )
