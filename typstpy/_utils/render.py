from enum import Enum, auto
from typing import Any, Callable

from cytoolz.curried import curry, isiterable, map  # type:ignore


class RenderType(Enum):
    KEY = auto()
    VALUE = auto()
    DICT = auto()


def _render(render_type: RenderType) -> Callable[[Any], str]:
    def render_key(key: str) -> str:
        return key.replace("_", "-")

    def render_value(value: Any) -> str:
        match value:
            case bool():
                return "true" if value else "false"
            case str():
                return f'"{value}"'
            case value if isiterable(value):
                return f"({', '.join(map(render_value, value))})"
            case _:
                return str(value)

    def render_dict(params: dict[str, Any]) -> str:
        if not params:
            return ""
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
    return _render(render_type)(target)