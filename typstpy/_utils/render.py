"""Render Python object to valid typst function parameter."""

from enum import Enum, IntFlag, auto
from typing import Any, Callable

from cytoolz.curried import curry, identity, isiterable, map  # type:ignore
from pymonad.maybe import Maybe  # type:ignore

from ..param_types.types import Content


class RenderType(Enum):
    KEY = auto()
    VALUE = auto()
    DICT = auto()


def _render(render_type: RenderType) -> Callable[[Any], str]:
    def render_key(key: str) -> str:
        return key.replace("_", "-")

    def render_value(value: Any) -> str:
        match value:
            case None:
                return "none"
            case bool():
                return "true" if value else "false"
            case str():
                return f'"{value}"'
            case IntFlag():
                name = value.name
                return (
                    Maybe(name, name)
                    .map(str.lower)
                    .map(lambda x: str.replace(x, "|", "+"))
                    .maybe(ValueError(), identity)
                )
            case Content() if value.content.startswith("#"):
                return value.content.lstrip("#")
            case value if isiterable(value):
                return f"({', '.join(map(render_value, value))})"
            case _:
                return str(value)

    def render_dict(params: dict[str, Any]) -> str:
        if not params:
            raise ValueError("Empty parameters.")
        return ", ".join(
            f"{render_key(k)}: {render_value(v)}" for k, v in params.items()
        )

    match render_type:
        case RenderType.KEY:
            return render_key
        case RenderType.VALUE:
            return render_value
        case RenderType.DICT:
            return render_dict


@curry
def render(render_type: RenderType, target: Any) -> str:
    """Render Python object to valid typst function parameter.

    Args:
        render_type (RenderType): The type of rendering.
        target (Any): The python object to be rendered.

    Returns:
        str: Generated code.

    Examples:
        >>> render(RenderType.VALUE, list("hello"))
        '("h", "e", "l", "l", "o")'
        >>> render(RenderType.VALUE, (i + "Spam!" for i in list("hello")))
        '("hSpam!", "eSpam!", "lSpam!", "lSpam!", "oSpam!")'
    """
    return _render(render_type)(target)
