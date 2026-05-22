import warnings
from collections.abc import Callable, Iterable, Mapping
from functools import singledispatch

from .ir import _MappingExpr, _RawExpr, _SequenceExpr, _TypstExpr
from .registry import _Implement


def _render_key(key: str) -> str:
    return key.replace('_', '-')


@singledispatch
def _to_expr(obj: object) -> _TypstExpr:
    return _RawExpr(str(obj))


@_to_expr.register
def _(obj: bool | None) -> _TypstExpr:
    return _RawExpr(str(obj).lower())


@_to_expr.register
def _(obj: str) -> _TypstExpr:
    if obj.startswith('#'):
        return _RawExpr(obj[1:])
    return _RawExpr(obj)


@_to_expr.register
def _(obj: bytes | bytearray | memoryview) -> _TypstExpr:
    raise TypeError(
        'Python bytes-like objects cannot be rendered as Typst code; pass a Typst '
        'source string such as `"image.png"` instead'
    )


@_to_expr.register
def _(obj: Mapping) -> _TypstExpr:
    entries = tuple((_render_key(k), _to_expr(v)) for k, v in obj.items())
    return _MappingExpr(entries)


@_to_expr.register
def _(obj: Iterable) -> _TypstExpr:
    return _SequenceExpr(tuple(_to_expr(v) for v in obj))


@_to_expr.register
def _(obj: Callable) -> _TypstExpr:
    implement = _Implement.permanent.get(obj, None)
    if implement is None:
        warnings.warn(
            f'The function {obj} has not been registered. Use `implement` decorator to register it and set the correct original name.',
            stacklevel=3,
        )
        return _RawExpr(obj.__name__)
    return _RawExpr(implement.original_name)


def _render_value(obj: object) -> str:
    return _to_expr(obj).render()


def _strip_brace(value: str) -> str:
    return value[1:-1]
