import warnings
from collections.abc import Callable, Iterable, Mapping
from functools import singledispatch

from .registry import _Implement


def _render_key(key):
    return key.replace('_', '-')


@singledispatch
def _render_value(obj):
    return str(obj)


@_render_value.register
def _(obj: bool | None):
    return str(obj).lower()


@_render_value.register
def _(obj: str):
    if obj.startswith('#'):
        return obj[1:]
    return obj


@_render_value.register
def _(obj: Mapping):
    if not obj:
        return '(:)'
    return f'({", ".join(f"{_render_key(k)}: {_render_value(v)}" for k, v in obj.items())})'


@_render_value.register
def _(obj: Iterable):
    return f'({", ".join(_render_value(v) for v in obj)})'


@_render_value.register
def _(obj: Callable):
    implement = _Implement.permanent.get(obj, None)
    if implement is None:
        warnings.warn(
            f'The function {obj} has not been registered. Use `implement` decorator to register it and set the correct original name.',
            stacklevel=2,
        )
        return obj.__name__
    return implement.original_name


def _strip_brace(value):
    return value[1:-1]
