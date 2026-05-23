from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from typing import ClassVar, Self
from weakref import WeakKeyDictionary, WeakSet


@dataclass(frozen=True)
class Implement:
    permanent: ClassVar[WeakKeyDictionary[Callable, Self]] = WeakKeyDictionary()
    temporary: ClassVar[WeakSet[Callable]] = WeakSet()

    original_name: str
    hyperlink: str | None = None
    version: str | None = None


def _function_label(func: Callable[..., object]) -> str:
    implement = Implement.permanent.get(func, None)
    if implement is not None:
        return implement.original_name
    return getattr(func, '__name__', repr(func))


def _keyword_defaults(func: Callable[..., object]) -> dict[str, object]:
    return func.__kwdefaults__ or {}


def _raise_unknown_fields(
    func: Callable[..., object], kwargs: Mapping[str, object]
) -> None:
    defaults = _keyword_defaults(func)
    invalid = sorted(set(kwargs) - set(defaults))
    if invalid:
        fields = ', '.join(invalid)
        raise TypeError(f'{_function_label(func)} does not accept field(s): {fields}')


def validate_value(
    func: Callable[..., object], name: str, value: object, allowed: Iterable[object]
) -> None:
    if value not in allowed:
        choices = ', '.join(repr(choice) for choice in sorted(allowed, key=repr))
        raise ValueError(
            f'{_function_label(func)} got invalid {name}={value!r}; expected one of: {choices}'
        )
