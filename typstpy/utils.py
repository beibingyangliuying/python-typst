from enum import Enum, auto
from typing import Any, Callable, Optional

from cytoolz.curried import curry, map  # type:ignore

# region render


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
            case tuple():
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


# endregion
# region format


class FormatType(Enum):
    FLOAT = auto()


def _format(format_type: FormatType) -> Callable[[Any], str]:
    def format_float(value: float) -> str:
        return f"{value:.2f}".rstrip("0").rstrip(".")

    match format_type:
        case FormatType.FLOAT:
            return format_float


@curry
def format(format_type: FormatType, target: Any) -> str:
    return _format(format_type)(target)


# endregion
# region decorator


def attach_func(func: Callable, name: Optional[str] = None) -> Callable:
    def wrapper(_func: Callable) -> Callable:
        _name = name if name else _func.__name__
        if _name.startswith("_"):
            raise ValueError(f"Invalid name: {_name}.")
        setattr(_func, _name, func)
        return _func

    return wrapper


# endregion
