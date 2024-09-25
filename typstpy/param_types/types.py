"""Classes in this module should only be used as parameter types in the `functions` module."""

from typing import TypeAlias

from attrs import field, frozen, validators

from ._base import _ValueUnit, _ValueUnits

Block: TypeAlias = str
"""Executable typst block."""


@frozen
class Content:
    """A piece of document content."""

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
    """A label for an element."""

    label: str = field()

    @label.validator
    def _check_label(self, attribute, value):
        # todo: Check for illegal characters in label.
        pass

    def __str__(self) -> str:
        return f"<{self.label}>"


@frozen(slots=False)
class Length(_ValueUnit):
    """A size or distance, possibly expressed with contextual units."""

    unit: str = field(validator=validators.in_(("pt", "mm", "cm", "em", "in")))

    @staticmethod
    def pt(value: float) -> "Length":
        return Length(value, "pt")

    @staticmethod
    def mm(value: float) -> "Length":
        return Length(value, "mm")

    @staticmethod
    def cm(value: float) -> "Length":
        return Length(value, "cm")

    @staticmethod
    def em(value: float) -> "Length":
        return Length(value, "em")

    @staticmethod
    def inch(value: float) -> "Length":
        return Length(value, "in")

    @staticmethod
    def zihao(name: str) -> "Length":
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
Color: TypeAlias = Content
"""A color in a specific color space."""


@frozen(slots=False)
class Angle(_ValueUnit):
    unit: str = field(validator=validators.in_(("deg", "rad")))
