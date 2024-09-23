"""Classes in this module should only be used as parameter types in the `functions` module."""

from itertools import starmap
from typing import TypeAlias, Union

from attrs import field, frozen
from cytoolz.curried import curry, map  # type:ignore
from pymonad.reader import Pipe  # type:ignore

from .utils import FormatType, format

Block: TypeAlias = str
"""Executable typst block."""


@frozen
class Content:
    content: Block = field()

    @content.validator
    def _check_content(self, attribute, value):
        # todo: Check if the content is executable typst block.
        pass

    def _can_simplify(self) -> bool:
        return self.content.startswith("#")

    @staticmethod
    def examine_sharp(content: Block) -> str:
        return content.lstrip("#")

    def __str__(self) -> str:
        if self._can_simplify():
            return Content.examine_sharp(self.content)
        return f"[{self.content}]"


@frozen
class Label:
    label: str = field()

    @label.validator
    def _check_label(self, attribute, value):
        # todo: Check for illegal characters in label.
        pass

    def __str__(self) -> str:
        return f"<{self.label}>"


@frozen
class Length:
    value: float = field(repr=format(FormatType.FLOAT))
    unit: str = field()

    @unit.validator
    def _check_unit(self, attribute, value):
        if value not in ("pt", "mm", "cm", "em"):
            raise ValueError(f"Invalid unit: {value}.")

    def __pos__(self) -> "Length":
        return self

    def __neg__(self) -> "Length":
        return Length(-self.value, self.unit)

    def __add__(self, other: Union["Length", "Ratio", "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative((self, other), ("+", "+"))
        elif isinstance(other, _Relative):
            return _Relative((self,) + other.items, ("+",) + other.signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: 'Length' and '{type(other)}'."
            )

    def __sub__(self, other: Union["Length", "Ratio", "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative((self, other), ("+", "-"))
        elif isinstance(other, _Relative):
            return _Relative((self,) + other.items, ("+",) + other.inverse_signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for -: 'Length' and '{type(other)}'."
            )

    def __str__(self) -> str:
        return f"{format(FormatType.FLOAT)(self.value)}{self.unit}"


@frozen
class Ratio:
    value: float = field(repr=format(FormatType.FLOAT))

    def __pos__(self) -> "Ratio":
        return self

    def __neg__(self) -> "Ratio":
        return Ratio(-self.value)

    def __add__(self, other: Union[Length, "Ratio", "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative((self, other), ("+", "+"))
        elif isinstance(other, _Relative):
            return _Relative((self,) + other.items, ("+",) + other.signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: 'Ratio' and '{type(other)}'."
            )

    def __sub__(self, other: Union[Length, "Ratio", "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative((self, other), ("+", "-"))
        elif isinstance(other, _Relative):
            return _Relative((self,) + other.items, ("+",) + other.inverse_signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for -: 'Ratio' and '{type(other)}'."
            )

    def __str__(self) -> str:
        return f"{format(FormatType.FLOAT)(self.value)}%"


@frozen
class _Relative:
    items: tuple[Length | Ratio, ...] = field()
    signs: tuple[str, ...] = field()

    @property
    def inverse_signs(self) -> tuple[str, ...]:
        def inverse(sign: str) -> str:
            match sign:
                case "+":
                    return "-"
                case "-":
                    return "+"
                case _:
                    raise ValueError(f"Invalid sign: {sign}.")

        return Pipe(self.signs).map(map(inverse)).map(tuple).flush()

    def __add__(self, other: Union[Length, Ratio, "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative(self.items + (other,), self.signs + ("+",))
        elif isinstance(other, _Relative):
            return _Relative(self.items + other.items, self.signs + other.signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: 'Relative' and '{type(other)}'."
            )

    def __sub__(self, other: Union[Length, Ratio, "_Relative"]) -> "_Relative":
        if isinstance(other, (Length, Ratio)):
            return _Relative(self.items + (other,), self.signs + ("-",))
        elif isinstance(other, _Relative):
            return _Relative(self.items + other.items, self.signs + other.inverse_signs)
        else:
            raise TypeError(
                f"Unsupported operand type(s) for -: 'Relative' and '{type(other)}'."
            )

    def __str__(self) -> str:
        return (
            Pipe(zip(self.signs, self.items))
            .map(curry(starmap)(lambda x, y: f"{x}{y}"))
            .map(lambda x: ("".join(x)).lstrip("+"))
            .map(
                lambda x: x.replace("+-", "-")
                .replace("--", "+")
                .replace("-+", "-")
                .replace("++", "+")
            )
            .flush()
        )


Relative: TypeAlias = Length | Ratio | _Relative
