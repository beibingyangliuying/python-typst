"""Format the representation of fields in `param_types` package."""

from enum import Enum, auto
from typing import Any, Callable

from cytoolz.curried import curry  # type:ignore


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
