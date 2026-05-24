import warnings
from collections.abc import Callable, Iterable, Mapping
from functools import singledispatch

from .ir import MappingExpr, RawExpr, SequenceExpr, TypstExpr
from .registry import Implement


def _render_key(key: str) -> str:
    """Convert Python snake_case parameter names to Typst kebab-case."""
    return key.replace('_', '-')


@singledispatch
def _to_expr(obj: object) -> TypstExpr:
    return RawExpr(str(obj))


@_to_expr.register
def _(obj: bool | None) -> TypstExpr:
    return RawExpr(str(obj).lower())


@_to_expr.register
def _(obj: str) -> TypstExpr:
    if obj.startswith('#'):
        return RawExpr(obj[1:])
    return RawExpr(obj)


@_to_expr.register
def _(obj: bytes | bytearray | memoryview) -> TypstExpr:
    raise TypeError(
        'Python bytes-like objects cannot be rendered as Typst code; pass a Typst '
        'source string such as `"image.png"` instead'
    )


@_to_expr.register
def _(obj: Mapping) -> TypstExpr:
    entries = tuple((_render_key(k), _to_expr(v)) for k, v in obj.items())
    return MappingExpr(entries)


@_to_expr.register
def _(obj: Iterable) -> TypstExpr:
    return SequenceExpr(tuple(_to_expr(v) for v in obj))


@_to_expr.register
def _(obj: Callable) -> TypstExpr:
    """Render a registered function to its original Typst name.

    Unregistered callables fall back to ``__name__`` with a warning,
    since the correct Typst name cannot be inferred automatically.
    """
    implement = Implement.permanent.get(obj, None)
    if implement is None:
        warnings.warn(
            f'The function {obj} has not been registered. '
            'Use `implement` decorator to register it and set the correct original name.',
            stacklevel=3,
        )
        return RawExpr(obj.__name__)
    return RawExpr(implement.original_name)


def render_value(obj: object) -> str:
    """Render a Python object to its full Typst source representation."""
    return _to_expr(obj).render()


def render_content(obj: object) -> str:
    """Render a Python object without outer parentheses, for use as inline arguments.

    Equivalent to ``strip_brace(render_value(obj))`` but implemented at the IR
    level to avoid fragile character-index assumptions.
    """
    return _to_expr(obj).render_content()
