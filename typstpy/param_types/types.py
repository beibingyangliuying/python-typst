"""Classes in this module should only be used as parameters' type in the `functions` module."""

from enum import IntFlag, auto
from typing import Any, Iterable, TypeAlias

from attrs import field, frozen, validators

from ._base import _ValueUnit, _ValueUnits

Block: TypeAlias = str
"""Executable typst block."""
Array: TypeAlias = Iterable
"""Represent the `array` type in typst."""


@frozen
class Auto:
    """A value that indicates a smart default."""

    def __str__(self) -> str:
        return "auto"


@frozen
class Content:
    """A piece of document content."""

    content: Block = field()

    @content.validator
    def _check_content(self, attribute, value):
        if not isinstance(value, Block):
            raise ValueError("Content must be a string.")
        # TODO: Check if the content is executable typst block.

    def __str__(self) -> str:
        return rf"[{self.content}]"


Dictionary: TypeAlias = dict[str, Any]


@frozen
class Function:
    """A mapping from argument values to a return value."""

    func_body: str = field()

    def __str__(self) -> str:
        return self.func_body


@frozen
class Label:
    """A label for an element."""

    label: str = field()

    @label.validator
    def _check_label(self, attribute, value):
        # TODO: Check for illegal characters in label.
        pass

    def __str__(self) -> str:
        return f"<{self.label}>"


Selector: TypeAlias = Function


@frozen(slots=False)
class Length(_ValueUnit):
    """A size or distance, possibly expressed with contextual units."""

    unit: str = field(validator=validators.in_(("pt", "mm", "cm", "em", "in")))

    @staticmethod
    def pt(value: float) -> "Length":
        """Create a new `Length` object with a `pt` unit.

        Args:
            value (float): The value of the `pt` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.pt(10)
            Length(value=10, unit='pt')
        """
        return Length(value, "pt")

    @staticmethod
    def mm(value: float) -> "Length":
        """Create a new `Length` object with a `mm` unit.

        Args:
            value (float): The value of the `mm` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.mm(10)
            Length(value=10, unit='mm')
        """
        return Length(value, "mm")

    @staticmethod
    def cm(value: float) -> "Length":
        """Create a new `Length` object with a `cm` unit.

        Args:
            value (float): The value of the `cm` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.cm(10)
            Length(value=10, unit='cm')
        """
        return Length(value, "cm")

    @staticmethod
    def em(value: float) -> "Length":
        """Create a new `Length` object with a `em` unit.

        Args:
            value (float): The value of the `em` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.em(10)
            Length(value=10, unit='em')
        """
        return Length(value, "em")

    @staticmethod
    def inch(value: float) -> "Length":
        """Create a new `Length` object with an `in` unit.

        Args:
            value (float): The value of the `in` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.inch(10)
            Length(value=10, unit='in')
        """
        return Length(value, "in")

    @staticmethod
    def zihao(name: str) -> "Length":
        """Create a new `Length` object with a `pt` unit based on a Chinese zihao.

        Args:
            name (str): The Chinese zihao of the `pt` unit.

        Returns:
            Length: The created `Length` object.

        Examples:
            >>> Length.zihao("一号")
            Length(value=26, unit='pt')
            >>> Length.zihao("小一")
            Length(value=24, unit='pt')
            >>> Length.zihao("二号")
            Length(value=22, unit='pt')
            >>> Length.zihao("小二")
            Length(value=18, unit='pt')
            >>> Length.zihao("三号")
            Length(value=16, unit='pt')
            >>> Length.zihao("小三")
            Length(value=15, unit='pt')
            >>> Length.zihao("四号")
            Length(value=14, unit='pt')
            >>> Length.zihao("小四")
            Length(value=12, unit='pt')
            >>> Length.zihao("五号")
            Length(value=10.5, unit='pt')
            >>> Length.zihao("小五")
            Length(value=9, unit='pt')
            >>> Length.zihao("六号")
            Length(value=7.5, unit='pt')
            >>> Length.zihao("小六")
            Length(value=6.5, unit='pt')
        """
        zihao_dict = {
            "一号": 26,
            "小一": 24,
            "二号": 22,
            "小二": 18,
            "三号": 16,
            "小三": 15,
            "四号": 14,
            "小四": 12,
            "五号": 10.5,
            "小五": 9,
            "六号": 7.5,
            "小六": 6.5,
        }
        return Length.pt(zihao_dict[name])


@frozen(slots=False)
class Ratio(_ValueUnit):
    """A ratio of a whole. Written as a number, followed by a percent sign."""

    unit: str = field(init=False, default="%")


Relative: TypeAlias = Length | Ratio | _ValueUnits
"""This type is a combination of a `Length` and a `Ratio`."""
Color: TypeAlias = Block
"""A color in a specific color space."""


@frozen(slots=False)
class Angle(_ValueUnit):
    """An angle describing a rotation."""

    unit: str = field(validator=validators.in_(("deg", "rad")))


class Alignment(IntFlag):
    START = auto()
    END = auto()
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()
    TOP = auto()
    HORIZON = auto()
    BOTTOM = auto()
    # TODO: Add inverse operation.
